# 分组密码——DES加密解密（python实现）

​	DES(Data Encryption Standard)采用64位的分组长度和56位的密钥长度。它将64位的输入经过一系列变换得到64为的输出。解密使用相同的步骤和相同的密钥，唯一不同的是密钥顺序与加密过程相反。

DES加密：

​	该算法的输入有需要加密的明文和加密使用的密钥，二者长度都为64位。其中密钥的第8,16,24,32,40,48,56,64位为奇偶校验位。

1、明文的处理

​	将明文读入程序并将其化为二进制串

```python
def inputText(filename):
    with open(filename,'r')as f:
        text = f.read()
    text = text.split('\n')
    text = [eval(x) for x in text]
    text = ['{:08b}'.format(x) for x in text]
    text = ''.join(text)
    
    return text
```

​	对明文进行IP置换，并划分为左右两个子串

```python
def IP_Transposition(plaintext):
    LR = []
    for i in IP:
        LR.append(int(plaintext[i-1]))
    L = LR[:32]
    R = LR[32:]
    return L,R
```

2、对密钥的处理

​	将密钥读入程序并以二进制串的形式存储

​	对密钥进行PC-1置换，并划分为两个子串

```python
#密钥置换
def Key_Transposition(key):
    CD = []
    for i in PC_1:
        CD.append(int(key[i-1]))
    C = CD[:28]
    D = CD[28:]
    return C,D
```

​	在生成迭代所需要的密钥之前需要对密钥进行置换压缩

```python
#密钥压缩
def Key_Compress(C,D):
    key = C+D
    new_key = []
    for i in PC_2:
        new_key.append(key[i-1])
    return new_key
```

​	生成DES每轮迭代所需要的子密钥，以便加密解密时直接使用

```python
def generateKset(key):
    key = inputKey(key)
    C,D = Key_Transposition(key)
    K = []
    for i in LeftRotate:
        C = Key_LeftRotate(C,i)
        C = Key_LeftRotate(D,i)
        K.append(Key_Compress(C,D))
    return K
```

3、F函数

在每轮变换中，整个过程可以用以下公式表示：
$$
L_i = R_{i-1}
$$

$$
R_i = L_{i-1}\bigoplus F(R_{i-1},K_i)
$$

其中轮密钥$K_i$长48位,$R$长32位，首先将$R$置换扩展为48位,这48位与$K_i$异或，得到的结果用替代函数作用产生32位的输出。这32位的输出经过$P$置换后与$L_{i-1}$异或得到新的$R_i$

代替函数由8个$S$盒来组成，每个$S$盒都有6位的输入和4位的输出。对每个$S$盒，输入的第一位和最后一位组成一个2位的二进制数，用来选择$S$盒4行替代值中的一行，中间4位用来选择16列中的某一列。
```python
#明文R扩展为48位
def R_expand(R):
    new_R = []
    for i in E:
        new_R.append(R[i-1])
    return new_R

#将两列表元素异或
def xor(input1,input2):
    xor_result = []
    for i in range(0,len(input1)):
        xor_result.append(int(input1[i])^int(input2[i]))
    return xor_result

#将异或的结果进行S盒代替
def S_Substitution(xor_result):
    s_result = []
    for i in range(0,8):
        tmp = xor_result[i*6:i*6+5]
        row = tmp[0]*2+tmp[-1]
        col = tmp[1]*8+tmp[2]*4+tmp[3]*2+tmp[4]
        s_result.append('{:04b}'.format(S[i][row][col]))
    s_result = ''.join(s_result)
    return s_result
#F函数
def F(R,K):
    new_R = R_expand(R)
    R_Kxor= xor(new_R,K)
    s_result = S_Substitution(R_Kxor)
    p_result = P_Transposition(s_result)
    return p_result

#将S盒代替的结果进行P置换
def P_Transposition(s_result):
    p_result = []
    for i in P:
        p_result.append(int(s_result[i-1]))
    return p_result
```
4、加密过程

DES加密需要经过$16$轮迭代，前$15$轮迭代每次结束需要交换$L_i$和$R_i$，第16次不交换
```python
def DES_encrypt(filename,key,outputFile):
    #从文件中读取明文
    plaintext = inputText(filename)
    #将明文进行置换分离
    L,R = IP_Transposition(plaintext)
    #生成Kset
    K = generateKset(key)
    for i in range(0,15):
        oldR = R
        #F函数
        p_result = F(R,K[i])
        R = xor(L,p_result)
        L = oldR
    p_result = F(R,K[15])
    L = xor(L,p_result)
    #IP逆置换
    reversedP = IP_reverseTransp(L+R)
    #生成16进制表示的密文
    Cipher = generateHex(reversedP)
    #将密文写入outputFile文件
    writeFile(outputFile,Cipher)
    return Cipher
```

DES解密：

```python
def DES_decrypt(filename,key,outputFile):
    #文件中读取密文
    Ciphertext = inputText(filename)
    #将密文进行置换分离
    L,R = IP_Transposition(Ciphertext)
    #生成Kset
    K = generateKset(key)
    for i in range(15,0,-1):
        oldR = R
        #F函数
        p_result = F(R,K[i])
        R = xor(L,p_result)
        L = oldR
    
    p_result = F(R,K[0])
    L = xor(L,p_result)
    reversedP = IP_reverseTransp(L+R)
    plaintext = generateHex(reversedP)
    writeFile(outputFile,plaintext)
    return plaintext
```