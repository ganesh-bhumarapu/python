T = int(input())

for _ in range(T):

    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    if A.issubset(B):
        print("True")
    else:
        print("False")