//
// Created by subuntu on 19-3-10.
//
//代换密码
#include <iostream>
using namespace std;
void substitution_crypt(char *plaintext,char*key,char*ciphertext){
    int k;
    if(isdigit(key[0])){
        k = atoi(key);
        int i;
        for(i=0;plaintext[i];i++){
            ciphertext[i] = plaintext[i]+k%26;
        }
        ciphertext[i]=0;
    }else{
        cout<<"key must be digit!"<<endl;
        exit(0);
    }
}
void substitution_decrypt(char*plaintext,char*key,char*ciphertext){
    int k;
    if(isdigit(key[0])){
        k = atoi(key);
        int i;
        for(i=0;ciphertext[i];i++){
            plaintext[i] = char(ciphertext[i]-(k%26));

        }
        plaintext[i] = 0;
    }else{
        cout<<"key must be digit!"<<endl;
        exit(0);
    }
}
int main(int argc,char** argv){
    char plaintext[100],key[100],ciphertext[100];
    cout<<"input plaintext:";
    cin>>plaintext;
    cout<<"input key:";
    cin>>key;
    substitution_crypt(plaintext,key,ciphertext);
    cout<<"ciphertext is :"<<ciphertext<<endl;
    char de_plaintext[100];
    substitution_decrypt(de_plaintext,key,ciphertext);
    cout<<"plaintext is :"<<de_plaintext<<endl;
    return 0;
}
