//#baekjoon twodimensional ordering 2738 9/18
//파이썬에는 메서드를 이용해서 값을 넣었다면 c프로그램은 더한 갑을 2차원 배열pri에 해당하는 값을 넣어서 출력하는 방식으로 구현
#include <stdio.h>

int main(void){
    int n,m;
    int input1[100][100];
    int input2[100][100];
    int pri[100][100];
    scanf("%d %d",&n,&m);
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%d", &input1[i][j]);
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%d", &input2[i][j]);
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            pri[i][j]=input1[i][j]+input2[i][j];
        }
    }
        for (int i=0; i<n; i++) {        
            for (int j=0; j<m; j++) {    
                printf("%d ", pri[i][j]);
        }
        printf("\n");
    }
}