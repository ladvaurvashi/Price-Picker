#include <stdio.h>
#include<stdbool.h>

// Function to check  prime number 
int prime(int n) {
    if (n < 2) {
        return false;
    }

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

// Function to check increasing order
int Increasing(int n) {
    int lastDigit = n % 10;
    n /= 10;

    while (n> 0) {
        if (n% 10 >= lastDigit) {
            return false;
        }

        lastDigit = n % 10;
        n /= 10;
    }

    return true;
}

int main() {
    printf("Prime numbers with increasing digits in the range 1 to 1000:\n");
    int c=0;
    for (int i = 2; i <= 1000; i++) {
        if (prime(i) && Increasing(i)) {
            c++;
            printf("%d\n", i);
        }
    }
    printf("Count is : %d",c);

    return 0;
}