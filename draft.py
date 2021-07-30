from sys import stdout
n = -1


def get_min_max(i: int, j: int) -> (int, int):
    print(f"? 1 {i + 1} {j + 1} {n - 1}")
    stdout.flush()
    max1 = int(input())
    print(f"? 2 {i + 1} {j + 1} {1}")
    stdout.flush()
    min1 = int(input())
    return min1, max1


def fix(p):
    ind1 = -1
    ind2 = -1
    for i in range(n):
        if p[i] == n - 1 and ind1 == -1:
            ind1 = i
        elif p[i] == n - 1:
            ind2 = i
    if ind2 != -1:
        ind = 0
        while ind in (ind1, ind2):
            ind += 1
        print(f"? 1 {ind + 1} {ind1 + 1} {n - 1}")
        stdout.flush()
        res1 = int(input())
        print(f"? 1 {ind1 + 1} {ind + 1} {n - 1}")
        res2 = int(input())
        if n in (res1, res2):
            p[ind1] = n
        else:
            p[ind2] = n
    ind1 = -1
    ind2 = -1
    for i in range(n):
        if p[i] == 2 and ind1 == -1:
            ind1 = i
        elif p[i] == 2:
            ind2 = i
    if ind2 != -1:
        ind = 0
        while ind in (ind1, ind2):
            ind += 1
        print(f"? 2 {ind + 1} {ind1 + 1} {1}")
        stdout.flush()
        res1 = int(input())
        print(f"? 2 {ind1 + 1} {ind + 1} {1}")
        res2 = int(input())
        if 1 in (res1, res2):
            p[ind1] = 1
        else:
            p[ind2] = 1


def main():
    global n
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [0 for i in range(n)]
        for i in range(n // 3):
            start = i * 3
            min1, max1 = get_min_max(start, start + 1)
            if min1 == max1:
                min1, max1 = get_min_max(start + 1, start)
            min2, max2 = get_min_max(start, start + 2)
            if min2 == max2:
                min2, max2 = get_min_max(start + 2, start)
            for el in (min1, max1):
                if el in (min2, max2):
                    p[start] = el
                    break
            p[start + 1] = max1 if el != max1 else min1
            p[start + 2] = max2 if el != max2 else min2
        if n % 3 == 1:
            min1, max1 = get_min_max(n - 2, n - 1)
            if min1 == max1:
                min1, max1 = get_min_max(n - 1, n - 2)
            p[n - 1] = min1 if p[n - 2] != min1 else max1
        elif n % 3 == 2:
            start = n - 3
            min1, max1 = get_min_max(start, start + 1)
            if min1 == max1:
                min1, max1 = get_min_max(start + 1, start)
            min2, max2 = get_min_max(start, start + 2)
            if min2 == max2:
                min2, max2 = get_min_max(start + 2, start)
            for el in (min1, max1):
                if el in (min2, max2):
                    p[start] = el
                    break
            p[start + 1] = max1 if el != max1 else min1
            p[start + 2] = max2 if el != max2 else min2
        fix(p)
        print('!', end=' ')
        for i in p:
            print(i, end=' ')
        print()
        stdout.flush()


def f1(a, i, j, x):
    return max(min(x, a[i - 1]), min(x + 1, a[j - 1]))


def f2(a, i, j, x):
    return min(max(x, a[i - 1]), max(x + 1, a[j - 1]))


if __name__ == '__main__':
    main()