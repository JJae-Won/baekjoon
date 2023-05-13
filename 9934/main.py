
def split_arr(arr, ith, results : dict):
    mid = len(arr)//2
    if len(arr) != 3:
        if results.get(ith):
            results[ith].append(arr[mid])
        else:
            results[ith] = [arr[mid]]
            
        split_arr(arr[:mid], ith+1, results)
        split_arr(arr[mid+1:], ith+1, results)
        
    else:
        if results.get(ith):
            results[ith].append(arr[mid])
        else:
            results[ith] = [arr[mid]]
        
        if results.get(ith+1):
            results[ith+1].append(arr[0])
            results[ith+1].append(arr[2])
        else:
            results[ith+1] = [arr[0]]
            results[ith+1].append(arr[2])

def main():
    K = int(input())
    num = K**2 - 1
    arr = list(map(int, input().split(' ')))
        
    if K == 1:
        print(arr[0])
        
    result = {}
    
    split_arr(arr, 1, result)
    
    for v in result.values():
        print(*v)
        
        
            
    
if __name__ == '__main__':
    main()
    