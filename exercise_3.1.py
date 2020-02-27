hrs = input("Enter Hours:")
h = float(hrs)
enterRate = input("Enter Rate:")
rate = float(enterRate)

limit_hours = 40.0;

if h <= limit_hours :
    pay = (h)*(rate)
else :
    pay = (limit_hours)*(rate) + (h-limit_hours)*(rate*1.5)


print(str(pay))
