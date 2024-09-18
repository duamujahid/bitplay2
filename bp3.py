def OddOccuring(arr):
    res = 0
    for element in arr :
        res = res^element
    return res


n = int(input("Enter the array size :"))
arr = []
while(n):
    num = int(input("Enter numbers :"))
    arr.append(num)
    n-=1
print(OddOccuring(arr))
