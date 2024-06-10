import unittest
from unittest.mock import patch
from tcp_client import tcp_client

class TestTCPClient(unittest.TestCase):
    def test_successful_file_transfer(self):
        file_path = "test_file.txt"
        server_ip = "127.0.0.1"
        server_port = 1234

        with patch("socket.socket") as mock_socket:
            mock_sock = mock_socket.return_value
            mock_sock.connect.return_value = None

            with patch("os.path.getsize") as mock_getsize:
                mock_getsize.return_value = 1024

                with patch("builtins.open", unittest.mock.mock_open(read_data=b"test data")) as mock_file:
                    tcp_client(file_path, server_ip, server_port)

                    mock_sock.sendall.assert_called_with(b'1024')
                    mock_file.assert_called_with(file_path, 'rb')
                    mock_sock.sendall.assert_called_with(b'test data')

    def test_connection_refused(self):
        file_path = "test_file.txt"
        server_ip = "127.0.0.1"
        server_port = 1234

        with patch("socket.socket") as mock_socket:
            mock_sock = mock_socket.return_value
            mock_sock.connect.side_effect = ConnectionRefusedError

            with patch("os.path.getsize") as mock_getsize:
                mock_getsize.return_value = 1024

                with patch("builtins.open", unittest.mock.mock_open(read_data=b"test data")) as mock_file:
                    with patch("builtins.print") as mock_print:
                        tcp_client(file_path, server_ip, server_port)

                        mock_print.assert_called_with(f"Connection refused by server at {server_ip}:{server_port}")

    def test_file_not_found(self):
        file_path = "nonexistent_file.txt"
        server_ip = "127.0.0.1"
        server_port = 1234

        with patch("socket.socket") as mock_socket:
            mock_sock = mock_socket.return_value
            mock_sock.connect.return_value = None

            with patch("os.path.getsize") as mock_getsize:
                mock_getsize.side_effect = FileNotFoundError

                with patch("builtins.print") as mock_print:
                    tcp_client(file_path, server_ip, server_port)

                    mock_print.assert_called_with(f"File not found: {file_path}")

    def test_generic_error(self):
        file_path = "test_file.txt"
        server_ip = "127.0.0.1"
        server_port = 1234

        with patch("socket.socket") as mock_socket:
            mock_sock = mock_socket.return_value
            mock_sock.connect.return_value = None

            with patch("os.path.getsize") as mock_getsize:
                mock_getsize.return_value = 1024

                with patch("builtins.open", unittest.mock.mock_open(read_data=b"test data")) as mock_file:
                    with patch("builtins.print") as mock_print:
                        mock_sock.sendall.side_effect = Exception("Some error")

                        tcp_client(file_path, server_ip, server_port)

                        mock_print.assert_called_with("An error occurred: Some error")

if __name__ == '__main__':
    unittest.main()