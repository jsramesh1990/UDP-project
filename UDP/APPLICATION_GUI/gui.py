import socket
import tkinter as tk
from tkinter import scrolledtext

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

# Function to send client message
def send_client_message():
    msg = client_input.get()
    if not msg:
        return
    client_output.insert(tk.END, f"You: {msg}\n")
    client_input.delete(0, tk.END)

    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

    try:
        data, _ = sock.recvfrom(1024)
        client_output.insert(tk.END, f"Server: {data.decode()}\n")
    except socket.timeout:
        client_output.insert(tk.END, "Server: [No Response]\n")

# Function to send server message (optional, for GUI testing server sending)
def send_server_message():
    msg = server_input.get()
    if not msg:
        return
    server_output.insert(tk.END, f"Server: {msg}\n")
    server_input.delete(0, tk.END)

    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

# Main Window
root = tk.Tk()
root.title("UDP Client-Server GUI")

# ---------------- Client Frame ----------------
client_frame = tk.LabelFrame(root, text="CLIENT", padx=10, pady=10)
client_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(client_frame, text="Input:").pack(anchor='w')
client_input = tk.Entry(client_frame, width=50)
client_input.pack(pady=5)

client_send_btn = tk.Button(client_frame, text="Send", command=send_client_message)
client_send_btn.pack(pady=5)

tk.Label(client_frame, text="Output:").pack(anchor='w')
client_output = scrolledtext.ScrolledText(client_frame, width=60, height=10)
client_output.pack(pady=5)

# ---------------- Server Frame ----------------
server_frame = tk.LabelFrame(root, text="SERVER", padx=10, pady=10)
server_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(server_frame, text="Input:").pack(anchor='w')
server_input = tk.Entry(server_frame, width=50)
server_input.pack(pady=5)

server_send_btn = tk.Button(server_frame, text="Send", command=send_server_message)
server_send_btn.pack(pady=5)

tk.Label(server_frame, text="Output:").pack(anchor='w')
server_output = scrolledtext.ScrolledText(server_frame, width=60, height=10)
server_output.pack(pady=5)

root.mainloop()

