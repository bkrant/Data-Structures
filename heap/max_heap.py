class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        insert_list = [None] + self.storage + [value]
        self.storage = self._heapify(insert_list)

    def delete(self):
        delete_list = [None] + [self.storage[-1]] + self.storage[1:-1]
        removed_element = self.get_max()
        self.storage = self._heapify(delete_list)
        return removed_element

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    def _heapify(self, list_to_heapify):
        while True:
            swaps = 0
            for i in range((len(list_to_heapify)-1)//2 ,0, -1):
                try: #if 2*i+1 <= len(list_to_heapify)-1:
                    if list_to_heapify[i] < list_to_heapify[2*i] or list_to_heapify[i] < list_to_heapify[2*i+1]:
                        max_child = max(list_to_heapify[2*i], list_to_heapify[2*i+1])
                        if list_to_heapify[2*i] == max_child:
                            max_child_index = 2*i
                        else:
                            max_child_index = 2*i+1
                        list_to_heapify[i], list_to_heapify[max_child_index] = max_child, list_to_heapify[i]
                        swaps += 1

                except:
                    if list_to_heapify[i] < list_to_heapify[2*i]:
                        list_to_heapify[i], list_to_heapify[2*i] = list_to_heapify[2*i], list_to_heapify[i]
                        swaps += 1

            if swaps == 0:
                break

        return(list_to_heapify[1:])