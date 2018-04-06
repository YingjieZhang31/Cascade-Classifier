from PIL import Image
import os.path
import glob

def convertjpg(jpgfile,outdir,width=20,height=20):
	img=Image.open(jpgfile)
	try:
		new_img=img.resize((width,height),Image.BILINEAR)
		new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
	except Exception as e:
		print(e)

for jpgfile in glob.glob(r'pos2\*.jpg'):
	convertjpg(jpgfile,r'pos')
