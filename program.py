

import pygame

pygame.init()
# считываем размер окна
size = width, height = 300, 600
screen = pygame.display.set_mode(size)


def draw():
    # задаем параметры прямоугольника
    rect_colors = pygame.Color('gold')
    rect_width = 0
    rect_point = [(10, 10), (5, 580)]
    # рисуем прямоугольник
    pygame.draw.rect(screen, rect_colors, rect_point, rect_width)


draw()


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()


pygame.quit()

'''
if __name__ == '__main__':
    print("first git file")
    print('main branch')
    print('fourth branch')
    print('hi boy')
    print("new branch, i see you")
    print('еще что то сделали')
    print('new branch, еще один коммит, не опупел еще?')
    #    app = QApplication(sys.argv)
    #    ex = Example()
    #    ex.show()
    #    sys.exit(app.exec()) '''
