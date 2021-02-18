import sys,average,pickle,random,os,datetime,re

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

##7

# class myexcept(Exception):
	
# 	def __init__(self,name,msg="Roll number should be unique"):			
# 		self.name=name
# 		self.msg=msg	
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"Student {self.name}'s {self.msg}"


# class Student:

# 	stud=[]

# 	def __init__(self,roll_no,name,contact,dob,gender,marks):		
# 		Student.check_roll_no(name,roll_no)
# 		self.id=roll_no
# 		self.name=name
# 		self.contact=contact
# 		self.dob=dob
# 		self.gender=gender
# 		self.marks=marks		
# 		self.add_stud()
	
# 	def add_stud(self):
# 		self.stud.append(self)

# 	def cal_spi(self):
# 		credit=[random.randint(4,9)]*len(self.marks)
# 		s=0		
# 		for i in range(0,len(self.marks)):
# 			s+=credit[i]*self.marks[i]
# 		self.spi=s//sum(credit)	
# 		# print(self.spi)		
# 		return self.spi
	
# 	def search_student(self,name):
# 		for i in self.stud:
# 			if name.strip().lower() == i.name.strip().lower():	
# 				print(f"User => {name} found ")			
# 				i.show()
# 		else:
# 			print(f"User => {name} does't exists ")	

# 	def show(self):			
# 			print(f"Name : {self.name} , Roll_NO : {self.id} , Contact : {self.contact}, Date of Birth : {self.dob}, Gender : {self.gender} , Marks : {self.marks}")


# 	def get_age(self):
# 		d=self.dob.split("-")
# 		c=datetime.datetime.now()
# 		return f"Age : {c.year-int(d[len(d)-1])}"

# 	def get_id(self):
# 		return self.id
	
# 	def set_id(self,id):
# 		self.id=id

# 	def get_name(self):
# 		return self.name

# 	def set_name(self,n):
# 		self.name=n
	

# 	def get_contact(self):
# 		return self.contact

# 	def set_contact(self,c):
# 		self.contact=c

# 	def get_dob(self):
# 		return self.dob
	
# 	def set_dob(self,d):
# 		self.dob=d

# 	def get_gender(self):
# 		return self.gender

# 	def set_gender(self,g):
# 		self.gender=g

# 	def get_marks(self):
# 		return self.marks

# 	def set_marks(self,m):
# 		self.marks=m	
    
	

# 	@classmethod
# 	def check_roll_no(cls,name,num):
# 		for i in cls.stud:			
# 			if num == i.id:
# 				print(f"{i.name} => {i.id}")
# 				raise myexcept(name)
# 		else:

# 			return		


# def write_pass(stud):
# 	p=[]
# 	with open(os.getcwd()+"/pass.txt","wb") as f:
# 		for i in stud:
# 			if i.spi>=50:
# 				p.append(i)

# 		pickle.dump(p,f)		


# try:
	
# 	dinesh=Student(46,"Dinesh","8490086339","25-10-1997","Male",[45,55,60,70])
# 	dinesh_copy=Student(47,"Naveen paul","8490086639","25-10-1997","Male",[5,55,60,70])
# 	print(dinesh.get_age())
# 	print(average.cal_avg(dinesh,dinesh.marks))
# 	dinesh.cal_spi()
# 	dinesh_copy.cal_spi()	
# 	dinesh.search_student("Naveen paul")
# 	with open(os.getcwd()+"/student.txt","wb") as f:
# 		pickle.dump(Student.stud,f)		
	
# 	with open(os.getcwd()+"/student.txt","rb") as f:		
# 		obj=pickle.load(f)		
# 		for i in obj:
# 			i.show()
# 	write_pass(Student.stud)		
# except Exception as e:
# 	print(e)
	
# finally:	
# 	pass


##8


# class myexcept(Exception):
	
# 	def __init__(self,msg="Interest rate of savings account should be greater than current account"):					
# 		self.msg=msg	
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"{self.msg}"

# class Account:

# 	d={}

# 	def __init__(self,name,date_open,balance,account,interest):
# 		self.name=name
# 		self.date_open=date_open
# 		self.balance=balance
# 		self.account=account
# 		self.interest=interest
		

