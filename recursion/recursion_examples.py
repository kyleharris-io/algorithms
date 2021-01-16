def factorial(n):
    if (n<=1):
        return 1
    else: 
        return n*factorial(n-1)

def consec_sum(n):
    if n<=1:
        return 1
    else: 
        return n+consec_sum(n-1)


# find the nth fibonacci number 
def nth_fib(n):
    if(n<=2):
        return 1 
    else: 
        return (nth_fib(n-1))+(nth_fib(n-2))

# Find the number of digits in a number with repeated /10
def len_num(num):
    if num<10: 
        return 1
    else: 
        return 1+len_num(num//10)

def list_max(max,l):
    if not (l):
        return max 
    else: 
        temp = l[0]
        if temp>max:
            return list_max(temp, l[1:])
        else: 
            return list_max(max, l[1:])



def reverse_list(string):
    print(reverse_list_rec(0,string))

def reverse_list_rec(index, string):
    if index==len(string):
        return string
    else: 
        return reverse_list(string.get(len(string)-index)+"")




print(list_max(0,[1,3,6,2,4,5]))
print(consec_sum(10))
print(nth_fib(35))
print(len_num(3300))
