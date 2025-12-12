##  UDP Client-Server Project

UDP (User Datagram Protocol) is a connectionless transport layer protocol. Unlike TCP:

There is no connection setup (no handshake).

It is faster and has lower overhead.

Packets may be lost — UDP does not guarantee delivery.

Useful for real-time applications, streaming, or lightweight messaging.

```
| Feature     | UDP                                 | TCP                                |
| ----------- | ----------------------------------- | ---------------------------------- |
| Connection  | Connectionless                      | Connection-oriented                |
| Reliability | Unreliable                          | Reliable, guaranteed               |
| Ordering    | No ordering                         | Ordered                            |
| Overhead    | Low                                 | Higher (handshake, acknowledgment) |
| Use Cases   | Streaming, games, real-time control | File transfer, web, email          |
```

#  Overview

This project demonstrates a UDP-based communication system with three components:

Server – C-based UDP server listening for client messages.

Client – C++ UDP client sending messages to the server.

GUI Application – Python Tkinter GUI to display client and server input/output in a structured interface.

The system allows you to send messages from the client, receive them on the server, and visualize communication via a GUI.

##  Project Structure
```
UDP/
│
├── SERVER/
│     └── server.c         ← C UDP server source
├── CLIENT/
│     └── client.cpp       ← C++ UDP client source
├── APPLICATION_GUI/
│     └── gui.py           ← Python Tkinter GUI
├── Makefile               ← Builds server & client
└── README.md              ← Project documentation
```

#  Requirements

C Compiler (gcc)

C++ Compiler (g++)

Python 3 (python3)

Tkinter for Python GUI

Install dependencies (Ubuntu/Debian example):
```
sudo apt update
sudo apt install build-essential python3 python3-tk
```

##  Build Instructions

Navigate to project folder:
```
cd UDP
```

Build server and client using Makefile:
```
make
```

Clean build artifacts:
```
make clean
```

After building, you will have two binaries:

server → C UDP server

client → C++ UDP client

The Python GUI does not require compilation.

#  Running the Project
Step 1 – Start the UDP server
```
./server
```

The server will start listening on UDP port 8080.

Step 2 – Run the C++ UDP client
```
./client
```

You can type messages in the terminal, which will be sent to the server. Server responses are printed back in the terminal.

Step 3 – Run the GUI
```
python3 APPLICATION_GUI/gui.py
```

GUI Features:

Client Section

Input box → Type messages

Output box → Shows messages from the server

Server Section

Input box → Optional for GUI simulation

Output box → Displays messages sent from GUI server simulation

Client messages sent via GUI will be delivered to the C server over UDP.

#  Notes

UDP protocol is connectionless. Messages may be lost if network issues occur.

Server runs on 127.0.0.1:8080 by default (loopback).

GUI uses Python Tkinter — works on Linux, Windows, and MacOS.

The project demonstrates cross-language communication: C server, C++ client, Python GUI.

#  How It Works

Client sends a message over UDP to the Server.

Server receives the message and prints it in terminal.

Client GUI can also send messages to server and display responses.

Server GUI section is optional for local simulation or testing.

#  Features

Cross-language UDP communication (C, C++, Python)

GUI displays input and output for both client and server

Clean, modular project structure

Easy to build and run using a single Makefile

#  Makefile Targets
Target	Description
make	Build both server and client
make server	Build only the server
make client	Build only the client
make clean	Remove binaries

#  Future Improvements

Automatic real-time GUI updates for messages from server

Logging messages to a file

Multiple clients support with threading
