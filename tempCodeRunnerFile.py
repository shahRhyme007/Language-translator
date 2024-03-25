from tkinter import *
from tkinter import ttk
from translate import Translator

def translateLang(text="type", src="english", dest="hindi"):
    translator = Translator(from_lang=src, to_lang=dest)
    translation = translator.translate(text)
    return translation

def dataVal():
    src_lang = combx_src.get().lower()  # Source language
    dest_lang = combx_dest.get().lower()  # Destination language
    msg = source_txt.get(1.0, END).strip()  # Text to translate
    if msg:
        translated_text = translateLang(text=msg, src=src_lang, dest=dest_lang)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated_text)
    else:
        dest_txt.insert(END, "Please enter text to translate.")

root = Tk()
root.title("Language Translator")
root.geometry("500x700")
root.config(bg="yellow")

# Create a header label
lab_txt = Label(root, text="Translator", font=("Time New Roman", 20, "bold"), bg="white")
lab_txt.pack(pady=20)

# Create a text box for input
source_txt = Text(root, font=("Time New Roman", 20, "bold"), wrap=WORD, height=5, width=40)
source_txt.pack(pady=10)

# Create a frame to hold the comboboxes and translate button
frame = Frame(root, bg="yellow")
frame.pack(pady=10)

# Create combobox for source language selection
combx_src = ttk.Combobox(frame, values=["English", "Spanish", "German", "French", "Bangla"], font=("Time New Roman", 14), state="readonly")
combx_src.pack(side=LEFT, padx=10)
combx_src.set("English")

# Create a translate button
button_change = Button(frame, text="Translate", font=("Time New Roman", 14), relief=RAISED, command=dataVal)
button_change.pack(side=LEFT, padx=10)

# Create combobox for destination language selection
combx_dest = ttk.Combobox(frame, values=["Hindi", "Spanish", "German", "French", "Bangla"], font=("Time New Roman", 14), state="readonly")
combx_dest.pack(side=LEFT, padx=10)
combx_dest.set("Hindi")

# Create a text box for output
dest_txt = Text(root, font=("Time New Roman", 20, "bold"), wrap=WORD, height=5, width=40)
dest_txt.pack(pady=10)

root.mainloop()
