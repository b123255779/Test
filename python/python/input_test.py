def calculate():
	# i = -1
	# userID_list = []
	# x_list = []
	# y_list = []
	
	i = 7
	userID_list = ["car","car","car","car","person","person","person","person"]
	x_list = [210,290,210,290,0,500,0,500]
	y_list = [170,170,330,330,0,0,500,500]
	
	while 1:
		run = raw_input(">>> Input run or quit:")
			
		if run == "quit":
			break
		else:
			userID = raw_input(">>> Input userID:")
			x = raw_input(">>> Input x axis:")
			y = raw_input(">>> Input y axis:")
			
			if userID == "car" or userID == "person":
				if int(x) >= 0 and int(x) <= 500:
					if int(y) >= 0 and int(y) <= 500:
						userID_list.append(userID)
						x_list.append(x)
						y_list.append(y)
						
						i = i + 1
			
			# print "userID = ",userID_list
			# print "x = ",x_list
			# print "y = ",y_list
			# print "i = ",i
	
	return i,userID_list,x_list,y_list





