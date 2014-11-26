

class Heap(object):

    def __init__(self, comparator=None):
        self.a = []

        # self.comp = None
        # if comparator:
        #     self.comp = comparator
        # else:
        #     self.comp = lambda x: x

    def add(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        fi = self._get_father_index(i)

        while fi is not None and self.a[i] > self.a[fi]:
            self.a[i], self.a[fi] = self.a[fi], self.a[i]
            i = fi
            fi = self._get_father_index(i)

    def get_max(self):
        if self.empty():
            return None

        if len(self.a) == 1:
            max_n = self.a[0]
            self.a = []
            return max_n

        max_n = self.a[0]
        self.a[0] = self.a.pop()

        i = 0
        ci = self._get_max_child_index(i)

        while ci is not None and self.a[i] < self.a[ci]:
            self.a[i], self.a[ci] = self.a[ci], self.a[i]
            i = ci
            ci = self._get_max_child_index(i)

        return max_n


    def _get_father_index(self, i):
        if i == 0:
            return None
        else:
            return i/2

    def _get_childs_index(self, i):
        c1 = 2*i
        c2 = 2*i+1
        if c1 >= len(self.a):
            c1 = None
        if c2 >= len(self.a):
            c2 = None
        return (c1, c2)

    def _get_max_child_index(self, i):
        c1, c2 = self._get_childs_index(i)
        if not c1 and not c2:
            return None

        if not c1:
            return c2
        if not c2:
            return c1

        if self.a[c1] >= self.a[c2]:
            return c1
        else:
            return c2

    def __str__(self):
        return str(self.a)

    def __len__(self):
        return len(self.a)

    def empty(self):
        return len(self.a) == 0


if __name__ == '__main__':
    import random
    h = Heap()

    for i in range(20):
        x = random.randint(1,50)
        h.add(x)
        print h

    a = []
    while not h.empty():
        a.append(h.get_max())
    print a
