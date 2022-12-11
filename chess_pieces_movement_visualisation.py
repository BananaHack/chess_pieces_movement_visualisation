from time import sleep
from os import system, name

def program():
    print('Добро пожаловать в программу по визуализации возможных направлений\nдвижения шахматных фигур исходя из заданной координаты.\n')

    sleep(2)
    n, current_figure = 8, ''

    print('Краткая справка:\n\nШахматная нотация - это способ, с помощью которого записываются партии.\nЧтобы отметить позицию фигуры, нужно сначала записать букву вертикали,\nна которой она находится, а следом — цифру горизонтали.\nПример: e4 - самое популярное начало в шахматах,\nпервый ход за белых королевской пешкой на две клетки вперёд.\n\nКакие бывают шахматные фигуры:\nПешка, Слон, Конь, Ладья, Ферзь, Король.\nПо-английски: Pawn, Bishop, Knight, Rook, Queen, King.\n\n')
    sleep(10)
    # Ввод координаты шахматной фигуры
    while True:
        xy = input('Введите координаты фигуры в шахматной нотации.\nБуква от a до h, цифра от 1 до 8:   ')
        print()
        try:
            len(xy) == 2
            if ord('a') <= ord(xy[0]) <= ord('h') and 1 <= int(xy[1]) <= 8:
                break
        except Exception:
            sleep(1)
            print("Неверный формат записи.\nВведите координаты заново по образцу в справке\n\n")
            sleep(1)
            continue

    # Создание пустой шахматной доски
    matrix = [['.' for _ in range(n)] for _ in range(n)]
    col, row = ord(xy[0]) - 97, n - int(xy[1])

    sleep(1)
    while True:
        matrix[row][col] = input('\nВведите название шахматной фигуры:  ').lower()
        # пешка(pawn): п = 1087, P = 80
        # слон(bishop): с = 1089, B = 66
        # конь(knight): к = 1082, N = 78
        # ладья(rook): л = 1083, R = 82
        # ферзь(queen): ф = 1092, Q = 81
        # король(king): к = 1082, K = 75

        if matrix[row][col] == 'пешка' or matrix[row][col] == 'pawn':
            if row == 7: 
                sleep(1)
                print("Невозможно, чтобы пешка стояла на 1 линии. Выберите другую фигуру.")
                continue
            else:
                current_figure = 'пешки'
                matrix[row][col] = chr(ord('п') - 1007)
                break

        elif matrix[row][col] == 'слон' or matrix[row][col] == 'bishop':
            current_figure = 'слона'
            matrix[row][col] = chr(ord("с") - 1023)
            break

        elif matrix[row][col] == 'конь' or matrix[row][col] == 'knight':
            current_figure = 'коня'
            matrix[row][col] = chr(ord("к") - 1004)
            break

        elif matrix[row][col] == 'ладья' or matrix[row][col] == 'rook':
            current_figure = 'ладьи'
            matrix[row][col] = chr(ord("л") - 1001)
            break

        elif matrix[row][col] == 'ферзь' or matrix[row][col] == 'queen':
            current_figure = 'ферзя'
            matrix[row][col] = chr(ord("ф") - 1011)
            break

        elif matrix[row][col] == 'король' or matrix[row][col] == 'king':
            current_figure = 'короля'
            matrix[row][col] = chr(ord("к") - 1007)
            break
		
        else:
            sleep(1)
            print("\nНеверная запись.\nВведите правильное название фигуры по-русски или по-английски.\n")
            sleep(1)
            continue


    print()
    for i in range(n):
        for j in range(n):      
            # когда пешка
            if matrix[row][col] == 'P':
                # когда пешка стоит на 2 линии, она может идти на 2 клетки вперед
                if row == 6:
                    if (row - i == 1 or row - i == 2) and col - j == 0:
                        matrix[i][j] = '*'
					
                # на других линиях пешка может идти только на 1 клетку вперед				
                else:
                    if row - i == 1 and col - j == 0:
                        matrix[i][j] = '*'

            # когда слон
            elif matrix[row][col] == 'B':
                if i != abs(row) and j != col:
                    if abs(row - i) == abs(col - j): matrix[i][j] = '*'
            # когда конь
            elif matrix[row][col] == 'N': 
                if (i - row) ** 2 + (j - col) ** 2 == 5: matrix[i][j] = '*'
            # когда ладья
            elif matrix[row][col] == 'R':
                if i != abs(row) and j != col:
                    matrix[i][col] = '*'
                    matrix[row][j] = '*'
            # когда ферзь
            elif matrix[row][col] == 'Q':
                if i != abs(row) and j != col:
                    matrix[i][col] = '*'
                    matrix[row][j] = '*'
                    if abs(row - i) == abs(col - j): matrix[i][j] = '*'
            # когда король
            elif matrix[row][col] == 'K':
                if (i - row) ** 2 + (j - col) ** 2 == 2 or (i - row) ** 2 + (j - col) ** 2 == 1: matrix[i][j] = '*'		

        
    print('\nВизуализация возможных ходов {0} выглядит следующим образом:'.format(current_figure))
    print()

    # Вывод шахматной доски с визуализацией возможных направлений движения шахматных фигур        
    for i in range(n):
        print(*[' ']*9, end='')
        print(str(n - i) + ' ', end='')
        print(*matrix[i])
	
    print(*[' ']*10, end='')
    print(*['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
	
    sleep(5)
    while True:
        repeat = input('\nПосмотреть визуализацию ещё раз или выйти?\nВведите 1 - если да, 0 - если нет:   ')
        if repeat == '1':
            return True
        elif repeat == '0':
            return False
        else:
            print('\nНекорректный ввод!\n')
            continue
			
# очистка экрана для нового запуска
def cls():
    system('cls' if name=='nt' else 'clear')
	
while True:
    result = program()
    if result == True:
        cls()
        continue
    else: break