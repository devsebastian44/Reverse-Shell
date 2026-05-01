import os
import py_compile


def test_payload_syntax():
    """Valida estáticamente que la sintaxis de Python del payload sea correcta."""
    payload_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'reverse_shell.py')
    if not os.path.exists(payload_path):
        raise AssertionError("Falló: El payload no se encuentra.")
    try:
        py_compile.compile(payload_path, doraise=True)
    except Exception as e:
        raise AssertionError(f"Error de sintaxis en reverse_shell.py: {e}") from e
