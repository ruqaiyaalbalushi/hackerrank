if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(arr, reverse=True)
    m = arr[0]
    while arr[0] == m:
        del arr[0]
        
    print(arr[0])