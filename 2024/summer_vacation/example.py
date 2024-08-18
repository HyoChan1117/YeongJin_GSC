import pygame
import random
import time

pygame.init()

# 색 정의
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 화면 비율 조정
SCREEN_WIDTH = 2800
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 기초 설정
player_size = 30
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

item_size = 20

obstacle_size = [15, 15]
obstacles = [[random.randint(0, SCREEN_WIDTH - obstacle_size[0]), random.randint(0, SCREEN_HEIGHT - obstacle_size[1]), random.choice([-5, 5]), random.choice([-5, 5])] for _ in range(55)]

# 아이템 박스
powerup_size = 25
red_box_size = 25  # 검은색 테두리를 가진 빨간색 아이템 박스 크기

clock = pygame.time.Clock()
speed = 10

font = pygame.font.SysFont(None, 75)

def draw_text(text, font, color, surface, x, y, alignment="center"):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if alignment == "center":
        textrect.center = (x, y)
    elif alignment == "topleft":
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_over_screen():
    screen.fill(WHITE)
    draw_text('Game Over!', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 300)
    draw_text('Try again?', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    draw_text('(Press the R Key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text('You loser?', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    draw_text('(Press the Q key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
    draw_text('Back to Menu? (Press the 3 Key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 300)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_3:
                    return "menu"
        clock.tick(15)

def win_screen(seconds, items_collected=None, goal=None):
    screen.fill(WHITE)
    draw_text('LOL!!!! You Win!!', font, BLUE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
    draw_text(f'Clear Time: {int(seconds)} seconds', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    if goal:
        draw_text(f'Goal: {goal}, Collected: {items_collected}', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text('Play again? (Press the R Key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    draw_text('Quit? (Press the Q key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
    draw_text('Back to Menu? (Press the 3 Key)', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 300)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_3:
                    return "menu"
        clock.tick(15)

def reset_game():
    global player_pos, items, obstacles, powerups, red_boxes, start_ticks, powerup_effect, items_collected, goal, mode
    player_pos = [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2]
    item_count = random.randint(10, 30) if mode == 1 else 10
    items = [[random.randint(0, SCREEN_WIDTH - item_size), random.randint(0, SCREEN_HEIGHT - item_size)] for _ in range(item_count)]
    obstacles = [[random.randint(0, SCREEN_WIDTH - obstacle_size[0]), random.randint(0, SCREEN_HEIGHT - obstacle_size[1]), random.choice([-5, 5]), random.choice([-5, 5])] for _ in range(55)]
    powerups = []
    red_boxes = []
    start_ticks = pygame.time.get_ticks()
    powerup_effect = None
    items_collected = 0
    goal = 0
    if mode == 2:
        goal = random.randint(5, 30)
        items = [[random.randint(0, SCREEN_WIDTH - item_size), random.randint(0, SCREEN_HEIGHT - item_size)] for _ in range(10)]

start_ticks = pygame.time.get_ticks()
grace_period = 1
powerup_effect = None
powerup_end_time = 0
blind_time = 0
immobile_time = 0
item_spawn_time = pygame.time.get_ticks() + 5000  # 아이템 박스 생성 시간
red_box_spawn_time = pygame.time.get_ticks() + 3000  # 빨간색 아이템 박스 생성 시간

def game_menu():
    screen.fill(WHITE)
    draw_text('Game Menu', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 300)
    draw_text('1. Collect All Items', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    draw_text('2. Collect Target Items', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    pygame.display.flip()

    waiting = True
    selected_mode = None
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_mode = 1
                    waiting = False
                elif event.key == pygame.K_2:
                    selected_mode = 2
                    waiting = False
        clock.tick(15)
    return selected_mode

running = True
mode = game_menu()
reset_game()

while running:
    current_ticks = pygame.time.get_ticks()
    elapsed_time = (current_ticks - start_ticks) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0 and current_ticks > immobile_time:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size and current_ticks > immobile_time:
        player_pos[0] += speed
    if keys[pygame.K_UP] and player_pos[1] > 0 and current_ticks > immobile_time:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - player_size and current_ticks > immobile_time:
        player_pos[1] += speed

    screen.fill(WHITE)

    if current_ticks < blind_time:
        draw_text('Blind', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    else:
        pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    if powerup_effect == "freeze" and current_ticks <= powerup_end_time:
        # 빨간 네모 멈춤
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size[0], obstacle_size[1]))
    else:
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size[0], obstacle_size[1]))
            if powerup_effect == "slow" and current_ticks <= powerup_end_time:
                obstacle[0] += obstacle[2] * 0.3  # 속도 감소
                obstacle[1] += obstacle[3] * 0.3
            else:
                obstacle[0] += obstacle[2]
                obstacle[1] += obstacle[3]

            if obstacle[0] <= 0 or obstacle[0] >= SCREEN_WIDTH - obstacle_size[0]:
                obstacle[2] = -obstacle[2]
            if obstacle[1] <= 0 or obstacle[1] >= SCREEN_HEIGHT - obstacle_size[1]:
                obstacle[3] = -obstacle[3]

    for item in items:
        pygame.draw.rect(screen, YELLOW, (item[0], item[1], item_size, item_size))

    # 아이템 박스 생성 타이머
    if current_ticks >= item_spawn_time:
        powerups.append([random.randint(0, SCREEN_WIDTH - powerup_size), random.randint(0, SCREEN_HEIGHT - powerup_size)])
        item_spawn_time = current_ticks + random.randint(5000, 10000)  # 5-10초 사이에 아이템 박스 생성

    for powerup in powerups:
        pygame.draw.rect(screen, GREEN, (powerup[0], powerup[1], powerup_size, powerup_size))

    # 빨간색 아이템 박스 생성 타이머
    if current_ticks >= red_box_spawn_time:
        if random.random() < 0.05:  # 5% 확률
            red_boxes.append([random.randint(0, SCREEN_WIDTH - red_box_size), random.randint(0, SCREEN_HEIGHT - red_box_size)])
        red_box_spawn_time = current_ticks + 3000  # 3초마다 검사

    for red_box in red_boxes:
        pygame.draw.rect(screen, RED, (red_box[0], red_box[1], red_box_size, red_box_size), 0)  # 빨간색 내부
        pygame.draw.rect(screen, BLACK, (red_box[0], red_box[1], red_box_size, red_box_size), 3)  # 검은색 테두리

    if (current_ticks - start_ticks) / 1000 > grace_period:
        for item in items[:]:
            if (player_pos[0] < item[0] + item_size and
                    player_pos[0] + player_size > item[0] and
                    player_pos[1] < item[1] + item_size and
                    player_pos[1] + player_size > item[1]):
                items.remove(item)
                items_collected += 1
                if mode == 2:
                    # 2번 모드에서 아이템을 먹으면 무작위 위치에 재생성
                    items.append([random.randint(0, SCREEN_WIDTH - item_size), random.randint(0, SCREEN_HEIGHT - item_size)])

        for powerup in powerups[:]:
            if (player_pos[0] < powerup[0] + powerup_size and
                    player_pos[0] + player_size > powerup[0] and
                    player_pos[1] < powerup[1] + powerup_size and
                    player_pos[1] + player_size > powerup[1]):
                powerups.remove(powerup)
                effect_type = random.choice(["invincible", "freeze", "slow", "blind", "immobile"])
                powerup_end_time = current_ticks + 2000  # 2초 동안 지속

                if effect_type == "invincible":
                    powerup_effect = "invincible"
                elif effect_type == "freeze":
                    powerup_effect = "freeze"
                elif effect_type == "slow":
                    powerup_effect = "slow"
                elif effect_type == "blind":
                    blind_time = current_ticks + 1000  # 1초 동안 블라인드
                elif effect_type == "immobile":
                    immobile_time = current_ticks + 1000  # 1초 동안 플레이어 못 움직임

        for red_box in red_boxes[:]:
            if (player_pos[0] < red_box[0] + red_box_size and
                    player_pos[0] + player_size > red_box[0] and
                    player_pos[1] < red_box[1] + red_box_size and
                    player_pos[1] + player_size > red_box[1]):
                red_boxes.remove(red_box)
                red_box_effect = random.choice(["instant_death", "remove_half_obstacles", "invincible", "add_quarter_obstacles"])
                if red_box_effect == "instant_death":
                    game_over = True
                    while game_over:
                        if game_over_screen() == "menu":
                            mode = game_menu()
                            reset_game()
                            game_over = False
                        elif game_over_screen():
                            reset_game()
                            game_over = False
                        else:
                            running = False
                            game_over = False
                elif red_box_effect == "remove_half_obstacles":
                    obstacles = obstacles[:len(obstacles) // 2]  # 방해물 절반 제거
                elif red_box_effect == "invincible":
                    powerup_effect = "invincible"
                    powerup_end_time = current_ticks + 5000  # 5초 동안 무적
                elif red_box_effect == "add_quarter_obstacles":
                    num_new_obstacles = max(1, len(obstacles) // 4)
                    for _ in range(num_new_obstacles):
                        obstacles.append([random.randint(0, SCREEN_WIDTH - obstacle_size[0]), random.randint(0, SCREEN_HEIGHT - obstacle_size[1]), random.choice([-5, 5]), random.choice([-5, 5])])

        # 충돌 체크: 무적 상태일 때만 충돌 무시
        if powerup_effect != "invincible" or current_ticks > powerup_end_time:
            for obstacle in obstacles:
                if (player_pos[0] < obstacle[0] + obstacle_size[0] and
                        player_pos[0] + player_size > obstacle[0] and
                        player_pos[1] < obstacle[1] + obstacle_size[1] and
                        player_pos[1] + player_size > obstacle[1]):
                    game_over = True
                    while game_over:
                        if game_over_screen() == "menu":
                            mode = game_menu()
                            reset_game()
                            game_over = False
                        elif game_over_screen():
                            reset_game()
                            game_over = False
                        else:
                            running = False
                            game_over = False
        else:
            # 무적 상태 메시지 출력
            draw_text('Im undead!', font, BLUE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

    if mode == 1 and not items:
        win = True
        while win:
            if win_screen(elapsed_time) == "menu":
                mode = game_menu()
                reset_game()
                win = False
            elif win_screen(elapsed_time):
                reset_game()
                win = False
            else:
                running = False
                win = False

    if mode == 2 and items_collected >= goal:
        win = True
        while win:
            if win_screen(elapsed_time, items_collected, goal) == "menu":
                mode = game_menu()
                reset_game()
                win = False
            elif win_screen(elapsed_time, items_collected, goal):
                reset_game()
                win = False
            else:
                running = False
                win = False

    draw_text(f'Time: {int(elapsed_time)}', font, BLACK, screen, SCREEN_WIDTH // 2, 50)
    if mode == 2:
        draw_text(f'Goal: {goal}, Collected: {items_collected}', font, BLACK, screen, SCREEN_WIDTH // 2, 150)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()