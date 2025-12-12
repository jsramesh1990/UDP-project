CC=gcc
CXX=g++

SERVER_SRC=SERVER/server.c
CLIENT_SRC=CLIENT/client.cpp

all: server client

server: $(SERVER_SRC)
	$(CC) $(SERVER_SRC) -o server

client: $(CLIENT_SRC)
	$(CXX) $(CLIENT_SRC) -o client

clean:
	rm -f server client

.PHONY: all clean

