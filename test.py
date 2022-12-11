import pygame
import pygame.freetype
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
score_time = 0
pause_len = 3000
pygame.init()


def move_player():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def move_AI():
    if ball.centerx > SCREEN_WIDTH/2 and ball_dx > 0:
        if ball.bottom < opponent.top:
            opponent.y -= opponent_speed
        if ball.top > opponent.bottom:
            opponent.y += opponent_speed


def move_ball(dx, dy):
    if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
        dy = dy * (-1)
        pong_sound.play()
    if ball.colliderect(player) and dx < 0:
        dx = -dx
    if ball.colliderect(opponent) and dx > 0:
        dx = -dx

    now = pygame.time.get_ticks()
    if now - score_time > pause_len:
        ball.x += dx
        ball.y += dy
    return dx, dy


def restart():
    ball.x = SCREEN_WIDTH/2
    ball.y = SCREEN_HEIGHT/2


win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Window')
main_font = pygame.freetype.Font(None, 42)
clock = pygame.time.Clock()
FPS = 60
play = True
player = pygame.Rect((0, SCREEN_HEIGHT/2, 10, 75))
ball = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20, 20)
opponent = pygame.Rect(SCREEN_WIDTH-10, SCREEN_HEIGHT/2, 10, 75)
color = (0, 0, 0)
BG_color = (20, 20, 20)
player_speed = 0
opponent_speed = 7
ball_dx = 7
ball_dy = 7
player_goals = 0
AI_goals = 0
print(player_goals, ':', AI_goals)
pong_sound = pygame.mixer.Sound('pong.wav')
lose_sound = pygame.mixer.Sound('lose.wav')
win_sound = pygame.mixer.Sound('win.wav')
score_sound = pygame.mixer.Sound('score.wav')
end = 7
play_stop = False
last_winner = 2
while play:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 7
            elif event.key == pygame.K_s:
                player_speed += 7
            elif event.key == pygame.K_r:
                play_stop = False
                last_winner = 2
            elif event.key == pygame.K_e:
                play = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            elif event.key == pygame.K_s:
                player_speed -= 7
    if ball.x < 0:
        restart()
        score_time = pygame.time.get_ticks()
        AI_goals += 1
        print(player_goals, ':', AI_goals)
        score_sound.play()
    if ball.x > SCREEN_WIDTH:
        restart()
        score_time = pygame.time.get_ticks()
        player_goals += 1
        print(player_goals, ':', AI_goals)
        score_sound.play()
    if player_goals == end:
        win_sound.play()
        win_sound.fadeout(1000)
        play_stop = True
        player_goals, AI_goals = 0, 0
        last_winner = 1
    if AI_goals == end:
        lose_sound.play()
        lose_sound.fadeout(1000)
        play_stop = True
        player_goals, AI_goals = 0, 0
        last_winner = 0
    move_player()
    move_AI()
    win.fill(BG_color)
    if play_stop == False:
        ball_dx, ball_dy = move_ball(ball_dx, ball_dy)
    else:
        if last_winner == 1:
            main_font.render_to(win, (SCREEN_WIDTH / 3, 70), 'YOU WIN', fgcolor=(0, 0, 0))
        if last_winner == 0:
            main_font.render_to(win, (SCREEN_WIDTH / 3, 70), 'YOU LOSE', fgcolor=(0, 0, 0))
        main_font.render_to(win, (SCREEN_WIDTH / 3, 120), 'Press R to restart', fgcolor=(0, 0, 0))
        main_font.render_to(win, (SCREEN_WIDTH / 3, 170), 'Press E to close', fgcolor=(0, 0, 0))
    main_font.render_to(win, (SCREEN_WIDTH/3, 20), str(player_goals), fgcolor=(0, 0, 0))
    main_font.render_to(win, (SCREEN_WIDTH / 1.5, 20), str(AI_goals), fgcolor=(0, 0, 0))
    pygame.draw.rect(win, color, player)
    pygame.draw.rect(win, color, opponent)
    pygame.draw.ellipse(win, color, ball)
    pygame.display.update()

