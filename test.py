sts ="1111111010001111111000011100001000"
def get_input_element_length(st):
	dics={}
	st = st.strip()
	global size
	size={}
	start=[]
	n=0
	for x in range(len(st)):
		
		
		if st[x] == "1":

			start.append(x)
		else:
			
			size[n]=start
			n=n+1
			start = []

	# print(len(size[2]))
	# print(len(size))

	# for y in range(len(size)):
	# 	if len(size[y]) == 0:
	# 		del size[y] 

	# for z in size.values():
	# 	length = max(z) - min(z) +1
	# 	print(length)

	return size

aa = get_input_element_length(sts)
print(aa)
	

