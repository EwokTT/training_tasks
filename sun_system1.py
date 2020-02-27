import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 700)
ball_start_coords=gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)
# def draw_ball(400,700):
#     circle = gr.Circle(coords, 10)
#     circle.setFill('red')
#     circle.draw(window)
#         Wh


clear_window()

circle = gr.Circle(ball_start_coords, 10)
circle.setFill('red')
circle.draw(window)
while True:
    #Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    circle.move(1, 1)

    gr.time.sleep(0.02)
window.getMouse()
