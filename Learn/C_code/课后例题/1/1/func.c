#include <stdio.h>

int max_2para(int x, int y)  //���庯��max, ����ֵΪ����, �β�Ϊ����, Ҫ�õ�ʱ����main����������һ��
{
	if (x > y)
		return x;
	else
		return y;
}

int max_3para(int x, int y, int z)  //�����β�x, y, z�е����ֵ
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

int funcB(int x)  //return�β�x�Ľ׳�
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
		// �ݹ����
		print_binary_recursive(num / 2);
	}
	// ��ӡ��ǰλ
	printf("%d", num % 2);
}

void printN(int N) {
	if (N) {
		printN(N - 1);
	}
	printf("%d\n", N);
}