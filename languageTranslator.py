from tkinter import *
from tkinter import ttk
from translate import Translator

# Function to handle the translation
def translate_text():
    source_lang = source_lang_combobox.get().lower()
    target_lang = target_lang_combobox.get().lower()
    text_to_translate = source_text.get("1.0", END).strip()
    
    if text_to_translate:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text_to_translate)
        target_text.delete("1.0", END)
        target_text.insert("1.0", translation)
    else:
        target_text.delete("1.0", END)
        target_text.insert("1.0", "Please enter some text to translate.")

# Main window
root = Tk()
root.title("Translator")
root.config(bg="yellow")

# Source Text Label and Text Box
source_text_label = Label(root, text="Provide your Text below", font=("Helvetica", 16), bg="red", fg="white")
source_text_label.pack(fill=X, padx=10, pady=5)

source_text = Text(root, height=8, width=40, font=("Helvetica", 14))
source_text.pack(padx=10, pady=5)

# Language Selection Comboboxes and Translate Button
language_frame = Frame(root, bg="yellow")
language_frame.pack(fill=X, padx=10, pady=5)

# Combobox for source language selection
source_lang_combobox = ttk.Combobox(language_frame, values=["English", "Spanish", "French", "German", "Bengali"], state="readonly", width=10)
source_lang_combobox.set("English")  # default value
source_lang_combobox.pack(side=LEFT, padx=5)

# Translate button
translate_button = Button(language_frame, text="Translate", command=translate_text, bg="black", fg="white", width=10)
translate_button.pack(side=LEFT, padx=5)

# Combobox for target language selection
target_lang_combobox = ttk.Combobox(language_frame, values=["Hindi", "Spanish", "French", "German", "Bengali"], state="readonly", width=10)
target_lang_combobox.set("Hindi")  # default value
target_lang_combobox.pack(side=LEFT, padx=5)

# Target Text Label and Text Box
target_text_label = Label(root, text="Translated Text", font=("Helvetica", 16), bg="red", fg="white")
target_text_label.pack(fill=X, padx=10, pady=5)

target_text = Text(root, height=8, width=40, font=("Helvetica", 14))
target_text.pack(padx=10, pady=5)

# Run the application
root.mainloop()
