def linear_search(list,target):
    """
    Some mistake
    This script finds only 1 at index 0, the rest can't be found 
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
        return None
    

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]
    
    
result = linear_search(numbers,12)

verify(result)

result = linear_search(numbers,3)

verify(result)