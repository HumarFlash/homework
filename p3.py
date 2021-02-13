def sum_per(n):
    n1 = int(str(n)[::-1])
    n += n1
    return n


def check(n):
    n = str(n)
    mid = len(n) // 2
    uk_def = True

    for i in range(mid):
        if n[i] != n[-i - 1]:
            uk_def = False
            break

    return uk_def


def main(q):
    uk = False
    while uk is False:
        uk = check(q)
        if uk is True:
            break
        q = sum_per(q)
    print(q)


k = int(input())
main(k)