import time

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

#немного интерактива следующие 7 строчек:)
for i in range(101):
    time.sleep(0.01)
    if i!=100:
        print('Загрузка: ', str(i)+'%', '\r', end="")
    else:
        print('Загрузка: ', str(i)+'%', '\r')
    
discriminant = (b**2 - 4*a*c)

if a != 0:
    if discriminant >= 0:
        x1 = ((-1)*b + discriminant**(0.5)) / 2*a
        x2 = ((-1)*b - discriminant**(0.5)) / 2*a
        print('Первый корень:', x1, '\nВторой корень:', x2)
    else:
        print('У данного уравнения нет корней корней, тк дискриминант отрицательный')
else:
    print('Единственный корень уравнения:', (-1)*c/b)