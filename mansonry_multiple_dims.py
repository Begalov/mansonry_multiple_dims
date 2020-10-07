# Masonry multiple dimensions for walls and openings considering seams v.0.1.0.
# author RUben Begalov@gmail.com
import re

brick = 250
seam = 10

brick_seam = brick + seam
module = round(brick_seam / 2)


def myround(x, base=.5):
	return round(base * round(float(x) / base))


def help():
	print(f'''Masonry multiple dimensions for walls and openings considering seams v.0.1.0.

Module = (brick + seam) / 2 = ({brick} + {seam}) / 2 = {module}

Inputs:
	length-		wall without last seam
	length+		openings with double seam
	+/-		add or subtract half
	help or h	this help
	quit or q	for exit
		''')

msize = None
while True:
	if msize:
		print('\n')
		# i = Input
		# +/- seam for piers openings
		i = input('Input new length in mm or help: ')
	else:
		help()
		i = input('Input length in mm or help: ')

	if i in ('quit', 'q'):
		break;
	elif i in ('help', 'h'):
		help()
	elif i in ('+','-'):
		if i == '+':
			msize = msize + module
		elif i == '-':
			msize = msize - module

		print(f'{msize} - {module} = {myround(msize)}')
		continue
	else:
		
		m = re.search('(\d*)?([-+]*)', i)
		if m:
			
			if m.group(2) == '+':
				ss = seam
			elif m.group(2) == '-':
				ss = -seam
			else:
				ss = 0
			
			length = int(m.group(1))

		ratio = length / module
		msize = round(myround(ratio) * module + ss)
		equal = 'True' if msize == length else ''

		print(f'Ratio: {round(ratio, 1)} vs {myround(ratio)}; Multiple size {int(msize)} {equal}')