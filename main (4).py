for i in range(1, 51):
    if i % 2 == 0 and i % 5 == 0:
        print(f"{i} is even and a multiple of 5")
    elif i % 2 != 0 and i % 5 == 0:
        print(f"{i} is odd and a multiple of 5")
    elif i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print("end the numbers from 1 to 50.")
