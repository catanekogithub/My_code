#include <stdio.h>

int max_2para(int x, int y)  //定义函数max, 函数值为整型, 形参为整型, 要用的时候在main函数里声明一下
{
	if (x > y)
		return x;
	else
		return y;
}

int max_3para(int x, int y, int z)  //返回形参x, y, z中的最大值
{
	int mid;
	if (x > y)
		mid = x;
	else
		mid = y;
	if (mid > z)
		return mid;
	else
		return z;
}

int funcB(int x)  //return形参x的阶乘
{
	if (x > 1)
		return x * funcB(x - 1);
	else
		return 1;
}

int funcC(int x)
{
	int sum, i;
	i = 1;
	sum = 1;
	while (i < x)
		sum = sum * (i + 1), 
		i = i + 1;
	return sum;
}


void print_binary_recursive(int num) {
	if (num > 1) {
		// 递归调用
		print_binary_recursive(num / 2);
	}
	// 打印当前位
	printf("%d", num % 2);
}

void printN(int N) {
	if (N) {
		printN(N - 1);
	}
	printf("%d\n", N);
}