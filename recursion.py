# import sys
# def fac(n):
#     print (sys.getrecursionlimit())
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n - 1)
#
# print (fac(-5))

import turtle

# def draw(l, n):
#     if n == 0:
#         turtle.left(180)
#         return
#
#     x = l / (n + 1)
#     for i in range(n):
#         turtle.forward(x)
#         turtle.left(45)
#         draw(0.5 * x * (n - i - 1), n - i - 1)
#         turtle.left(90)
#         draw(0.5 * x * (n - i - 1), n - i - 1)
#         turtle.right(135)
#
#     turtle.forward(x)
#     turtle.left(180)
#     turtle.forward(l)
#     turtle.speed('fastest')
#
# draw(400, 4)
a=0.8
def coh_line(l,n):

    if n==0:
        turtle.left(180)
        return
    else:
        turtle.forward(l/3)
        turtle.left(60)
        turtle.forward(l/3)
        turtle.right(120)
        turtle.forward(l/3)
        turtle.left(60)
        turtle.forward(l / 3)
        turtle.left(60)
        coh_line(l * a, n - 1)







coh_line(100,25)
window.getMouse()



