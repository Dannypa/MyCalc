from typing import List

from UFraction import UFraction
import math


def lower_than(a: str, b: str):
    # compares big integers
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    index = 0
    while a[index] == b[index]:
        index += 1
    return a[index] < b[index]


def divide(numerator: int, denominator: int, digits=3) -> List[str]:
    if numerator >= denominator:
        raise ValueError("This function is supposed to return something in the interval [0;1)")
    len_denominator = math.log10(denominator)
    ans = ['.']
    cur = numerator
    multiple = False
    while len(ans) - 2 < digits:
        first = True
        if cur != 0:
            len_cur = math.ceil(math.log10(cur))
        else:
            multiple = True
            break
        while len_cur < len_denominator:
            cur *= 10
            len_cur += 1
            if not first:
                ans.append('0')
            else:
                first = False
        if cur < denominator:
            cur *= 10
            if not first:
                ans.append('0')
            else:
                first = False
        left = 1
        right = 10
        while right - left > 1:
            mid = (left + right) // 2
            if denominator * mid <= cur:
                left = mid
            else:
                right = mid
        ans.append(str(left))
        cur = cur - left * denominator
    if multiple:
        return ans
    if ans[len(ans) - 1] >= '5':
        ans.pop(len(ans) - 1)
        cur_ind = len(ans) - 1
        while ans[cur_ind] == '9':
            ans[cur_ind] = '0'
            cur_ind -= 1
        assert cur_ind > 0
        ans[cur_ind] = str(int(ans[cur_ind]) + 1)
    return ans


def find_n(digits=3) -> int:
    left = 0
    right = 1000
    while right - left > 1:
        mid = (left + right) // 2
        if len(str(math.factorial(mid + 1) // 3)) < digits:
            left = mid
        else:
            right = mid
    return right


def count_exp(digits=3) -> UFraction:
    e = UFraction(0)
    lim = find_n(digits)
    for i in range(lim + 1):
        e += UFraction(1, math.factorial(i))
    return e


def main():
    digits = int(input("Input number of digits, please:\n>> "))
    val = count_exp(digits)
    res = ['2']
    res += divide(val.numerator - 2 * val.denominator, val.denominator, digits)
    str_res = ''.join(res)
    print(str_res)
    base = "2,7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274 2746639193 2003059921 8174135966 2904357290 0334295260 5956307381 3232862794 3490763233 8298807531 9525101901 1573834187 9307021540 8914993488 4167509244 7614606680 8226480016 8477411853 7423454424 3710753907 7744992069 5517027618 3860626133 1384583000 7520449338 2656029760 6737113200 7093287091 2744374704 7230696977 2093101416 9283681902 5515108657 4637721112 5238978442 5056953696 7707854499 6996794686 4454905987 9316368892 3009879312 7736178215 4249992295 7635148220 8269895193 6680331825 2886939849 6465105820 9392398294 8879332036 2509443117 3012381970 6841614039 7019837679 3206832823 7646480429 5311802328 7825098194 5581530175 6717361332 0698112509 9618188159 3041690351 5988885193 4580727386 6738589422 8792284998 9208680582 5749279610 4841984443 6346324496 8487560233 6248270419 7862320900 2160990235 3043699418 4914631409 3431738143 6405462531 5209618369 0888707016 7683964243 7814059271 4563549061 3031072085 1038375051 0115747704 1718986106 8739696552 1267154688 9570350354".replace(' ', '').replace(',', '.')
    for i in range(len(str_res)):
        if str_res[i] != base[i]:
            print(f"Fail at i = {i}; res[i] = {str_res[i]}, base[i] = {base[i]}")


if __name__ == '__main__':
    main()
