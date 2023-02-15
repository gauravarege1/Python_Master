''' 
List  :-  collection of object (object means  string,int,flot,complex any  types of data are saved in list and refrence 
by [] )
x= [45,abc,4.5]
type(x)
object are always saved in index ( it's always start from 0)
''' 
x= [45,'abc',4.5,78,96]
y=['ac',78,96,"pf"]
z=[x+y]
print (z)
print (y[-1])
print (78 in y)


# # update and delete
# list1=[45,'a',8,9]
# list1[-1]='alok'
# del list1[-2]
# print(list1) 


# list1=[45,85,54,898,82,'alok',82,82]
# list1.remove(82)
# print (list1)

server_list1=['server1','server2','server3','server4']
server_list2=['server5','server6','server7','server8']
# server_list= server_list1 +  server_list2
server_list2.insert (4,'server9')
# if server_list == server_list1 and server_list == server_list2:
#     print  ("Difference")
# else:
print (server_list2)
print (server_list1)