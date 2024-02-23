#include <iostream>

using namespace std;

// Node structure to represent each element in the stack
struct Node
{
    int data;     // Data of the node
    Node *next;   // Pointer to the next node
};

// Stack structure to implement stack operations
struct Stack
{
    Node *top = nullptr;   // Pointer to the top of the stack

    /**
     * @brief Pushes a new element onto the stack.
     * 
     * @param data The data to be pushed onto the stack.
     */
    void push(int data);

    /**
     * @brief Pops the top element from the stack.
     * 
     * @return int The data of the popped element, or -1 if the stack is empty.
     */
    int pop();
};

void Stack::push(int data)
{
    // Create a new node
    Node *newNode = new Node;
    newNode->data = data;
    
    // Set the next pointer of the new node to the current top
    newNode->next = top;
    
    // Update the top pointer to the new node
    top = newNode;   
}

int Stack::pop()
{
    // Check if the stack is empty
    if (top == nullptr)
    {
        cout << "Stack is empty" << endl;
        return -1;
    }

    // Store the data of the top node
    int data = top->data;
    
    // Move the top pointer to the next node
    Node *temp = top;
    top = top->next;
    
    // Delete the original top node
    delete temp;
    
    return data;
}

int main()
{
    // Create a new stack object
    Stack s;
    
    // Push some elements onto the stack
    s.push(5);
    s.push(7);
    s.push(-3);
    
    // Pop and print elements from the stack
    cout << s.pop() << endl;
    s.push(9);
    while(s.top != nullptr)
        cout << s.pop() << endl;

    return 0;
}
