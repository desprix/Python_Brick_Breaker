from pgzero.actor import Actor
def level_1():
    bricks = []

    for i in range(10):
        brick_r = Actor('brick.red')
        brick_r.left = i * brick_r.width
        bricks.append(brick_r)

    for i in range(10):
        brick_y = Actor('brick.yellow')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height
        bricks.append(brick_y)

    for i in range(10):
        brick_g = Actor('brick.green')
        brick_g.left = i * brick_g.width
        brick_g.top = brick_g.height * 2
        bricks.append(brick_g)

    for i in range(10):
        brick_b = Actor('brick.blue')
        brick_b.left = i * brick_b.width
        brick_b.top = brick_b.height * 3
        bricks.append(brick_b)
    return bricks
def level_2():
    bricks = []

    for i in range(1,2):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 2
        bricks.append(brick_y)
    for i in range(2,8):
        brick_y = Actor('brick.blue')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 2
        bricks.append(brick_y)
    for i in range(8,9):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 2
        bricks.append(brick_y)

    for i in range(1,2):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 3
        bricks.append(brick_y)
    for i in range(2,8):
        brick_y = Actor('brick.blue')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 3
        bricks.append(brick_y)
    for i in range(8,9):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 3
        bricks.append(brick_y)

    for i in range(1,9):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 4
        bricks.append(brick_y)

    for i in range(1,9):
        brick_y = Actor('brick.red')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height * 5
        bricks.append(brick_y)
    return bricks
from pgzero.actor import Actor
def level_3():
    bricks = []
    for i in range(4,6):
        brick_y = Actor('brick.blue')
        brick_y.left = i * brick_y.width
        bricks.append(brick_y)

    for i in range(3,7):
        brick_y = Actor('brick.blue')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_y.height
        bricks.append(brick_y)

    for i in range(2,8):
        brick_g = Actor('brick.blue')
        brick_g.left = i * brick_g.width
        brick_g.top = brick_g.height * 2
        bricks.append(brick_g)

    for i in range(2,8):
        brick_b = Actor('brick.blue')
        brick_b.left = i * brick_b.width
        brick_b.top = brick_b.height * 3
        bricks.append(brick_b)

    for i in range(3,7):
        brick_b = Actor('brick.blue')
        brick_b.left = i * brick_b.width
        brick_b.top = brick_b.height * 4
        bricks.append(brick_b)

    for i in range(4,6):
        brick_y = Actor('brick.blue')
        brick_y.left = i * brick_y.width
        brick_y.top = brick_b.height * 5
        bricks.append(brick_y)
    return bricks
