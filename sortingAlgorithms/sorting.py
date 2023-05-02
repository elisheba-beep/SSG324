#bubble sort
def bubble_sort(array):
    n = len(array)
    #traverse through all array elements
    for i in range(n):
        #last i elements are already sorted
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


#selection sort
def selection_sort(array):
    n = len(array)
    #traverse through all array elements
    for i in range(n):
        #find the min element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
            #swap the found min element with the first element
        array[i], array[min_index] = array[min_index], array[i]
        
    return array

myArray = [5,2,9,1,5]
print(bubble_sort(myArray))
print(selection_sort(myArray))
