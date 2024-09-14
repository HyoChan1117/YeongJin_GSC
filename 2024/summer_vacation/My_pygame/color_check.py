# 마우스 좌클릭 이벤트 처리
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 왼쪽 버튼 클릭
    mouse_x, mouse_y = event.pos
    # 클릭한 위치의 색상 가져오기
    clicked_color = screen.get_at((mouse_x, mouse_y))
    print(f"Mouse clicked at ({mouse_x}, {mouse_y}) with color: {clicked_color}")