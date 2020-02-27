phrase = "X-DSPAM-Confidence:    0.8475";

if(phrase.find(':') == -1) :
	print('Incorrect Format for the message');
else :
	position = phrase.find(':');
	number = phrase[position:];
	number = number.replace(':','');
	numberConverted = float(number);
	print(float(number));