# 	def deposit(self,amount):
# 		self.balance+=amount
# 		return self.balance

	
# 	def withdraw(self,amount):
# 		if self.balance>=amount:
# 			self.balance-=amount
# 			return self.balance
# 		return f"Withraw amount {amount} is more than available balance {self.balance}"	

# 	def get_monthly_int(self):

# 		mon_interest=(self.interest/100)/12
# 		return mon_interest*self.balance
		
# 	def add_int(self,add):
	
# 		self.interest+=add
# 		return self.interest

# 	def get_interest_dict(self):
# 		return self.d

# 	def show_details(self):
# 		print(f"Name : {self.name} , Account Opened :{self.date_open}, Balance : {self.balance}, Accound Number :  {self.account}, Interest : {self.interest}")

# class SavingsAccount(Account):

# 	def __init__(self,name,dop,bal,acc,mon_int):

# 		d=super().get_interest_dict()
		
# 		if len(d.keys())>0:
# 			if "int_current" in d.keys():
# 				if mon_int>d["int_current"]:
# 					d["int_savings"]=mon_int
# 					super().__init__(name,dop,bal,acc,mon_int)
# 				else:
# 					raise myexcept	
# 			else:
# 				d["int_savings"]=mon_int
# 				super().__init__(name,dop,bal,acc,mon_int)
# 		else:					
# 			super().__init__(name,dop,bal,acc,mon_int)
# 			d["save_interest"]=mon_int

	
	

# class CurrentAccount(Account):

# 	def __init__(self,name,dop,bal,acc,mon_int):

# 		d=super().get_interest_dict()

# 		if len(d.keys())>0:
# 			if "int_savings" in d.keys():
# 				if mon_int<d["int_savings"]:
# 					d["int_current"]=mon_int
# 					super().__init__(name,dop,bal,acc,mon_int)
# 				else:					
# 					raise myexcept	
# 			else:
# 				d["int_current"]=mon_int
# 				super().__init__(self,name,dop,bal,acc,mon_int)
# 		else:
# 			d["int_current"]=mon_int					
# 			super().__init__(name,dop,bal,acc,mon_int)
			
	
# 	def withdraw(self,amount):

# 		if (self.balance-amount)>1000:
# 			super().withdraw(amount)
# 			return
# 		print(f"Minimum account balance should be Rs. 1000 and available balance is {self.balance}")

			

# def createaccount(name,dop,bal,acc,mon_int,ac_type):	

# 	if ac_type == 1:
# 		return SavingsAccount(name,dop,bal,acc,mon_int)
# 	else:
# 		return CurrentAccount(name,dop,bal,acc,mon_int)


# def find_user(name,data):

# 	for i in data:
# 		if i.name.strip().lower() == name.strip().lower():
# 			return i
# 	return None


# accounts=[]

# try:
# 	while True:

# 		print("1 . Create Account")
# 		print("2 . Deposit")
# 		print("3 . Withraw")
# 		print("4 . Check balance")
# 		print("5 . Check Monthly Interest")
# 		print("6 . Exit")

# 		print("Enter Your Choice : ")
# 		ch=int(input())

# 		if ch == 1:
# 			print("Type of account( 1 - Savings/ 2 - Current) : ",end="\n")
# 			ac=int(input())
# 			name=input("Enter A/c user name : ")
# 			bal=int(input("Enter Initial balance amount : "))
# 			acc=int(input("Enter A/c Number : "))
# 			interest=float(input("Enter Rate of interest : "))


# 			if ac == 1:
				
# 				a=createaccount(name,datetime.date.today(),bal,acc,interest,1)
# 				a.show_details()
# 				accounts.append(a)

# 			else:
# 				print("Inside current")
# 				b=createaccount(name,datetime.date.today(),bal,acc,interest,2)
# 				b.show_details()
# 				accounts.append(b)				
		
# 		elif ch == 2:

# 			amount=float(input("Enter deposit amount : "))
# 			name=input("Enter account holder name : ")
# 			user=find_user(name,accounts)
# 			if user != None:
# 				user.deposit(amount)
# 			else:
# 				print("{} account doesn't exists.".format(name))

# 		elif ch == 3:

