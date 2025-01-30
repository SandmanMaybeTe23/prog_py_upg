##5.3
pn = "0711230110"
person_number_list = []
gender_number=0
number_check=0

for letter in pn:
    person_number_list.append(int(letter))
number_amount=len(person_number_list)
print(number_amount)

second_last_number=number_amount-1


for i in person_number_list :
    number_check+=1
    
    if number_check==second_last_number:
        gender_number=i
    else:  
        print()

if gender_number%2==0:
    print(f"with the second last number bing {gender_number} you a female or are you?")
else:
    print(f"with the second last number bing {gender_number} you are a male or are you ?")