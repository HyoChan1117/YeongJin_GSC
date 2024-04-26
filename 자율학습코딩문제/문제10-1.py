# 빈 리스트를 생성합니다.
books = []

# 사용자 입력을 처리하는 루프를 시작합니다.
while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    if title == '종료':
        break
    books.append(title)
    
# 최종 도서 목록을 출력합니다.
print("도서 목록:", books)