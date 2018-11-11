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
    elif c in ['quit', 'exit']:
        break
