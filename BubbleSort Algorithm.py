def bubble_sort():
    
    n=int(input("Enter the Size of Array: "))
    
    array=[]
    
    for i in range(n):
        
        a=int(input("Enter the Number to be inserted: "))
        array.append(a)
    print(array)


    for i in range(len(array)):
        
        for j in range(len(array)-1):
            
            if array[j]>array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]
    print(array)

bubble_sort()