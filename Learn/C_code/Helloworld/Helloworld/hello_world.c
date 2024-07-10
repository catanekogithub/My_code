#define _CRT_SECURE_NO_WARNINGS

// 预处理
# include <stdio.h>

//业务代码
int main()
{
	printf("hello world!\n");

	// 打印整型数据
	printf("打印一个整型数据:%d\n", 888888);

	// 打印实型数据(浮点数)
	printf("我有%.0f个大香蕉\n", 1.0);

	// 打印一个字符数据
	printf("打印一个字符数据: %c\n", 'A');

	//整合打印
	printf("打印一个浮点数: %f, 一个整型数: %d, 一个字符串数据: %s\n", 1.67,2, "114514");

	// 定义一个变量并输出
	int a = 1;
	printf("变量a的值为%d\n", a);
	int b = 1; int c = 2;
	printf("变量b的值为%d, c的值为%d\n", b, c);

	// 进制转换
	int d = 0x10;
	printf("十六进制10转化为十进制为%d\n", d);

	// 使用输入语句scanf
	/*int num1;
	int num2;*/
	//scanf("输入两个数:%d %d\n", &num1, &num2);
	/*int sum = num1 + num2;
	printf("两数相加之和为: %d", sum);*/

	// 测试数据类型占用内存大小
	printf("long类型占用的内存大小为: %dbyte\n", sizeof(long));
	printf("long long类型占用的内存大小为: %dbyte\n", sizeof(long long));
	short int abc = 1;
	long ab = 100L;
	long long ba = 1000LL;
	return 0;  //1231341231


}

