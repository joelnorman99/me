TODO: Reflect on what you learned this week and what is still unclear.

The append() method in python adds a single item to the existing list. It doesn’t return a new list of items but will modify the original list by adding the item to the end of the list.

 pyramid = [] #main list  
    tmp = [] #list inside list
    mid_val = 4 #the middle value
    k = 0

    for i in range(5): #5 rows
        for j in range(9): #9 columns
            tmp.append(" ") #adds spaces inside

        #this loop will add the "*" inside
        temp_value = 1
        while k != 0 and temp_value <= k:
            tmp[mid_val - temp_value] = "*" #placement of star to the left
            tmp[mid_val + temp_value] = "*" #placement of star to the right 
            temp_value += 1 #temp_value = temp_value + 1

        tmp[mid_val] = "*" #adds a star to the middle value
        pyramid.append(tmp) #puts tmp list inside pyramid list 
        k += 1 #k = k+1
        tmp = [] #resets tmp list :)
    
    return pyramid