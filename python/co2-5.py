# 5.	Display the given pyramid with step number accepted from user. Eg: N=4
'''1
2 4
3 6 9
4 8 12 16'''


N = int(input("Enter the number of steps: "))


for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print() 
