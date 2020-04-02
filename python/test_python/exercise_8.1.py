# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
counter = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue;
    position = line.find(':')
    number = line[position:]
    number = number.replace(':','')
    numberConverted = float(number)
    total = numberConverted + total
    counter = counter + 1

average = total/counter
print("Average spam confidence:", average)