# 			amount=float(input("Enter withdraw amount : "))
# 			name=input("Enter account holder name : ")
# 			user=find_user(name,accounts)
# 			if user != None:
# 				user.withdraw(amount)
# 			else:

# 				print("{} account doesn't exists.".format(name))			
# 		elif ch == 4:
			
# 			name=input("Enter account holder name : ")
# 			user=find_user(name,accounts)
# 			if user != None:
# 				print(f"Name : {user.name}, Account : {user.account}, Balance : {user.balance} ")
# 			else:
# 				print("{} account doesn't exists.".format(name))			

# 		elif ch == 5:

# 			name=input("Enter accound holder name : ")
# 			user=find_user(name,accounts)

# 			if user != None:
# 				print(user.get_monthly_int())
# 			else:
# 				print("{} account doesn't exists.".format(name))			
	
# 		elif ch == 6:
# 			break
					



# except Exception as e:
# 	print(e)

##9

# class myexcept(Exception):
	
# 	def __init__(self,name,msg="doesn't exists in the following directory"):					
# 		self.msg=msg	
# 		self.name=name
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"File {self.name} {self.msg} {os.getcwd()}"

# try:
# 	if len(sys.argv)>=2:
# 		file=sys.argv[1]+".txt"
# 		if not (os.path.exists(file)):
# 				raise myexcept(file)
# 		else:	
# 			l_count=0
# 			w_count=0
# 			ch_count=0	
# 			avg_ch_l=0
# 			avg_ch_w=0
# 			avg_w_l=0
# 			with open(file,"r") as f:
				
# 				data=f.read().split("\n")				
# 				for i in data:
# 					words=i.strip().split()
# 					l_count+=1
# 					w_count+=len(words)						
# 					for j in words:
# 						for k in j:
# 							ch_count+=1
				
# 				avg_ch_l=ch_count//l_count
# 				avg_w_l=w_count//l_count
# 				avg_ch_w=ch_count//w_count			

# 				print(f"Total Number of lines : {l_count} , number of words : {w_count}, number of characters : {ch_count}")	
# 				print(f"Average number of characters per line : {avg_ch_l}")
# 				print(f"Average number of words per line : {avg_w_l}")
# 				print(f"Average number of characters per words : {avg_ch_w}")

# 	else:
# 		print(f"Please provide the file name in command line")

# except Exception as e:
# 	print(e)		


##10

# class myexcept(Exception):
	
# 	def __init__(self,name,msg="doesn't exists in the following directory"):					
# 		self.msg=msg	
# 		self.name=name
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"File {self.name} {self.msg} {os.getcwd()}"


# class InvalidUserException(Exception):
	
# 	def __init__(self,name,msg="Invalid User"):					
# 		self.msg=msg	
# 		self.name=name
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"{self.name} {self.msg}"

# class InvalidPasswordException(Exception):
	
# 	def __init__(self,msg="Invalid Password"):					
# 		self.msg=msg	
# 		super().__init__(self.msg)	

# 	def __str__(self):
# 		return f"{self.msg}"

# class User():

# 	def __init__(self,name,password,balance=0):
	
# 		self.name=name
# 		self.password=password
# 		self.bal=balance

# 	def withdraw(self,amount):

# 		if self.bal>amount:
			
# 			self.bal-=amount
# 			return f"Available balance is {self.bal}"

# 		return f"Insufficient balance {self.bal}"	

# 	def deposit(self,amount):

# 		self.bal+=amount
# 		return f"Available balance is {self.bal}"

# 	def get_bal(self):

# 		return f"Available balance is {self.bal}"

		
		
# try:
	
# 	if len(sys.argv)>=2:

# 		file=sys.argv[1]

# 		if not (os.path.exists(file)):
			
# 			raise myexcept(file)
# 	else:
						
# 		raise Exception("Provide file name in command line")	
			
# except Exception as e:
# 	print(e)      

# finally:

# 	try:	

# 		print("Default file name was student.dat will be created..")
# 		file="Student.dat"
# 		dummy_user=User("Peter","peter123")
# 		dummy_user_new=User("Pankaj","pankaj345")
# 		print("Default Users..")		
# 		obj=[]
# 		obj.append(dummy_user)
# 		obj.append(dummy_user_new)

