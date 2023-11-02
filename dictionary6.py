d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x=int(input("ENter the key: "))
if x in d.keys():
    print(f"Yes {x} is present in the given dictionary")
else:
    print(f"No {x} is not present in the given dictionary")