import sys

#####Assing-3
##1
# file=open(sys.argv[1]+".txt","r")
# l_count=0
# f=file.read().split("\n")
# for i in f:
# 	# print(i)	
# 	print("=======")
# 	print(i)
# 	if not i.startswith("T"):			
# 		l_count+=1
# print(f" Number of lines in {file.name} is {l_count}")

##2

# def check_prime(num):
# 	if num>1:
# 		for i in range(2,num):
# 			if num%i == 0:
# 				return f"{num} is not prime number"
# 			else:
# 				return f"{num} is prime number"
# 		else:
# 			return f"{num} is not prime number"
# 	else:
# 		return f"{num} is not prime number"		
					
# file=open(sys.argv[1]+".txt","r")
# for i in file:	
# 	print(check_prime(int(i)))

##3

# class myexcept(Exception):
	
# 	def __init__(self,name,msg="doesn't exists in dictionary"):
# 		self.name=name	
# 		self.msg=msg	
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"Key --> {self.name} {self.msg}"

# def search(d,name):

# 	if name in d.keys():
# 		return "Name : {}, age : {}, Course : {}, Semester : {}, Marks : {}".format(name,d[name][0],d[name][1],d[name][2],d[name][3])
# 	else:
# 		raise myexcept(name)	

# stud={"Dinesh":[23,"MCA",1,45],"Naveen":[23,"MBA",2,65],"Pankaj":[23,"Msc",1,55]}
# name=input("Enter student name to search : ")
# print(search(stud,name.title()))



##4

# def hash_display(file):
# 	file=file.read().strip()
# 	out=""
# 	for i in file:
# 		out+=i+"#" 
# 	print(out)	
# try:	
# 	f=open(sys.argv[1]+".txt","r")	
# 	hash_display(f)
# except FileNotFoundError:
# 	print(f"file doesn't exists")
# except Exception as e:
# 	print(e)	


##5

# def find_max(a,b):
# 	if a>b:
# 		return a
# 	return b	
# try:
# 	f=open(sys.argv[1]+".txt","r")
# 	f_write=open(sys.argv[2]+".txt","w+")
# 	#5-1
# 	nums=[]
# 	for i in f:
# 		nums.append(int(i.strip()))
# 	print(f"Stored Integers in List => {nums}")	
# 	#5-2
# 	print(f"Maximum of two numbers {nums[0]} and {nums[1]} : {find_max(nums[0],nums[1])}")
# 	#5-3
# 	sum=0
# 	for j in nums:
# 		sum+=j
# 	print("Summation of all number from the file : {}".format(sum))	
# 	#5-4
# 	f.seek(0)
# 	for z in f:		
# 		f_write.write(str(z))
# 	f_write.write(f"Total : {sum}")		
# except Exception as e:
# 	print(e)
# finally:
# 	f_write.close()	
# 	f.close()

