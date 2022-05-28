def ith_order_statistic(array, i):
    pivot = array[0]
    partitioned_array = ['']*len(array)
    left_counter = 0
    right_counter = -1
    for number in array:
        if pivot > number:
            partitioned_array[left_counter] = number
            left_counter += 1
        elif pivot < number:
            partitioned_array[right_counter] = number
            right_counter -= 1
    partitioned_array[left_counter] = pivot
    
    #Partitions the array so that the elements smaller than the pivot are on the left and the bigger ones on the right.

    if left_counter == i-1:  
        return partitioned_array[left_counter]

    #The pivot ends up being the ith order statistic.

    if left_counter > i-1:
        return ith_order_statistic(partitioned_array[0:left_counter], i)
    
    #The right side of the partitioned array is cut out and a recursive call is done with the remaining elements
    #of the array.

    else: 
        return ith_order_statistic(partitioned_array[left_counter+1::], i-left_counter-1)
        
    #A recursive call is done with the right side of the array and new i that takes into account the 
    #lesser statistical orders that were eliminated.



