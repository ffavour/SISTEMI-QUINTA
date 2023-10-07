def daStringaACifre(stringa, diz):
    stringaInCifre = []

    for elemento in stringa:
        stringaInCifre.append(diz[elemento])

    return stringaInCifre


def daCifreAStringa(listaCifre, diz):
    stringaInCaratteri = ""

    for elemento in listaCifre:
        for carattere, valore in diz.items():
            if valore == elemento:
                stringaInCaratteri += carattere

    return stringaInCaratteri


def cifraMessaggio(mex, chiave):
    # (mex + chiave) % 21
    mexCifrato = []

    for i in range(len(mex)):
        mexCifrato.append((mex[i] + chiave[i]) % 21)

    return mexCifrato


def deCifraMessaggio(mexCifrato, chiave):
    # mex - chiave
    mex = []

    for i in range(len(mexCifrato)):
        mex.append((mexCifrato[i] - chiave[i]) % 21)

    return mex


def main():
    alfabeto = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "l": 9, "m": 10, "n": 11,
                "o": 12, "p": 13, "q": 14, "r": 15, "t": 16, "s": 17, "u": 18, "v": 19, "z": 20}

    mex = "ciao"
    chiave = "itisdelpozzo"

    mexInCifre = daStringaACifre(mex, alfabeto)
    print(mexInCifre)

    chiaveInCifre = daStringaACifre(chiave, alfabeto)
    print(chiaveInCifre)

    mexCifrato = cifraMessaggio(mexInCifre, chiaveInCifre)
    print(mexCifrato)

    stringaOriginale = daCifreAStringa(deCifraMessaggio(mexCifrato, chiaveInCifre), alfabeto)
    print(stringaOriginale)


if __name__ == '__main__':
    main()
