# 단어 맞추기 게임
# 미리 지정된 영어 단어의 알파벳 중 50%를 Blind 처리 후 사용자로부터 알파벳을
# 입력받아, 입력 받은 알파벳이 단어 내에 있을 경우 해당 알파벳을 Blind 해제,
# 없을 경우 "없음" 메시지를 출력하여 지정된 단어의 스펠링을 맞추는 프로그램 작성

import random

list_words = []

# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장한다.
for i in ["첫", "두", "세"]:
    print(f"{i} 번째 단어를 입력하세요")
    # 단어의 글자 범위는 5 이상, 20 이하로 제한된다.
    # 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구한다.
    while True:
        input_word = input()
        if 5 <= len(input_word) <= 20:
            list_words.append(input_word)
            break
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")

word_selected = list(list_words[random.randint(0, 2)])
word_printed = word_selected[:]

# 선택된 단어
current_word = ""
for char in word_printed:
    current_word += char

print(f"\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {current_word}\n")

# 선택된 단어의 글자 수
char_num_word = len(word_selected)

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2
# 반올림 처리 알고리즘 // 연산자는 몫만 가지고 온다.
if blind_num_word > char_num_word // 2:
    blind_num_word += 1
    
blind_num_word = int(blind_num_word)

list_blind_index = [value for value in range(0, char_num_word)]

for index in range(0, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]

for index in list_blind_index:
    word_printed[index] = "_"

# 게임 횟수 초기화
attempt_count = 0

# 게임 루프
while True:
    print(f"{attempt_count + 1}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    current_word = ""
    for char in word_printed:
        current_word += char
    print(current_word)
    
    # 게임 종료 조건: '_'가 없는 경우
    game_finished = True
    for char in word_printed:
        if char == "_":
            game_finished = False
            break
    if game_finished:
        break
    
    print("")
    input_value = input()
    print("")
    
    found = False
    new_blind_index = []
    for index in list_blind_index:
        if word_selected[index] == input_value:
            word_printed[index] = input_value
            found = True
        else:
            new_blind_index.append(index)
    
    if found == False:
        print("단어 내 포함되지 않은 알파벳입니다.")
    else:
        print("입력한 알파벳 단어 내 포함: ")
    
    list_blind_index = new_blind_index
    attempt_count += 1  # 시도 횟수 증가
    
    # 게임 종료 조건: 모든 블라인드가 해제된 경우
    if len(new_blind_index) == 0:
        break
    
print(f"Clear - 선택된 단어: {current_word}, 총 시도 횟수: {attempt_count + 1}")