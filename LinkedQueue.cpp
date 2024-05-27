#include <stdio.h>
#include <stdlib.h>
#include "LinkedQueue.h"

// 공백 연결 큐를 생성하는 연산
LQueueType* createLinkedQueue(void) {
	LQueueType* LQ;
	LQ = (LQueueType*)malloc(sizeof(LQueueType));
	LQ->front = NULL;
	LQ->rear = NULL;
	return LQ;
}

// 연결 큐가 공백인지 확인
int isLQEmpty(LQueueType* LQ) {
	if (LQ->front == NULL) {
		printf("Linked Queue is empty. ");
		return 1;
	}
	else return 0;
}

// 연결 큐의 rear에 원소 삽입
void enLQueue(LQueueType* LQ, element item) {
	QNode* newNode = (QNode*)malloc(sizeof(QNode));
	newNode->data = item;
	newNode->link = NULL;
	if (LQ->front == NULL) { // 현재 연결큐 공백
		LQ->front = newNode;
		LQ->rear = newNode;
	}
	else { // 현재 연결 큐가 공백이 아닐 때
		LQ->rear->link = newNode;
		LQ->rear = newNode;
	}
}

// 연결 큐에서 원소를 삭제하고 반환
element deLQueue(LQueueType* LQ) {
	QNode* old = LQ->front;
	element item;
	if (isLQEmpty(LQ)) return;
	else {
		item = old->data;
		LQ->front = LQ->front->link;
		if (LQ->front == NULL)
			LQ->rear == NULL;
		free(old);
		return item;
	}
}

// 연결 큐에서 원소 검색
element peekLQ(LQueueType* LQ) {
	element item;
	if (isLQEmpty(LQ)) return;
	else {
		item = LQ->front->data;
		return item;
	}
}

// 연결 큐의 원소 출력
void printLQ(LQueueType* LQ) {
	QNode* temp = LQ->front;
	printf("Linked Queue : [");
	while (temp) {
		printf("%3c", temp->data);
		temp = temp->link;
	}
	printf(" ] ");
}