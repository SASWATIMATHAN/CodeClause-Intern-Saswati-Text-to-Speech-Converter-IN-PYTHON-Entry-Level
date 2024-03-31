import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyttsx3

def text_to_speech():
    text = text_entry.get()
    voice = voice_var.get()
    
    engine = pyttsx3.init()
    
    # Set the voice
    voices = engine.getProperty('voices')
    if voice == "Male":
        engine.setProperty('voice', voices[1].id)  # Select male voice
    elif voice == "Female":
        engine.setProperty('voice', voices[0].id)  # Select female voice
    
    engine.say(text)
    engine.runAndWait()

def show_notification():
    messagebox.showinfo("Notification", "Text converted to speech successfully!")

root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create a label
label = ttk.Label(root, text="Enter text to convert to speech:")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry field
text_entry = ttk.Entry(root, width=40)
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label for voice selection
voice_label = ttk.Label(root, text="Select voice:")
voice_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Create a Combobox for voice selection
voice_var = tk.StringVar()
voice_combobox = ttk.Combobox(root, width=15, textvariable=voice_var, state="readonly")
voice_combobox['values'] = ("Male", "Female")
voice_combobox.current(0)  # Set default value to Male
voice_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Create a button for converting text to speech
convert_button = ttk.Button(root, text="Convert to Speech", command=text_to_speech)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a button for showing notification
notification_button = ttk.Button(root, text="Show Notification", command=show_notification)
notification_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Add a logo (change path to your logo file)
logo = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo)
logo_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
