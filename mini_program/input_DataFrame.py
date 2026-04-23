import pandas as pd

students = []
for i in range(4):
    print(f"\n----- Enter information for student {i+1} -----")
    name = input("Name: ")
    cls = input("Class: ")
    math = int(input("Math score: "))
    english = int(input("English score: "))
    python = int(input("Python score: "))

    students.append({
        "names": name,
        "classes": cls,
        "math score": math,
        "English score": english,
        "python score": python
    })


F = pd.DataFrame(students)

print("=== grade frame ===")
print(F)
print()

print("=== average score ===")
print(F[["math score","English score", "python score"]].mean())
print()

print("=== highest scores ===")
print(F[["math score","English score", "python score"]].max())
print()

print("=== number of class ===")
print(F["classes"].value_counts())
print()


F["Totally score"] = F["math score"] + F["English score"] + F["python score"]
print("=== Overall score ranking ===")
print(F.sort_values(by="Totally score", ascending=False)[["names", "classes", "Totally score"]])
print()
