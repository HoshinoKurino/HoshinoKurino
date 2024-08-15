import tkinter as tk
from tkinter import *

current_color='black'

# Color Selection Function

def Color_Selection(color):
    global current_color
    current_color = color

# Painting Function

def Paint(event):
    x,y=event.x,event.y
    canvas.create_oval(x-2,y-2,x+2,y+2,
                    fill=current_color,
                    outline=current_color)

# Clear What Was Previously Drawn

def delete():
    canvas.delete('all')

# Window

DrawingCanvas=tk.Tk()
DrawingCanvas.title('Kurinos canvas')

# The Drawing Canvas
canvas=tk.Canvas(DrawingCanvas,
                    bg='white',
                    width=600,)

canvas.pack()

# Colors to use in drawing

colors=['black','red','green','blue','yellow','purple','brown','Gray']

for c in colors:
    button=tk.Button(
        DrawingCanvas,
        bg=c,
        width=3,
        height=1,
        command=lambda color=c:Color_Selection(color)
    )
    button.pack(side=tk.LEFT)

# Clear all drawn button

Clear_Button=tk.Button(
    DrawingCanvas,
    text='clear',
    command=delete
)
Clear_Button.pack(side=tk.RIGHT)


# Mouse controlling

canvas.bind('<B1-Motion>',Paint)

DrawingCanvas.mainloop()