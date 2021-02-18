from threading import *
from time import * 
class Library:

	d={"rich dad":10,"poor dad":20}

	def __init__(self):
		self.i=Lock()

	def issue(self,num,b_name):

		self.i.acquire()

		print(f" Available number of book {self.d[b_name]}")

		if self.d[b_name]>=num:

			print(f"book {b_name}  need to issued {num}")

			sleep(1.5)

			self.d[b_name]-=num

		else:

			print(f"{b_name} book was not available")

		self.i.release()


roman=Library()

t1=Thread(target=roman.issue,args=(5,"rich dad"))
t2=Thread(target=roman.issue,args=(6,"rich dad"))

t1.start()
t2.start()