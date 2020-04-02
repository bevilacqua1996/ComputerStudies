def isWeekDay(dayInput):
    weekDays = ['Mon', 'Tue','Wed','Thu','Fri','Sat','Sun',];
    for day in weekDays:
        if dayInput==day : return 1;
    else:
        return 0;

fhand = open('names.txt');
for line in fhand:
    words = line.split();
    if len(words)==0 or words[0]!='From': continue;
    if isWeekDay(words[2]):
        print(words[2]);
    else:
        print('Not a valid week day');
