# You will create a desktop application with a Graphical User Interface (GUI)
# where you can upload an image and use Python to add a watermark logo/text.

import tkinter
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont




file_path = r''

#Step One : Create and open the GUI
window = tkinter.Tk()

window.title('Wades Wonderful Watermarker')
window.minsize(width = 500, height = 100)

def action_two():
   file_path = tkinter.filedialog.askopenfilename()
   image = Image.open(file_path)
   watermark_image = image.copy()
   width, height = watermark_image.size
   draw = ImageDraw.Draw(watermark_image)
   text = "sample watermark"

   font = ImageFont.truetype('arial.ttf', 36)
   textwidth, textheight = draw.textsize(text, font)
   margin = 10
   x = width - textwidth - margin
   y = height - textheight - margin

   draw.text((x, y), text, font=font)

   draw.text((0, 0), "This is a Wade Coghlan Image.",
             (0, 0, 0), font=font)
   image.save(r'C:\Users\wcogh\Desktop\Watermarked Images\watermark.jpg')


button_two = tkinter.Button(text="Watermark an Image...", height=5,width=50, command=action_two)
button_two.pack()




window.mainloop()
