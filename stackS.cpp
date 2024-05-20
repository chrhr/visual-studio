#include <stdio.h>
#include "stackS.h"

int top = -1;

// 스택이 공백 상태인지 확인
int isStackEmpty(void) {
	if (top == -1) return 1;
	else return 0;
}

// 스택이 포화 상태인지 확인
int isStackFull(void) {
	if (top == STACK_SIZE - 1) return 1;
	else return 0;
}

// 스택의 top에 원소를 삽입하는 연산
void push(element item) {
	if (isStackFull()) { // 스택이 포화상태일 때
		printf("\n\n Stack is Full. \n");
		return;
	}
	// top을 증가시킨 후 현재 top에 원소 삽입
	else stack[++top] = item;
}

// 스택의 top에서 원소를 삭제하는 연산
void pop(element item) {
	if (isStackEmpty()) { // 스택이 공백상태일 때
		printf("\n\n Stack is Empty. \n");
		return;
	}
	// 현재 top의 원소를 삭제한 후 top 감소
	else stack[top--];
}

// 스택의 top 원소를 검색하는 연산
element peek(void) {
	if (isStackEmpty()) { // 스택이 공백 상태인 경우
		printf("\n\n Stack is Empty. \n");
		return 0;
	}
	else return stack[top]; // 현재 top의 원소 확인
}

// 스택의 원소 출력
void printStack(void) {
	int i;
	printf("\n STACK [ ");
	for (i = 0; i <= top; i++)
		printf("%d ", stack[i]);
	printf("] ");
}