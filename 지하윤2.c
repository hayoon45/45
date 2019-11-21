#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
	int score[4][20];
	srand((long)time(NULL));
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 20; j++) {
			score[i][j] = rand() % 100 + 1;
		}
	}
	int temp;
	//1��, 3�� ��������, 2��, 4�� ��������
	for (int i = 0; i < 19; i++) {
		for (int j = i + 1; j < 20; j++) {
			if (score[0][i] < score[0][j]) {
				temp = score[0][j];
				score[0][j] = score[0][i];
				score[0][i] = temp;
			}
			if (score[1][i] > score[1][j]) {
				temp = score[1][j];
				score[1][j] = score[1][i];
				score[1][i] = temp;
			}
			if (score[2][i] < score[2][j]) {
				temp = score[2][j];
				score[2][j] = score[2][i];
				score[2][i] = temp;
			}
			if (score[3][i] > score[3][j]) {
				temp = score[3][j];
				score[3][j] = score[3][i];
				score[3][i] = temp;
			}
			
		}
	}

	for (int i = 0; i < 4; i++) {
		printf("[%d�� ���� ���]\n", i + 1);
		for (int j = 0; j < 20; j++) {
			printf("%d ", score[i][j]);
		}
		puts("");
		printf("%d�� ��ռ���: %d, �ְ���: %d, ������: %d", i + 1, SUM(score[i], 1)/20, MAX(score[i], 1), MIN(score[i], 1));
		puts("");
		puts("");
	}
	int sum = SUM(score, 4);
	int max = MAX(score, 4);
	int min = MIN(score, 4);

	printf("��ü �л��� ��� ������ %d���̴�.\n", sum/80);
	printf("��ü �л��� �ְ� ������ %d���̴�.\n", max);
	printf("��ü �л��� ���� ������ %d���̴�.\n", min);
	
	return 0;
}

int MAX(int ary[][20], int a) {
	int max = 0;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < 20; j++) {
			if (max < ary[i][j])
				max = ary[i][j];
		}
	}
	return max;
}

int MIN(int ary[][20], int a) {
	int min = 100;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < 20; j++) {
			if (min > ary[i][j])
				min = ary[i][j];
		}
	}
	return min;
}

int SUM(int ary[][20], int a) {
	int sum = 0;
	for (int i=0; i < a; i++) {
		for (int j = 0; j < 20; j++) {
			sum = sum + ary[i][j];
		}
	}
	return sum;
}