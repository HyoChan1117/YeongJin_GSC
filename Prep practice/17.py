# 단어 맞추기 게임
# 미리 지정된 영어 단어의 알파벳 중 50%를 Blind 처리 후 사용자로부터 알파벳을
# 입력받아, 입력 받은 알파벳이 단어 내에 있을 경우 해당 알파벳을 Blind 해제,
# 없을 경우 "없음" 메시지를 출력하여 지정된 단어의 스펠링을 맞추는 프로그램 작성
import random

eng_word = []

# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장한다.
for i in ["첫", "두", "세"]:
    print(f"{i} 번째 단어를 입력하세요")
    # 단어의 글자 범위는 5 이상, 20 이하로 제한된다.
    # 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구한다.
    while True:
        input_word = input()
        if 5 <= len(input_word) <= 20:
            eng_word.append(input_word)
            break
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")

# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택한다.
random_index = random.randint(0, 2)
random_word = eng_word[random_index]
print(f"\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {random_word}\n")

# 올림하는 함수를 정의한다.
def round_up():
    if len(visual_alpha) % 2 != 0:
        amount_alpha = (len(visual_alpha) // 2) + 1
    else:
        amount_alpha = len(visual_alpha) // 2
        return amount_alpha

# 선택된 단어의 글자 중 50%를 Blind 처리한다.
visual_alpha = []
blind_alpha = []
for char in random_word:
    visual_alpha.append(char)
    blind_alpha.append(char)

for alpha in visual_alpha:
    

# Blind 처리된 알파벳은 랜덤하게 선택된다.
random_blind = random.randint()

# 키보드로부터 알파벳 한 글자를 입력 받는다.


# 입력받은 알파벳이 단어 내에 존재할 경우 Blind를 해제한다.


# 존재하지 않을 경우 "없음" 메시지를 출력한다.


# 단어의 모든 글자를 맞출 경우 게임이 종료된다.


# 게임 종료 시 시도 횟수를 출력한다.


