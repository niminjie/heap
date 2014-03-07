def insert_max(heap, value):
    if len(heap) <= 0:
        heap.append(0)
    heap.append(value)
    heap_up(heap, len(heap) - 1)

def delete_max(heap, idx):
    last = len(heap) - 1
    heap[idx] = heap[last]
    heap_down(heap, idx)
    del heap[last]

def heap_down(heap, idx):
    number = len(heap) - 2
    
    child = -1
    # Havn't any child
    if 2 * idx > number:
        return

    # Have both left and right child
    elif 2 * idx < number:
        left = 2 * idx
        right = 2 * idx + 1
        if heap[left] < heap[right]:
            child += right

    # Only have left child
    elif 2 * idx == number:
        child = 2 * idx

    if heap[idx] < heap[child]:
        swap(heap, child, idx)
        heap_down(heap, child)

def heap_up(heap, idx):
    if idx > 1:
        parent = idx // 2
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

    print heap_value
    delete_max(heap_value, 1)
    print heap_value


if __name__ == '__main__':
    test_heap()
