# A=[1,2,3,4,5]
# for x in A:
#     print(x)
#     x+=1
#     print (x)
# print (A)
#
# A=[1,2,3,4,5]
# for k in range(len(A)):
#     print(k)
#     A[k]*=A[k]
# print (A)
# A=[0]*100
# print(A)
# top=0
# x=int(input())
# while x!=0:
#     A[top]=x
#     top+=1
#     x=int(input())
#     print (A)
# print (top)
# for k in range(4,-1,-1):
#     print (A[k])



#
# N=int(input())
# A=[0]*N
# B=[0]*N
# print (A)
# print(B)
# for k in range(N):
#     A[k]=int(input())
# for k in range(N):
#     B[k]=A[k]
# print (A)
# print(B)

# def array_search(A:list,N:int,x:int):
#     """Осуществляет поиск числа X в массиве А от 0 до N-1 индекса включительно.
#     Возвращает индекс элемента Х в массиве А. Или -1, если такого нет
#     Если в массиве несколько одинаковых элементов равных Х, то вернуть индекс первого по счету
#     """
#     for k in range(N):
#         if A[k] ==x:
#             return k
#
# def test_array_search():
#     A1=[1,2,3,4,5]
#     m=array_search(A1,5,8)
#     if m==-1:
#         print("#Test1 - ok")
#     else:
#         print('#Test1 - fail')
#
#     A2=[-1,-2,-3,-4,-5]
#     m=array_search(A2,5,-3)
#     if m==-1:
#         print("#Test2 - ok")
#     else:
#         print('#Test2 - fail')
#
#     A3=[11,22,44,44,55]
#     m=array_search(A2,5,44)
#     if m==-1:
#         print("#Test3 - ok")
#     else:
#         print('#Test3 - fail')
# test_array_search()

# def invert_array(A:list,N:int):
#     """Обращение списка (поворот задом наперед
#
#     :param A:
#     :return:
#     """
#     for k in range(N//2):
#         A[k],A[N-1-k]=A[N-1-k],A[k]
#
# def test_invert_array():
#     A1 = [1, 2, 3, 4, 5]
#     print(A1)
#     invert_array(A1,5)
#     print(A1)
#     if A1==[5,4,3,2,1]:
#         print("#Test1 - ok")
#     else:
#         print('#Test1 - fail')
#     A2 = [0,0,0,0,0,10]
#     print(A2)
#     invert_array(A2, 6)
#     print(A2)
#     if A2 == [10,0,0,0,0,0]:
#         print("#Test2 - ok")
#     else:
#         print('#Test2 - fail')
#
# test_invert_array()

# B=[1,2,3,4,5,6]
# invert_array(B,6)
# print(B)

# A = [1, 2, 3, 4, 5] #Циклический сдвиг влево
# print(A)
# N=len(A)
# tmp=A[0]
# for k in range (N-1):
#     A[k]=A[k+1]
# A[N-1]=tmp
# print(A)

# A = [1, 2, 3, 4, 5] #Циклический сдвиг вправо
# print(A)
# N=len(A)
# tmp=A[N-1]
# for k in range (N-2,-1,-1):
#     A[k+1]=A[k]
# A[0]=tmp
# print(A)

'''Решето Эратосфена'''
N=100
A=[True]*N
A[0]=A[1]=False
for k in range (2,N):
    if A[k]:
        for m in range(2*k,N,k):
            A[m]=False
for k in range(N):
    print(k,'-','простое' if A[k] else 'составное')