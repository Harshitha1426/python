# Please Write your code here...

def sort_String(s):
    lower_case = []
    upper_case = []
    odd_digits = []
    even_digits = []
 ## the char/int is checked and goes to the particular strings
    for i in s:
        if i.islower():
            lower_case.append(i)
        elif i.isupper():
            upper_case.append(i)
        elif i.isdigit(): 
## even or odd digits are checked and go to the respective strings       
            if int(i)%2==0:
                even_digits.append(i)
            else:
                odd_digits.append(i)
    return (''.join(sorted(lower_case)+sorted(upper_case)+sorted(odd_digits)+sorted(even_digits)))
## string S is appending by the summation of sorted strings

if __name__=='__main__':
    
    S = input()
    print (sort_String(S))
