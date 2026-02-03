import os
import pytest

def test_shell_py_exists():
    """Verify that the Python reverse shell payload exists."""
    payload_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'shell.py')
    assert os.path.isfile(payload_path)

def test_shell_sh_exists():
    """Verify that the Bash reverse shell payload exists."""
    payload_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'shell.sh')
    assert os.path.isfile(payload_path)

# In a real environment, we would also mock the socket connection to ensure the script
# establishes a connection correctly, without actually transferring a shell.
