import py_compile
import os

def test_windows_payload_syntax():
    """Valida estáticamente que la sintaxis de Python del payload sea correcta."""
    payload_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'shell.py')
    assert os.path.exists(payload_path), "Falló: El payload de Windows no se encuentra."
    try:
        py_compile.compile(payload_path, doraise=True)
    except Exception as e:
        assert False, f"Error de sintaxis en shell.py: {e}"

def test_bash_payload_exists():
    """Verifica que el script de bash esté en la ruta correcta."""
    payload_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'shell.sh')
    assert os.path.exists(payload_path), "Falló: El payload de Linux no se encuentra."
