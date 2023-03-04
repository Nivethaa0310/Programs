def dec_to_base(num, base):
    d = []
    while num > 0:
        rem = num % base
        d.append(str(rem))
        num //= base
    return ''.join(d[::-1])


N1, N2,= map(int, input().split()) 
B1, B2 = map(int, input().split())


X = dec_to_base(N1, N2)
Y = dec_to_base(B1, B2)


s = sum(int(i) for i in X + Y)


print(s)

