# Python implementation to
# find longest increasing
# subsequence
# in O(n Log n) time.
 
# Binary search

def GetCeilIndex(arr, T, l, r, key):
 
    while (r - l > 1):
     
        m = l + (r - l)//2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
 
    return r
  
def LongestIncreasingSubsequence(arr, n):
 
    # Add boundary case,
    # when array n is zero
    # Depend on smart pointers
     
    # Initialized with 0
    tailIndices =[0 for i in range(n + 1)] 
 
    # Initialized with -1
    prevIndices =[-1 for i in range(n + 1)] 
     
    # it will always point
    # to empty location
    len_internal = 1
    for i in range(1, n):
     
        if (arr[i] < arr[tailIndices[0]]):
         
            # new smallest value
            tailIndices[0] = i
         
        elif (arr[i] > arr[tailIndices[len_internal-1]]):
         
            # arr[i] wants to extend
            # largest subsequence
            prevIndices[i] = tailIndices[len_internal-1]
            tailIndices[len_internal] = i
            len_internal += 1
         
        else:
         
            # arr[i] wants to be a
            # potential condidate of
            # future subsequence
            # It will replace ceil
            # value in tailIndices
            pos = GetCeilIndex(arr, tailIndices, -1,
                                   len_internal-1, arr[i])
  
            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i
         
    #print("LIS of given input")
    i = tailIndices[len_internal-1]
    constructarr = []
    while(i >= 0):
        constructarr.append(arr[i])
        #print(arr[i], " ", end ="")
        i = prevIndices[i]
    #print()
    
    constructarr.reverse()
    
    #print(constructarr)
  
    return constructarr # len_internal
    

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

def testing(arr, debug=False):
    moves = []
    # driver code
    #arr = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    arr_orig = list(arr)
    arr = list(arr)
    assert len(list(set(arr))) == len(arr)

    n = len(arr)
      
    LIS_output = LongestIncreasingSubsequence(arr, n)

    sorted_arr = list(sorted(arr))

    arr_with_flags = [(x, x in LIS_output) for x in arr]


    elem_not_in = list(elem for elem in arr if elem not in LIS_output)

    elem_not_in.sort()


    

    for elem in elem_not_in:
    
        arr_with_flags.remove(tuple((elem, False)))
        #print(arr_with_flags)
        if elem < min(x[0] for x in arr_with_flags if x[1]):
            arr_with_flags = [tuple((elem, 1))] + arr_with_flags
            moves.append((elem, 1))
            arr = moveelem_discord(arr, elem, 1)
            continue
            
        elif elem > max(x[0] for x in arr_with_flags if x[1]):
            arr_with_flags = arr_with_flags + [tuple((elem, 1))]
            moves.append((elem, len(arr)))
            arr = moveelem_discord(arr, elem, len(arr))
            continue
        else:
            ind = 0
            while True:
                if arr_with_flags[ind][1] and arr_with_flags[ind][0] > elem:
                    break
                ind += 1
                
            target_i = ind
                    
           
        new_index = target_i
        #print(new_index)
        if debug:
            print("move Elem[{}] to {}".format(elem, new_index))
        
        
        
        if target_i == -1:
            arr_with_flags.append(tuple((elem, 1)))
        else:
            arr_with_flags.insert(new_index, tuple((elem, 1)))
        
        
        moves.append((elem, target_i + 1))
        
        arr = moveelem_discord(arr, elem, target_i + 1)
            
    # arr = [x[0] for x in arr_with_flags]
    if not arr == sorted_arr:
        print(arr_orig)
        print(arr)
        print(arr_with_flags)
        print(sorted_arr)
        print("BAD!!!!!!!!!!!!!!!!!!!!!")
        return False
    return moves
    
import itertools


shuffledlists = list(itertools.permutations([1, 2, 3, 4, 5, 6,7,8,9]))

import os

from tqdm import tqdm
for shuffledlist in tqdm(shuffledlists):
    #os.system("cls")
    #print("---BEGIN---")
    moves = testing(shuffledlist, False)
    print(moves)
    #print("----END----")
print(bads)
'''
import os
os.system("cls")'''
# testing([1, 2, 4, 5, 3], True)
# This code is contributed
# by Anant Agarwal.