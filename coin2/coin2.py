N, C = 14, 4
sqaure = 0
string = ''
backeup = 0
sw = 1

for i in range(C):
    square = 2 ** i
    backup = square
    for j in range(square-1, N):
        if(sw % 2 == 1):
            string += str(j+1) + ' '
            backup -= 1
        else:
            backup -= 1

        if(backup == 0):
            sw += 1
            backup = square

    print(string)
    string = ''
    sw = 1
