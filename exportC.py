#!/usr/bin/python

from gimpfu import *

def ord3(data): 
    r=data[0]
    g=data[1]
    b=data[2]
    return "{%(i)d,%(j)d,%(k)d}" % {"i":ord(r), "j":ord(g), "k":ord(b)}
    
def plugin_main(timg, tdrawable,filename):
    pr =tdrawable.get_pixel_rgn(0, 0, timg.width,timg.height, False, False);
    i=0
    j=0
    print "/* width: %(width)d, height: %(height)d " % {"width":timg.width, "height":timg.height} + " */"
    size = timg.width*timg.height #LCD size
    output = "typedef struct{ \nunsigned char \nr,\ng,\nb;\n}RGB;\n\nRGB image[" + "%(size)d" % {"size":size} + "]={\n" 
    while (j<timg.height-1):
        while (i<timg.width-1):
            output += ord3(pr[i,j]) + ","
            i+=1
        output += ord3(pr[i,j]) #the last column, no comma
        output += ",\n" #end of each row
        j+=1
        i=0
    while (i<timg.height-1): #the last row, no comma
        output += ord3(pr[i,j]) + ","
        i+=1
    output += ord3(pr[i,j]) #the last column, no comma
    output += "\n};"
           
    savefile = open(filename,"w")
    savefile.write(output)
    savefile.close()
    
    
register(
        "python_fu_LCDexport",
        "Saves the image data as LCD RGB data structure for C programming",
        "Saves the image data as LCD RGB data structure for C programming",
        "David Muriuki Karibe",
        "David Muriuki Karibe",
        "2015",
        "LCD C code",
        "RGB*, GRAY*",
        [
         (PF_IMAGE, "timg", "Input image", None),
         (PF_DRAWABLE, "tdrawable", "Input drawable", None),
         (PF_STRING,"filename","file to save code to","untitled.c"),
        ],
        [],
        plugin_main, menu="<Image>/File/Export/")

main()
