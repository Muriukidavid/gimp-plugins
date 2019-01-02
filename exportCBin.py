#!/usr/bin/python
from gimpfu import register, PF_IMAGE, PF_DRAWABLE, PF_STRING, PF_OPTION, main,gimp
import struct # for packing pixel data as two bytes

# Packs the r, g and b channels into a 2 byte value
def packColor(d):
	return (((int(ord(d[0])/255.0*31.0+0.5) << 11) & 0xf800) | ((int(ord(d[1])/255.0*63.0+0.5) << 5) & 0x7e0) | (int(ord(d[2])/255.0*31.0+0.5) & 0x1f))

def exportCcodeBin(timg,tdrawable,filename,colormode):
	pr =tdrawable.get_pixel_rgn(0,0,timg.width,timg.height,False,False)
	i=0
	j=0
	size = timg.width*timg.height #image size 
	if colormode==0:
		gimp.message("12-bit mode not yet implemented")
	elif colormode==1:
		data=[]
		while (j<timg.height):
			while (i<timg.width):
				data.append(packColor(pr[i,j]))
				i+=1
			j+=1
			i=0
		savefile = open(filename,"wb")
		for byte in data:
			savefile.write(struct.pack('H',byte))
		savefile.close() 
	elif colormode==2:
		gimp.message("18-bit mode not yet implemented")
	elif colormode==3:
		gimp.message("24-bit mode not yet implemented")
	else:
		gimp.message("Error: No color mode selected")

register(
        "export-C-code-bin",
        "Saves binary image data for loading LCD",
        "Save image binary data for LCD loading",
        "David Muriuki Karibe",
        "2017",
        "2017",
        "export binary image data",
        "RGB*, GRAY*",
        [
         (PF_IMAGE, "timg", "Input image", None),
         (PF_DRAWABLE, "tdrawable", "Input drawable", None),
         (PF_STRING,"filename","file to save code to","t.bin"),
         (PF_OPTION,"colormode","RGB Color Mode",2,("12-bit(4-4-4): not implemented","16-bit(5-6-5)", "18-bit(6-6-6): not implemented","24-bit(8-8-8): not implemented"))
        ],
        [],#no return params from the plugin function
        exportCcodeBin, menu="<Image>/File/Export/")

main()
