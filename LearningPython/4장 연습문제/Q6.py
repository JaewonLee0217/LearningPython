#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.

def file_strSave():
    user_input = input("저장할 내용을 입력하세요: ")
    f1 = open('test.txt','a') #내용을 추가하기 위해서 'a'를 사용함
    f1.write(user_input)
    f1.write("\n")
    f1.close()
    print("저장이 완료되었습니다")

    
