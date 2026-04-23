import pandas as pd

data ={
    "names":["wang1","wang2","wang3","wang4"],
    "math score":[45,64,89,67],
    "English score":[88,67,98,34],
    "python score":[78,77,87,69],
    "classes":["class 502","class 501","class 501","class 502"]
}

F = pd.DataFrame(data)

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
