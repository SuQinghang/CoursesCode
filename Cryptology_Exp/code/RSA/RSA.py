from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
#扩展欧几里得算法计算私钥x
#a=(p-1)*(q-1),b = e
def ex_gcd(a,b):
    if b==0:
        return 1,0,a
    if b<0:
        b=-b
    x,y,r = ex_gcd(b,a%b)
    x,y = y,x-a//b*y
    return x,y,r

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
#简单的示例程序
def example_rsa():
    plaintext =[33,14,22,62,00,17,4,62,24,14,20,66]
    plaintext = [plaintext[i]*100+plaintext[i+1] for i in range(0,len(plaintext),2)]
    print('plaintext: ',plaintext)
    print('----------------------------------')
    p = 73
    q = 151
    e = 11
    n = p*q
    print('n: ',n)
    print('----------------------')
    #计算密钥d
    x,y,r = ex_gcd((p-1)*(q-1),e)
    d = y%((p-1)*(q-1))
    if d<0:
        d +=((p-1)*(q-1))
    print('d: ',d)
    print('--------------------')
    #加密
    ciphertext  = [mod(m,e,n) for m in plaintext]
    print('ciphertext: ',ciphertext)
    print('---------------------------')
    #解密
    decryptext = [mod(m,d,n) for m in ciphertext]
    print('decryptext: ',decryptext)

#利用Crypto实现RSA
def rsa():
    #伪随机数生成
    random_generator = Random.new().read
    #生成rsa实例,默认e=65537
    rsa = RSA.generate(1024,random_generator)
    #生成密钥对
    private_pem = rsa.exportKey()
    public_pem = rsa.publickey().exportKey()
    #生成公私钥文件
    with open('privateKey.pem','wb') as f:
        f.write(private_pem)
        f.close()
    with open('publicKey.pem','wb')as f:
        f.write(public_pem)
        f.close()
    #利用公私钥进行加密解密
    message = 'Hello world! Today is Friday!'
    #利用公钥加密
    with open('publicKey.pem','r')as f:
        key = f.read()
        publicKey = RSA.importKey(key)
        f.close()
    cipher = PKCS1_v1_5.new(publicKey)
    ciphertext = cipher.encrypt(bytes(message,'utf8'))
    print('ciphertext: ',ciphertext)
    print('------------------------------')
    #利用私钥解密
    privateKey = RSA.importKey(open('privateKey.pem').read())
    decipher = PKCS1_v1_5.new(privateKey)
    plaintext = decipher.decrypt(ciphertext,'Error')
    print('plaintext: ',plaintext)
    
if __name__ == "__main__":
    #expample
    #example_rsa()
    rsa()