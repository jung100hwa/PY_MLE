#include <stdio.h>

/** 아래와 같이 컴파일 */
/** gcc -o test.so -shared -fPIC test.c */

int add_int(int a, int b);

int add_int(int a, int b)
{
	return a + b;
}

