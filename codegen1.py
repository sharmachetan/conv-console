import json
class reader:
	# Instance variables are placed here.
	file_list=[]
	file_element_table={}
	input_element_position_length={}
	count=0
	# soc = "<*cics*>"		will do later 
	# eoc = "</*cics*>"
	def __init__(self,name):
		self.name = name
		
		
		

		# def populate_list(self):
		# 	n=0
			
		# 	try:
		# 		with open (name,'r+') as f:
		# 			while (n<15):
		# 				feed_line = f.readline()
		# 				file_list.append(feed_line)
		# 				n = n+1
		# 	except:pass

		# 	return print(feed_line)
		# 	populate_list()

# Calculates the no. of lines in a file.
	def calculate_lines(self,name):
		EOF = ""
		
		for x in open(name,'r'):
			if (x != EOF):
				self.count = self.count + 1
			elif (x == EOF):
				return print("Empty File")
			else:
				return calculate_lines()
		return self.count
#To get line from the list.
	def get_line(self,f):
		line = f.readline()
		return line
# To read all the lines at once of File 'f'.
	#Status : Go
	def get_all_lines(self,f):
		all_lines = f.read()
		return all_lines

# To find the start and End tags of file 
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
	

#Populate the list with file lines.
	def file_in_list(self,name):
		
		try:
			with open(name,'r+') as f:

				n=0
				
				while (n<16):
					feed_line = f.readline()
					self.file_list.append(feed_line)

					n = n+1
				
		except IOError:
			pass

#Byte Identifier.
#Function extracts word from a line and stores it 
#it in a list
	#'l_number' args take the line number we want to process.
	# status: Go
	def locate_byte(self,l_number):
		line = self.file_list[l_number]
		line = line.strip()
		line_len = len(line)
		a_line = line.split('$')

		flag_w=False
		flag_c=True
		flag_i=False

		return a_line
		
	def w_spaces():
		pass
	def c_value():
		pass
	def c_input():
		pass

 # Find the index point of start and End tag. It will delete the rest of lines from the index.
  # def get_StartTag_index():

  # 	for x in range(self.count):
  # 		test_line = self.file_list[1]
  # 		if (test_line == )

#Function locates the index positionof '$' sign in string.
	# 'num' argument is line Number of file.
	# status: Go
	def get_dollar_pos(self,num):
		str="$"
		pos={}
		line = self.file_list[num]
		line_length=len(line)
		for x in range(line_length):
			if line[x]==str:
				pos[x]=str
			else:
				continue
		
		pos_key = sorted(pos)
		
		
		pos_length = len(pos_key)
		check_flag = (pos_length % 2)
		if (check_flag==0):
			return pos_key
		else:
			return print(u"\u2588" + '[Error] --> "$" Sign Missing in line {:d}'.format(num))


		

#Function get the properties of each word btw '$' sign
	# Argument 'index' takes index of line element.
	# Status: incomplete
	def get_element_prop(self,index):
		a = self.get_dollar_pos(index)
		b = self.locate_byte(1)
		element_name = b[index]
		element_length = len(b[index])


		return 

	def get_element_length(self,index):
		element = self.locate_byte(index)
		element = len(element)
		return element

# Function to create a dictionary of name and store it. 
	#status: Go
	def get_element_name(self,l_number):
		
		line= self.get_element_pos_length(l_number)		
		a = self.file_list[l_number]
		n=0
		for k,v in line.items():
			
			v = list(v)[0]
			end=k+v
			start=k
			name = a[k+1:k+v]
			self.file_element_table[n]={name}
			n=n+1
		return self.file_element_table

#Function finds the Position and length of elements in a line .
	# 'l_number' args is the line number
	#Return: It return the dictionary containing {pos,length}.
	#status: Go
	def get_element_pos_length(self,l_number):
		element_position={}
		position_length={} # stores key='Position ' and Value= 'length of element'.

		test=self.file_list[l_number]
		element = self.locate_byte(l_number)
		element_pos = self.get_dollar_pos(l_number)

		dollar_list = self.get_dollar_pos(l_number)
		dollar_count = len(dollar_list)
		# calculates the length of elements and store in position_length dictionary.
		for x in range(0,int(dollar_count/2),1):
			high_k=2*x+1
			low_k=2*x
			value=self.get_dollar_pos(l_number)
			result=(value[high_k]-value[low_k] - 1)
			position_length[element_pos[2*x]] = {result}

		return position_length
