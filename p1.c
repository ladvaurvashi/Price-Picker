#include<stdio.h>

int main(){
    int age;
    printf("Enter your age");
    scanf("%d", &age);
    if(age<18){
        Printf("you can not vote");
    }
    else(age>=18){
        printf("You can vote");
    }
}
