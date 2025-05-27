# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
