def calculate():
	x_list = []
	y_list = []
	userID_list = []
	i = -1

	while 1:
		run = raw_input(">>> Input run or quit:")
		# print run
			
		if run == "quit":
			#print "qqqqqqqqqqqqquit"
			break
		else:
			#print "rrrrrrrrrrrrrrun"
			userID = raw_input(">>> Input userID:")
			x = raw_input(">>> Input x axis:")
			y = raw_input(">>> Input y axis:")
				
			userID_list.append(userID)
			x_list.append(x)
			y_list.append(y)
				
			i = i + 1
		
	return i,userID_list,x_list,y_list





