### note:-  
#File are saved in same location where your pyton scripts are saved
# if you want to change the path in somewhere in your laptop you need to defile  path  in s.write scripts like  this
# "C:/Users/GR7921/Downloads/file_name.txt"  (.txt,xls,.csv)all extenstion are support

s=open('file.txt','a') #a= append ,w=write , r=read
s.write("this is modify from visula studio code for checking" )
s.close ()  # this option are using for saving and close the file
read_file =open("file.txt" ,'r').read()
print (read_file)
