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
    T.reverse()
    return T

def calcul_x(x1, M, N):
    List = tronc(M)
    d = dict([("1", x1)])
    ex = 1
    size1 = log(M,2)
    i = floor(size1)
    ii = 0
    while i > 0:
        i = i-1
        if ((M>>i) & 1) == 0 :
            d[str(List[ii+1])] = 2*d[str(List[ii])]**2 - 1
            d[str(List[ii+1]+1)] = 2*d[str(List[ii])]*d[str(List[ii]+1)] - x1
            print(d)
        if ((M>>i) & 1) == 1:
            d[str(List[ii+1])] = Integer(2)*d[str(List[ii])]*d[str(List[ii]+1)] - x1
            d[str(List[ii+1]+1)] = 2*d[str(List[ii])]**2 - 1
            print(d)

        ii = ii + 1            
#        ex = l
#        z1 = 2*Xi[1]*Xi[l+1] - x1
    print(d)
#        print(z1)
