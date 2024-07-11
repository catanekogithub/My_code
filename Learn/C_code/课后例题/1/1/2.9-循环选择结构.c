//#define _CRT_SECURE_NO_WARNINGS  //禁止scanf报错
//#define PI 3.14159  //定义符号常量
//#include <stdio.h>
//#include <string.h>
//#include <math.h>
//
//int main() {
//	
//	////for循环
//	//int sum = 0;
//	//for (int i = 1 ; i <= 100 ; i++)
//	//{
//	//	sum += i;
//	//}
//	//printf("%d\n", sum);
//
//
//	////while
//	//int i = 1;
//	//int sum = 0;
//	//while (i <= 100)
//	//{
//	//	sum += i;
//	//	i++;
//	//}
//	//printf("%d\n", sum);
//	
//	////do while
//	//int sum = 0;
//	//int i = 1;
//	//do
//	//{
//	//	sum += i;
//	//	//printf("%d\n", sum);
//	//	++i;
//	//} while (i <= 100);
//	//printf("%d\n", sum);
//
//	////break
//	//int money;
//	//int sum = 0;
//	//int condition;
//	//for (condition = 1; condition <= 100; ++condition)
//	//{
//	//	scanf("%d", &money);
//	//	sum += money;
//	//	if (sum >= 10000)
//	//		break;
//	//}
//	//printf("input time: %d, result:%d", condition, sum);
//
//	//循环求素数
//	//int n;
//	//printf("find the prime of the intput num in 2-num:\n");
//	//scanf("%d", &n);
//	//int remain = 0;
//	//for (int num = 2 ; num <= n ; num++) {
//	//	for (int condition = (num - 1) ; condition > 1 ; condition--) {
//	//		if ((num % condition) == 0) {
//	//			//printf("%d不是素数\n", num);
//	//			break;
//	//		}
//	//		else {
//	//			if (condition == 2) {
//	//				printf("%d\n", num);
//	//			}
//	//		}
//	//	}
//	//}
//	//求素数/质数方法二
//	//for (int i = 1; i <= 100; i++) {
//	//	int is_prime = 1;  //设定一个状态值
//	//	for (int num = i - 1; num > 1; num--) {
//	//		if ((i % num) == 0) {
//	//			is_prime = 0;
//	//		}
//	//	}
//	//	// 检测状态值
//	//	if (is_prime == 1) {
//	//		printf("%d\n", i);
//	//	}
//	//}
//
//	//输出矩阵
//	//for (int z = 1; z <= 4; z++) {
//	//	int print_num = z;
//	//	for (int y = 1 ; y <= 5 ; y++) {
//	//		printf("%d\t", print_num);
//	//		print_num += z;
//	//	}
//	//	printf("\n");
//	//}
//
//	//计算斐波那契数列
//	int num1 = 1, num2 = 1, current_num = 1;  //定义前两项的变量和一个存储当前项的变量
//	for (int i = 1; i < 10; i++) {
//		//输出第一, 二项
//		if (i <= 2) {
//			printf("1  ");
//		}
//		else {
//			current_num = num1 + num2;
//			printf("%d  ", num1 + num2);  //打印当前项
//			//对前两项进行重新赋值
//			num1 = num2;
//			num2 = current_num;
//		}
//	}
//
//	//用公式求pai/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...加到10^-6为止
//	double flag = 1;
//	double bottom_num = 1;
//	double sum = 0;
//	for (; (1 / bottom_num) > 1e-8; bottom_num += 2) {
//		//printf("%.8f %c %.8f = ", sum, flag > 0 ? '+': '-', (1 / bottom_num));
//		sum += (flag / bottom_num);
//		flag = -flag;
//		//printf("%.8f\n", sum);
//	}
//	//double sum = 0;
//	//double sign = 1;  //表示符号
//	//double under_num = 1;  //底数
//	//while(1 / under_num > 1e-6) {
//	//	printf("%.8f %c %.8f", sum, sign > 0 ? '+': '-', (1 / under_num));
//	//	sum += sign/under_num;
//	//	printf(" = %.8f\n", sum);
//	//	under_num += 2;
//	//	sign = -sign;
//	//}
//	//最后打印pai的值
//	printf("4 * %.8f = %.8f", sum, 4 * sum);
//	
//
//
//	return 0;
//}