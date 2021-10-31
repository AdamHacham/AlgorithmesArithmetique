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
        x = floor(x>>1)
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
        x = floor(M>>i)
        if x & 1 == 0:
            d[str(List[ii+1])] = (2*d[str(List[ii])]**2 - 1)%N
            d[str(List[ii+1]+1)] = (2*mul_mod_P(d[str(List[ii])],d[str(List[ii]+1)],N) - x1)%N
        if x & 1 == 1:            
            d[str(List[ii+1])] = (2*mul_mod_P(d[str(List[ii])],d[str(List[ii]+1)],N) - x1)%N
            d[str(List[ii+1]+1)] = (2*d[str(List[ii])]**2 - 1)%N
        ii = ii + 1            
        print(d)    
    return d[str(M)]

def williams(B,N):
    d = N
    M = compute_bound(B)
    e = tronc(M)
    print(e)
    while d == N:
        x1 = randint(1,N-1)
        d1 = gcd(x1,N)
        if d1 != 1:
            return d1
        xM = calcul_x(x1,M,N)
        d1 = gcd(xM - 1, N)
        print(d1)
        if d1 != 1:
            d = d1
    return d

def pow_mod_P(A, n, P):
    R = P.parent()
    n_dec = Integer(n).digits(base=2)
    n_dec.reverse()
    res = R(1)
    for c in n_dec:
        if c == 1:
            res = res*res*A % P
        else:
            res = res*res % P
    return res

def mul_mod_P(A, n, P):
    res = 0
    while A != 0:
        if (A&1) == 1:
            res = res+n 
            A = A - 1
        else:
            A = (A>>1) %P
            n = (n<<1)
    return res%P
