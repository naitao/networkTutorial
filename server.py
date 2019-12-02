import socket
from _thread import start_new_thread
import sys
from player import Player
import pickle

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            #reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps((reply)))
        except Exception as e:
            print(str(e))
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    #currentPlayer = currentPlayer % 2