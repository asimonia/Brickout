import tkinter as tk



"""
3 Lives 

Tkinter provides classes that allow display, control and positioning of widgets.
Tk() is the outer top level widget -> Frame is inside Tk() which can contain other widgets
-> Canvas will display graphics and text
Tk -> Frame -> Canvas

"""
lives = 3
root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width=6000, height=400, bg='#aaaaff')
frame.pack()
canvas.pack()
root.title("Hello")
root.mainloop()