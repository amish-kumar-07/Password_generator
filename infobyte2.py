import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    password = ""
    
    if complexity == "Low":
        chars = string.ascii_letters
    elif complexity == "Medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    

root = tk.Tk()
root.title("Password Generator")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

length_label = tk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, pady=5, sticky=tk.W)

length_entry = tk.Entry(main_frame, width=20)
length_entry.grid(row=0, column=1, pady=5)

complexity_label = tk.Label(main_frame, text="Complexity:")
complexity_label.grid(row=1, column=0, pady=5, sticky=tk.W)

complexity_var = tk.StringVar()
complexity_var.set("Low")

low_button = tk.Radiobutton(main_frame, text="Low", variable=complexity_var, value="Low")
low_button.grid(row=1, column=1, sticky=tk.W)

medium_button = tk.Radiobutton(main_frame, text="Medium", variable=complexity_var, value="Medium")
medium_button.grid(row=2, column=1, sticky=tk.W)

high_button = tk.Radiobutton(main_frame, text="High", variable=complexity_var, value="High")
high_button.grid(row=3, column=1, sticky=tk.W)


generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password, width=20)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

copy_button = tk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, width=20)
copy_button.grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(main_frame, width=30, font=('Arial', 12, 'bold'))
password_entry.grid(row=6, column=0, columnspan=2, pady=10)

root.option_add('*Font', 'Arial 12')
root.option_add('*Button.Background', '#4CAF50')
root.option_add('*Button.Foreground', 'white')
root.option_add('*Button.Font', 'Arial 12 bold')
root.option_add('*Label.Font', 'Arial 12')
root.option_add('*Entry.Font', 'Arial 12')

root.mainloop()
