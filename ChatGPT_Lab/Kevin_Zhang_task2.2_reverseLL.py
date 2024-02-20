class ListNode:
    # ListNode class for representing a node in a singly linked list
    def __init__(self, value=0, next=None):
        self.value = value  # Value of the node
        self.next = next    # Reference to the next node in the list

def reverse_linked_list(head):
    # Function to reverse a singly linked list
    prev = None          # Initialize previous node to None
    current = head       # Start with the head of the list
    while current:
        next = current.next  # Store reference to the next node
        current.next = prev  # Reverse the link
        prev = current       # Move prev to the current node
        current = next       # Move to the next node in the original list
    return prev              # Return the new head of the reversed list

def print_list(node):
    # Function to print all values in the linked list
    while node:
        print(node.value, end=" ")  # Print the value of the current node
        node = node.next            # Move to the next node
    print()                         # Print a newline at the end

def main():
    # Main function to demonstrate the functionality
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(head)  # Print the original list

    head = reverse_linked_list(head)  # Reverse the linked list
    print("Reversed List:")
    print_list(head)  # Print the reversed list

if __name__ == "__main__":
    main()  # Execute the main function
