#pragma once
typedef char element; // ���� ť ������ �ڷ����� char�� ����

typedef struct QNode { // ���� ť�� ��带 ����ü�� ����
	element data;
	struct QNode* link;
} QNode;

typedef struct { // ���� ť���� ����ϴ� ������ fornt �� rear�� ����ü�� ����
	QNode * front, *rear;
} LQueueType;

LQueueType* createLinkedQueue(void);
int isLQEmpty(LQueueType* LQ);
void enLQueue(LQueueType* LQ, element item);
element deLQueue(LQueueType* LQ);
element peekLQ(LQueueType* LQ);
void printLQ(LQueueType* LQ);