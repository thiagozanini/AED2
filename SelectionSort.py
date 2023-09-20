def selectionSort(itemsList):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList
#arq = ('arquivo.csv', 'r')
#arq.readlines()
#arq.close()
a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
selectionSort(a)
 
print(a)