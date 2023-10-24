import math


def trovaC(m):
    c = 2
    while c < m:
        if math.gcd(c, m) == 1:
            break
        else:
            c += 1
    return c


def trovaD(c, m):
    d = 0
    while 0 <= d < m:
        if (c * d) % m == 1:
            break
        else:
            d += 1
    return d


def codifica(mex, c, n):
    mexCodificato = []
    for lettera in mex:
        b = (ord(lettera) ** c) % n
        mexCodificato.append(b)
    return mexCodificato


def decodifica(mexCodificato, d, n):
    stringaDecodificata = ""
    for elemento in mexCodificato:
        a = (elemento ** d) % n
        stringaDecodificata += chr(a)
    return stringaDecodificata


def main():
    p = 4001
    q = 3889
    n = p * q
    m = math.lcm(p - 1, q - 1)
    print(f"m: {m}")

    c = trovaC(m)
    print(f"c: {c}")

    d = trovaD(c, m)
    print(f"d: {d}")

    mex = "ciao a tutti"
    mexCodificato = codifica(mex, c, n)
    print(mexCodificato)

    mexDecodoficato = decodifica(mexCodificato, d, n)
    print(mexDecodoficato)


if __name__ == '__main__':
    main()
