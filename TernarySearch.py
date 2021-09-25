#Ternary Search(Iterative)

def ternarySearch (arr, l, r, key):
    while(l <= r):  
        mid1 = l + (r-l) // 3 
        mid2 = r - (r-l) // 3
               
        if(key == arr[mid1] or key == arr[mid2]):
            return True
                 
        if(key < arr[mid1]): 
            r = mid1 - 1    
        elif(key > arr[mid2]): 
            l = mid2 + 1                        
        else:
            l,r = mid1 + 1, mid2 - 1 
              
    return False 

#Ternary Search (Recursive)

# def ternarySearch (arr, l, r, key):
#     if(l <= r):  
#         mid1 = l + (r-l) // 3 
#         mid2 = r - (r-l) // 3
               
#         if(key == arr[mid1] or key == arr[mid2]):
#             return True                
        
#         if(key < arr[mid1]): 
#             return ternarySearch(arr,l,mid1-1,key)  
#         elif(key > arr[mid2]):  
#             return ternarySearch(arr,mid2+1,r,key)            
#         else:
#             return ternarySearch(arr,mid1+1,mid2-1,key)   
              
#     return False 