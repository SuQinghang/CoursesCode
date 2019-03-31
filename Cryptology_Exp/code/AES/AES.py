import numpy as np 

S = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],   
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]
S_1 = [
    [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251],
    [124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203],
    [84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78],
    [8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37],
    [114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146],
    [108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132],
    [144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6],
    [208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107],
    [58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115],
    [150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110],
    [71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27],
    [252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244],
    [31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95],
    [96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239],
    [160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97],
    [23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]
]
Rcon = [[0x01,0x00,0x00,0x00],
        [0x02,0x00,0x00,0x00],
        [0x04,0x00,0x00,0x00],
        [0x08,0x00,0x00,0x00],
        [0x10,0x00,0x00,0x00],
        [0x20,0x00,0x00,0x00],
        [0x40,0x00,0x00,0x00],
        [0x80,0x00,0x00,0x00],
        [0x1b,0x00,0x00,0x00],
        [0x36,0x00,0x00,0x00]]

#循环左移
def LeftRotate(line,n):
    new_line = line[n:]
    for i in range(0,n):
        new_line.append(line[i])
    return new_line

#读入文件
def inputText(filename):
    with open(filename,'r')as f:
        text = f.read()
    text = text.split('\n')
    text = [eval(x) for x in text]
    return text

#轮密钥加,输入为4x4矩阵
def AddRoundKey(state,w):
    w = np.array(w)
    w = w.T
    new_state = []
    for i in range(len(state)):
        s = [state[i][j] ^ w[i][j] for j in range(len(state[i]))]
        new_state.append(s)
    return new_state

#加轮密钥
def RoundKeyAdd(state,w):
    w = np.array(w)
    new_state = []
    for i in range(len(state)):
        s = [state[i][j] ^ w[i][j] for j in range(len(state[i]))]
        new_state.append(s)
    return new_state

#字代替
def SubWord(w):
    new_w = [S[int(x/16)][x%16] for x in w]
    return new_w

#两个list中元素异或
def xor(a,b):
    s = []
    for i in range(len(a)):
        s.append(a[i] ^ b[i])
    return s

#密钥扩展
def KeyExpansion(key):
    w = []
    for i in range(0,4):
        w.append(key[4*i])
        w.append(key[4*i+1])
        w.append(key[4*i+2])
        w.append(key[4*i+3])
    for i in range(4,44):
        tmp = w[4*(i-1):4*i]
        if i%4==0:
            tmp = xor(SubWord(LeftRotate(tmp,1)),Rcon[int(i/4)-1])
        new_w = xor(w[4*(i-4):4*(i-3)],tmp)
        w = w+new_w
    return w

#字节代替变换
def SubBytes(state):
    new_s = []
    for l in state:
        row = [S[int(x/16)][x%16] for x in l]
        new_s.append(row)
    return new_s

#正向行移位变换
def positive_Shift(state):
    n=1
    new_s = []
    new_s.append(state[0])
    for l in state[1:]:
        new_s.append(LeftRotate(l,n))
        n=n+1
    return new_s

#逆向行变换
def negetive_Shift(state):
    n=3
    new_s = []
    new_s.append(state[0])
    for l in state[1:]:
        new_s.append(LeftRotate(l,n))
        n=n-1
    return new_s

#列混淆元素乘法运算
def mul(a):
    ashift = (a<<1)%0x100
    if (a&0x80 == 0):
        return ashift
    else:
        return ashift^0x1b
#列混淆
def MixMatrix(state):
    new_state = []
    for i in range(len(state)):
        s = []
        for j in range(len(state[i])):
            r = (mul(state[i%4][j])
                    ^mul(state[(i+1)%4][j])^state[(i+1)%4][j]
                    ^(state[(i+2)%4][j])
                    ^(state[(i+3)%4][j]))
            s.append(r)
        new_state.append(s)
    return new_state

#逆字节代替
def Rev_SubBytes(state):
    new_s = []
    for l in state:
        row = [S_1[int(x/16)][x%16] for x in l]
        new_s.append(row)
    return new_s

