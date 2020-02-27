def insert_sort(A):
    '''Сортировка списка А вставками'''
    N=len(A)
    for top in range(1,N):
        k=top
        while k>0 and A[k-1]>A[k]:
            A[k],A[k-1]=A[k-1],A[k]
            k-=1


def choise_sort (A):
    """Сортировка списка А сортировкой"""
    N=len(A)
    for pos in range (0,N-1):
        for k in range(pos+1,N):
            if A[k]<A[pos]:
                A[k],A[pos]=A[pos],A[k]

def buble_sort (A):
    """Сортировка A методом пузырька"""
    N=len(A)
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if A[k]>A[k+1]:
                A[k],A[k+1]=A[k+1],A[k]
def random_list():
    """Генерирует случайный"""

    import random
    A=list()
    for i in range (random.randint(10,20)):
        A.append(random.randint(10,40))
    return  A
print (random_list())

def test_sort(sort_algorithm):
    print ("Тестируем", sort_algorithm.__doc__)
    print ('Testcase #1:', end='')
    import random
    A=[4,2,1,3,5]
    A_sorted=[1,2,3,4,5]
    sort_algorithm(A)
    print('Ок' if A==A_sorted else "fail")

    print("Тестируем", sort_algorithm.__doc__)
    print('Testcase #2:', end='')
    import random
    A = list(range (10,20))+list(range (0,10))
    A_sorted = list(range (20))
    sort_algorithm(A)
    print('Ок' if A == A_sorted else "fail")
    print("Тестируем", sort_algorithm.__doc__)
    print('Testcase #3:', end='')
    import random
    A = [4, 2, 1, 2, 4]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('Ок' if A == A_sorted else "fail")
if __name__=="__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)


    """Сортировка подсчетом. только для цифр, ограниченное значение"""


