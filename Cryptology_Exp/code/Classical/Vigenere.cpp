//
// Created by subuntu on 19-3-10.
//
//Vigenere密码实现
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

void ISD_Vigenere_crypt(string m,string k,char*r){
    int i,j,s = 0;
    j = k.size();
    for(i=0;m[i];i++){
        m[i] = tolower(m[i]);
    }
    for(i=0;k[i];i++){
        k[i] = tolower(k[i]);
    }
    for(i=0;m[i];i++){
        if(isalpha(m[i])){
            r[i] = (m[i]-'a'+k[s%j]-'a')%26+'a';
            s++;
        }else{
            r[i] = m[i];
        }
    }
    r[i]=0;
}
void ISD_Vigenere_decrypt(char *c,char k[],char m[]){
    int i,j,s=0;
    j = strlen(k);
    for(i=0;c[i];i++){
        c[i] = tolower(c[i]);
    }
    for(i=0;k[i];i++){
        k[i] = tolower(k[i]);
    }
    for(i=0;c[i];i++){
        if(isalpha(c[i])){
            m[i] = (c[i]-k[s%j]+26)%26+'a';
            s++;
        }else{
            m[i] = c[i];
        }
    }
    m[i]=0;
}
int main(int argc,char *argv[]){

    char plaintext[100],ciphertext[100],key[100];
    cout<<"input plaintext:";
    cin>>plaintext;
    cout<<"input key:";
    cin>>key;
    ISD_Vigenere_crypt(plaintext,key,ciphertext);
    cout<<"输入的明文：";
    cout<<plaintext<<endl;
    cout<<"输入的key：";
    cout<<key<<endl;
    cout<<"加密后的密文：";
    cout<<ciphertext<<endl;
    char *de_plaintext ;
    char *de_ciphertext =ciphertext;
    ISD_Vigenere_decrypt(de_ciphertext,key,de_plaintext);
    cout<<"解密后得到的明文:"<<de_plaintext<<endl;

    return 0;
}
