Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12.0
>>> a
12.0
>>> type(a)
<class 'float'>
>>> print(a)
12.0
>>> print(str(a))
12.0
>>> def chop(t):
	del t[0];
	del t[len(t)-1];
	print(t);

	
>>> t = [0 1 2 3 4 5 6 7 8 9]
SyntaxError: invalid syntax
>>> t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> t
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> chop(t)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> def chop(t):
	t[0] = 'NONE';
	t[len(t)-1] = 'NONE';
	print(t);

	
>>> T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> chop(T)
['NONE', 1, 2, 3, 4, 5, 6, 7, 8, 'NONE']
>>> 
=============== RESTART: /home/user/RTR108/lists_exercise1.py ===============
>>> 
=============== RESTART: /home/user/RTR108/lists_exercise1.py ===============
>>> B = middle(t);
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    B = middle(t);
NameError: name 't' is not defined
>>> t
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> B = middle(T);
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    B = middle(T);
NameError: name 'T' is not defined
>>> T
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> B = middle(T);
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    B = middle(T);
  File "/home/user/RTR108/lists_exercise1.py", line 4, in middle
    del a[len[a]-1];
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
=============== RESTART: /home/user/RTR108/lists_exercise1.py ===============
>>> T
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> B = middle(T);
Array input
[1, 2, 3, 4, 5, 6, 7, 8]
Array output
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
=============== RESTART: /home/user/RTR108/lists_exercise1.py ===============
>>> T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> B = middle(T);
Array input
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Array output
[1, 2, 3, 4, 5, 6, 7, 8]
>>> B
[1, 2, 3, 4, 5, 6, 7, 8]
>>> T
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
Sat
Sat
Sat
Sat
Sat
Sat
Sat
Sat
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
Sat
Sat
Sat
Sat
Sat
Sat
Sat
Sat
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
Traceback (most recent call last):
  File "/home/user/RTR108/list_exercise3.py", line 12, in <module>
    if isWeekDay(words[2]):
  File "/home/user/RTR108/list_exercise3.py", line 4, in isWeekDay
    if dayInput==day : return true;
NameError: name 'true' is not defined
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Sun
>>> 
================ RESTART: /home/user/RTR108/list_exercise3.py ================
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Not a valid week day
>>> 
======== RESTART: /home/user/RTR108/list_exercises/list_exercise3.py ========
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Not a valid week day
>>> 
