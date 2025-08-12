//baekjoon string 27866 8/12
//파이썬과 같은 방식으로 string 값을 리스트처럼 나누어서 i에 해당하는 값을 구하는 방식으로 구현
#include <iostream>
using namespace std;
#include <string>

int main(){
    string s;
    int i;
    cin>>s>>i;
    cout<<s[i-1];
}