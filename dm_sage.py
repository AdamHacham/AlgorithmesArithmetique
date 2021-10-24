def is_powersmooth(x, B):
    dec_fp = list(factor(x))
    for f in dec_fp:
        if f[0]**f[1] > B:
           return false
    return true

def ppcm(a, b):
    return (a * b /gcd(a, b))

def compute_bound(B):
    args = range(2,B+1)
    r = 1
    for i in args:
        r = ppcm(r,i)
    return r

def tronc(M):
    x = M
    T = []
    while x > 1:
        T.append(x)
        x = x>>1
    T.append(x)
    print(T)
