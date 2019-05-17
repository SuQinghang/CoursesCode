from Crypto import  Random 
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD

#蒙哥马利幂模算法
#return m^e%n
def mod(m,e,n):
    #把e化为二进制
    E = list('{:b}'.format(e))
    d = 1
    for i in E:
        if i=='0':
            d = (d*d)%n
        else:
            d = (d**2*m)%n
    return d
#扩展欧几里得算法
def ex_gcd(a,b):
    if b==0:
        return 1,0,a
    if b<0:
        b=-b
    x,y,r = ex_gcd(b,a%b)
    x,y = y,x-a//b*y
    return x,y,r
def elgamal():
    #伪随机数生成器
    random_generator = Random.new().read
    #生成elgamal Key
    elgKey = ElGamal.generate(256,random_generator)
    #生成私钥
    while 1:
        alpha = random.StrongRandom().randint(1,elgKey.p-1)
        if GCD(alpha,elgKey.p-1)==1:
            break

    h = mod(elgKey.g,alpha,elgKey.p)
    message =[33,14,22,62,00,17,4,62,24,14,20,66]
    print('message: ',message)
    #加密过程
    #1.随机选择整数y
    y = random.StrongRandom().randint(1,elgKey.p-1)
    #2.计算c1
    c1 = mod(elgKey.g,y,elgKey.p)
    #3.计算s
    s = mod(h,y,elgKey.p)
    #4.对message进行加密
    ciphertext = [(m*s)%(elgKey.p) for m in message]
    print('ciphetext: ',ciphertext)

    #解密过程
    #1.通过c1计算得到s
    de_s = mod(c1,alpha,elgKey.p)
    #2.获得明文
    x,y,r = ex_gcd(elgKey.p,de_s)
    s_reverse = y%(elgKey.p)
    if s_reverse<0:
        s_reverse+=elgKey.p
    plaintext = [(m*s_reverse)%(elgKey.p) for m in ciphertext]
    print('plaintext: ',plaintext)

if __name__ == "__main__":
    elgamal()