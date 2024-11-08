import tkinter as tk
from tkinter import ttk, Canvas, PhotoImage, Entry
import customtkinter as ctk
from pathlib import Path
from PIL import Image, ImageTk
from PIL.XbmImagePlugin import xbm_head


def strech_image(event):
    global resized_tk
    # Size Change
    width = event.width
    height = event.height

    # Image Creation
    resized_image = image_original.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=resized_tk, anchor='nw')

  # Introduction | Need a sign-in here

window = tk.Tk()
window.title("Sign In")
window.geometry('1280x720')
window.configure(bg = "#220C49")
window.resizable(True, True)
# Main Page
leftimage = Image.open('image_1.png').resize((640,720))
leftimage_in_tk = ImageTk.PhotoImage(leftimage)



#label = ttk.Label(window, text = 'Sign in', image = leftimage_in_tk)
#label.pack()

canvas = tk.Canvas(window, bg = "#220C49", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    300.0,
    image=image_image_1
)
canvas.create_text(
    290.0,
    0.0,
    anchor="nw",
    text="M\nE\nD\nU",
    fill="#FFFFFF",
    font=("Livvic Regular", 124 * -1)
)
canvas.create_text(
    775.0,
    22.0,
    anchor="nw",
    text="Welcome!",
    fill="#FFFFFF",
    font=("Livvic Regular", 96 * -1)
)

entry_image_2 = PhotoImage(
    file=("entry_2.png"))
entry_bg_2 = canvas.create_image(
    990.0,
    270.5,
    image=entry_image_2
)
entry_image_1 = PhotoImage(
    file=("entry_2.png"))
entry_bg_1 = canvas.create_image(
    990.0,
    400.5,
    image=entry_image_2
)
entry_1 = Entry(
    font = ("Livvic Regular", 24),
    fg = 'white',
    bd=0,
    bg="#3C2B58",
    highlightthickness=0
)
entry_1.place(
    x=760.0,
    y=240.0,
    width=450,
    height=55.0
)
canvas.create_text(
    750.0,
    325.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Livvic Regular", 32 * -1)
)
canvas.create_text(
    750.0,
    190.0,
    anchor="nw",
    text="Email:",
    fill="#FFFFFF",
    font=("Livvic Regular", 32 * -1)
)
entry_2 = Entry(
    font = ("Livvic Regular", 24), show = '•',
    fg = 'white',
    bd=0,
    bg="#3C2B58",
    highlightthickness=0
)
entry_2.place(
    x=760.0,
    y=368.0,
    width=450,
    height=55.0
)
forgotpass = tk.Button(
    text = "Forgot your password?",
    font = ('Livvic Regular', 16),
    fg = 'white',
    bd = 0,
    cursor = 'hand2',
    highlightthickness = 0,
    background = '#220C49'
)
forgotpass.place(
    x = 875,
    y = 432
)
submit_image = PhotoImage(
    file = ('button_2.png'))

submitbutton = tk.Button(
    #text = 'Sign In',
    #font = ('Livvic Regular', 25, 'bold'),
    image = submit_image,
    bd = 0,
    fg = 'white',
    cursor = 'hand2',
    highlightthickness = 0,
    background = '#220C49'
)
submitbutton.place(
    x = 886,
    y = 550
)

notwithus = tk.Button(
    text='Not with us?\nClick here',
    font=('Livvic Regular', 14),
    bd=0,
    fg='white',
    cursor='hand2',
    highlightthickness=0,
    background = '#220C49'
)
notwithus.place(
    x = 922,
    y = 635
)

# Running the window
window.mainloop()
  # Functions Page for IEP's, Writing, and other functions


  # IEP's Page


  # Writing Page


  # Data Organization


  # Problem Creator