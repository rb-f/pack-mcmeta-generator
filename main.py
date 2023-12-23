import tkinter as tk
import tkinter.messagebox as messages
import sys
import json

name = ""
form = tk.Tk()
form.wm_title("pack.mcmeta generator")

def generatepackmcmeta():
    name = desc.get()
    try:
        output.insert(0.0, json.JSONEncoder().encode({"pack": {"pack_format": int(ver.get()), "description": name}}))
    except:
        messages.showerror("Error", "Error: " + str(sys.exception()))

def about():
    messages.showinfo("About this app", "This is a simple Python script that uses Tkinter to generate pack.mcmeta files. Could be useful for pack-maker beginners.\n\nSee rb-f on GitHub!")

def helps():
    messages.showinfo("Help", "Welcome to pack.mcmeta generator!\n\nThis allows you to generate a pack.mcmeta file in less than a minute. To use:\n\nDescription: Enter the description of the pack. Could be anything.\nPack format: Enter a number for a pack format. See \"List of pack formats...\" for more information.\n\nThen press \"Generate pack.mcmeta\" to generate it. Then, voila! You have a pack.mcmeta. Press the box, then press Ctrl+A on the box, copy the output from the box by pressing Ctrl+C then paste it into a pack.mcmeta file.\n\nAnd that's it.")

def verhelp():
    messages.showinfo("List of pack formats", "1.20.3 - 1.20.4: 22\n1.20.2: 18\n1.20 - 1.20.1: 15\n1.19.4: 13\n\nFor more info, go to https://minecraft.fandom.com/wiki/Resource_pack")

menu = tk.Menu(form)

appmenu = tk.Menu(menu, tearoff=0)
appmenu.add_command(label="Quit", command=form.destroy)
menu.add_cascade(label="App", menu=appmenu)

helpmenu = tk.Menu(menu, tearoff=0)
helpmenu.add_command(label="Help...", command=helps)
helpmenu.add_command(label="List of pack formats...", command=verhelp)
helpmenu.add_separator()
helpmenu.add_command(label="About this app...", command=about)
menu.add_cascade(label="Help", menu=helpmenu)

form.config(menu=menu)

frames = tk.LabelFrame(form, borderwidth=2,relief="ridge",text="Input")
frames.pack()

desclabel = tk.Label(frames, text="Pack Description:")
desclabel.pack()

desc = tk.Entry(frames, width=50)
desc.pack()

verlabel = tk.Label(frames, text="Pack Format:")
verlabel.pack()

ver = tk.Entry(frames, width=5, justify="center")
ver.pack()

submit = tk.Button(frames,text="Generate pack.mcmeta",command=generatepackmcmeta)
submit.pack()

outputframe = tk.LabelFrame(form, borderwidth=2,relief="ridge",text="Output (copy & paste)")
outputframe.pack()

output = tk.Text(outputframe, width=60, height=10)
output.pack()

tk.mainloop()