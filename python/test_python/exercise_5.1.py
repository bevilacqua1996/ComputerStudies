def computepay(h,r):
    limit_hours = 40.0;
    if h <= limit_hours :
        pay = (h)*(r)
    else :
        pay = (limit_hours)*(r) + (h-limit_hours)*(r*1.5)
    return pay;

hrs = input("Enter Hours:")
h = float(hrs)
enterRate = input("Enter Rate:")
rate = float(enterRate)

p = computepay(h,rate)
print("Pay",p)
