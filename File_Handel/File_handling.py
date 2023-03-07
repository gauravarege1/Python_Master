# ##
# 'r' ,'rt' : read , default mode
# 'w' ,'wt' : wtite : if file exist : override , if file not exist : create
# 'a' ,'at' : append : if file exist : append , if file not exist : create
# 'r+','rt+' : read and write
# 'w+' ,'wt+' : write and read
# 'a+' ,'at+' : append and read
# ##

# new_file= open("newfile.txt", 'w')
# new_file.write("this is new file")
# new_file.close
# print(new_file)

new_file= open("newfile.txt",'r+')
new_file.write("this is the append file \n")
new_file.write("this is the thrid file \n")
new_file.write("this is the 4th file \n")
new_file.writelines(['this is example\n' , 'this is second\n'])
new_file.close
new_file.truncate(10)
print(new_file)

# new_file= open("newfile.txt",'r+')
# # data=new_file.read()
# new_file.truncate()  ## all value shoud be truncate
# print (new_file)
