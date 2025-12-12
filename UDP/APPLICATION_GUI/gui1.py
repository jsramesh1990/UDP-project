import socket
import tkinter as tk
from tkinter import scrolledtext

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

def send_message():
    msg = entry.get()
    if not msg:
        return

    text_area.insert(tk.END, f"YOU: {msg}\n")
    entry.delete(0, tk.END)

    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

    try:
        data, _ = sock.recvfrom(1024)
        text_area.insert(tk.END, f"SERVER: {data.decode()}\n")
    except socket.timeout:
        text_area.insert(tk.END, "SERVER: [No Response]\n")

root = tk.Tk()
root.title("UDP Client GUI")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

send_btn = tk.Button(root, text="SEND", command=send_message)
send_btn.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=50, height=15)
text_area.pack(pady=5)

root.mainloop()

