#pragma once
typedef int element; // ���� ������ �ڷ����� int�� ����

typedef struct stackNode {
	element data;
	struct stackNode* link;
} stackNode;

// ������ top ��带 �����ϱ� ���� ������ top ����
stackNode* top;

int isStackEmpty(void);
void push(element item);
element pop(void);
element peek(void);
void printStack(void);