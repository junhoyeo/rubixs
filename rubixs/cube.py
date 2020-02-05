class Cube:
    def __init__(self):
        self.cube = [[[i, i, i] for j in range(3)] for i in range(6)]
        # self.cube[5][2][0] = 1 # for testing rotation
        # self.cube[0][2][0] = 1 # for testing rotation

    def print_block(self, color):
        table = [
            '\x1b[0;37;47m',  # 0: white
            '\x1b[0;31;41m',  # 1: red
            '\x1b[0;34;44m',  # 2: blue
            '\x1b[0;35;45m',  # 3: purple
            '\x1b[0;32;42m',  # 4: green
            '\x1b[0;33;43m'  # 5: yellow
        ]
        print(table[color] + str(color) * 2 + '\x1b[0m', end='')

    def print_face(self, face, margin=False):
        for row in self.cube[face]:
            if margin:
                print(' ' * 6, end='')
            for c in row:
                self.print_block(c)
            print()

    def print_cube(self):
        self.print_face(0, 1)
        for col in range(3):
            for idx in range(1, 5):
                for c in self.cube[idx][col]:
                    self.print_block(c)
            print()
        self.print_face(5, 1)

    def U(self, clockwise=True):
        # counterclockwise if clockwise=False
        shift = -1 if not clockwise else 1
        # rotate the sides
        side = [face[0] for face in self.cube[1:5]]
        side = side[shift:] + side[:shift]
        for idx, face in enumerate(self.cube[1:5]):
            face[0] = side[idx]
        # rotate the top
        if clockwise:
            top = [list(i) for i in list(zip(*self.cube[0][::-1]))]
        else:  # rotate counterclockwise
            top = [list(i) for i in list(
                map(list, reversed(list(zip(*self.cube[0])))))]
        self.cube[0] = top

    def D(self, clockwise=True):
        # counterclockwise if clockwise=False
        shift = -1 if not clockwise else 1
        # rotate the sides
        side = [face[2] for face in self.cube[1:5]]
        side = side[shift:] + side[:shift]
        for idx, face in enumerate(self.cube[1:5]):
            face[2] = side[idx]
        # rotate the bottom
        if clockwise:
            bot = [list(i) for i in list(
                map(list, reversed(list(zip(*self.cube[5])))))]
        else:  # rotate counterclockwise
            bot = [list(i) for i in list(zip(*self.cube[5][::-1]))]
        self.cube[5] = bot

    def F(self, clockwise=True):
        w = self.cube[0][2]
        if clockwise:
            r = [self.cube[1][i][2] for i in range(2, -1, -1)]
            p = [self.cube[3][i][0] for i in range(2, -1, -1)]
        else:
            r = [self.cube[1][i][2] for i in range(2, -1, -1)]
            p = [self.cube[3][i][0] for i in range(2, -1, -1)]
        y = self.cube[5][0]
        if clockwise:
            self.cube[0][2] = r
            for idx in range(3):
                self.cube[1][idx][2] = y[idx]
                self.cube[3][idx][0] = w[idx]
            self.cube[5][0] = p
            front = [list(i) for i in list(zip(*self.cube[2][::-1]))]
        else:
            self.cube[0][2] = p
            for idx in range(3):
                self.cube[1][idx][2] = w[idx]
                self.cube[3][idx][0] = y[idx]
            self.cube[5][0] = r
            front = [list(i) for i in list(
                map(list, reversed(list(zip(*self.cube[2])))))]
        self.cube[2] = front

    def B(self, clockwise=True):
        pass

    def R(self, clockwise=True):
        pass

    def L(self, clockwise=True):
        pass


if __name__ == '__main__':
    pass
