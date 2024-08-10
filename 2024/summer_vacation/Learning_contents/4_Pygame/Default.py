import pygame

pygame.init()

#=======================================================================

# <<-- 환경 변수 설정
# 화면 사이즈
screen_width = 800
screen_height = 600

#=======================================================================

# 기본 설정 및 객체 생성
# 화면, FPS 설정
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#=======================================================================

running = True
while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))
    
    
    pygame.display.flip()
    
#=======================================================================

pygame.quit()