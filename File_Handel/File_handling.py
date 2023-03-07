# new_file= open("newfile.txt", 'w')
# new_file.write("this is new file")
# new_file.close
# print(new_file)

new_file= open("newfile.txt", 'a')
new_file.write("this is the append file \n")
new_file.write("this is the thrid file \n")
new_file.close
print(new_file)
