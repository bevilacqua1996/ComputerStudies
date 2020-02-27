largest = None
smallest = None
while True:
        
    try :
        num = input("Enter a number: ")
        if num == "done" : break
        
        if num>largest or largest==None :
            largest = num
        
        if num<smallest or smallest==None :
            smallest = num
            
        print(num)   
        
     except ValueError :
            
        print("Invalid data")

print("Maximum", largest)
