def print_info(student):
    print("="*20)
    for key, value in student.items():
        print(f"{key}:{value}")
    print("="*20)

stu={
    "Name":input("please enter the name:"),
    "Age" :int(input("please enter the age:")),
    "grade":int(input("please enter the grade:"))
}

if stu["grade"] >= 90:
    stu["status"]= "Very Good"
elif stu["grade"]>=80:
    stu["status"]="Good"
elif stu["grade"]>=70:
    stu["status"]="Not bad"
elif stu["grade"]>=60:
    stu["status"]="Pass"
else:
    stu["status"]="Not Pass"

print_info(stu)