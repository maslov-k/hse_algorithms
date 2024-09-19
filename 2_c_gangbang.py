class Gangbang:
    def __init__(self):
        self.first_biggest_ = 0
        self.second_biggest_ = 0

    def add_dwarf(self, dwarf_height):
        if dwarf_height >= self.first_biggest_:
            self.second_biggest_ = self.first_biggest_
            self.first_biggest_ = dwarf_height
        elif dwarf_height >= self.second_biggest_:
            self.second_biggest_ = dwarf_height

    def first_biggest(self):
        return self.first_biggest_

    def second_biggest(self):
        return self.second_biggest_


if __name__ == '__main__':
    gangbang = Gangbang()

    while True:
        _h = int(input())

        if _h != 0:
            gangbang.add_dwarf(_h)
        else:
            break

    print(gangbang.first_biggest())
    print(gangbang.second_biggest())
