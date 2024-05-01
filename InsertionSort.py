def InsertionSort():

    n=int(input("Enter teh Size of Array: "))

    array=[]

    for i in range(n):
        a=int(input("Enter the Number to be inserted: "))
        array.append(a)

    print(array)

    for i in range(1,len(array)):
        key=array[i]
        j=i-1

        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1

        array[j+1]=key

    print(array)

InsertionSort()