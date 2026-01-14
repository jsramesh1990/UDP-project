##  UDP Client-Server Project

[![UDP Protocol](https://img.shields.io/badge/UDP-Protocol-blue.svg)](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
[![Network Programming](https://img.shields.io/badge/Network-Programming-orange.svg)](https://en.wikipedia.org/wiki/Computer_network_programming)
[![Socket Programming](https://img.shields.io/badge/Socket-Programming-green.svg)](https://en.wikipedia.org/wiki/Network_socket)
[![Connectionless Protocol](https://img.shields.io/badge/Connectionless-Transport%20Layer-red.svg)](https://en.wikipedia.org/wiki/Connectionless_communication)
[![Client-Server Architecture](https://img.shields.io/badge/Client--Server-Architecture-yellow.svg)](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
[![C Programming](https://img.shields.io/badge/C-Network%20Programming-purple.svg)](https://en.wikipedia.org/wiki/C_(programming_language))
[![Real-Time Applications](https://img.shields.io/badge/Real--Time-Applications-8b0000.svg)](https://en.wikipedia.org/wiki/Real-time_computing)
[![Low Latency](https://img.shields.io/badge/Low-Latency-0066cc.svg)](https://en.wikipedia.org/wiki/Latency_(engineering))
[![Datagram Communication](https://img.shields.io/badge/Datagram-Communication-lightgrey.svg)](https://en.wikipedia.org/wiki/Datagram)
[![Transport Layer](https://img.shields.io/badge/Transport-Layer%204-ff69b4.svg)](https://en.wikipedia.org/wiki/Transport_layer)
[![IP Networking](https://img.shields.io/badge/IP-Networking-009688.svg)](https://en.wikipedia.org/wiki/Internet_Protocol)
[![BSD Sockets](https://img.shields.io/badge/BSD-Sockets-blueviolet.svg)](https://en.wikipedia.org/wiki/Berkeley_sockets)
[![Unreliable Delivery](https://img.shields.io/badge/Unreliable-Delivery-32CD32.svg)](https://en.wikipedia.org/wiki/Best-effort_delivery)
[![Streaming Protocol](https://img.shields.io/badge/Streaming-Protocol-FF8C00.svg)](https://en.wikipedia.org/wiki/Streaming_media)
[![Message-Oriented](https://img.shields.io/badge/Message--Oriented-Protocol-181717.svg)](https://en.wikipedia.org/wiki/Message_oriented_middleware)
[![Network Utilities](https://img.shields.io/badge/Network-Utilities-333333.svg)](https://en.wikipedia.org/wiki/Network_utility)
[![Linux/Unix](https://img.shields.io/badge/Linux-Unix%20Sockets-brightgreen.svg)](https://en.wikipedia.org/wiki/Unix_domain_socket)
[![Multicast Support](https://img.shields.io/badge/Multicast-Broadcast%20Support-4B0082.svg)](https://en.wikipedia.org/wiki/Multicast)
[![Port Communication](https://img.shields.io/badge/Port-Communication-800000.svg)](https://en.wikipedia.org/wiki/Port_(computer_networking))
[![Non-Blocking IO](https://img.shields.io/badge/Non--Blocking-IO-2E8B57.svg)](https://en.wikipedia.org/wiki/Asynchronous_I/O)
[![Header Overhead](https://img.shields.io/badge/Low-Overhead%20Protocol-483D8B.svg)](https://en.wikipedia.org/wiki/Protocol_overhead)
[![VoIP Compatible](https://img.shields.io/badge/VoIP-Compatible-8A2BE2.svg)](https://en.wikipedia.org/wiki/Voice_over_IP)
[![Gaming Network](https://img.shields.io/badge/Gaming-Network%20Protocol-DAA520.svg)](https://en.wikipedia.org/wiki/Online_game)
[![DNS Protocol](https://img.shields.io/badge/DNS-Underlying%20Protocol-2F4F4F.svg)](https://en.wikipedia.org/wiki/Domain_Name_System)
[![Multithreaded Server](https://img.shields.io/badge/Multithreaded-Server-FF4500.svg)](https://en.wikipedia.org/wiki/Thread_(computing))
[![Cross-Platform Networking](https://img.shields.io/badge/Cross--Platform-Networking-00CED1.svg)](https://en.wikipedia.org/wiki/Cross-platform)
[![Educational Project](https://img.shields.io/badge/Educational-Networking%20Project-9400D3.svg)](https://en.wikipedia.org/wiki/Educational_technology)

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
