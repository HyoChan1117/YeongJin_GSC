sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

while True:
    words = sentence.split()

    input_words = input("검색할 문자열을 입력하세요: ")

    # 입력 받은 문자열이 문장 내 있을 경우
    if input_words in words:
        # 검색된 문자열에 대한 정보를 출력
        # 검색된 문자열의 개수
        string_count = 0
        words_count = 0
        for value in words:
            if input_words == value:
                string_count += 1
            words_count += 1
        
        spell_count = 0
        line_count = 1
        for spell in sentence:
            if spell == "\n":
                line_count += 1
            if spell == " " or spell == "\n":
                continue
            spell_count += 1
        
        whole_count = 0
        position_count = 0
        input_list = []
        input_list.append(input_words)
        index_list = []
        for value1 in words:
            if value1 == input_list[0]:
                position_count += 1
                index_list.append(position_count)
            whole_count += 1
            
            
        print(f"검색된 문자열의 위치: {input_list}")
        
        print(f"검색된 문자열의 개수: {string_count}")
        print(f"단어의 개수: {words_count}")
        print(f"전체 문자 수: {spell_count}")
        print(f"줄 수: {line_count}")
        break
    # 입력 받은 문자열이 문장 내 없을 경우
    else:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
                