# 		for k in obj:
			
# 			print("Name : {}, Password : {}".format(k.name,k.password))

# 		with open(file,"wb") as f:
# 			pickle.dump(obj,f)	 

# 		name=input("Enter username : ")	

# 		with open(file,"rb") as f:

# 			objects=pickle.load(f)
# 			flag=False

# 			for i in objects:

# 				if name.strip().lower() == i.name.strip().lower():
					
# 					flag=True
			
# 			if flag:	

# 				password=input("Enter your four digit PIN NO. :  ")
# 				flag_p=False
# 				user=None
# 				for j in objects:

# 					if password.strip().lower() == j.password.strip().lower():

# 						flag_p=True
# 						user=j
# 				if flag_p:
						
# 						# print("password matched!!!")

# 						while True:
							
# 							print("1 . Deposit")
# 							print("2 . Withraw")
# 							print("3 . Check balance")
# 							print("4 . Quit")

# 							ch=int(input("Select Option : "))

# 							if ch == 1:

# 								amount=float(input("Enter deposit amount :"))
# 								print(user.deposit(amount))

# 							elif ch == 2:

# 								amount=float(input("Enter withdraw amount :"))
# 								print(user.withdraw(amount))

# 							elif ch == 3:
								
# 								print(user.get_bal())	

# 							elif ch == 4:

# 								break

# 							else:

# 								break	
							


# 				else:

# 					raise InvalidPasswordException()	

# 			else:

# 				raise InvalidUserException(name)	

# 	except Exception as e:
# 		print(e)			

##11



# class Library():

	

# 	def __init__(self,name):

# 		self.name=name
# 		self.books=[]		
		
		

# 	def add_book(self,book):

# 		for i in self.books:

# 			if book.id == i.id:

# 				return f" {book.id} already exists "
			
				
# 		self.books.append(book)
		
# 		return f"Id : {book.id} => Book : {book.name}  had successfully added."

	
# 	def issue_book(self,b_id):

# 		for i in self.books:

# 			if b_id == i.id:

# 				if i.no >=1:

# 					i.no-=1	
# 					return f"{i.name} was successfully issued "

# 				else:
					
# 					raise Exception(f"{i.name} Book was out of stock {i.no}")
					
		
# 		return f"{b_id} doesn't exists in library."

# 	def deposit_book(self,b_id):

# 		for i in self.books:

# 			if b_id == i.id:
				
# 					i.no+=1	
# 					return f"{i.name} was successfully Deposited "									
		
# 		return f"{b_id} doesn't exists in library."	

# 	def set_copy(self,n,b_id):

# 		for i in self.books:

# 			if b_id == i.id:	

# 				i.no=n	
# 				return f"Book id :  {i.id} has {i.no} available number of stocks."	

# 		return f"Book id : {b_id} doesn't exists in library"		

# 	def search_book(self,a_name):

# 		for i in self.books:

# 			if a_name == i.name:

# 				return f"Book id : {i.id}, Author name : {i.author}, Book : {i.name} , In Stock : {i.no}"

# 	def search_author(self,a_author):

# 		for i in self.books:

# 			a=re.findall("^"+a_author,i.author)			
# 			if a:	
# 				return f"Book id : {i.id}, Author name : {i.author}, Book : {i.name} , In Stock : {i.no}"				
# 			else:
# 				return f"author : {a_author} doesn't exists"	

# 	def add_record(self,file):
		
# 		with open(os.getcwd()+"/"+file,"wb") as f:			
# 			pickle.dump(self.books,f)
# 			return f"Records added to {file}"

# class Book(Library):

# 	def __init__(self,b_id,name,author,no_copy=1):

# 		self.id=b_id
# 		self.name=name
# 		self.author=author
# 		self.no=no_copy


# 	def add_book(self,book):

# 		if book != None:

# 			return super().add_book(book)

# 		return f"please provide book details"	

# def create_book(num=None,name=None,author=None):

# 	if num != None and name!=None and author!=None:
# 		return Book(num,name,author)

# try:

# 	roman_lib=Library("Roman Library")

# 	while True:

