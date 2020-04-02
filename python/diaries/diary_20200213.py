Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> random.randint(5, 10)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    random.randint(5, 10)
NameError: name 'random' is not defined
>>> import random
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
10
>>> random.randint(5, 10)
10
>>> random.randint(5, 10)
7
>>> random.randint(5, 10)
10
>>> random.randint(5, 10)
10
>>> random.randint(5, 10)
7
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
7
>>> random.randint(5, 10)
9
>>> random.randint(5, 10)
8
>>> random.randint(5, 10)
9
>>> random.randint(5, 10)
8
>>> random.randint(5, 10)
6
>>> random.randint(5, 10)
10
>>> random.randint(5, 100)
13
>>> random.randint(5, 100)
36
>>> random.randint(5, 100)
38
>>> random.randint(5, 100)
51
>>> random.randint(5, 100)
94
>>> random.randint(5, 100)
70
>>> random.randint(5, 100)
78
>>> 
>>> 
>>> 
>>> 
>>> t = [1, 2, 3]
>>> random.choice(t)
3
>>> random.choice(t)
2
>>> random.choice(t)
2
>>> random.choice(t)
2
>>> random.choice(t)
2
>>> random.choice(t)
3
>>> random.choice(t)
2
>>> random.choice(t)
2
>>> random.choice(t)
2
>>> random.choice(t)
3
>>> 
>>> 
>>> 
>>> 
>>> 



>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> calculatePayHour(5,10)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    calculatePayHour(5,10)
NameError: name 'calculatePayHour' is not defined
>>> calculatePayHour()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    calculatePayHour()
NameError: name 'calculatePayHour' is not defined
>>> def calculatePayHour(enterHours, enterRate):
	pay = float(enterHours) * float(enterRate)
	print('Enter Hours: ' + str(enterHours) + '\n' +
        'Enter Rate: ' + str(enterRate) + '\n' +
        'Pay: ' + str(pay) + '\n')

	
>>> calculatePayHour(2,3)
Enter Hours: 2
Enter Rate: 3
Pay: 6.0

>>> def calculatePayHour(enterHours, enterRate):
	pay = float(enterHours) * float(enterRate);
	
	print('Enter Hours: ' + str(enterHours) + '\n' +
        'Enter Rate: ' + str(enterRate) + '\n' +
        'Pay: ' + str(pay) + '\n');
	
	return pay;

>>> calculatePayHour(3,4)
Enter Hours: 3
Enter Rate: 4
Pay: 12.0

12.0
>>> a = calculatePayHour(3,4)
Enter Hours: 3
Enter Rate: 4
Pay: 12.0

>>> a
12.0
>>> class(a)
SyntaxError: invalid syntax
>>> type(a)
<class 'float'>
>>> def convertCelsiusToFarenheint(degreesCelsius):
	degreesFarenheint = (degreesCelsius*(9/5)) + 32;
	print('Celsius temperature: ' + str(degreesCelsius) '\n')
	
