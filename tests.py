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



if __name__ == "__main__":
    unittest.main()
