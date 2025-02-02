class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def sort_list(head):
    if not head or not head.next:
        return head

    def get_middle(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(head):
        if not head or not head.next:
            return head
        middle = get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = merge_sort(head)
        right = merge_sort(next_to_middle)
        return merge_sorted_lists(left, right)

    return merge_sort(head)

if __name__ == '__main__':
  # Usage examples
  def print_list(head):
      current = head
      while current:
          print(current.value, end=" -> ")
          current = current.next
      print("None")

  # Creating a linked list
  head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
  print("Original list:")
  print_list(head)

  # Reversing the linked list
  reversed_head = reverse_list(head)
  print("Reversed list:")
  print_list(reversed_head)

  # Sorting the linked list
  sorted_head = sort_list(reversed_head)
  print("Sorted list:")
  print_list(sorted_head)

  # Merging two sorted linked lists
  l1 = ListNode(1, ListNode(3, ListNode(5)))
  l2 = ListNode(2, ListNode(4, ListNode(6)))
  merged_head = merge_sorted_lists(l1, l2)
  print("Merged sorted lists:")
  print_list(merged_head)