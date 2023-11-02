user1=int(input("Enter your age(user1): "))
user2=int(input("Enter your age(user2): "))
user3=int(input("Enter your age(user3): "))
if user1==user2==user3:
    print("All three have equal age")
elif user1>user2 and user1>user3:
    print("user1 is the oldest one among the three")
    if user2>user3:
        print("user3 is the youngest one among them")
    elif user2==user3:
        print("user2 and user3 are the youngest ones among the three")
    else:
        print("user2 is the youngest one among the three")
elif user2>user3:
    print("user2 is the oldest one among the three")
    if user1>user3:
        print("user3 is the youngest one among them")
    elif user1==user3:
        print("user1 and user3 are the youngest ones among the three")
    else:
        print("user1 is the youngest one among them")
else:
    print("user3 is the oldest one among the three")
    if user2>user1:
        print("user1 is the youngest one among them")
    elif user1==user2:
        print("user1 and user2 are the youngest ones among the three")
    else:
        print("user2 is the youngest one among them")

    