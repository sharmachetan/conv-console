# sample code to read fiel and identify the pattern
# 
import fileinput



class reader():
	global file 
	global element
	global file 
	global f
	file = 'cicscreen.txt'
	dict={}
	word = 0
	
	f=''
	
	def list(self,f):
		n=0
		while (n < 14):
			line_feeder = f.readline()
			print(type(line_feeder))
			print ("tthe lenghth is",len(line_feeder))
				
			list1.append(line_feeder)
			n=n+1
			
			return print(list1[n-1])
		
	
# Finds the required Start or End tags of CICSC code.
	def find_start(self,f,element):
		global n
		n=0
		end = ''
		a= f.readline(9)
		if element in a:
			#pos = f.tell()
			return (print("found"),True)
			
		else:
			if a == end:
				return (print("Not found"),False)
			else:			
				return self.find_start(f,element)
		
		
		
	
			
	 # def line_pos(self,f):
		 # next = f.readline()
		 # pattern = "\n"
			 # while next !=" ":
				 # if next == pattern:
					# count = count + 1
				 # else:
					# continue


# To display the contents of Files
	def allLines(self,f):
		asd = f.read()
		return asd

	# print (self.allLines(f))	 // paste this line in main() to display.

# Get a single line form the file as Object.
	def get_line(self,f):
		dsd = f.readline()
		return dsd
		
#***********************under testing**************************
# we are trying to insert this 'while' code into function but as the result are opposite.
# In return value we are getting Null vaules .Therfore we have put this code inside main() open.
	# def set_in_list(self,f):
		# global r1,r2,r3
		# n=0
		# while (n<16):
			# aaa = f.readline()
			# aa = str(aaa)
			# r1=print(type(aa))
			# r2=print ("tthe lenghth is",len(aa))
				
			# list1.append(aa)
			# n=n+1
			# r3=print(list1[n-1])
		# return r1,r2,r3	
		
	
			
# Here, main() is the entry point of the class.	
	
	def main(self):	
		
	
	#file is opened with persion of read only.	
		with open(file,'r') as f:
			#ou = f.readline(80)
			global soc
			global eoc
			global list1
			global EOF
			global aaa
			global line_feeder
			line_feeder=""
			EOF=""
			list1=[]
			soc = "<*cics*>"	#'soc' is Start of CICS code
			eoc = "</*cics*>"	#'eoc' is End of CICS code
		
		###	Code to insert into a list. Commented temporarily. Status = GOOD
		
			# n=0
			# while (n < 14):
				 # line_feeder = f.readline()
				 # print(type(line_feeder))
				 # print ("tthe lenghth is",len(line_feeder))
					
				 # list1.append(line_feeder)
				 # n=n+1
				 # print(list1[n-1])
				 
			
			
			fo = open('output.txt','w')
			fo.write(list1[1])
		


			
	# Find the Start tag of CICS code
			element = soc
			soc_search = self.find_start(f,element)
			print(soc_search)

	# Find the End tag of CICS code
			element = eoc
			eoc_search = self.find_start(f,element)
			print(eoc_search)
			#print(self.find_end(f))	
			if (soc_search and eoc_search):
				print(" [ok]: Found Start and End Tags")	
			else:
				print(" [Failed] : To Find Start or End Tags")
			
			# a=self.set_in_list(f)     // uncomment it when set_in_list() function is used .
			# print(a)
			print (self.get_line(f))
			
			a = self.list(f)
			print(a)
			
		f.close()		
			
# Declare the file name .Uncommen the below line for including the name		
	#file = 'put name of file here'
		
obj = reader()
obj.main()




