//baekjoon one dimensional ordering 5597 c++ 8/11
// bool을 이용해서 found배열을 이용해서 받은 리스트 값과 비교해서 유무에 따라 false와 true로 구분해서 false인 값을 찾아내는 방식으로 구현
//이전 파이썬에 내장함수와 달리 for문을 이용해서 일일히 비교하면서 구현

#include <iostream>
using namespace std;

int main(void){
    int arr[28];
    int n=0, m=0;
    for(int i=0; i<28; i++){
        cin >> arr[i];
    }
    bool found[31] = {false}; // 1부터 30까지의 숫자를 찾기 위해 31크기의 배열을 사용
    for(int i=0; i<28; i++){
        found[arr[i]] = true; //해당값이 존재함으로 true로 변경
    }
    for(int i=1; i<=30; i++){
        if(!found[i]){
            if(n == 0) {
                n = i; 
            } else {
                m = i;
            }      
        }
    }
    if(n < m) {
        cout << n << endl << m;
    } else {
        cout << m << endl << n;
    }
}

// 초기 코드
// 시간 초과 문제--- 불필요한 반복문이 문제

// #include <iostream>
// using namespace std;

// int main(void){
//     int arr[28];
//     int pri[2];
//     int x=0;
//     for(int k=0; k<28; k++){
//         cin >> arr[k];
//     }
//     for(int i=1; i<=30;){
//         for(int j=0; j<=27;){
//             if (arr[j]!=i){
//                 x=i;
//                 for(int t=0; t<28; t++){
//                     if(arr[t]==x){
//                         x=0;
//                         break;}
//                     else{
//                         pri[0]=x;
//                         if (pri[0]!=0){
//                             pri[1]=x;}}}
//                 i++;}
//             if(arr[j]==i){
//                 i=1;
//                 j++;
//                 x=0;}}   
//         if (pri[0]<pri[1]){
//             cout<<pri[0];
//             cout<<pri[1];}
//         else{
//             cout<<pri[1];
//             cout<<pri[0];}}}

