from shutil import copy
import os
import time

def encode(key, text):
	return text

def decode(key, text):
	return text

print('\nWelcome to imassages!\n')
print('Please select a destination (by typing a number):\n' +
	'1 Encode\n' +
	'2 Decode\n' +
	'3 Exit')
d = input('-> ')
if(d == '1'):
	file = input('Please enter a file path (currently supported: *.jpg, *.jpeg & *.png): ').strip()
	extensions = ['jpg', 'jpeg', 'png']
	extension = ''
	for e in extensions:
		if(file[-len(e):] == e):
			extension = e
	if(len(extension) > 0):
		newPath = os.path.dirname(file) + '/imassage' + str(time.time())[-5:] + '.' + extension
		m = input('Please enter the message: ')
		message = ''
		code = input('Please enter the encryption code (or leave this field blank): ')
		if(len(code) > 0):
			message = str(encode(code, m))
		else:
			message = m
		print('\nCreating file...')
		copy(file, newPath)
		with open(newPath, 'a') as f:
			f.write(message)
			print('Done! The image with the hidden message can be found at:\n' + newPath)
			f.close()
	else:
		print('This extension is not supported.')
elif(d == '2'):
	file = input('Please enter a file path: ').strip()
	code = input('Please enter the encryption code (if needed): ')
	with open(file, 'rb') as f:
		c = f.read()
		if(file[-4:] == '.jpg' or file[-5] == '.jpeg'):
			found = str(c)[str(c).index('\\xff\\xd9')+8:-1]
			message = ''
			if(len(code) > 0):
				message = str(decode(code, found))
			else:
				message = found
			print('Found this:\n' + message)
			print('Done! Length: ' + str(len(message)) + ' characters.')
		elif(file[-4:] == '.png'):
			found = str(c)[str(c).index('\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82')+30:-1]
			message = ''
			if(len(code) > 0):
				message = str(decode(code, found))
			else:
				message = found
			print('Found this:\n' + found)
			print('Done! Length: ' + str(len(found)) + ' characters.')
		else:
			print('This extension is not supported.')
else:
	print('Have a nice day!')
