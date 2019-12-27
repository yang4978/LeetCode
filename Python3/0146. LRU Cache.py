class ListNode:

    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {}


    def del_first_node(self):
        key = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return key

    
    def delete_node(self,node):
        prev,next = node.prev,node.next
        next.prev = prev
        prev.next = next


    def insert_node_to_end(self,node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.delete_node(node)
            self.insert_node_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete_node(self.hashmap[key])
            self.hashmap[key].val = value
            self.insert_node_to_end(self.hashmap[key])
        else:
            node = ListNode(key,value)
            self.hashmap[key] = node
            self.insert_node_to_end(node)
            if len(self.hashmap)>self.capacity:
                del self.hashmap[self.del_first_node()]
        

# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self:
#             return - 1
        
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last = False)


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.queue = []
#         self.val_map = {}
        

#     def get(self, key: int) -> int:
#         if key in self.queue:
#             self.queue.pop(self.queue.index(key))
#             self.queue.append(key)
#             return self.val_map[key]
#         else:
#             return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.val_map:
#             self.queue.pop(self.queue.index(key))
#         self.queue.append(key)
#         self.val_map[key] = value

#         if len(self.queue) > self.capacity:
#             temp = self.queue.pop(0)
#             del self.val_map[temp]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
