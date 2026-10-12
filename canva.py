# import tkinter as tk

# root=tk.Tk()
# root.title("my first canvas")
# canvas=tk.Canvas(root,width=500,
#                  height=350,bg="white")
# canvas.create_rectangle(40,40,220,150,fill="coral")
# canvas.create_oval(280,50,440,190,fill="lightblue")
# canvas.create_line(50,250,500,250,width=4)
# canvas.create_text(275,310,text="hello canvas",font=("arial",20))
# canvas.pack()


# root.mainloop()


# import tkinter as tk
# root=tk.Tk()
# root.title("house")
# canvas=tk.Canvas(root,width=600,
#                  height=500,bg="#ee0ea336")

# canvas.pack()
# #House wall - large rectangle
# canvas.create_rectangle(
#     120, 180, 380, 350,
#     fill="lightyellow",
#     outline="black",
#     width=3
# )
# #Roof - triangle
# canvas.create_polygon(
#     100, 180,
#     250, 60,
#     400, 180,
#     fill="red",
#     outline="black",
#     width=3
# )
# # Left window - square
# canvas.create_rectangle(
#     150, 220, 200, 270,
#     fill="lightblue",
#     outline="black",
#     width=3
# )
# # Right window - square
# canvas.create_rectangle(
#     300, 220, 350, 270,
#     fill="lightblue",
#     outline="black",
#     width=3
# )

# # Door - rectangle
# canvas.create_rectangle(
#     220, 270, 280, 350,
#     fill="brown",
#     outline="black",
#     width=3
# )

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("My House")

canvas = tk.Canvas(root, width=650, height=400, bg="skyblue")
canvas.pack()

# =========================
# MAIN HOUSE
# =========================

# House wall
canvas.create_rectangle(
    120, 180, 380, 350,
    fill="lightyellow",
    outline="black",
    width=3
)

# Roof
canvas.create_polygon(
    100, 180,
    250, 60,
    400, 180,
    fill="red",
    outline="black",
    width=3
)

# Left window
canvas.create_rectangle(
    150, 220, 200, 270,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window
canvas.create_rectangle(
    300, 220, 350, 270,
    fill="lightblue",
    outline="black",
    width=3
)

# Door
canvas.create_rectangle(
    220, 270, 280, 350,
    fill="brown",
    outline="black",
    width=3
)

# =========================
# SMALL DOG HOUSE
# =========================

# Dog house wall
canvas.create_rectangle(
    440, 270, 570, 350,
    fill="burlywood",
    outline="black",
    width=3
)

# Dog house roof
canvas.create_polygon(
    425, 270,
    505, 210,
    585, 270,
    fill="brown",
    outline="black",
    width=3
)

# Dog house entrance
canvas.create_rectangle(
    475, 300, 535, 350,
    fill="black",
    outline="black",
    width=2
)

# Small door opening
canvas.create_arc(
    475, 280, 535, 330,
    start=0,
    extent=180,
    fill="black",
    outline="black"
)
#sun
canvas.create_oval(
    500, 20, 580, 100,
    fill="yellow",
    outline="orange",
    width=3
)

root.mainloop()