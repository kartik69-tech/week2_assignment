def average(array):
    # your code goes here
     distinct_heights = set(array)
    
     return round(sum(distinct_heights) / len(distinct_heights), 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
