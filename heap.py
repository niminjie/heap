from ipdb import set_trace
import random
import time
import logging


def max_heap(a, b):
    return a > b

def min_heap(a, b):
    return a < b

class Heap(object):
    """This is a heap"""
    def __init__(self, max_size=None, compare=max_heap):
        super(Heap, self).__init__()
        self.max_size = max_size
        self.compare = compare
        self.heap = ['#']
        self.cursor = 0

    def get_top(self):
        top = self.heap[1]
        self.delete(1)
        return top

    def insert(self, value):
        if self.max_size == None:
            self.heap.append(value)
            self.cursor += 1
            self.heap_up(self.cursor)
        else:
            if self.cursor < self.max_size:
                self.heap.append(value)
                self.cursor += 1
                self.heap_up(self.cursor)
            else:
                if (not self.compare(value, self.heap[1])):
					self.heap[1] = value
					self.heap_down(1)


    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def heap_up(self, index):
        if index > 1:
            parent = index // 2
            parent_value = self.heap[parent]
            index_value = self.heap[index]
            #if parent_value < index_value:
            if self.compare(index_value, parent_value):
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
            # if self.heap[left] < self.heap[right]:
            if self.compare(self.heap[right], self.heap[left]):
                child = right
            else:
                child = left
        # Only have left child
        elif 2 * index == number:
            child = 2 * index

        # if self.heap[index] < self.heap[child]:
        if self.compare(self.heap[child], self.heap[index]):
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
    #insert_queue = [45, 36, 18, 53, 72, 30, 48, 93 ,15 ,35]
    insert_queue = []
    for i in range(0, 1000000):
        insert_queue.append(random.randint(1, 1000))
    heap = Heap(max_size = 2000000,compare=max_heap)    
    for item in insert_queue:
        heap.insert(item)
    start = time.clock()
    print "Delete a eme"
    heap.delete(1)
    end = time.clock()
    print (end - start)
    start = time.clock()
    print max(insert_queue)
    end = time.clock()
    print (end - start)
    #print heap.heap

    #for i in range(1, heap.cursor):
    #    print heap.get_top()
