import sys,average,pickle,random,os

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

##6

class myexcept(Exception):
	
	def __init__(self,name,msg="Roll number should be unique"):			
		self.name=name
		self.msg=msg	
		super().__init__(self.msg)	

	def __str__(self):
		return f"Student {self.name}'s {self.msg}"


class Student:

	stud=[]

	def __init__(self,roll_no,name,contact,dob,gender,marks):
		print("Constructor called...")
		Student.check_roll_no(name,roll_no)
		self.id=roll_no
		self.name=name
		self.contact=contact
		self.dob=dob
		self.gender=gender
		self.marks=marks		
		self.add_stud()
	
	def add_stud(self):
		self.stud.append(self)

	def cal_spi(self):
		credit=[random.randint(4,9)]*len(self.marks)
		s=0
		# print(credit)
		for i in range(0,len(self.marks)):
			s+=credit[i]*self.marks[i]
		self.spi=s//sum(credit)	
		print(self.spi)		
		return self.spi
	
	def search_student(self,name):
		for i in self.stud:
			if name.strip().lower() == i.name.strip().lower():	
				print(f"User => {name} found ")			
				i.show()
		else:
			print(f"User => {name} does't exists ")	

	def show(self):			
			print(f"Name : {self.name} , Roll_NO : {self.id} , Contact : {self.contact}, Date of Birth : {self.dob}, Gender : {self.gender} , Marks : {self.marks}")


	def get_id(self):
		return self.id
	
	def set_id(self,id):
		self.id=id

	def get_name(self):
		return self.name

	def set_name(self,n):
		self.name=n
	

	def get_contact(self):
		return self.contact

	def set_contact(self,c):
		self.contact=c

	def get_dob(self):
		return self.dob
	
	def set_dob(self,d):
		self.dob=d

	def get_gender(self):
		return self.gender

	def set_gender(self,g):
		self.gender=g

	def get_marks(self):
		return self.marks

	def set_marks(self,m):
		self.marks=m	
    


	@classmethod
	def check_roll_no(cls,name,num):
		for i in cls.stud:
			# print("hello")
			# print(i.id)
			if num == i.id:
				print(f"{i.name} => {i.id}")
				raise myexcept(name)
		else:

			return		


def write_pass(stud):
	p=[]
	with open(os.getcwd()+"/pass.txt","wb") as f:
		for i in stud:
			if i.spi>=50:
				p.append(i)

		pickle.dump(p,f)		


try:
	print(os.getcwd())
	dinesh=Student(46,"Dinesh","8490086339","25-10-1997","Male",[45,55,60,70])
	dinesh_copy=Student(47,"Naveen paul","8490086639","25-10-1997","Male",[5,55,60,70])
	print(average.cal_avg(dinesh,dinesh.marks))
	dinesh.cal_spi()
	dinesh_copy.cal_spi()	
	dinesh.search_student("Naveen paul")
	with open(os.getcwd()+"/student.txt","wb") as f:
		pickle.dump(Student.stud,f)		
	
	with open(os.getcwd()+"/student.txt","rb") as f:		
		obj=pickle.load(f)
		# print(obj)
		for i in obj:
			i.show()
	write_pass(Student.stud)		
except Exception as e:
	print(e)
	
finally:
	# for i in Student.stud:
	# 	print(i.contact)
	pass
