N, C = 20, 5
string = ''
sq, bi, sw = 0, 0, 0

def cf_coin(string):
    result = ''
    cf_coin = 15
    lst = string.split('-')
    length = len(lst)
    for i in range(length):
        if str(cf_coin) in lst[i].split():
            result += str(len(lst[i].split()) * 10 - 1)
        else:
            result += str(len(lst[i].split()) * 10)
        result += '-'
    return result[:-1]

for i in range(C):
    sq = 2 ** i
    bi = sq
    for j in range(bi, N):
        if(sw % 2 == 0):
            string += str(j) + ' '
            bi -= 1
        else:
            bi -= 1

        if(bi == 0):
            sw += 1
            bi = sq
    string = string[:-1] + '-'
    sw = 0

string = string[:-1]
print(cf_coin(string))
