#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;
};

struct Queue
{
    Node *front = NULL;
    Node *rear = NULL;
    void enqueue(Queue *q, int data);
    int dequeue(Queue *q);
};

void Queue::enqueue(Queue *q, int data)
{
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = NULL;
    if (q->front == NULL)
    {
        q->front = newNode;
        q->rear = newNode;
    }
    else
    {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

int Queue::dequeue(Queue *q)
{
    if(q->front == NULL)
    {
        cout << "The Queue is empty" << endl;
        return -1;
    }
    else
    {
        Node *temp = q->front;
        int data = temp->data;
        q->front = temp->next;
        delete temp;
        return data;
    }
}

int main()
{
    Queue *q = new Queue;
    q->enqueue(q,5);
    q->enqueue(q,7);
    q->enqueue(q,-3);
    cout << q->dequeue(q) << endl;
    q->enqueue(q,9);
    while(q->front != NULL)
        cout << q->dequeue(q) << endl;
}