import string 
import sys

def decode(oristr): 
	upperdict = {}  
	lowerdict = {}  
	upperletters =string.ascii_uppercase
	lowerletters =string.ascii_lowercase
  
  
	dststr = []  

  
	for i in range(0,len(lowerletters)):                         
		if i<13:  
			lowerdict[lowerletters[i]] = lowerletters[i+13]  
		else:  
			lowerdict[lowerletters[i]] = lowerletters[i-13] 
		
	for i in range(0,len(upperletters)):                         
		if i<13:  
			lowerdict[upperletters[i]] = upperletters[i+13]  
		else:  
			lowerdict[upperletters[i]] = upperletters[i-13]  
  
  
	for ch in oristr:  
		if ch in lowerdict:  
			dststr.append(lowerdict[ch])  
		elif ch in upperdict:  
			dststr.append(upperdict[ch])  
		else:  
			dststr.append(ch)  
	dststr = ''.join(dststr)  
  
  
	print(dststr ) 

Judge=input('are you going to decode a file or string? f/s \n')
if Judge == ('s' or 'S'):
	oristr = input()
	print(oristr ) 
	decode(oristr)
elif Judge == ('f' or 'F'):
	filename = input("Please enter your filename: ").strip()
	with open(filename,'r') as file_object:
		lines=file_object.readlines()
		fist_line=lines[0].rstrip()
		print(fist_line) 
		decode(fist_line)
else: print('wrong input!')
