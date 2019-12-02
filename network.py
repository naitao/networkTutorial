import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        #self.id = self.connect()
        print("networking connected: {}".format(self.p))

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        print("network...sending:{}".format(pickle.dumps(data)))
        try:
            self.client.send(pickle.dumps(data))
            "finished sending..."
            #result = pickle.loads(self.client.recv(2048))
            #print("network...received: {}".format(result))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


'''
n = Network()
print(n.send("Hello"))
print(n.send("working"))
'''