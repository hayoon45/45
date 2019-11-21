#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int main(void)
{
	while (1) { //대문자 Q가 입력되기 전까지 무한히 반복되어야 하기 때문에 while문 사용
		char x;
		printf("임의의 문자를 하나만 입력하세요: ");
		scanf(" %c", &x);
		
		if (x == 'Q') {
			printf("입력하신 문자 '%c'는 영문 대문자이며 변환하면 '%c'입니다. \n", x, x + 32);
			break; //while문 밖으로 빠져나가 프로그램 종료
		}
		if (x >= 'A' && x <= 'Z') //변수 x가 대문자인지 판별
		{
			printf("입력하신 문자 '%c'는 영문 대문자이며 변환하면 '%c'입니다. \n", x, x + 32);
			//아스키코드에서 대문자와 소문자가 32 만큼 차이가 남
		}
			else if (x >= 'a' && x <= 'z') //변수 x가 소문자인지 판별
		{
			printf("입력하신 문자 '%c'는 영문 소문자이며 변환하면 '%c'입니다. \n", x, x - 32);
			//아스키코드에서 대문자와 소문자가 32 만큼 차이가 남
		}
			else if (x >= '0' && x <= '9') //변수 x가 숫자인지 판별
		{
			printf("입력하신 문자 '%c'는 숫자 입니다.\n", x);
		}
			else printf("입력하신 문자 '%c'는 기타문자 입니다.\n", x);
	}

	return 0;
}