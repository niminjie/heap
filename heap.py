from ipdb import set_trace
import logging


def max_heap(a, b):
    return a > b

def min_heap(a, b):
    return a < b

class Heap(object):
    """This is a heap"""
    def __init__(self, max_size=1000, compare=max_heap):
        super(Heap, self).__init__()
        self.max_size = max_size
        self.compare = max_heap
        self.heap = ['#']
        self.cursor = 0

    def insert(self, value):
        # if self.index <= 0:
        #     self.heap.append('#')
        self.heap.append(value)
        self.cursor += 1
        self.heap_up(self.cursor)

    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def heap_up(self, index):
        if index > 1:
            parent = index // 2
            parent_value = self.heap[parent]
            index_value = self.heap[index]
            if parent_value < index_value:
                self.swap(parent, index)
                self.heap_up(parent)

    def delete(self, index):
        #set_trace()
        #logging.warning("Deleting a element index : %d, value: %d" % (index, heap[index]))
        self.heap[index] = self.heap[self.cursor]
        self.heap_down(index)
        del self.heap[self.cursor]
        self.cursor -= 1

    def heap_down(self, index):
        number = self.cursor
        #logging.warning("Heap_down ,Index: %d, Number of tree: %d" % (index, number))
        child = -1

        # Havn't any child
        if 2 * index > number:
            return
        # Have both left and right child
        elif 2 * index < number:
            left = 2 * index
            right = 2 * index + 1
            if self.heap[left] < self.heap[right]:
                child = right
            else:
                child = left
        # Only have left child
        elif 2 * index == number:
            child = 2 * index

        if self.heap[index] < self.heap[child]:
            #logging.warning("Before swap:" +  str(heap))
            #logging.warning("Swap: %d and %d" % (child, index))
            self.swap(child, index)
            #logging.warning("After swap:" +  str(heap))
            self.heap_down(child)

def test_heap():
    insert_queue = [45, 36, 18, 53, 72, 30, 48, 93 ,15 ,35]
    heap_value = [0]

    for item in insert_queue:
        insert_max(heap_value, item)

    print 'Successfully create a maxium heap :'
    print heap_value
    #delete_max(heap_value, 1)
    #print heap_value

    for i in range(1, len(heap_value)):
        #print 'Delete: (Index: 1, Value: %d)'%heap_value[1] 
        delete_max(heap_value, 1)
        #print heap_value

if __name__ == '__main__':
    #set_trace()
    #test_heap()
    heap = Heap()    
    insert_queue = [45, 36, 18, 53, 72, 30, 48, 93 ,15 ,35]
    for item in insert_queue:
        heap.insert(item)
    print heap.heap

    for i in range(1, heap.cursor):
        print heap.heap[1]
        heap.delete(1)
