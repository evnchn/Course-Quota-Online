def moveelem_discord(arr, elem, ind):
    if ind == len(arr):
        arr.remove(elem)
        arr.append(elem)
        return arr
    if ind == 1:
        arr.remove(elem)
        return [elem] + arr
    
    
    arr.remove(elem)
    arr.insert(ind-1, elem)
    return arr
    
    
arr = ["a", "b", "c", "d", "e"]

arr = moveelem_discord(arr, "d", 2)

print(arr)
    