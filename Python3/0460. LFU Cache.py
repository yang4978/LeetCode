# class dll_Node:

#     def __init__(self,key,value,count):
#         self.key = key
#         self.val = value
#         self.count = count
#         self.pre = None
#         self.next = None

# class LFUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.key_dict = {}
#         self.head = dll_Node(1,1,float('inf'))
#         self.tail = dll_Node(-1,-1,-float('inf'))
#         self.head.next = self.tail
#         self.tail.pre = self.head
    
#     def __update__(self,node):
#         node.count += 1
#         t_pre = node.pre
#         t_next = node.next
#         temp = node.pre

#         while node.count >= temp.count:
#             temp = temp.pre
        
#         if temp != t_pre:
#             node.pre = temp
#             node.next = temp.next
#             temp.next.pre = node
#             temp.next = node

#             t_pre.next = t_next
#             t_next.pre = t_pre

#     def get(self, key: int) -> int:
#         if key in self.key_dict:
#             node = self.key_dict[key]
#             self.__update__(node)
#             return node.val
#         else:
#             return -1
        
#     def put(self, key: int, value: int) -> None:
#         if self.capacity < 1:
#             return

#         if key in self.key_dict:
#             node = self.key_dict[key]
#             self.__update__(node)
#             node.val = value
#         else:
            
#             if len(self.key_dict) == self.capacity:
#                 del self.key_dict[self.tail.pre.key]
#                 new_pre = self.tail.pre.pre
#                 new_pre.next = self.tail
#                 self.tail.pre = new_pre

#             node = dll_Node(key,value,0)
#             node.pre = self.tail.pre
#             node.next = self.tail
#             self.tail.pre.next = node
#             self.tail.pre = node
#             self.key_dict[key] = node
#             self.__update__(node)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}
        self.counterbook = collections.defaultdict(list)

    
    def __update__(self,key,count):
        self.counterbook[count].remove(key)
        if len(self.counterbook[count]) == 0:
            del self.counterbook[count]
        self.counterbook[count+1].append(key)

    def get(self, key: int) -> int:
        if key in self.key_dict:
           value, count = self.key_dict[key]
           self.key_dict[key] = [value,count+1]
           self.__update__(key,count)
           return value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if self.capacity < 1:
            return

        if key in self.key_dict:
            _, count = self.key_dict[key]
            self.key_dict[key] = [value,count+1]
            self.__update__(key,count)

        else:
            if len(self.key_dict) == self.capacity:
                del self.key_dict[self.counterbook[min(self.counterbook.keys())].pop(0)]
            
            self.key_dict[key] = [value,0]
            self.counterbook[0].append(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
