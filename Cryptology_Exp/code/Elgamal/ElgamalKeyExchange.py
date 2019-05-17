from Crypto.Util import number
from elgamal import mod,ex_gcd
from Crypto import  Random 
from Crypto.Random import random

#扩展欧几里得算法
def Euclid(a,b):
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    q = 0
    if r1==0:
        s = s0
        t = t0
    else:
        q = r0//r1
        r0 = r0-q*r1
    while(r0!=0):
        s = s1
        s1 = s0-q*s1
        s0 = s
        t = t1
        t1 = t0-q*t1
        t0 = t
        q = t1//r0
        r = r0
        r0 = r1-q*r0
        r1 = r
    s = s1
    t = t1
    if s<0:
        s = b+s
    return s
#Elgamal加密函数
def Encrypt(g,y,m,p):
    #随机生成一个整数r
    r = random.StrongRandom().randint(1,p-1)
    c1 = mod(g,r,p)
    tmp = mod(y,r,p)
    c2 = (m*tmp)%p
    print('Y的加密结果为({0},{1})'.format(c1,c2))
    return c1,c2

#Elgamal数字签名函数
def Sign(c1,c2,g,p,x):
    k = int(input('请输入随机数k:'))
    # k1 = Euclid(k,p-1)
    x1,k1,r = ex_gcd(p-1,k)
    k1 = k1%(p-1)
    if k1<0:
        k1+=p-1
    #对c1进行数字签名
    r1 = mod(g,k,p)
    tmp = c1-x*r1
    s1 = (tmp*k1)%(p-1)
    #对c2进行数字签名
    r2 = mod(g,k,p)
    tmp = c2-x*r2
    s2 = (tmp*k1)%(p-1)
    if s1<0:
        s1 += p-1
    if s2<0:
        s2 += p-1
    print('密文的数字签名分别为(r1:{0},s1:{1},r2:{2},s2:{3})'.format(r1,s1,r2,s2))
    return r1,s1,r2,s2

#签名验证函数
def Verify(y,g,r,s,m,p):
    tmp1 = mod(y,r,p)
    tmp2 = mod(r,s,p)
    i = (tmp1*tmp2)%p
    j = mod(g,m,p)
    if i==j:
        return True
    else:
        return False

#Elgamal解密函数
def Decrypt(c1,c2,d,p):
    tmp = mod(c1,d,p)
    #y = Euclid(tmp,p)
    x,y,r = ex_gcd(p,tmp)
    y = y%p
    if y<0:
        y+=p
    print('Decrypt ax^(-1):',y)
    m = (c2*y)%p
    #print('解密结果：',m)
    return m
#
def KeyExchange():    
    #D-H密钥交换
    #先取一个大素数p和生成元G
    p1 = int(input('请输入D-H大素数p1:'))
    while not number.isPrime(p1):
        p1 = int(input('输入的p1非素数，请重新输入:'))
    g1 = int(input('请输入D-H生成元g1：'))

    #Elgamal加密，取一个小素数p和生成元g
    p2 = int(input('请输入加密素数p2:'))
    while not number.isPrime(p2):
        p2 = int(input('输入的p2非素数，请重新输入:'))
    g2 = int(input('请输入加密生成元g2:'))
    #选择一个随机数d作为密钥，计算y
    d = int(input('请输入私钥d:'))
    y1 = mod(g2,d,p2)
    print('Elgamal加密的公钥为({0},{1},{2})'.format(y1,g2,p2))
    print('------------------------------------------')

    #Elgamal数字签名
    p3 = int(input('请输入用于数字签名的素数p3:'))
    while not number.isPrime(p3):
        p3 = int(input('输入的p3非素数，请重新输入:'))
    g3 = int(input('请输入数字签名生成元g3:'))
    x = int(input('请输入数字签名随机整数x:'))
    y2 = mod(g3,x,p3)
    print('数字签名的公钥y2=',y2)
    print('---------------------------------------------')

    #Alice和Bob进行密钥交换
    #1、Alice秘密选定一个整数XA，1<=XA<=p1-2,并计算YA=g^XA mod p1，将YA发送给Bob
    XA = int(input('Alice 秘密选定一个XA:'))
    while not (XA>=1 and XA<=p1-2):
        XA = int(input('XA需满足1<=XA<=p1-2,请重新输入:'))
    YA = mod(g1,XA,p1)
    print('YA=',YA)
    c1,c2 = Encrypt(g2,y1,YA,p2)
    r1,s1,r2,s2 = Sign(c1,c2,g3,p3,x)

    #2、Bob秘密选定一个整数XB,计算YB发送给Alice
    XB = int(input('Bob 秘密选定一个XB:'))
    while not (XB>=1 and XB<=p1-2):
        XB = int(input('XB需满足1<=XA<=p1-2,请重新输入:'))
    YB = mod(g1,XB,p1)
    print('YB=',YB)
    c3,c4 = Encrypt(g2,y1,YB,p2)
    #print('c1={0},c2={2}'.format(c1,c2))
    r3,s3,r4,s4 = Sign(c3,c4,g3,p3,x)

    #验证数字签名的有效性
    z0 = Verify(y2,g3,r3,s3,c3,p3)
    z1 = Verify(y2,g3,r4,s4,c4,p3)
    z2 = Verify(y2,g3,r1,s1,c1,p3)
    z3 = Verify(y2,g3,r2,s2,c2,p3)
    print('验证结果:',z0,z1,z2,z3)
    if (z0 and z1 and z2 and z3):
        print('数字签名验证有效')
    else:
        print('数字签名验证无效，密钥k无效')
        exit()
    YA1 = Decrypt(c1,c2,d,p2)
    YB1 = Decrypt(c3,c4,d,p2)
    print('解密得到的YA:',YA1)
    print('解密得到的YB:',YB1)

    k = mod(YB1,XA,p1)
    print('Alice 计算得到的密钥k=',k)
    k = mod(YA1,XB,p1)
    print('Bob 计算得到的密钥k=',k)
if __name__ == "__main__":
    KeyExchange()

