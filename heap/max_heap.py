class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        insert_list = [None] + self.storage + [value]
        while True:
            swaps = 0
            for i in range((len(insert_list)-1)//2 ,0, -1):
                if 2*i+1 <= len(insert_list)-1:
                    if insert_list[i] < insert_list[2*i] or insert_list[i] < insert_list[2*i+1]:
                        max_child = max(insert_list[2*i], insert_list[2*i+1])
                        if insert_list[2*i] == max_child:
                            max_child_index = 2*i
                        else:
                            max_child_index = 2*i+1
                        insert_list[i], insert_list[max_child_index] = max_child, insert_list[i]
                        swaps += 1

                else:
                    if insert_list[i] < insert_list[2*i]:
                        insert_list[i], insert_list[2*i] = insert_list[2*i], insert_list[i]
                        swaps += 1

            if swaps == 0:
                break

        self.storage = insert_list[1:]


    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
