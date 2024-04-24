///week10-3.cpp
///課本第5章 函式/函數 function
///課本 Page 5-5, 5-6
#include <stdio.h>
/// 有參數進來 int a
void myPrint(int a){
    for(int i=0; i<a; i++) printf("星");
    printf("\n");
    ///沒有return, 沒有參數出去
}

int main()
{ ///主要的函式
    myPrint(5);
    myPrint(4);
    myPrint(3);
    myPrint(2);
    myPrint(1);
}