# 		print("1 . Add New Book")
# 		print("2 . Issue")
# 		print("3 . Deposit")
# 		print("4 . Set number of copies : ")
# 		print("5 . Search book using author name :")
# 		print("6 . Search book using book name :")
# 		print("7 . Add records in file :")
# 		print("8 . Exit")

# 		ch=int(input("Enter your choice : "))

# 		if ch == 1:

# 			num=int(input("Enter book Id : "))
# 			name=input("Enter book name : ")
# 			a_name=input("Enter author name : ")
# 			print(roman_lib.add_book(create_book(num,name,a_name)))

# 		elif ch == 2:

# 			num=int(input("Enter book Id : "))
# 			print(roman_lib.issue_book(num))

# 		elif ch == 3:

# 			num=int(input("Enter book Id : "))
# 			print(roman_lib.deposit_book(num))

# 		elif ch == 4:

# 			num=int(input("Enter number of copies to stock up : "))	
# 			b_id=int(input("Enter book Id : "))	
# 			print(roman_lib.set_copy(num,b_id))

# 		elif ch == 5:

# 			name=input("Enter author name : ")
# 			print(roman_lib.search_author(name))

# 		elif ch == 6:

# 			name=input("Enter book name : ")	
# 			print(roman_lib.search_book(name))

# 		elif ch == 7:

# 			file=input("Enter file name ")	
# 			roman_lib.add_record(file)

# 		elif ch == 8:

# 			break

# 		else:

# 			break

# except Exception as e:

# 	print(e)			

# finally:

# 	sys.exit()	


##12

# class Book():

# 	def __init__(self,num,name,auth,price):

# 		self.num=num
# 		self.name=name
# 		self.auth=auth
# 		self.price=price

# 	def display(self):
# 		print("Id : {}, Name : {}, Author : {}, Price : {}".format(self.num,self.name,self.auth,self.price))


# def createBook(num,name,auth,price):

# 	if num!=None and name!=None and auth!=None and price!=None:

# 		return Book(num,name,auth,price)

# 	return None	

# def createFile():

# 	num=int(input("Enter Book number : "))
# 	name=input("Enter Book Name : ")
# 	auth=input("Enter Author Name : ")
# 	price=float(input("Enter Book price : "))

# 	if num!=None and name!=None and auth!=None and price!=None:

# 		with open(os.getcwd()+"/Book.dat","ab") as f:

# 			pickle.dump(createBook(num,name,auth,price),f)

# 		return f"Book :  {name}, Author : {auth} has been successfully added to the file {f} ."	

# 	return "Book not to File the student.dat"	


# def loadall():
#     with open(os.getcwd()+"/Book.dat", "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break	

# def countRec(author):

# 	data=loadall()
# 	auth_count=0
	
# 	for i in data:
		
# 		if i.auth.strip().lower() == author.strip().lower():
			
# 			auth_count+=1
	
# 	return	f"Author : {author} was given {auth_count} number of books."

	
# try:
	
# 	while True:

# 		print("1 . Input record and add to Book.dat file")
# 		print("2 . To count number of books written by specific author")
# 		print("3 . Quit")

# 		ch=int(input("Enter your choice : "))

# 		if ch == 1:

# 			print(createFile())

# 		elif ch == 2:

# 			name=input("Enter author name : ")
# 			print(countRec(name))

# 		elif ch == 3:

# 			break

# 		else:

# 			break	
				

# except Exception as e:
# 	print(e)



##13

# def createPlayer():

# 	c=int(input("Enter player code : "))
# 	p_name=input("Enter player Name : ")
# 	p_country=input("Enter player Country : ")
# 	runs=int(input("Enter player  total runs : "))

# 	if c!=None and p_name!=None and p_country!=None and runs!=None:

# 		return [c,p_name,p_country,runs]
	
# 	return None	

# def loadall():
#     with open(os.getcwd()+"/players.dat", "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break	


# def regex_search():

# 	with open(os.getcwd()+"/players.dat","rb") as f:	

# 		data=loadall()
		
# 		for i in data:

# 			x=re.findall("^A",i[1])

# 			if x:
				
# 				print(f"Code : {i[0]}, Name : {i[1]}, Country : {i[2]}, Total Runs : {i[3]} ")

		

