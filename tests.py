from pset6 import *
import unittest


class Test_pset6(unittest.TestCase):
   
    """ test TreeNode class """

    def test_TreeNode_init(self):
        node = TreeNode(1)
        self.assertEqual(node.priority, 1)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.l_child, None)
        self.assertEqual(node.r_child, None)

    """ test MaxHeap class """

    def test_MaxHeap_get_heap(self):
        
        ints = [6, 5, 4, 3, 2, 1, 0]
        heap = MaxHeap(ints)
        exp_lst = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(heap.get_heap(), exp_lst)

        ints = [-1, -2, -3, -4, -5]
        heap = MaxHeap(ints)
        exp_lst = [-1, -2, -3, -4, -5]
        self.assertEqual(heap.get_heap(), exp_lst)

        ints = [0]
        heap = MaxHeap(ints)
        exp_lst = [0]
        self.assertEqual(heap.get_heap(), exp_lst)

    def test_Maxheap_max_child_index(self):
        ints = [0, 1, 2]
        heap = MaxHeap(ints)
        self.assertEqual(heap.max_child_index(0), 1)

        ints = [0, 2, 1]
        heap = MaxHeap(ints)
        self.assertEqual(heap.max_child_index(0), 2)

        ints = [2, 1, 0]
        heap = MaxHeap(ints)
        self.assertEqual(heap.max_child_index(0), 1)

    def test_MaxHeap_heapify(self):
        ints = [0, 1, 2, 3, 4, 5, 6]
        heap = MaxHeap(ints)
        exp_lst = [6, 4, 5, 3, 1, 0, 2]
        self.assertEqual(heap.heapify(ints), exp_lst) 

        ints = [11, 2, 24, 9, 4, 5]
        heap = MaxHeap(ints)
        exp_lst = [24, 9, 11, 2, 4, 5]
        self.assertEqual(heap.heapify(ints), exp_lst) 
        
        ints = [4, 6, 1, 2, 8, 9, 0]
        heap = MaxHeap(ints)
        exp_lst = [9, 8, 4, 2, 6, 1, 0]
        self.assertEqual(heap.heapify(ints), exp_lst) 

    def test_MaxHeap_perc_down(self):
        ints = [1, 0, 2]
        heap = MaxHeap(ints)
        heap.perc_down(0)
        exp_lst = [2, 0, 1]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [1, 2, 0]
        heap = MaxHeap(ints)
        heap.perc_down(0)
        exp_lst = [2, 1, 0]
        self.assertEqual(heap.heap_lst, exp_lst)

        #      3                6
        #    /   \            /   \
        #   6     4          5     4
        #  / \   / \        / \   / \
        # 5   2 1   0      3   2 1   0
        ints = [3, 6, 4, 5, 2, 1, 0]
        heap = MaxHeap(ints)
        heap.perc_down(0)
        exp_lst = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(heap.heap_lst, exp_lst)

        #      2                6
        #    /   \            /   \
        #   6     4          5     4
        #  / \   / \        / \   / \
        # 3   5 1   0      3   2 1   0
        ints = [2, 6, 4, 3, 5, 1, 0]
        heap = MaxHeap(ints)
        heap.perc_down(0)
        exp_lst = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(heap.heap_lst, exp_lst)

    def test_MaxHeap_perc_up(self):
        
        ints = [0, 1, 2, 3, 4, 5, 6]
        heap = MaxHeap(ints)
        heap.perc_up(6)
        exp_lst = [6, 4, 5, 3, 1, 0, 2]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [33, 66, 22, 77, 99, 11]
        heap = MaxHeap(ints)
        heap.perc_up(5)
        exp_lst = [99, 77, 22, 33, 66, 11]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [-77, -6, -4, -7, -9]
        heap = MaxHeap(ints)
        heap.perc_up(4)
        exp_lst = [-4, -6, -77, -7, -9]
        self.assertEqual(heap.heap_lst, exp_lst)
        

    def test_MaxHeap_init(self):
        ints = [6, 5, 4, 3, 2, 1, 0]
        heap = MaxHeap(ints)
        exp_lst = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(heap.heap_lst, exp_lst)

        #      3                19
        #    /   \            /   \
        #   19    1          14    7
        #  / \   / \        / \   / \
        # 14  8 7   0      3   8 1   0
        ints = [3, 19, 1, 14, 8, 7, 0]
        heap = MaxHeap(ints)
        exp_lst = [19, 14, 7, 3, 8, 1, 0]
        self.assertEqual(heap.heap_lst, exp_lst)

        #      3                6
        #    /   \            /   \
        #   6     2          3     5
        #  / \   /          / \   / 
        # 1   0 5          1   0 2  
        ints = [3, 6, 2, 1, 0, 5]
        heap = MaxHeap(ints)
        exp_lst = [6, 3, 5, 1, 0, 2]
        self.assertEqual(heap.heap_lst, exp_lst)


    def test_MaxHeap_insert(self):

        #        6                7
        #      /   \            /   \
        #     5     4          6     4
        #    / \   / \       /  \   /  \
        #   3   2 1   0     5    2 1    0
        #  /               /
        # 7  <--- new_int 3
        ints = [6, 5, 4, 3, 2, 1, 0]
        heap = MaxHeap(ints)
        new_int = 7
        heap.insert(new_int)
        exp_lst = [7, 6, 4, 5, 2, 1, 0, 3]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [3, 5, 1, 7, 8, 9, 2]
        heap = MaxHeap(ints)
        new_int = 100
        heap.insert(new_int)
        exp_lst = [100, 9, 3, 8, 5, 1, 2, 7]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [-22, -74, -8, -1, -7, 0]
        heap = MaxHeap(ints)
        new_int = 200
        heap.insert(new_int)
        exp_lst = [200, -1, 0, -74, -7, -22, -8]
        self.assertEqual(heap.heap_lst, exp_lst)

    def test_MaxHeap_delet(self):
        
        ints = [6, 5, 4, 3, 2, 1, 0]
        heap = MaxHeap(ints)
        self.assertEqual(heap.delete(), 6)
        exp_lst = [5, 3, 4, 0, 2, 1]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [44, 11, 66, 77, 88, 33, 0]
        heap = MaxHeap(ints)
        self.assertEqual(heap.delete(), 88)
        exp_lst = [77, 44, 66, 0, 11, 33]
        self.assertEqual(heap.heap_lst, exp_lst)

        ints = [0, -2, 4, 99, -5, -3, 88]
        heap = MaxHeap(ints)
        self.assertEqual(heap.delete(), 99)
        exp_lst = [88, 0, 4, -2, -5, -3]
        self.assertEqual(heap.heap_lst, exp_lst)

    def test_MaxHeap_create_tree(self):

        ints = [3, 2, 1]
        heap = MaxHeap(ints)
        root = heap.create_tree()
        current_3 = root
        current_2 = current_3.l_child
        current_1 = current_3.r_child
        self.assertEqual(current_3.priority, 3)
        self.assertEqual(current_2.priority, 2)
        self.assertEqual(current_1.priority, 1)
        
        ints = [5, 3, 4]
        heap = MaxHeap(ints)
        root = heap.create_tree()
        current_5 = root
        current_3 = current_5.l_child
        current_4 = current_5.r_child
        self.assertEqual(current_5.priority, 5)
        self.assertEqual(current_3.priority, 3)
        self.assertEqual(current_4.priority, 4)

        ints = [9, 8, 7]
        heap = MaxHeap(ints)
        root = heap.create_tree()
        current_9 = root
        current_8 = current_9.l_child
        current_7 = current_9.r_child
        self.assertEqual(current_9.priority, 9)
        self.assertEqual(current_8.priority, 8)
        self.assertEqual(current_7.priority, 7)

        #                      10
        #                   /      \
        #                 9          8
        #               /  \        /  \
        #             7     6      5    4
        #            / \   / \
        #           3   2 1   0
        ints= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        heap = MaxHeap(ints)
        root = heap.create_tree()
        current_10 = root
        current_9 = current_10.l_child
        current_8 = current_10.r_child
        current_7 = current_9.l_child
        current_6 = current_9.r_child
        current_5 = current_8.l_child
        current_4 = current_8.r_child
        current_3 = current_7.l_child
        current_2 = current_7.r_child
        current_1 = current_6.l_child
        current_0 = current_6.r_child

        self.assertEqual(current_
    def test_MaxHeap_heap_sort(self):
        
        ints = [2, 4, 3, 6, 7, 8, 1, 0]
        heap = MaxHeap(ints)
        exp_lst = [8, 7, 6, 4, 3, 2, 1, 0]
        act_lst = heap.sort_heap()
        self.assertEqual(act_lst, exp_lst) 

        ints = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]
        heap = MaxHeap(ints)
        exp_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        act_lst = heap.sort_heap()
        self.assertEqual(act_lst, exp_lst) 

        ints = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        heap = MaxHeap(ints)
        exp_lst = [8, 7, 6, 5, 4, 3, 2, 1, 0]
        act_lst = heap.sort_heap()
        self.assertEqual(act_lst, exp_lst) 


if __name__ == "__main__":
    unittest.main()
