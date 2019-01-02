# my python Gimp 2.8 plugins 

To use the plugins, copy the plugin scripts to the Gimp plugins folder (.gimp2.8/plug-ins/ folder under your home directory on a Linux installation) and relaunch Gimp.

## exportC.py 
This plugin exports C code for LCD icons designed in RGB and grayscale color modes or LCD font data for creating lookup tables.
To use this plugin, launch GIMP, use the **File->Create->LCD icon** menu to create a file with speific dimensions. 
Use **View->Zoom->Fit Image** in Window menu (Keyboard shortcut __Shift+Ctl+J__) to maximize the image.
For LCD font design, convert the image to binary (0,1) by selecting **Image->Mode->Indexed** and **Use black and white(1-bit) palette**
Use **Tools->Paint Tools->Pencil** menu (Keyboard shortcut __N__) to select the Pencil tool. Set the brush property Hardness to 0. Select foreground and background as required and paint the artwork. 
Select **File->Export C Code** menu to export the artwork in code. Select the file to save code in and options as desired.
Hit save button to save the file.

## exportCBin.py 
This plugin exports an image from Gimp as binary data to be loaded from an SD Card into an LCD, e.g using a microcontroller.
To use this plugin, open any image in Gimp, use the **Image->Scale Image** and **Image->Canvase Size** to scale and crop the image to desired size.
Select **File->Export Binary Pixel Data** and save to file.

## new_icon.py 
This is a simple plugin, a great example reference for learning the basics of writing Gimp plugins in gimpfu API
It only helps create am image of specific dimensions. It could be improved to select the color mode (RGB, GRAY, INDEXED)
To use it, launch Gimp and select **File->Create->LCD Icon**. Fill in the options are required and create the file.

