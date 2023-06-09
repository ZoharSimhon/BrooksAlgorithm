from collections import OrderedDict

class OrderedSet:
    def __init__(self):
        self.ordered_dict = OrderedDict()

    def add(self, element):
        self.ordered_dict[element] = None

    def remove(self, element):
        self.ordered_dict.pop(element, None)

    def __contains__(self, element):
        return element in self.ordered_dict

    def __iter__(self):
        return iter(sorted(self.ordered_dict))

    def __len__(self):
        return len(self.ordered_dict)
