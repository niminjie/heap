from ipdb import set_trace
import logging


def insert_max(heap, value):
    if len(heap) <= 0:
        heap.append(0)
    heap.append(value)
    heap_up(heap, len(heap) - 1)

def delete_max(heap, idx):
    #set_trace()
    logging.warning("Deleting a element index : %d, value: %d" % (idx, heap[idx]))
    last = len(heap) - 1
    heap[idx] = heap[last]
    heap_down(heap, idx)
    del heap[last]

def heap_down(heap, idx):
    number = len(heap) - 2
    logging.warning("Heap_down ,Index: %d, Number of tree: %d" % (idx, number))
    child = -1

    # Havn't any child
    if 2 * idx > number:
        return
    # Have both left and right child
    elif 2 * idx < number:
        left = 2 * idx
        right = 2 * idx + 1
        if heap[left] < heap[right]:
            child = right
        else:
            child = left
    # Only have left child
    elif 2 * idx == number:
        child = 2 * idx

    if heap[idx] < heap[child]:
        logging.warning("Before swap:" +  str(heap))
        logging.warning("Swap: %d and %d" % (child, idx))
        swap(heap, child, idx)
        logging.warning("After swap:" +  str(heap))
        heap_down(heap, child)

def heap_up(heap, idx):
    if idx > 1:
        parent = idx / 2
        parent_value = heap[parent]
        idx_value = heap[idx]

        if parent_value < idx_value:
            swap(heap, parent, idx)
            heap_up(heap, parent)

def swap(heap, value1, value2):
    tmp = heap[value1]
    heap[value1] = heap[value2]
    heap[value2] = tmp

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
    test_heap()
