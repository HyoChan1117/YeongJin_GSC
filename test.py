sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

while True:
    words = sentence.split()

    input_words = input("검색할 문자열을 입력하세요: ")

    if input_words in words:

        # 검색된 문자열의 개수
        list_words = []
        for value in words:
            if value == input_words:
                list_words.append(value)
        print(f"검색된 문자열의 개수: {len(list_words)}")

        # 검색된 문자열의 위치
        list_input = []
        for i in input_words:
            list_input.append(i)
        
        index = 0
        list_index = []
        for count in sentence:
            list_index.append(index)
        index += len(count)
        
        print(list_index)
                
        
        # 단어의 개수
        words_count = 0
        for count1 in words:
            words_count += 1
        print(f"단어의 개수: {words_count}")
        
        # 전체 문자 수
        spell_count = 0
        for count2 in sentence:
            if count2 == " " or count2 == "\n":
                continue
            else:
                spell_count += 1        
        print(f"전체 문자 수: {spell_count}")
        
        # 줄 수
        line_count = 1
        for count3 in sentence:
            if count3 == "\n":
                line_count += 1
        print(f"줄 수: {line_count}")
        break
    else:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")