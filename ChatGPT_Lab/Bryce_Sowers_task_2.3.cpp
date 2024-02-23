#include <iostream>
using namespace std;

// Define a structure for a node in the queue
struct Node {
    int data;
    Node *next;
};

// Define a structure for the queue
struct Queue {
    Node *front = nullptr; // Initialize front pointer to nullptr
    Node *rear = nullptr;  // Initialize rear pointer to nullptr
    
    // Function to add an element to the queue
    void enqueue(int data);
    
    // Function to remove an element from the queue
    int dequeue();
};

// Function to add an element to the queue
void Queue::enqueue(int data) {
    // Create a new node
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = nullptr; // Set next pointer to nullptr
    
    // If the queue is empty, set both front and rear to the new node
    if (front == nullptr) {
        front = newNode;
        rear = newNode;
    } else {
        // Otherwise, add the new node to the rear and update rear pointer
        rear->next = newNode;
        rear = newNode;
    }
}

// Function to remove an element from the queue
int Queue::dequeue() {
    // If the queue is empty, print a message and return -1
    if (front == nullptr) {
        cout << "The Queue is empty" << endl;
        return -1;
    } else {
        // Otherwise, remove the front node and return its data
        Node *temp = front;
        int data = temp->data;
        front = front->next;
        delete temp;
        return data;
    }
}

int main() {
    Queue q; // Create a queue object
    
    // Enqueue some elements
    q.enqueue(5);
    q.enqueue(7);
    q.enqueue(-3);
    
    // Dequeue and print elements until the queue is empty
    cout << q.dequeue() << endl;
    q.enqueue(9);
    while (q.front != nullptr)
        cout << q.dequeue() << endl;
    
    return 0;
}
