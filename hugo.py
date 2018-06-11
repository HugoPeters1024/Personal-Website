import PIL
from PIL import Image, ImageFont, ImageDraw
import sys

try:
	text_top = sys.argv[1]
        text_bottom = sys.argv[2]
except:
	text_top = "yer pretty gay!"
        text_bottom = "gay is okay!"

def create_text_field(size, text):
	wordlist = text.split(' ')
	font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 72)

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
 
img = PIL.Image.open("public/hugo-template.png")
field = create_text_field((1200, 500), text_top)
img.paste(field, (905,50), field)
field = create_text_field((1200, 500), text_bottom)
img.paste(field, (905, 800), field)
img.save("public/hugo.png")



