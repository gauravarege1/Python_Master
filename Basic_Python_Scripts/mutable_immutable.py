# ## File and Elif 
# a=int(input("Enter your numberA :"))
# b=int(input("Enter your NumberB :"))
# c=int(input("Enter your numberC :"))
# print (a+b/c)

# ## for Loop
# name="enter your name"
# for i in "dinesh":
#     print ('hello')
# #### for varriable in squance  ( this is defaination for for loop in squnace :- list, dict,str,tupple,object)

# for i in range (1,10):
#     if i==8:
#         continue    
#     print ('hello')

    
# ### While loop
# i=1
# while i <10:
#     print ("hello word")
#     i+=1

# user=['abc','ram','root','deepak','ram']
# for i in user:
#     if i=='root':
#         continue
#     print (i)


# name=input("Enter your name: ")
# age=int(input("Ener your age: "))
# if age <=20:
#     print ("you Don't play")
# if age >=30:
#     print ("You play")
   
# name=input("Enter your name: ")
# age=int(input("Ener your age: "))
# if age <=20 or (name== "[0]" or name=='a' or name=='A'):
#     print ("you Don't play")
# elif age >= 21 and  age  <= 30:
#     print ("You play")
# else:
#    print ('Your are eligiable to play')


# a=int(input("Enter your numberA :"))
# b=int(input("Enter your NumberB :"))
# c=int(input("Enter your numberC :"))

# if a>b and  b>c:
#     print  (a)
# elif b>a and b>c:
#     print (b)
# else:
#     print (c)
    

# lottery_number=29
# count=0
# guess_number=int(input("Enter your  number:"))
# while guess_number != lottery_number:
#     if guess_number == lottery_number:
#         print ("You Win !!!")
#     elif guess_number < lottery_number:
#         print ("Your number is too low")
#     elif guess_number > lottery_number:
#         print ("Your numbner is too high")
#     else:
#         print ('Exit')
#     count += 1
#     if  count ==3:
#         print ("Repet again")

lottery=25
number = 0
count = 0
while number != lottery:
#    print(type(number))
#    print(type(lottery))
    number = int(input("Plese enter your  number: "))
    if lottery > number:
        print ("You are too close")
    elif lottery < number:
        print ("your value to too high")
    elif lottery == number:
        print ("you win")
    count = count + 1
    if count == 4:
        print("Retries exceeded")
        break
else:
    print("Money deposit")

print(count)
         
    