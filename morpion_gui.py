# from tkinter import *
# from tkinter import ttk
#
#
# def on_click(px, py):
#     print("Clic gauche sur le bouton (", px, ", ", py, ")")
#     nbtn = Button(frame, command=lambda x=px, y=py: on_click(x, y), state=DISABLED, bg='blue')
#     nbtn.grid(row=px, column=py, sticky=N + S + E + W)
#
#
# # Create & Configure windows
# windows = Tk()
# windows.title("Jeu de morpion")
# windows.geometry('250x250')
# windows.resizable(True, True)
#
# nb_colonne = 3
# nb_ligne = 3
#
# Grid.rowconfigure(windows, 0, weight=1)
# Grid.columnconfigure(windows, 0, weight=1)
#
# # Create & Configure frame
# frame = Frame(windows)
# frame.grid(row=0, column=0, sticky=N + S + E + W)
#
# # Create a 5x10 (rows x columns) grid of buttons inside the frame
# for row_index in range(nb_ligne):
#     Grid.rowconfigure(frame, row_index, weight=1)
#     for col_index in range(nb_colonne):
#         Grid.columnconfigure(frame, col_index, weight=1)
#         # btn = Button(frame, command=lambda pos=case:on_click(pos[0], pos[1]))  # create a button inside frame
#         btn = Button(frame, command=lambda x=row_index, y=col_index: on_click(x, y))  # create a button inside frame
#         btn.grid(row=row_index, column=col_index, sticky=N + S + E + W)
#
# windows.mainloop()

# import tkinter as Tk
#
# def AfficheLabel(txt):
#     label.config(text = txt)
#
# root = Tk.Tk()
# label = Tk.Label(root, text = "Clic sur le bouton ")
# label.grid(row = 0, column = 0, columnspan = 3)
# svEntry = Tk.StringVar()
# edit = Tk.Entry(root, textvariable = svEntry)
# edit.grid(row = 1, columnspan = 3)
# btn1 = Tk.Button(root, text = "Button1", command = lambda x=1:AfficheLabel("Clic sur le bouton "+str(x)))
# btn2 = Tk.Button(root, text = "Button2", command = lambda x=2:AfficheLabel("Clic sur le bouton "+str(x)))
# btn3 = Tk.Button(root, text = "Button3", command = lambda x=svEntry:AfficheLabel("valeur de l'entry: "+x.get()))
# btn1.grid(row = 2, column = 0)
# btn2.grid(row = 2, column = 1)
# btn3.grid(row = 2, column = 2)
#
# root.mainloop()



from tkinter import *

canvas = Canvas(width=300, height=300)
canvas.pack(expand=YES, fill=BOTH)
canvas.
canvas.create_oval(10, 10, 200AAAA, 200)

mainloop()
