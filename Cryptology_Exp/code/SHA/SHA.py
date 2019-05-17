'''
SHA-1压缩函数
'''
from hashlib import sha1
import struct
import hmac as HMac
def XOR(X,Y):
    R = []
    for i in range(len(X)):
        if int(X[i]) != int(Y[i]):
            R.append('1')
        else:
            R.append('0')
    R = ('').join(R)
    return R
class SHA_1():
    regA = 0x67452301
    regB = 0xefcdab89
    regC = 0x98badcfe
    regD = 0x10325476
    regE = 0xc3d2e1f0
    message = ''
    def __init__(self,message=None):
        '''
        读入消息字符串，转化成二进制
        '''
        if message!=None:
            self.message = ('').join([format(ord(x),'08b') for x in message])

    def expandMessage(self,message=None,kind='str'):
        '''
        消息填充
        对于长度%512不足448的消息,其后第一位补1后全部补0
        return message
        '''
        if message==None:
            length = len(self.message)
        else:
            if kind=='str':
                length = len(message)*8
            elif kind=='bin':
                length = len(message)
        if length%512<448:
            expandMessage = ['1']
            curLength = length+1
            while curLength%512<448:
                expandMessage.append('0')
                curLength+=1
        if message==None:
            return self.message+('').join(expandMessage)+('').join('{:064b}'.format(length))
        else:
            if kind=='str':
                return ('').join([format(ord(x),'08b') for x in message])+('').join(expandMessage)+('').join('{:064b}'.format(length))
            elif kind=='bin':
                return message+('').join(expandMessage)+('').join('{:064b}'.format(length))
    def group(self,message):
        '''
        对填充后的消息进行分组，分组长度为512bit
        '''
        M = []
        length = len(message)
        for i in range(length//512):
           M.append(''.join(message[512*i:512*(i+1)]))
        return M
    def AND(self,X,Y):
        '''
        对两个32位字符串进行逻辑或,返回一个32位字符串
        '''
        R = []
        for i in range(len(X)):
            if int(X[i]) and int(Y[i]):
                R.append('1')
            else:
                R.append('0')
        R = ('').join(R)
        return R
    def OR(self,X,Y):
        '''
        对两个32位字符串进行逻辑或,返回一个32位字符串
        '''
        R = []
        for i in range(len(X)):
            if int(X[i]) or int(Y[i]):
                R.append('1')
            else:
                R.append('0')
        R = ('').join(R)
        return R
    def XOR(self,X,Y): 
        '''
        对两个32位字符串进行逻辑异或,返回一个32位字符串
        '''
        R = []
        for i in range(len(X)):
            if int(X[i]) != int(Y[i]):
                R.append('1')
            else:
                R.append('0')
        R = ('').join(R)
        return R
    def NOT(self,X):
        '''
        对一个32位字符串进行逻辑取反,返回一个32位字符串
        '''
        R = []
        for i in range(len(X)):
            if int(X[i]) :
                R.append('0')
            else:
                R.append('1')
        R = ('').join(R)
        return R
    def PLUS(self,X,Y):
        x = int(X,2)
        y = int(Y,2)
        z = (x+y)%(2**32)
        Z = '{:032b}'.format(z)
        return Z
    def F(self,t,B,C,D):
        if t>=0 and t<=19:
            return self.OR(self.AND(B,C),self.AND(self.NOT(B),D)) 
        elif(t>=20 and t<=39):
            return self.XOR(self.XOR(B,C),D)
        elif(t>=40 and t<=59):
            return self.OR(self.OR(self.AND(B,C),self.AND(B,D)),self.AND(C,D)) 
        elif((t>=60 and t<=79)):
            return self.XOR(self.XOR(B,C),D)
    def S(self,n,X):
        '''
        将32位字符串X循环左移n位
        '''
        R = X[n:]
        R = R+X[:n]
        return R
    def compresssionFunc(self,M):
        K = ['{:032b}'.format(0x5a827999),'{:032b}'.format(0x6ed9eba1),
                '{:032b}'.format(0x8f1bbcdc),'{:032b}'.format(0xca62c1d6)]
        H = ['{:032b}'.format(self.regA),'{:032b}'.format(self.regB),
                '{:032b}'.format(self.regC),'{:032b}'.format(self.regD),
                '{:032b}'.format(self.regE)]
        for m in M:
            W = []
            #初始化W0~W79
            for i in range(16):
                W.append(m[32*i:32*(i+1)])
            for i in range(16,80):
                W.append(self.S(1,self.XOR(self.XOR(W[i-3],W[i-8]),self.XOR(W[i-14],W[i-16]))))
            A = H[0]
            B = H[1]
            C = H[2]
            D = H[3]
            E = H[4]
            for t in range(0,80):
                TEMP = self.PLUS(self.PLUS(self.PLUS(self.PLUS(self.S(5,A),self.F(t,B,C,D)),E),W[t]),K[t//20])
                E = D
                D = C
                C = self.S(30,B)
                B = A
                A = TEMP
            H[0] = self.PLUS(H[0],A)
            H[1] = self.PLUS(H[1],B)
            H[2] = self.PLUS(H[2],C)
            H[3] = self.PLUS(H[3],D)
            H[4] = self.PLUS(H[4],E)
        result = ('').join(H)
        return result

    def getDigest(self,m=None):
        message = self.expandMessage(message=m)
        M = self.group(message)
        result = self.compresssionFunc(M)
        return result

        
def hmac(key,m,kind='sha1'):
    if kind=='sha1':
        blockSize = 512
        sha1 = SHA_1(message=m)
        #对m进行填充
        m = sha1.expandMessage()

        key = ('').join([format(ord(x),'08b')for x in key])

        if len(key)>blockSize:
            #对key进行消息摘要
            shakey = SHA_1()
            expandMessage = shakey.expandMessage(key,'bin')
            M = shakey.group(expandMessage)
            key = shakey.compresssionFunc(M)
        if len(key)<blockSize:
            #对key进行0填充
            expandk = ('').join(['0']*(blockSize-len(key)))
            k = key+expandk

        okeypad =('').join(['{:08b}'.format(0x5c)]*64)
        # print(okeypad)
        ikeypad =('').join(['{:08b}'.format(0x36)]*64)
        # print(ikeypad)
        o_key_pad = XOR(k,okeypad)
        i_key_pad = XOR(k,ikeypad)
        sha = SHA_1()
        M = sha.group(i_key_pad+m)
        result = sha.compresssionFunc(M)#result = H(k^ipad+m)

        okeypad_result = o_key_pad+result
        expandMessage = sha.expandMessage(okeypad_result,'bin')

        M = sha.group(expandMessage)
        print(M)
        result = sha.compresssionFunc(M)#result = H(k^opad+H(k^ipad+m))

        return result


if __name__ == "__main__":

    key = b'yangwaiwai'
    message = b'nishishui,weileshui,wodexiongdijiemeibuliulei.'  
    h = HMac.new(key,message,digestmod = 'sha1')
    print('HMAC结果:',h.hexdigest())
