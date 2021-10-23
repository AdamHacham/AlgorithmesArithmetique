def is_powersmooth(x, B):
    dec_fp = list(factor(x))
    for f in dec_fp:
        if f[0]**f[1] > B:
           return false
    return true

def lcm(a, b):
    return (a * b /gcd(a, b))

def compute_bound(B):
    args = range(2,B+1)
    r = 1
    for i in args:
        r = lcm(r,i)
    return r
