# k >= n

def fact(f):
    f_def = 1
    for i in range(1, f + 1):
        f_def *= i
    return f_def


def soch_ch(n_def, k_def):
    q_def = fact(k_def) / (fact(k_def - n_def) * fact(n_def))
    return q_def


def main():
    n, k = map(int, input().split())
    q = soch_ch(n, k)
    print(int(q))


main()