SyntaxError: invalid syntax
>>> def convertCelsiusToFarenheint(degreesCelsius):
	degreesFarenheint = (degreesCelsius*(9/5)) + 32;
	print('Celsius temperature: ' + str(degreesCelsius) '\n' +
	      
SyntaxError: invalid syntax
>>> def convertCelsiusToFarenheint(degreesCelsius):
	      
	degreesFarenheint = (degreesCelsius*(9/5)) + 32;
	      
	print('Celsius temperature: ' + str(degreesCelsius) + 'C' + '\n' +
	      'Farenheint Temperature: ' + str(degreesFarenheint) + 'F' + '\n');

	      
>>> convertCelsiusToFarenheint(32)
	      
Celsius temperature: 32C
Farenheint Temperature: 89.6F

>>> convertCelsiusToFarenheint(2)
	      
Celsius temperature: 2C
Farenheint Temperature: 35.6F

>>> def convertCelsiusToFarenheint(degreesCelsius):
	      
	degreesFarenheint = (degreesCelsius*(9/5)) + 32;
	      
	print('Celsius temperature: ' + str(degreesCelsius) + ' C' + '\n' +
	      'Farenheint Temperature: ' + str(degreesFarenheint) + 'F' + '\n');

	      
>>> convertCelsiusToFarenheint(2)
	      
Celsius temperature: 2 C
Farenheint Temperature: 35.6F

>>> def convertCelsiusToFarenheint(degreesCelsius):
	      
	degreesFarenheint = (degreesCelsius*(9/5)) + 32;
	      
	print('Celsius temperature: ' + str(degreesCelsius) + ' C' + '\n' +
	      'Farenheint Temperature: ' + str(degreesFarenheint) + ' F' + '\n');

	      
>>> convertCelsiusToFarenheint(2)
	      
Celsius temperature: 2 C
Farenheint Temperature: 35.6 F

>>> str = 'X-DSPAM-Confidence:0.8475'
	      
>>> str
	      
'X-DSPAM-Confidence:0.8475'
>>> find.str(':')
	      
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    find.str(':')
NameError: name 'find' is not defined
>>> str.find(':')
	      
18
>>> number = str[18:]
	      
>>> number
	      
':0.8475'
>>> number.replace(':','')
	      
'0.8475'
>>> number
	      
':0.8475'
>>> number = number.replace(':','')
	      
>>> float(number)
	      
0.8475
>>> type(number)
	      
<class 'str'>
>>> def getNumberonString(str):
	if(str.find(':') == -1) {
		print('Incorrect Format for the message');
	} else {
		position = str.find(':');
		number = str[position:];
		numberConverted = float(number.replace(':',''));
		print(number + ' ' + str(type(numberConverted)));
	}
	      
SyntaxError: invalid syntax
>>> def getNumberonString(str):
	if(str.find(':') == -1) :
		print('Incorrect Format for the message');
	else :
		position = str.find(':');
		number = str[position:];
		numberConverted = float(number.replace(':',''));
		print(number + ' ' + str(type(numberConverted)));

	      
>>> getNumberonString('X-DSPAM-Confidence:0.8475')
	      
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    getNumberonString('X-DSPAM-Confidence:0.8475')
  File "<pyshell#99>", line 8, in getNumberonString
    print(number + ' ' + str(type(numberConverted)));
TypeError: 'str' object is not callable
>>> def getNumberonString(phrase):
	if(phrase.find(':') == -1) :
		print('Incorrect Format for the message');
	else :
		position = phrase.find(':');
		number = phrase[position:];
		numberConverted = float(number.replace(':',''));
		print(number + ' ' + str(type(numberConverted)));

	      
>>> getNumberonString('X-DSPAM-Confidence:0.8475')
	      
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    getNumberonString('X-DSPAM-Confidence:0.8475')
  File "<pyshell#102>", line 8, in getNumberonString
    print(number + ' ' + str(type(numberConverted)));
TypeError: 'str' object is not callable
>>> def getNumberonString(phrase):
	if(phrase.find(':') == -1) :
		print('Incorrect Format for the message');
	else :
		position = phrase.find(':');
		number = phrase[position:];
		numberConverted = float(number.replace(':',''));
		print(number + ' ' + (type(numberConverted)));

	      
>>> getNumberonString('X-DSPAM-Confidence:0.8475')
	      
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    getNumberonString('X-DSPAM-Confidence:0.8475')
  File "<pyshell#105>", line 8, in getNumberonString
    print(number + ' ' + (type(numberConverted)));
TypeError: must be str, not type
>>> a = 5
	      
>>> a
	      
5
>>> str(a)
	      
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str(a)
TypeError: 'str' object is not callable
>>> del str
	      
>>> str
	      
<class 'str'>
>>> str(a)
	      
'5'
>>> def getNumberonString(phrase):
	if(phrase.find(':') == -1) :
		print('Incorrect Format for the message');
	else :
		position = phrase.find(':');
		number = phrase[position:];
		numberConverted = float(number.replace(':',''));
		print(number + ' ' + str((type(numberConverted))));

	      
>>> getNumberonString('X-DSPAM-Confidence:0.8475')
	      
:0.8475 <class 'float'>
>>> def getNumberonString(phrase):
	if(phrase.find(':') == -1) :
		print('Incorrect Format for the message');
	else :
		position = phrase.find(':');
		number = phrase[position:];
		number = number.replace(':','');
		numberConverted = float(number);
		print(number + ' ' + str((type(numberConverted))));

	      
>>> getNumberonString('X-DSPAM-Confidence:0.8475')
	      
0.8475 <class 'float'>
>>> 
