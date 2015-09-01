def remove_last_odd(numbers):
    has_odd = False
    last_odd=0
    for num in numbers:
        if num % 2==1:
            has_odd= True
            last_odd = num
            print (last_odd,numbers.index(last_odd))
          
    if has_odd:
        numbers.remove(last_odd)
        ## doing this, remove the first "7".


###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


        
def remove_last_odd2(numbers):
    has_odd = False
    last_odd=0
    for num in range(len(numbers)):
        if numbers[num] % 2==1:
            has_odd= True
            last_odd = num
            print (last_odd,numbers[last_odd])
            ## instead going through the elements in 
            ## "numbers" list, we take the position index as
            ##  the loop index.
          
    if has_odd:
        numbers.pop(last_odd)
        ## doing this, remove the third "7" whhose position is
        ## at 14 th on the "numbers" list.
 
        
        

def run():
    numbers = [1,7,2,34,8,7,2,5,14,22,93,48,76,15,7]
    print (numbers)
    remove_last_odd2(numbers)
    print (numbers)
    
run()