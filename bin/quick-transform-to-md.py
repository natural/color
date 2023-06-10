#!/usr/bin/env python
import subprocess 
import sys

colors = "black blue brown cyan green grey magenta orange pink purple red violet white yellow"
names = colors.split()

markdown = open('color.md', 'w')
print('# Colors', file=markdown)

for name in names:
	csv = name + '.csv'
	lines = [line.strip() for line in open(csv).readlines()]
	lines.sort()

	print(name, file=sys.stdout)
	print('## ' + name.title(), file=markdown)
	print(file=markdown)

	for line in lines:

		color, hex = line.rsplit(',', maxsplit=1)
		print('#### ' + color, file=markdown)
		print('Hex: ' + hex,  file=markdown)

		code = hex[1:]

		command = '../bin/color-thumbnail ' + code + ' -d 64 | base64'
		output = subprocess.getoutput(command)
		print('Swatch: ' + '![' + name + '](data:image/png;base64,' + output + ')',  file=markdown)
		print('',  file=markdown)


markdown.flush()
markdown.close()
