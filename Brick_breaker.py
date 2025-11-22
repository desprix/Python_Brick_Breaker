import random, sys, time,os,copy
from levels import level_1,level_2,level_3
from threading import Thread
os.environ['SDL_VIDEO_CENTERED'] = '1'

HEIGHT = 480
WIDTH = 640
TITLE = "Brick breaker"

level_cache = {
    1: None,
    2: None,
    3: None
}
levels_ready = False

game_state = "title"

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.dx = 1
ball.dy = -1
ball.speed = 0
ball.through = False
ball.through_hits = 0
steps = 10
offset = 0
balls = [ball]
ball_ready = True

paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 7

Score = 0
input_cooldown = 0

game_over = False

bricks = []
hit_bricks = []
powerups = []

selected_level = 1
total_levels = 3

game_over_sound = False
victory_sound = False
music.play('menu_music')
music.set_volume(0.25)
def update():
    global Score,game_over,offset,god,power,game_state,balls,bricks,powerups,victory_sound,game_over_sound,ball,input_cooldown,selected_level,ball_ready,levels_ready
    if input_cooldown > 0:
        input_cooldown = input_cooldown - 1
    if keyboard.escape:
        sys.exit()
    if keyboard.left == True:
        paddle.x = paddle.x - paddle.speed

        if paddle.left < 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x = paddle.x + paddle.speed

        if paddle.right > WIDTH:
            paddle.right = WIDTH

    if ball_ready == True:
        ball.x = paddle.x
        ball.bottom = paddle.top - 2
    #God mode
    #for ball in balls:
     #   paddle.x = ball.x + random.randint(-60,60)
    for ball in balls:
        if ball.right >= WIDTH:
            ball.right = WIDTH
            ball.dx = -ball.dx
            sounds.wall_hit.play()
        elif ball.left <= 0:
            ball.dx = -ball.dx
            ball.left = 0
            sounds.wall_hit.play()

        if ball.top <= 0:
            ball.dy = 1
            sounds.wall_hit.play()
        elif ball.bottom >= HEIGHT:
            #lose game
            # ball.dy = -1
            balls.remove(ball)
            if len(balls) == 0:
                game_over = True
                bricks.clear()
                powerups.clear()
    if game_state == "playing":
        if ball_ready == True and (keyboard.y or keyboard.z) and input_cooldown == 0:
            ball_ready = False
            ball.speed = 5
            ball.dx = random.uniform(-0.6, 0.6)
            ball.dy = -1

    # collision detection paddle vs ball
    for ball in balls:
        if paddle.colliderect(ball) == True:
            hit_bricks.clear()

            ball.bottom = paddle.top

            offset = (ball.x - paddle.x) / (paddle.width/2) * 0.75

            ball.dx = offset * (ball.speed/2)

            ball.speed = ball.speed + 0.05
            if ball.through:
                ball.through_hits = ball.through_hits + 1
                if ball.through_hits >= 2:
                    ball.through = False
                    ball.image = 'ball'
                    ball.through_hits = 0
            ball.dy = -1
            sounds.paddle_hit.play()
    # collision detection brick vs ball
    for ball in balls:
        for i in range(steps):
             # update game
            ball.x = ball.x + ball.dx * ball.speed / steps
            ball.y = ball.y + ball.dy * ball.speed / steps
            for brick in bricks:
                if ball.colliderect(brick) == True and brick not in hit_bricks:
                    if ball.through:
                        hit_bricks.append(brick)
                        if brick.image == 'brick.red':
                            brick.image = 'brick.yellow'
                            Score = Score + 100
                            sounds.brick_hit.play()
                        elif brick.image == 'brick.yellow':
                            brick.image = 'brick.green'
                            Score = Score + 50
                            sounds.brick_hit.play()
                        elif brick.image == 'brick.green':
                            brick.image = 'brick.blue'
                            Score = Score + 25
                            sounds.brick_hit.play()
                        else:
                            bricks.remove(brick)
                            Score = Score + 10
                            sounds.brick_destroyed.play()
                            if random.randint(1,100) <= 20:
                                choice = random.randint(1,4)
                                if choice == 1:
                                    power = Actor('blue_power')
                                elif choice == 2:
                                    power = Actor('green_power')
                                elif choice == 3:
                                    power = Actor('yellow_power')
                                else:
                                    power = Actor('red_power')
                                power.pos = brick.pos
                                powerups.append(power)
                    else:
                        if abs(ball.bottom - brick.top) < 5 and ball.dy > 0:
                        # hit the top
                            ball.bottom = brick.top
                            ball.dy = -ball.dy
                        elif abs(ball.top - brick.bottom) < 5 and ball.dy < 0:
                        # hit the bottom
                            ball.top = brick.bottom
                            ball.dy = -ball.dy
                        elif abs(ball.right - brick.left) < 5 and ball.dx > 0:
                        # hit the left
                            ball.right = brick.left
                            ball.dx = -ball.dx
                        elif abs(ball.left - brick.right) < 5 and ball.dx < 0:
                        # hit the right
                            ball.left = brick.right
                            ball.dx = -ball.dx
                        if brick.image == 'brick.red':
                            brick.image = 'brick.yellow'
                            Score = Score + 100
                            sounds.brick_hit.play()
                        elif brick.image == 'brick.yellow':
                            brick.image = 'brick.green'
                            Score = Score + 50
                            sounds.brick_hit.play()
                        elif brick.image == 'brick.green':
                            brick.image = 'brick.blue'
                            Score = Score + 25
                            sounds.brick_hit.play()
                        else:
                            bricks.remove(brick)
                            Score = Score + 10
                            sounds.brick_destroyed.play()
                            if random.randint(1,100) <= 20:
                                choice = random.randint(1,4)
                                if choice == 1:
                                    power = Actor('blue_power')
                                elif choice == 2:
                                    power = Actor('green_power')
                                elif choice == 3:
                                    power = Actor('yellow_power')
                                else:
                                    power = Actor('red_power')
                                power.pos = brick.pos
                                powerups.append(power)

    for power in powerups:
        power.y += 2
        if power.colliderect(paddle):
            sounds.powerup_collected.play()
            if power.image == 'blue_power':
                if paddle.image == 'paddle':
                    paddle.image = 'paddle_wide1'
                elif paddle.image == 'paddle_wide1':
                    paddle.image = 'paddle_wide2'
                elif paddle.image == 'paddle_wide2':
                    paddle.image = 'paddle_wide3'
                else:
                    Score = Score + 500
            elif power.image == 'green_power':
                for ball in balls:
                    ball.through = True
                    ball.through_hits = 0
                    ball.image = 'big_ball'
            elif power.image == 'yellow_power':
                Score = Score * 1.25
            elif power.image == 'red_power':
                new_ball = Actor('ball')
                new_ball.x = paddle.x
                new_ball.bottom = paddle.top -2
                new_ball.dx = random.uniform(-0.8, 0.8)
                new_ball.dy = -1
                new_ball.speed = balls[0].speed
                new_ball.through = False
                balls.append(new_ball)
            powerups.remove(power)
    if len(bricks) == 0 and not game_over:
        for ball in balls:
            ball.speed = 0
    if game_state == "title" and input_cooldown == 0:
        if keyboard.z or keyboard.y:
            game_state = "level_select"
            input_cooldown = 10
            return
    if game_state == "level_select" and input_cooldown == 0 and levels_ready == True:
        if keyboard.right:
            selected_level = selected_level + 1
            if selected_level > total_levels:
                selected_level = 1
            input_cooldown = 10
        elif keyboard.left:
            selected_level = selected_level - 1
            if selected_level < 1:
                selected_level = total_levels
            input_cooldown = 10
        if keyboard.z or keyboard.y:
            music.stop()
            Score = 0
            game_over = False
            victory_sound = False
            game_over_sound = False
            ball.through = False
            powerups.clear()
            balls = [ball]
            ball.x = paddle.x
            ball.bottom = paddle.top - 1
            ball_ready = True
            ball.image = 'ball'
            ball.speed = 0
            paddle.image = 'paddle'
            game_state = "playing"
            music.play('background')
            music.set_volume(0.25)
            bricks = [copy.copy(b) for b in level_cache[selected_level]]
            input_cooldown = 10
            return
    if game_over == True and input_cooldown == 0:
        if keyboard.r:
            music.stop()
            Score = 0
            game_over = False
            victory_sound = False
            game_over_sound = False
            powerups.clear()
            balls = [ball]
            ball.x = paddle.x
            ball.bottom = paddle.top - 1
            ball.dx = 1
            ball.dy = -1
            ball.speed = 0
            ball_ready = True
            music.play('background')
            music.set_volume(0.25)
            ball.image = 'ball'
            ball.through = False
            paddle.x = WIDTH / 2
            paddle.image = 'paddle'
            bricks = [copy.copy(b) for b in level_cache[selected_level]]
            input_cooldown = 10
        if keyboard.x:
            game_state = "level_select"
            music.play('menu_music')
            input_cooldown = 10
        return
    if victory_sound == True and input_cooldown == 0:
        if keyboard.y or keyboard.z:
            victory_sound = False
            game_state = "level_select"
            music.play('menu_music')
            input_cooldown = 10
