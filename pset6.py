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


    def create_helper(self, node, i):
        size = len(self.heap_lst)
        if i * 2 + 1 < size:
            node.l_child = TreeNode(self.heap_lst[i * 2 + 1])
            self.create_helper(node.l_child, i * 2 + 1)
        if i * 2 + 2 < size:
            node.r_child = TreeNode(self.heap_lst[i * 2 + 2])
            self.create_helper(node.r_child, i * 2 + 2)


    def create_tree(self):
        if len(self.heap_lst) > 0:
            root = TreeNode(self.heap_lst[0])
            self.create_helper(root, 0)
            return root
        else:
            return None

    def sort_heap(self):
        temp = list(self.heap_lst)
        result_lst = []
        while len(self.heap_lst) > 0:
            result_lst = [self.delete()] + result_lst
        self.heap_lst = temp
        return result_lst

        
