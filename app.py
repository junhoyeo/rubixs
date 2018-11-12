from cube import Cube

A = Cube()
print()
A.print_cube()

while(1):
    c = input('>>> ')
    if c == 'U':  
        A.U()
        A.print_cube()
    elif c in ['U\'', 'U`']:
        A.U(clockwise=False)
        A.print_cube()
    elif c == 'U2':
        A.U()
        A.U()
        A.print_cube()
    elif c == 'D':
        A.D()
        A.print_cube()
    elif c in ['D\'', 'D`']:
        A.D(clockwise=False)
        A.print_cube()
    elif c == 'D2':
        A.D()
        A.D()
        A.print_cube()
    elif c == 'F':
        A.F()
        A.print_cube()
    elif c == 'F2':
        A.F()
        A.F()
        A.print_cube()
    elif c.lower() == 'print':
        A.print_cube()
    elif c.lower() == 'init':
        A.cube = [[[i, i, i] for j in range(3)] for i in range(6)]
        A.print_cube()
    elif c.lower() in ['quit', 'exit']:
        break
