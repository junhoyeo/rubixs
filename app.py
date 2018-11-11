from cube import Cube

A = Cube()
print()
A.print_cube()

while(1):
    c = input('>>> ')
    if c == 'U':  
        A.U()
        A.print_cube()
    elif c == 'quit' or c == 'exit':
        break
