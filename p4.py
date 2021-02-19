def find_a_r(t):
    best1, best2, best3, best4 = '', '', '', ''
    t1, t2, t3, t4 = 0, 0, 0, 0
    r1, r2, r3, r4 = 0, 0, 0, 0
    for i in range(len(t)):
        x = t[i][0]
        y = t[i][1]
        if t[i][2] == '1':
            r = min(abs(x), abs(y))
            if type(best1) == str or r < best1:
                best1 = r
                t1 = [x, y]
                r1 = r
        if t[i][2] == '2':
            r = min(abs(x), abs(y))
            if type(best2) == str or r < best2:
                best2 = r
                t2 = [x, y]
                r2 = r
        if t[i][2] == '3':
            r = min(abs(x), abs(y))
            if type(best3) == str or r < best3:
                best3 = r
                t3 = [x, y]
                r3 = r
        if t[i][2] == '4':
            r = min(abs(x), abs(y))
            if type(best4) == str or r < best4:
                best4 = r
                t4 = [x, y]
                r4 = r
    return [[t1, r1], [t2, r2], [t3, r3], [t4, r4]]


def srav_chetvert(best_t, all_ch):
    t_max = -1
    koord = -1
    for i in range(len(all_ch)):
        if all_ch[i] > t_max:
            t_max = all_ch[i]
            koord = i
        elif all_ch[i] == t_max:
            if best_t[koord][1] > best_t[i][1]:
                t_max = all_ch[i]
                koord = i
    tochka = best_t[koord][0]
    r = best_t[koord][1]
    return koord+1, t_max, tochka, r


def init_1(n):
    t = []
    ch1, ch2, ch3, ch4 = 0, 0, 0, 0
    for i in range(n):
        k = list(map(int, input().split()))
        x = k[0]
        y = k[1]
        if x > 0:
            if y > 0:
                ch1 += 1
                t.append([x, y, '1'])
            elif y < 0:
                ch4 += 1
                t.append([x, y, '4'])
        elif x < 0:
            if y > 0:
                ch2 += 1
                t.append([x, y, '2'])
            elif y < 0:
                ch3 += 1
                t.append([x, y, '3'])
    all_ch = [ch1, ch2, ch3, ch4]
    return t, all_ch


def output(koord, elem, tochka, r):
    print(f'K = {koord}')
    print(f'M = {elem}')
    print(f'A = {tochka[0], tochka[1]}')
    print(f'R = {r}')


def main(n):
    t, all_ch = init_1(n)
    best_t = find_a_r(t)
    koord, elem, tochka, r = srav_chetvert(best_t, all_ch)
    output(koord, elem, tochka, r)


n = int(input())
main(n)
