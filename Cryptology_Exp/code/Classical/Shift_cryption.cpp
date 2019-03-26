//
// Created by subuntu on 19-3-10.
//
//移位密码算法
#include <iostream>
#include <string>
using namespace std;
    void ISD_Shift_Crypt(string &code,int k){
        int i;
        for(i=0;i<code.length();i++){
            //向右移动k位，相当于求补
            if((code[i]+k)>'z'){
                code[i] = ((code[i]+k)%'z')+'a'-1;
            }else{
                code[i] = code[i]+k;
            }
            code[i] = code[i]-32;
        }
    }
void ISD_Shift_decrypt(string &code,int k){
    int i;
    for(i=0;i<code.length();i++){
        if((code[i]-k)<'A'){
            //向左
            code[i] = 'Z'-('A'-(code[i]-k))+1;
        }else{
            code[i] = code[i]-k;
        }
        code[i]=code[i]+32;
    }
}
int main(){
    int k;
    string code;
    cout<<"请选择\n 移位加密：0,解密：1:";
    int n;
    cin>>n;
    switch (n){
        case 0:
            cout<<"input plaintext:";
            cin>>code;
            cout<<"input key:";
            cin>>k;
            ISD_Shift_Crypt(code,k);
            cout<<"ciphertext is :"<<code;
            break;
        case 1:
            cout<<"input ciphertext:";
            cin>>code;
            cout<<"input key:";
            cin>>k;
            ISD_Shift_decrypt(code,k);
            cout<<"plaintext is :"<<code;
            break;
    }
}