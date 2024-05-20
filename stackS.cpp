#include <stdio.h>
#include "stackS.h"

int top = -1;

// ������ ���� �������� Ȯ��
int isStackEmpty(void) {
	if (top == -1) return 1;
	else return 0;
}

// ������ ��ȭ �������� Ȯ��
int isStackFull(void) {
	if (top == STACK_SIZE - 1) return 1;
	else return 0;
}

// ������ top�� ���Ҹ� �����ϴ� ����
void push(element item) {
	if (isStackFull()) { // ������ ��ȭ������ ��
		printf("\n\n Stack is Full. \n");
		return;
	}
	// top�� ������Ų �� ���� top�� ���� ����
	else stack[++top] = item;
}

// ������ top���� ���Ҹ� �����ϴ� ����
void pop(element item) {
	if (isStackEmpty()) { // ������ ��������� ��
		printf("\n\n Stack is Empty. \n");
		return;
	}
	// ���� top�� ���Ҹ� ������ �� top ����
	else stack[top--];
}

// ������ top ���Ҹ� �˻��ϴ� ����
element peek(void) {
	if (isStackEmpty()) { // ������ ���� ������ ���
		printf("\n\n Stack is Empty. \n");
		return 0;
	}
	else return stack[top]; // ���� top�� ���� Ȯ��
}

// ������ ���� ���
void printStack(void) {
	int i;
	printf("\n STACK [ ");
	for (i = 0; i <= top; i++)
		printf("%d ", stack[i]);
	printf("] ");
}