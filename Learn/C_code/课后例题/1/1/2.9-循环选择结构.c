//#define _CRT_SECURE_NO_WARNINGS  //��ֹscanf����
//#define PI 3.14159  //������ų���
//#include <stdio.h>
//#include <string.h>
//#include <math.h>
//
//int main() {
//	
//	////forѭ��
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
//	//ѭ��������
//	//int n;
//	//printf("find the prime of the intput num in 2-num:\n");
//	//scanf("%d", &n);
//	//int remain = 0;
//	//for (int num = 2 ; num <= n ; num++) {
//	//	for (int condition = (num - 1) ; condition > 1 ; condition--) {
//	//		if ((num % condition) == 0) {
//	//			//printf("%d��������\n", num);
//	//			break;
//	//		}
//	//		else {
//	//			if (condition == 2) {
//	//				printf("%d\n", num);
//	//			}
//	//		}
//	//	}
//	//}
//	//������/����������
//	//for (int i = 1; i <= 100; i++) {
//	//	int is_prime = 1;  //�趨һ��״ֵ̬
//	//	for (int num = i - 1; num > 1; num--) {
//	//		if ((i % num) == 0) {
//	//			is_prime = 0;
//	//		}
//	//	}
//	//	// ���״ֵ̬
//	//	if (is_prime == 1) {
//	//		printf("%d\n", i);
//	//	}
//	//}
//
//	//�������
//	//for (int z = 1; z <= 4; z++) {
//	//	int print_num = z;
//	//	for (int y = 1 ; y <= 5 ; y++) {
//	//		printf("%d\t", print_num);
//	//		print_num += z;
//	//	}
//	//	printf("\n");
//	//}
//
//	//����쳲���������
//	int num1 = 1, num2 = 1, current_num = 1;  //����ǰ����ı�����һ���洢��ǰ��ı���
//	for (int i = 1; i < 10; i++) {
//		//�����һ, ����
//		if (i <= 2) {
//			printf("1  ");
//		}
//		else {
//			current_num = num1 + num2;
//			printf("%d  ", num1 + num2);  //��ӡ��ǰ��
//			//��ǰ����������¸�ֵ
//			num1 = num2;
//			num2 = current_num;
//		}
//	}
//
//	//�ù�ʽ��pai/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...�ӵ�10^-6Ϊֹ
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
//	//double sign = 1;  //��ʾ����
//	//double under_num = 1;  //����
//	//while(1 / under_num > 1e-6) {
//	//	printf("%.8f %c %.8f", sum, sign > 0 ? '+': '-', (1 / under_num));
//	//	sum += sign/under_num;
//	//	printf(" = %.8f\n", sum);
//	//	under_num += 2;
//	//	sign = -sign;
//	//}
//	//����ӡpai��ֵ
//	printf("4 * %.8f = %.8f", sum, 4 * sum);
//	
//
//
//	return 0;
//}