# def country(name):

# 	with open(os.getcwd()+"/players.dat","rb") as f:	

# 		data=loadall()
# 		count=0

# 		for i in data:

# 			if name.strip().lower() == i[2].strip().lower():

# 				count+=1
# 				print(f"Code : {i[0]}, Name : {i[1]}, Country : {i[2]}, Total Runs : {i[3]} ")		

# 		print(f"Total Number of Players in {name} country is {count}")		


# try:

# 	while True:

# 		print("1. Add Player")
# 		print("2. Display player details whose name startswith \'A\'")
# 		print("3. Search player by country")
# 		print("4. Add player record to the end of file")
# 		print("5. Quit")


# 		ch=int(input("Enter your choice : "))

# 		if ch == 1:

# 			with open(os.getcwd()+"/players.dat","ab") as f:
# 				pickle.dump(createPlayer(),f)

# 		elif ch == 2:

# 			regex_search()
						
# 		elif ch == 3:
							
# 			c=input("Enter country name : ")	
# 			country(c)

# 		elif ch == 4:

# 			player=createPlayer()
			
# 			with open(os.getcwd()+"/players.dat","ab") as f:
# 				pickle.dump(player,f)

# 		elif ch == 5:

# 			break		

# 		else:

# 			break	


# except Exception as e:
# 	print(e)


##14

# def loadall(file="game.dat"):
#     with open(os.getcwd()+"/"+file, "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break	

# def createGame():
	
# 	g_name=input("Enter Name of the game : ")	
# 	p=int(input("Enter Number of participants : "))

# 	if g_name!=None and p!=None:

# 		return [g_name,p]
	
# 	return None	

# def copy_game():

# 	with open(os.getcwd()+"/basket.dat","ab") as f:

# 		data=loadall()		
# 		for i in data:		
# 			if i[0].strip().lower() == "Basket Ball".strip().lower():				
# 				pickle.dump(i,f)

	


		
# def print_data(data):

# 	for i in data:
# 		print(f"Game : {i[0]}, Participants : {i[1]}")

# try:

# 	while True:

# 		print("1. Add Game")
# 		print("2. Display player details whose name startswith \'A\'")
# 		print("3. Search player by country")
# 		print("4. Add player record to the end of file")
# 		print("5. Quit")


# 		ch=int(input("Enter your choice : "))

# 		if ch == 1:

# 			with open(os.getcwd()+"/game.dat","ab") as f:

# 				pickle.dump(createGame(),f)
# 				data=loadall()
# 				print_data(data)

# 		elif ch == 2:
			
# 			copy_game()
# 			data=loadall("basket.dat")			
# 			print_data(data)
# 			# for i in data:
# 			# 	print(f"Game : {i[0]}, Participants : {i[1]}")

# 		elif ch == 3:
		
# 			break

# 		else:
		
# 			break

# except Exception as e:
	
# 	print(e)						

##15 

# def loadall(file="Student.dat"):
#     with open(os.getcwd()+"/"+file, "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break	

# def createStudent():
	
	
# 	number=int(input("Enter Admission Number : "))
# 	name=input("Enter Student Name : ")	
# 	p=float(input("Enter Percentage of Student : "))	

# 	if name!=None and p!=None and number!=None:

# 		return [number,name,p]
	
# 	return None	


# def check_stud():

# 	with open(os.getcwd()+"/Student.dat","rb") as f:

# 		data=loadall()
# 		count=0

# 		for i in data:

# 			if i[2]>75:

# 				print("Name : {}, Admission Number : {}, Percentage : {}".format(i[1],i[0],i[2]))
# 				count+=1

# 		print(f" Total Number of Students those who scored above 75% was {count}")	


# try:

# 	while True:

# 		print("1. Add Student")
# 		print("2. Check Student above 75% ")
# 		print("3. Quit")
		
# 		ch=int(input("Enter your choice : "))

# 		if ch == 1:

# 			with open(os.getcwd()+"/Student.dat","ab") as f:

# 				pickle.dump(createStudent(),f)

# 		elif ch == 2:

# 			check_stud()		

# 		elif ch == 3:

# 			break

# 		else:

# 			break

# except Exception as e:

# 	print(e)