#逆列混淆 
def Rev_MixMatrix(state):
    new_state = []
    for i in range(len(state)):
        s = []
        for j in range(len(state[i])):
            r = (mul(mul(mul(state[i%4][j])))^mul(mul(state[i%4][j]))^mul(state[i%4][j])    #0x0e
                    ^mul(mul(mul(state[(i+1)%4][j])))^mul(state[(i+1)%4][j])^state[(i+1)%4][j]#0x0b
                    ^mul(mul(mul(state[(i+2)%4][j])))^mul(mul(state[(i+2)%4][j]))^state[(i+2)%4][j]#0x0d
                    ^mul(mul(mul(state[(i+3)%4][j])))^state[(i+3)%4][j]#0x09
                    )
            s.append(r)
        new_state.append(s)
    return new_state
#将密文写入文件
def writeFile(filename,Cipher):
    f = open(filename,'w+')
    for i in range(len(Cipher)-1):
        f.write(Cipher[i]+'\n')
    f.write(Cipher[-1])

#AES加密    
def AES_Encrypt(ptfile,keyfile,cipherfile):
    #读入明文
    plaintext = inputText(ptfile)
    print('明文: ',[hex(x) for x in plaintext])
    plaintext = np.array(plaintext)
    plaintext = plaintext.reshape(4,4)
    #求转置
    plaintext = plaintext.T
    #读入密钥
    key = inputText(keyfile)
    #密钥扩展
    w = KeyExpansion(key)
    new_w = []
    for i in range(0,int(len(w)/4)):
        new_w.append(w[4*i:4*i+4])
    w = new_w
    #加密过程#
    #第一次轮密钥加
    state = AddRoundKey(plaintext,w[0:4][:])
    #9轮四步变换
    for i in range(1,10):
        state = SubBytes(state)
        state = positive_Shift(state)
        state = MixMatrix(state)
        state = AddRoundKey(state,w[4*i:4*(i+1)][:])

    #第10三步变换
    state = SubBytes(state)
    state = positive_Shift(state)
    state = AddRoundKey(state,w[40:44][:])

    Cipher = []
    for l in state:
        Cipher+=(['0x{:02x}'.format(x) for x in l])
    print('加密后的密文: ',Cipher)
    writeFile(cipherfile,Cipher)

#AES解密
def AES_Decrypt(cipherfile,keyfile,ptfile):
    #读入密文
    ciphertext = inputText(cipherfile)
    ciphertext = np.array(ciphertext)
    ciphertext = ciphertext.reshape(4,4)
    # print('密文')
    # for l in ciphertext:
    #     print([hex(x) for x in l])
    # print('---------------------------------------')
    #读入密钥
    key = inputText(keyfile)
    #密钥扩展
    w = KeyExpansion(key)
    new_w = []
    for i in range(0,int(len(w)/4)):
        new_w.append(w[4*i:4*i+4])
    w = new_w
    #解密过程
    #第一次轮密钥加
    state =AddRoundKey(ciphertext,w[40:44][:])

    #9轮四步变换
    for i in range(9,0,-1):
        state = negetive_Shift(state)
        # print('逆向移位: ')
        # for l in state:
        #     print([hex(x) for x in l])
        # print('-----------------------------------------')

        state = Rev_SubBytes(state)
        # print('逆向字节代替:' )
        # for l in state:
        #     print([hex(x) for x in l])
        # print('-----------------------------------------')

        state = AddRoundKey(state,w[4*i:4*(i+1)])
        # print('加轮密钥: ')
        # for l in state:
        #     print([hex(x) for x in l])
        # print('-----------------------------------------')

        state = Rev_MixMatrix(state)
        # print('逆向列混淆: ')
        # for l in state:
        #     print([hex(x) for x in l])
        # print('-----------------------------------------')
        
        
    #第10轮三步变换
    state = negetive_Shift(state)
    state = Rev_SubBytes(state)
    state = AddRoundKey(state,w[0:4])
    state = np.array(state).T
    plaintext = []
    for l in state:
        plaintext+=(['0x{:02x}'.format(x) for x in l])
    print('解密后的明文: ',plaintext)
    writeFile(ptfile,plaintext)
            

if __name__ == "__main__":
    AES_Encrypt('plaintext.txt','key.txt','Cipher.txt')
    AES_Decrypt('Cipher.txt','key.txt','de_pliantext.txt')