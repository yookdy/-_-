#include <stdio.h>

int main(void) {
    int N;
    if (scanf("%d", &N) != 1) return 0;
    int Arr[N];

    double Sum = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
        Sum += Arr[i];
    }

    for (int j = 0; j < N - 1; j++) {
        for (int i = 0; i < N - 1 - j; i++) {
            if (Arr[i] > Arr[i + 1]) {
                int temp = Arr[i];
                Arr[i] = Arr[i + 1];
                Arr[i + 1] = temp;
            }
        }
    }

    int avg = (int)(Sum / N + (Sum >= 0 ? 0.5 : -0.5));

    int mid = Arr[N / 2];
    int mode = Arr[0];
    int max_count = 0;
    int current_count = 0;

    for (int i = 0; i < N; i++) {
        if (i > 0 && Arr[i] == Arr[i - 1]) {
            current_count++;
        } else {
            current_count = 1;
        }

        if (current_count > max_count) {
            max_count = current_count;
            mode = Arr[i];
        }
    }

    int range = Arr[N - 1] - Arr[0];

    printf("%d\n", avg);
    printf("%d\n", mid);
    printf("%d\n", mode);
    printf("%d\n", range);

    return 0;
}