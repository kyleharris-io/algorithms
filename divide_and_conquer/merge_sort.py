l1 = [38,27,43,3,9,82,10]



def sort(iteration,my_list):
    if(len(my_list)==1):
        return my_list
    else:
        print("\n\nIteration: {}".format(iteration))
        left_half = my_list[0:(len(my_list)/2)]
        right_half = my_list[(len(my_list)/2):]
        print("Left Half: {}".format(left_half))
        print("Right Half: {}".format(right_half))


        left = sort((iteration+1),my_list[0:(len(my_list)/2)])
        right = sort(iteration+1,my_list[(len(my_list)/2):])
        #return merge(left, right)

def merge(l1,l2):
    # merge sorted two arrays in linked list fashion
    result = []
    while (l1 or l2):
        if l1 and l2:
            if l1[0]<l2[0]:
                result.append(l1.pop(0))
            else:
                result.append(l2.pop(0))
        
        if l1 and not l2: 
            result.append(l1.pop(0))

        if l2 and not l1: 
            result.append(l2.pop(0))
    
    return result
    






print(sort(0,l1))

