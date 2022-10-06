# You will create a desktop application with a Graphical User Interface (GUI)
# where you can upload an image and use Python to add a watermark logo/text.

import tkinter
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Step One : Create and open the GUI
window = tkinter.Tk()

window.title('Wades Wonderful Watermarker')
window.minsize(width = 300, height = 100)

#Step Two : Create the function that will sit behind the button.
#when pressed, will ask the user to show the file, and then will watermark in the bottom left corner
def action():
   #open the file using windows explorer
   file_path = tkinter.filedialog.askopenfilename()

   #create the image file
   image = Image.open(file_path)

   #create a copy of the image file so we can watermark it
   watermark_image = image.copy()

   #get the dimensions of the original file, so watermark will always be in bottom left
   width, height = watermark_image.size
   draw = ImageDraw.Draw(watermark_image)

   #setting the font and location
   text = "Wade's Watermark : Do Not Copy"
   font = ImageFont.truetype('arial.ttf', 36)
   textwidth, textheight = draw.textsize(text, font)
   margin = 10
   x = width - textwidth - margin
   y = height - textheight - margin

   #adding the watermark
   draw.text((x, y), text, font=font)

   #show the file and save it
   watermark_image.show()
   watermark_image.save(r'C:\Users\wcogh\Desktop\Watermarked Images\watermark.jpg')


#Step Three : create the actual button to put the function on.
button_two = tkinter.Button(text="Watermark an Image...", height=5,width=50, command=action)
button_two.pack()

window.mainloop()
