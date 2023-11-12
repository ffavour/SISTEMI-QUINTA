import socket as sck
import threading
import random


class ClientThread(threading.Thread):
    def __init__(self, conn, address, B, b, N):
        super().__init__()
        self.conn = conn
        self.address = address
        self.B = B
        self.b = b
        self.N = N

    def run(self):
        A = self.conn.recv(4096)
        print(f"messaggio ricevuto: {A.decode()} da {self.address}")
        self.conn.sendall(str(self.B).encode())
        A = int(A.decode())
        numeroSegreto = (A ** self.b) % self.N
        print(f"numero segreto: {numeroSegreto}")
        self.conn.close()


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    clientList = []

    g = 20
    N = 53

    b = random.randint(g, N)
    # print(b)

    B = (g ** b) % N
    # print(B)
    while True:
        conn, address = s.accept()
        client = ClientThread(conn, address, B, b, N)
        clientList.append(client)
        client.start()
        client.run()



if __name__ == "__main__":
    main()
