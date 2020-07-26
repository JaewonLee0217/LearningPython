student2score = {
    "Darius":100,
    "Dr.Mundo":80,
    "Morgana":60,
    "Sivir":75,
    "Yummi":20,
    "Viktor":97
}

def get_special_students(student2score):
    special_students=[]
    
    for i in student2score.values():
        if i>=80:
            special_students.append(i)

    return special_students
    

