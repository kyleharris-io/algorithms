testArray = []

def initArray():
    f = open('input.txt')
    lines = f.readlines()
    for line in lines: 
        testArray.append(int(line))


def count_inversions(element_list):
    if len(element_list) <=1:
        return (element_list, 0)
    else: 
        n = len(element_list)
        (C, left_inv) = count_inversions(element_list[:(n/2)])
        (D, right_inv) = count_inversions(element_list[(n/2):])
        (B, split_inv) = countSplitInv(C,D)
        return (B, (left_inv+right_inv+split_inv))

def get_inversions(l1):
    (l, inversions) = count_inversions(l1)
    print(inversions)


    


def countSplitInv(left, right):
    # merge sorted two arrays 
    result = []
    inversions = 0
    while (left or right):
        if left and right:
            if left[0]<right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                inversions += len(left)
        
        if left and not right: 
            result.append(left.pop(0))

        if right and not left: 
            result.append(right.pop(0))
    
    return (result, inversions)

initArray()
get_inversions(testArray)