# Function Finds input value '_' inside the line.
# uncomment the lines and do the required changes
	#Status : complete
	
	def get_input_element(self,l_number):

		# print(length)
		strng = self.file_list[l_number]
		strng = strng.rstrip()
		lis=[]
		one="1"
		zero="0"
		length=len(strng)
		aa=strng.replace('$','x')
		bb=aa.replace(" ","y")

		# Replaces AlphaNumeric char to "1" and Input Spaces i.e "_" with "0".
		for x in range(length):
			if (bb[x].isalnum() or bb[x]==":"):
				lis.append(one)
			else:
				lis.append(zero)

		

		le=len(lis)
		
		# Placed Delimiter before Input Fields. Delimiter used "*".
		try:

			for st in range(1,le-1,):

				if(lis[st-1]=="1" and lis[st]=="0" and lis[st+1]=="1"):
					lis[st-1]="*"
					lis[st+1]="*"
				elif(lis[st-1]== "1" and lis[st]=="0" and lis[st+1]=="0"):
					lis[st-1]="*"
				
				elif(lis[st-1]== "0" and lis[st]=="0" and lis[st+1]=="1"):
					lis[st+1]="*"


			
				else:
					pass

			#Checks presence of Input field at Index[1] to between before last index but last not included field of list.
			if (lis[0] == "0" and lis[1] !=0):
				lis.insert(0,"*")
				
			else:
				print("caught")


		

		except IndexError:
				print('Something went wrong at line:',st)

		
		# Check for the presence of input field at first and last index .

		try:	
			

			if (lis[len(lis)-1] == "0" and lis[len(lis)-2] != "0"):
					
					lis.append("*")
			else:
				if(lis[len(lis)-1] == "0" and lis[len(lis)-2] == "0"):
					lis.append("*")
		except IndexError:
			print("There is Something Worng!!!")

		return lis

# Records the Start position and Length of the elements.
	#Status: Complete
		
	def get_input_element_length(self,l_number):
		strng = self.file_list[l_number]
		strng = strng.rstrip()	
		st=[]
		lis=[]

		for x in range(len(strng)):
			if (strng[x] != "_"):
				lis.append("0")
			else:
				lis.append("1")

		st = "".join(lis)


		dics={}
		st = st.strip()
		global size
		size={}
		start=[]
		n=0
		try:
			for x in range(len(st) + 1):
				
				
				if st[x] == "1":

					start.append(x)
				else:
					
					size[n]=start
					n=n+1
					start = []

		except IndexError:
			
			size[n]=start

		for y in range(len(size)):
			if len(size[y]) == 0:
				del size[y] 

		for z in size.values():
			length = max(z) - min(z) +1
			print(length)

		#Iterarting over keys to store value in dictionary.

		for k in size.keys():
			index_pos = min(size[k])
			length_element = int(max(size[k]) - min(size[k]) + 1)
			self.input_element_position_length[index_pos] = length_element 

		return size

# Create jSON object.
	#status: incomplete
	# def set_json(self,l_number):
	# 	json_obj = self.get_element_name(l_number)
	# 	json_str = json.load(json)
	# 	return print(json_str)
#-------------------------------------------------------------------------------------------------------
obj = reader('cif.txt')
name = obj.name
op = obj.file_in_list('cif.txt')
# ct = obj.calculate_lines(name)
# eg = obj.file_list[6]
# print(obj.locate_byte(10))
# mm = memoryview(b'eg')

# print(type(eg))
# print(mm)
# bb=bytes(mm[1])
# # print(bb)

# #This is the way to slice the string. As strings are nothning 
# #but sequence of characters in python. 
# print(eg[2])
# print(ct)



# aaa = obj.get_dollar_pos(11)
# print("This is dollar funct",aaa)

# xxx = obj.get_element_pos_length(11)
# print("This is get_element_pos",xxx)

# abc = obj.get_element_prop(0)
# print("this sis get_element_prop funct",abc)

badas = obj.get_input_element_length(10)
print("this is badass",badas)


abcd = obj.get_element_name(10)
print("this sis get_element_name",abcd)
print()

print("***",obj.input_element_position_length)

try:
	var=obj.file_list[2]
	# bfr = buffer(var,1,3)

	# print(var)
	# print("buffer is :",bfr)
except IndexError:
	print("")
	print(' ->[ ERROR ] You tried to have more than ')



# Creates a list of lines of File 'f'.






		

