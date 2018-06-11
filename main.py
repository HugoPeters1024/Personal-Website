import PIL
from PIL import Image, ImageFont, ImageDraw
import sys

try:
	text = sys.argv[1];
except:
	text = "yer pretty gay!"

def create_text_field(size, text):
	wordlist = text.split(' ')
	font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 19)

	line = []
	for z in xrange(size[1] / font.size):
		line.append([])


	n=0
	for word in wordlist:
		line[n].append(word)
		if len(' '.join(line[n])) > (size[0] / font.size):
			line[n].remove(word)
			n+=1
			try:
				line[n].append(word)
			except IndexError:
				break
	img = PIL.Image.new('RGBA', size)
	edit = PIL.ImageDraw.Draw(img)

	y=50
	for i in line:	
		edit.text((0, y), ' '.join(i), (15, 15, 15), font=font)
		y += font.size
		if y > size[1]:
			break

	return img
 
img = PIL.Image.open("public/meempie-template.png")
field = create_text_field((300, 200), text)
field = field.rotate(-20)
img.paste(field, (405,450), field)
img.save("public/meempie.png")



