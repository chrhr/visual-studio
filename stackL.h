#pragma once
typedef int element; // 스택 원소의 자료형을 int로 지정

typedef struct stackNode {
	element data;
	struct stackNode* link;
} stackNode;

// 스택의 top 노드를 지정하기 위해 포인터 top 선언
stackNode* top;

int isStackEmpty(void);
void push(element item);
element pop(void);
element peek(void);
void printStack(void);