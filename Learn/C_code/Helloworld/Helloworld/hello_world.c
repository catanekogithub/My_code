#define _CRT_SECURE_NO_WARNINGS

// Ԥ����
# include <stdio.h>

//ҵ�����
int main()
{
	printf("hello world!\n");

	// ��ӡ��������
	printf("��ӡһ����������:%d\n", 888888);

	// ��ӡʵ������(������)
	printf("����%.0f�����㽶\n", 1.0);

	// ��ӡһ���ַ�����
	printf("��ӡһ���ַ�����: %c\n", 'A');

	//���ϴ�ӡ
	printf("��ӡһ��������: %f, һ��������: %d, һ���ַ�������: %s\n", 1.67,2, "114514");

	// ����һ�����������
	int a = 1;
	printf("����a��ֵΪ%d\n", a);
	int b = 1; int c = 2;
	printf("����b��ֵΪ%d, c��ֵΪ%d\n", b, c);

	// ����ת��
	int d = 0x10;
	printf("ʮ������10ת��Ϊʮ����Ϊ%d\n", d);

	// ʹ���������scanf
	/*int num1;
	int num2;*/
	//scanf("����������:%d %d\n", &num1, &num2);
	/*int sum = num1 + num2;
	printf("�������֮��Ϊ: %d", sum);*/

	// ������������ռ���ڴ��С
	printf("long����ռ�õ��ڴ��СΪ: %dbyte\n", sizeof(long));
	printf("long long����ռ�õ��ڴ��СΪ: %dbyte\n", sizeof(long long));
	short int abc = 1;
	long ab = 100L;
	long long ba = 1000LL;
	return 0;  //1231341231


}

