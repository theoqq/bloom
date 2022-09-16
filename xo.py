# создаем матрицу 3х3
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range (3):
    print (A[i])
N = 0
M = 0 # счетчик

# блок функций

def nachaloX():
    while True:
        flag = input ('начать с начала? [да/нет]')
        if flag == 'да':
            xxx(A)
            break
        else:
            break
    return ()

def prodolgenieO():
    ooo(A)
    return()

def xxx(A):
    global N
    vvodX = int(input('введите цифру куда поставить Х '))
    if 0 < vvodX <= 9:
        for i in range(3):
            for j in range(3):
                if vvodX == A[i][j]:
                    A[i][j] = "X"
                    N+=1
    else:
        print ('вы ввели недопустимое значение. Введите число от 1 до 9')
        nachaloX()
    return A

def ooo(A):
    global M
    vvodO = int(input('введите цифру куда поставить O '))
    if 0 < vvodO <= 9:
        for i in range(3):
            for j in range(3):
                if vvodO == A[i][j]:
                    A[i][j] = "O"
                    M+=1
    else:
        print('вы ввели недопустимое значение')
        prodolgenieO()
    return(A)

def check(A):
    global fl
    for i in range (3):
        for j in range (3):
            if A[0][0]==A[1][1]==A[2][2] or A[0][0]==A[0][1]==A[0][2] or A[0][0]==A[1][0]==A[2][0] \
                    or A[0][2]==A[1][1]==A[2][0] or A[0][1]==A[1][1]==A[2][1] or A[0][2]==A[1][2]==A[2][2] \
                    or A[1][0]==A[1][1]==A[1][2] or A[2][0]==A[2][1]==A[2][2]:
                fl=0
                break
    return A

# ОСНОВНОЙ МОДУЛЬ

fl=1
while True:
    if M+N == 9:
        print ('ничья')
        break
    elif fl == 1:
        xxx(A)
        for i in range (3):
            print (A[i])
            check(A)
    else:
        print('игра закончена.')
        print('победа второго игрока')
        break
    if fl == 1:
        ooo(A)
        for i in range (3):
            print (A[i])
            check(A)
    else:
        print('игра закончена.')
        print('победа первого игрока')
        break




