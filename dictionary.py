dict={"name": "Alice", "age": 25, "grade": "A"}
for key in dict.keys():
    print(f"{key}")
for value in dict.values():
    print(f"{value}")
if "age" in dict:
    print("yes age is present")