def draw():
    global Score,game_over,game_over_sound,victory_sound,game_state
    if game_state == "title":
        screen.clear()
        screen.blit('title_screen', (0, 0))
        screen.draw.text("Press Y or Z to Start", center=(WIDTH/2, 325), fontsize=35, color="yellow")
        return
    if game_state == "level_select":
        screen.clear()
        screen.blit("menu_screen",(0,0))
        screen.draw.text(f"Level {selected_level}", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="yellow")
        screen.draw.text("Use <- / -> to choose", center=(WIDTH/2, HEIGHT/2 + 60), fontsize=30, color="yellow")
        return

    if len(bricks) == 0 and game_over == False:
        screen.clear()
        screen.blit('game_won',(WIDTH/2-240, 0))
        screen.draw.text(
        f"Score: {int(Score)}",
        (WIDTH/2-50, HEIGHT/2-50),
        color="yellow",
        fontsize=40
        )
        screen.draw.text(
        f"Press Y or Z to Return",
        (WIDTH/2-150, HEIGHT/2),
        color="yellow",
        fontsize=40
        )
        powerups.clear()

        if victory_sound == False:
            sounds.victory.play()
            victory_sound = True
            music.stop()
            input_cooldown = 10
    elif game_over == False:
        screen.blit('background', (0, 0))
        for brick in bricks:
            brick.draw()
        for ball in balls:
            ball.draw()
        paddle.draw()

    else:
        screen.clear()
        screen.blit('game_over',(WIDTH/2-125, 0))
        screen.draw.text(
        f"Score: {int(Score)}",
        (WIDTH/2-50, HEIGHT/2-50),
        color="yellow",
        fontsize=40
        )
        screen.draw.text(
        f"Press R to Restart",
        (WIDTH/2-100, HEIGHT/2),
        color="yellow",
        fontsize=40
        )
        screen.draw.text(
        f"Press X to Return",
        (WIDTH/2-100, HEIGHT/2 + 50),
        color="yellow",
        fontsize=40
        )
        powerups.clear()
        if game_over_sound == False:
            sounds.defeat.play()
            game_over_sound = True
            music.stop()
    for power in powerups:
        power.draw()

def run_in_parallel(function, args):
    thread = Thread(target=function, args=args)
    thread.start()

def load_levels():
    global level_cache, levels_ready
    level_cache[1] = level_1()
    level_cache[2] = level_2()
    level_cache[3] = level_3()
    levels_ready = True

run_in_parallel(load_levels, ())
