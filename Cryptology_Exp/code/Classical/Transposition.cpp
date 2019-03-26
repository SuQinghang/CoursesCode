#include <iostream>
using namespace std;

//m为输入的明文
char a[20][6],b[20][6],bb[10],c[20][6],m[102],key[6],ky[6],mw[10];
int zh[6],zh1[6];
int row,len,length,e,f;
void ISD_zhihuan(int le){
    int i,j=0,s=0;
    //明文长度为6的倍数
    if(len%6==0){
        for(j=0;j<(le/6);j++){
            for(i=0;i<6;i++,s++){
                a[j][i] = m[s];
            }
        }
    }else{
        //在明文后补X
        for(j=0;j<(le-le%6)/6;j++){
            for(i=0;i<6;i++,s++){
                a[j][i]=m[s];
            }
        }
        j++;
        int w=0;
        for(int l=le-le%6;l<le;l++,w++){
            a[j][w]=m[w];
        }
        for(int ll=le%6;ll<6;ll++){
            a[j][ll]='X';
        }
    }
    row = j;
    length = 6*j;
}
void ISD_zhihuan_encrypt(){
    cout<<"请输入密钥,要求是6位字母："<<endl;
    cin>>key;
    for(int i=0;i<6;i++) {
        ky[i] = key[i];
    }
    char tmp;
    for(int i=0;i<6;i++){
        for(int j=0;j<5;j++){
            if(key[j]>key[j+1]){
                tmp = key[j];
                key[j] = key[j+1];
                key[j+1] = tmp;
            }
        }
    }
    for(int i=0;i<6;i++) {
        cout<<key[i];
    }
    cout<<endl;
    int w,v;
    for(w=0;w<6;w++){
        for(v=1;v<=6;v++){
            if(ky[w]==key[v-1]){
                zh[w] = v;
            }
        }
    }
    //置换过程
    int q=0;
    for(int g=0;g<row;g++){
        for(int h=0;h<6;h++,q++){
            b[g][h] = a[g][zh[h]-1];
            bb[q] = b[g][h];
        }
    }
    cout<<"加密后的密文："<<endl;
    for(int i=0;i<=q;i++){
        cout<<bb[i];
    }
    cout<<endl;
}
void ISD_zhihuan_decrypt(){
    int ss[6] = {1,2,3,4,5,6};
    for(int w=0;w<6;w++){
        for(int p=0;p<6;p++){
            if(ss[w]==zh[p])
                zh1[w]=p+1;
        }
    }
    int t=0;
    for(int g=0;g<=row;g++){
        for(int h=0;h<6;h++,t++){
            c[g][h] = b[g][zh1[h]-1];
            mw[t] = c[g][h];
        }
    }
    cout<<"解密后的明文："<<endl;
    for(int i=0;i<=t;i++){
        cout<<mw[i];
    }
    cout<<endl;
}
int main() {
    cout<<"请输入明文:";
    cin>>m;
    int k=0;
    while(m[k]!='\0'){
        k++;
    }
    len = k;
    cout<<"明文长度len="<<len<<endl;
    ISD_zhihuan(len);
    ISD_zhihuan_encrypt();
    ISD_zhihuan_decrypt();
    return 0;
}