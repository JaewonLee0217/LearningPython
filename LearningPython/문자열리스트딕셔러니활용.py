text = "Apple is fruit. Orange is also fruit. Tomato is fruit?"

def word_index_count(text):

    word_id = {} # word id 딕셔너리
    id_frequency = {} # id 에 따른 빈도수

    text = text.replace(".","")
    text = text.replace("?","") #텍스트 안에 특수기호 제거
    text = text.lower() # 모두 소문자로 변경.
    a= text.split(" ") # 리스트 형태로 단어 추출
    for i, word in enumerate(a):
        word_id[i] =word

    #텍스트 안에 단어에 id부여.
    for i, s in enumerate(a):
        id_frequency[i] = a.count(s)
    
    
    return word_id,id_frequency

print(word_index_count(text))
