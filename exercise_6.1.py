largest = None
smallest = None
while True:    
	try :
		num = input("Enter a number: ")
		if num == "done" : break
		
		int(num)
        
		if largest==None or int(num)>int(largest) :
			largest = num
        
		if  smallest==None or int(num)<int(smallest) :
			smallest = num
        
	except ValueError:
		print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
