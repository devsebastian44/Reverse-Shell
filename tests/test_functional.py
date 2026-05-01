import os
import unittest
from unittest.mock import MagicMock, patch

from src.reverse_shell import ReverseShell


class TestReverseShell(unittest.TestCase):
    """
    Functional tests for the ReverseShell class using mocks.
    Ensures logic is sound without side effects.
    """

    def setUp(self):
        # Set dummy env vars
        os.environ["LHOST"] = "1.2.3.4"
        os.environ["LPORT"] = "9999"
        self.shell = ReverseShell()

    def test_initialization(self):
        """Verifies that the shell initializes with correct parameters."""
        self.assertEqual(self.shell.host, "1.2.3.4")
        self.assertEqual(self.shell.port, 9999)

    @patch('socket.socket')
    @patch('subprocess.Popen')
    def test_start_connection_flow(self, mock_popen, mock_socket):
        """
        Tests the connection flow and process startup.
        Uses mocks to avoid real network/subprocess activity.
        """
        # Configure mocks
        mock_sock_inst = MagicMock()
        mock_socket.return_value = mock_sock_inst

        mock_proc_inst = MagicMock()
        mock_popen.return_value = mock_proc_inst

        # We need to break the infinite loop in start() for testing
        # We can do this by making the first wait() call raise a KeyboardInterrupt
        mock_proc_inst.wait.side_effect = KeyboardInterrupt

        with self.assertLogs(level='INFO') as cm:
            self.shell.start()

        # Verify socket was created and connected
        mock_socket.assert_called()
        mock_sock_inst.connect.assert_called_with(("1.2.3.4", 9999))

        # Verify process was started
        mock_popen.assert_called()

        # Verify logging
        self.assertIn("Attempting to connect to 1.2.3.4:9999...", cm.output[0])
        self.assertIn("Connection established.", cm.output[1])

    def test_stop_cleanup(self):
        """Verifies that stop() cleans up resources."""
        mock_socket = MagicMock()
        mock_process = MagicMock()

        self.shell.socket = mock_socket
        self.shell.process = mock_process

        self.shell.stop()

        mock_socket.close.assert_called_once()
        mock_process.terminate.assert_called_once()

if __name__ == '__main__':
    unittest.main()
