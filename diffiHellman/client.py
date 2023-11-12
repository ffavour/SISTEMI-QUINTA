import socket as sck
import random


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server_address = ("127.0.0.1", 8000)

    s.connect(server_address)

    g = 20
    N = 53

    a = random.randint(g, N)
    # print(a)

    A = (g ** a) % N
    # print(A)

    mex = str(A)
    """if mex == "EXIT":
        break"""
    s.sendall(mex.encode())
    B = s.recv(4096)
    print(f"messaggio ricevuto: {B.decode()}")
    B = int(B.decode())
    numeroSegreto = (B ** a) % N
    print(f"numero segreto: {numeroSegreto}")
    s.close()


if __name__ == "__main__":
    main()
