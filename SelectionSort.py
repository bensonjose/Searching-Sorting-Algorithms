def SelectionSort():

    n=int(input("Enter the Size of Array: "))

    array=[]

    for i in range(n):
        a=int(input("Enter the Number to be inserted: "))
        array.append(a)
    print(array)


    for i in range(len(array)):
        minindex=i

        for j in range(i+1,len(array)):

            if array[minindex]>array[j]:
                minindex=j

        array[i],array[minindex]=array[minindex],array[i]


    print(array)


SelectionSort()
                

