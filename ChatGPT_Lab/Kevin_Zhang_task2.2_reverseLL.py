class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def print_list(node):
    while node:
        print(node.value, end=" ")
        node = node.next
    print()

def main():
    # Creating a sample linked list 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(head)

    head = reverse_linked_list(head)
    print("Reversed List:")
    print_list(head)

if __name__ == "__main__":
    main()
