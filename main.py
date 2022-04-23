import re, os
import tkinter.filedialog as fd

regex = re.compile("(R)([0-9]\d{4})")
d,c,h = [],0,''

os.system('cls')
path = fd.askdirectory()
for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(".txt") and 'Cookies' not in os.path.join(root,file):
			try:
				a = open(os.path.join(root,file),encoding='utf-8').read()
			except:
				pass
			if regex.search(a):
				text = regex.search(a).group()+' | File: '+file
				print(f'{c}. {text}')
				h = h + f'{c}. {text}\n'
				d.append(regex.search(a).group()+'|'+file+'|'+os.path.join(root,file))
				c += 1
os.system('cls')
print(h)
while True:
	ids = int(input('\nInfo: '))
	info = d[ids]
	os.system('cls')
	print(f'{h}\n{ids}. {info}')
	os.startfile(info.split('|')[2])