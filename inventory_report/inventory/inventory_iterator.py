from collections.abc import Iterator


class InventoryIterator(Iterator):

    def __init__(self, products):
        self.list = products
        self.index = 0

    def __next__(self):
        list = self.list[self.index]
        if not list:
            raise StopIteration()

        self.index += 1

        return list
