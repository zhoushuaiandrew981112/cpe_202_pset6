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
        while ((i - 1) // 2) > 0:
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
        
