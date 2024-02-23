#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;
};

struct stack
{
    Node *top = NULL;
    void push(stack *s, int data);
    int pop(stack *s);
};

void stack::push(stack *s, int data)
{
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = s->top;
    s->top = newNode;   
}

int stack::pop(stack *s)
{
    if (s->top == NULL)
    {
        cout << "Stack is empty" << endl;
        return -1;
    }

    Node *temp = s->top;
    int data = temp->data;
    s->top = temp->next;
    delete temp;
    return data;
}


int main()
{
    stack *s = new stack;
    s->push(s,5);
    s->push(s,7);
    s->push(s,-3);
    cout << s->pop(s) << endl;
    s->push(s,9);
    while(s->top != NULL)
        cout << s->pop(s) << endl;

}