#!/usr/bin/python
from gimpfu import register, PF_IMAGE, PF_DRAWABLE, PF_STRING, PF_OPTION, main,gimp

def array2struct(data): 
    return "{%(i)d,%(j)d,%(k)d}" % {"i":ord(data[0]), "j":ord(data[1]), "k":ord(data[2])}

def packColor(data):
    return str((ord(data[0]) << 11) & 0xf800 | (ord(data[1]) << 5) & 0x07c0 | (ord(data[2]) & 0x003f))
    
def plugin_main(timg, tdrawable,iconname,filename,colormode):
    pr =tdrawable.get_pixel_rgn(0, 0, timg.width,timg.height, False, False);
    i=0
    j=0
    size = timg.width*timg.height #LCD size
    output = "/*\nC code Exported from Gimp\n\nicon size in pixels: width="+str(timg.width)+", height:"+str(timg.height)+"\n*/\n\n" 
    if colormode==0:
        gimp.message("12-bit mode not yet implemented")
    elif colormode==1:
        output += "uint16_t "+iconname+"[" + "%(size)d" % {"size":size} + "]={\n" 
        while (j<timg.height-1):
            while (i<timg.width-1):
                output += packColor(pr[i,j]) + ","
                i+=1
            output += packColor(pr[i,j]) #the last column, no comma
            output += ",\n" #end of each row
            j+=1
            i=0
        while (i<timg.width-1): #the last row, no comma
            output += packColor(pr[i,j]) + ","
            i+=1
        output += packColor(pr[i,j]) #the last column, no comma
        output += "\n};"
        savefile = open(filename,"w")
        savefile.write(output)
        savefile.close() 
    elif colormode==2:
        gimp.message("18-bit mode not yet implemented")
    elif colormode==3:
        output += "typedef struct{ \nunsigned char \nr,\ng,\nb;\n}RGB;\n\nRGB "+iconname+"[" + "%(size)d" % {"size":size} + "]={\n" 
        while (j<timg.height-1):
            while (i<timg.width-1):
                output += array2struct(pr[i,j]) + ","
                i+=1
            output += array2struct(pr[i,j]) #the last column, no comma
            output += ",\n" #end of each row
            j+=1
            i=0
        while (i<timg.height-1): #the last row, no comma
            output += array2struct(pr[i,j]) + ","
            i+=1
        output += array2struct(pr[i,j]) #the last column, no comma
        output += "\n};"
        savefile = open(filename,"w")
        savefile.write(output)
        savefile.close() 
    else:
        gimp.message("Error: No color mode selected")    
  
    
register(
        "export-C-code",
        "Saves the image data for LCD C programming",
        "Saveimage data for LCD C programming",
        "David Muriuki Karibe",
        "David Muriuki Karibe",
        "2015",
        "export C code",
        "RGB*, GRAY*",
        [
         (PF_IMAGE, "timg", "Input image", None),
         (PF_DRAWABLE, "tdrawable", "Input drawable", None),
         (PF_STRING, "iconname", "Icon variable name","icon"),
         (PF_STRING,"filename","file to save code to","untitled.c"),
         (PF_OPTION,"colormode","RGB Color Mode",1,("12-bit(4-4-4): not implemented","16-bit(5-6-5)", "18-bit(6-6-6): not implemented","24-bit(8-8-8)"))
        ],
        [],
        plugin_main, menu="<Image>/File/Export/")

main()