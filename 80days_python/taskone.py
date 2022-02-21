names = {"Beomgyu":81,"Taehyun":97,"Yeonjun":62,"Soobin":92,"Hueningkai":100}
grade ={}
for student in names:
    score = names[student]
    if score>90 :
        grade[student]="Outstanding"
    elif score>80:
        grade[student]="Exceeds Expectations"
    elif score>70:
        grade[student]="Acceptable"
    else:
        grade[student]="FAIL"           

print(grade)    