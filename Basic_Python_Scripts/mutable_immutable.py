## File and Elif 
a=int(input("Enter your numberA :"))
b=int(input("Enter your NumberB :"))
c=int(input("Enter your numberC :"))
print (a+b/c)

## for Loop
name="enter your name"
for i in "dinesh":
    print ('hello')
#### for varriable in squance  ( this is defaination for for loop in squnace :- list, dict,str,tupple,object)

for i in range (1,10):
    if i==8:
        continue    
    print ('hello')

    
### While loop
i=1
while i <10:
    print ("hello word")
    i+=1

user=['abc','ram','root','deepak','ram']
for i in user:
    if i=='root':
        continue
    print (i)
    