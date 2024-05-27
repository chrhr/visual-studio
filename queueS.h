#pragma once
#define Q_SIZE 4
typedef char element; // ť ������ �ڷ����� char�� ����

typedef struct {
	element queue[Q_SIZE]; // 1���� �迭 ť ����
	int front, rear;
} QueueType;

QueueType* createQueue(void);
int isQueueEmpty(QueueType* Q);
int isQueueFull(QueueType* Q);
int isQueue(QueueType* Q, element item);
element deQueue(QueueType* Q);
element peekQ(QueueType* Q);
void printQ(QueueType* Q);