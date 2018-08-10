# Name:         Zhoushuai (Anderw) Wu
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Pset 6: Binary Heap
# Term:         Summer 2018


class TreeNode:

    def __init__(self, priority):
        self.priority = priority
        self.parent = None
        self.l_child = None
        self.r_child = None


class MaxHeap:

    def __init__(self, ints):
        self.heap_lst = ints
        self.heap_lst = self.heapify(self.heap_lst)


    def get_heap(self):
        return self.heap_lst


    def max_child_index(self, i):
        if i * 2 + 2 > len(self.heap_lst) - 1:
            return i * 2 + 1
        else:
            l_child = self.heap_lst[i * 2 + 1]
            r_child = self.heap_lst[i * 2 + 2]
            if l_child > r_child:
                return i * 2 + 1
            else:
                return i * 2 + 2 


    def perc_up(self, i):
        while ((i - 1) // 2) >= 0:
            parent_i = (i - 1) // 2
            if self.heap_lst[i] > self.heap_lst[parent_i]:
                temp = self.heap_lst[parent_i]
                self.heap_lst[parent_i] = self.heap_lst[i]
                self.heap_lst[i] = temp
            i = parent_i

 
    def perc_down(self, i):
        while(i * 2 + 1) < len(self.heap_lst):
            max_c_i = self.max_child_index(i)
            if self.heap_lst[i] < self.heap_lst[max_c_i]:
                temp = self.heap_lst[i]
                self.heap_lst[i] = self.heap_lst[max_c_i]
                self.heap_lst[max_c_i] = temp
            i = max_c_i


    def heapify(self, ints):
        i = len(ints) // 2 - 1
        while i >= 0:
            self.perc_down(i)
            i = i - 1
        return self.heap_lst


    def insert(self, new_int):
        self.heap_lst.append(new_int)
        self.perc_up(len(self.heap_lst) - 1)


    def delete(self):
        result = self.heap_lst[0]
        self.heap_lst[0] = self.heap_lst[len(self.heap_lst) - 1]
        self.heap_lst.pop()
        self.perc_down(0)
        return result


    def create_tree(self):
        root_node = TreeNode(self.delet())
        current = root_node
        while len(self.heap_lst) >= 0:
            priority = self.delete()
            new_node = TreeNode(priority)
            while current != None:
                if priority < current.priority:
                    if current.l_child == None:
                        current.l_child = new_node
                    else:
                        current = current.l_child
                elif priority > current.priority:
                    if current.r_chiild == None:
                        current.r_child = new_Node
                    else:
                        current = current.r_child
        return root_node



        
