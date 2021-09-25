#Binary Search

#Recursive
# def binarySearch (arr, l, r, key):

#     if(l <= r):  
#         mid = (l+r) //2 
               
#         if(key == arr[mid]):
#             return True                
#         elif(key < arr[mid]): 
#             return binarySearch(arr,l,mid-1,key)            
#         else:
#             return binarySearch(arr,mid+1,r,key)  
              
#     return False

#Iterative
def binarySearch (arr, l, r, key):
    while(l <= r):  
        mid = (l+r) //2 
               
        if(key == arr[mid]):
            return True                 
        elif(key < arr[mid]): 
            r = mid - 1                        
        else:
            l = mid + 1
               
    return False

arr = [2, 3, 4, 10, 40]

