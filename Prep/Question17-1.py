# 단어 맞추기 게임
# 미리 지정된 영어 단어의 알파벳 중 50%를 Blind 처리 후 사용자로부터 알파벳을
# 입력받아, 입력 받은 알파벳이 단어 내에 있을 경우 해당 알파벳을 Blind 해제,
# 없을 경우 "없음" 메시지를 출력하여 지정된 단어의 스펠링을 맞추는 프로그램 작성

import random

list_words = ["kkiikk", "aannaaf", "aeekeet"]

word_selected = list(list_words[random.randint(0, 2)])
word_printed = word_selected[:]

print(word_printed)

word_printed[0] = "z"

print(word_printed, word_selected)