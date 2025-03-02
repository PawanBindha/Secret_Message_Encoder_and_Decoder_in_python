import random
import string
#  Take Input from customer
str = input("Enter Your Massage :-")
str1= str.split(' ')

# encoding code

print("\n Your Massage is Encoding into secret Language:-")
res_output = []
for i in str1:
    if len(i) <= 2 :
        res = i[::-1]
        
    else:
        res = i[-2::-1]
        res += i[-1]
        random_start = ''.join(random.choices(string.ascii_letters, k=3))
        random_end = ''.join(random.choices(string.ascii_letters, k=3))
        res = random_start + res + random_end
    res_output.append(res)
    
str_output = ' '.join(res_output)

print(str_output)

# decode code

print('\n Decode Masage:-')
output1 = []
str_output1 = str_output.split(' ')
for i in str_output1:
    if len(i) <= 2 :
        res1 = i[::-1]
    else:
        res = i[3:-3]
        res1 = res[-2::-1]
        res1 += res[-1]
    output1.append(res1)
finally_massage = ' '.join(output1)
print(finally_massage)

