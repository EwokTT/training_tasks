def matryoshka(n):
    '''Пишет матрешку, с уровнем вложения n. Тестовая функция'''
    if n==1:
        print ('Матрешечка')
    else:
        print ('Верх матрешки n=', n)
        matryoshka(n-1)
        print('Низ матрешки n=', n)
import graphics as gr
# window=gr.GraphWin ("Work Window", 600,600)
# alpha=0.1
def fractal_rectangle (A,B,C,D,deep=10):
    if deep<1:
        return
    for M,N in (A,B), (B,C),(C,D),(D,A):                # цикл фор пробегает по парам переменных
        gr.Line(gr.Point(*M),gr.Point(*N)).draw(window) # *- разворачивает список или кортеж как параметры
    A1 = (A[0] * (1-alpha) + B[0] * alpha, A[1] * (1-alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1,B1,C1,D1,deep-1)
# fractal_rectangle((100,100),(500,100),(500,500),(100,500),100)
# window.getMouse()

def faktorial(n):
    """Функция считает факториал

    :param n: число от которого нужно взять факториал
    :return:
    """
    assert n>=0, "Факториал не определен"
    if n==0:
        return 1
    return faktorial(n-1)*n
print(faktorial(8))

def evklid_algorithm(a,b):
    if b==0:
        return a
    else:
        return evklid_algorithm(b,a%b)

def gcd (a,b):
    return a if b==0 else gcd (b,a%b)

print (gcd (128,805))

def pow(a,n):
    """ Возведение числа а в степень n"""
    if n==0:
        return 1
    elif n%2==1:
        return pow (a,n-1)*a
    else:
        return pow(a**2,n//2)
print (pow (3,100))

# def hanoi_towers(n,k):