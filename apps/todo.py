import tkinter as tk
from tkinter import PhotoImage
class todo(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('TO DO LIST')
        self.geometry('650x410+300+150')
        self.configure(bg="#d0bfff")
        self.resizable(False, False)
        self.icon = PhotoImage(file="images/icon/list.png")
        self.iconphoto(False, self.icon)
        # "To Do List" Title
        self.label = tk.Label(self, text='To Do List',
            font=("Acme", 30), width=10,bd=0.5,bg='#5c67a6', fg='#FCFDF2')
        self.label.pack(side='top', fill=tk.BOTH)
        # All tasks
        self.main_text = tk.Listbox(self, height=4, bd=0.5, width=31, font=("Friendly", 25, "bold"), justify="center")
        self.main_text.place(x=14, y=180)
        # Adding task label
        self.text = tk.Text(self, bd=0.5, height=1, width=30, font=("Friendly", 25, "bold"))
        self.text.place(x=23, y=60)
        
        def add():
            """ Add contents by append text from Add Text label """
            content = self.text.get(1.0, tk.END) #get text from user
            self.main_text.insert(tk.END, content) #append task in list
            # add content in .txt file
            with open('data.txt', 'a') as file:
                # write in file
                file.write(content)
                # change the position of the File Handle to a given specific position
                file.seek(0)
                # closes the opened file
                file.close()
            self.text.delete(1.0, tk.END)
        
        def delete():
            """ delete selection text """
            delete_ = self.main_text.curselection() # display the selected item
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                # resizes the file.
                f.truncate()
            self.main_text.delete(delete_)
        with open('data.txt', 'r') as file: # open file data
            # readlines -> returns one line from the file ans then get in value.
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(-1, ready)
                file.close()

        # Add button
        self.button = tk.Button(self, text="Add", font=("Acme", 19),
                    width=8,bd=0.5, bg='#40c057',fg='#FBFACD', command=add) #command use to call function
        # Add button position
        self.button.place(x=90, y=122)
        # Delete button
        self.button2 = tk.Button(self, text='Delete', font=("Acme", 19),
                    width=8,bd=0.5, bg='#e64980', fg='#FBFACD', command=delete)
        # Delete button position
        self.button2.place(x=420, y=122)

def main():
    root = todo()
    root.mainloop()
