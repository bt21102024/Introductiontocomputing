#1
m=int(input("Enter marks: "))
if(m<25):
    print("Grade: F")
elif(m>=25 and m<45):
    print("Grade: E")
elif(m>=45 and m<50):
    print("Grade: D")
elif(m>=50 and m<60):
    print("Grade: C")
elif(m>=60 and m<80):
    print("Grade: B")
elif(m>=80):
    print("Grade: A")
else:
    print("No Result")
    
#2
yr=int(input("Enter year: "))
 
if yr%4==0:
    print("Leap year")
elif yr%100==0:
    print("Not a leap year")
elif yr%400==0:
    print("Leap year")
else:
    print("Not a leap year")
    
#3
import random

for i in range(10):
    n1=random.randint(1,10)
    n2=random.randint(1,10)
    print(f"Question{i+1}:",end=" ")
    user_output=int(input(f"{n1}*{n2}="))
    if user_output==(n1*n2):
        print("Right!")
    else:
        print("Wrong. The right answer is {n1*n2}")
        
#4
x=200

for candies in range(x):
    
    if candies%5==2:
        if candies%6==3:
            if candies%7==2:
                print(candies, "candies are in the bowl!")
                break
            
            
