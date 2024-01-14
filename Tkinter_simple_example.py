import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

top = tk.Tk()

top.title('Example App')
iconFile = 'spring_logo.ico'
top.iconbitmap(iconFile)

top.geometry('1000x800')

def FileBrowse(): 
    im_path = tkinter.filedialog.askopenfilename(filetypes = (("PNG, JPG or tiff files", "*.png *.jpg *.tiff *.TIF")
                                                             ,("All files", "*.*") ))
    #display image
    image1 = Image.open(im_path)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=10, y=10)
    
B = tk.Button(top, text ="Browse", command = FileBrowse)
B.place(x=100,y=100, width=100,height=50)

top.mainloop()
