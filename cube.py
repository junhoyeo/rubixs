class Cube:
    def __init__(self):
        self.cube = [[[i, i, i] for j in range(3)] for i in range(6)]
    
    def print_block(self, color):
        table = [
            '\x1b[0;37;47m', # 0: white
            '\x1b[0;31;41m', # 1: red
            '\x1b[0;34;44m', # 2: blue
            '\x1b[0;35;45m', # 3: purple
            '\x1b[0;32;42m', # 4: green
            '\x1b[0;33;43m'  # 5: yellow
        ]
        print(table[color] + str(color)*2 + '\x1b[0m', end='')

    def print_face(self, face, margin=False):
        for row in self.cube[face]:
            if margin:
                print(' '*6, end='')
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
        side = [face[0] for face in self.cube[1:5]]
        side = side[1:] + side[:1]
        for idx, face in enumerate(self.cube[1:5]):
            face[0] = side[idx]
        top = [list(i) for i in list(zip(*self.cube[0][::-1]))]
        self.cube[0] = top
