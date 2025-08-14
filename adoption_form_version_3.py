from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json
from tkinter import messagebox
import re

cat_images = [
    "Images/84CBE81C-BEC8-413D-A327-05EFB7649942 (1).png",
    "Images/5151C93C-2D24-4AF0-A0E6-F39A1C21CA34 (1).png",
    "Images/DDD67ACF-E26B-4A63-92D5-18C807769B10 (1).png",
    "Images/IMG_6214 (1).png",
    "Images/6720ef6b-cd92-40ef-9331-74bb931bfb8c - Copy.JPG",
    "Images/6720ef6b-cd92-40ef-9331-74bb931bfb8c.JPG"
]

cat_info = [
    "Comet\n Age: 13 \n Lazy",
    "Bratboy\n Age: 19\n Killer",
    "Sylvester\n Age: 13 \n Goated",
    "Simba\n Age: 10\n Cuddly",
    "Timtam\n Age: 7\n Not all there",
    "Yoyo\n Age: 15\n Senile"
]

cat_names = [
    "Comet",
    "Bratboy",
    "Sylvester",
    "Simba",
    "Timtam",
    "Yoyo",
]

class CatAdoption:
    '''
    Main applications
    '''
    def __init__(self):
        self.root = Tk()
        self.root.title("Adopt A Cat!! :-)")
        self.root.geometry("700x720")

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        # Add each frame to the dictionary
        for F in (FormFrame,):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial frame
        self.show_frame("FormFrame")

        self.bottom_frame = Frame(self.root, bg="#D6CCC2")
        self.bottom_frame.pack(side="bottom", fill="x")

    def show_frame(self, frame_name):
        # shows requested frame
        frame = self.frames[frame_name]
        frame.tkraise()

    def quit_app(self):
        # Method to quit the program
        self.root.destroy()

    def run(self):
        # tkinter loop
        self.root.mainloop()

        
class FormFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#D6CCC2")

        # cHANGING COLUMNS TO ALLOW CENTERING
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        # header and text
        FormHeader_label = Label(self,
                                 text="Adoption Form!",
                                 font=("PMingLiU", 20, "bold"),
                                 fg="#827268",
                                 background="#E3D5CA",
                                 width=30,
                                 height=2)
        FormHeader_label.grid(row=0, column=0, columnspan=3, pady=(20, 0), padx=10, sticky='nsew')

        FormSubHeader_label = Label(self,
                                         text="All Information Kept Private.",
                                         font=("PMingLiU", 8, "bold"),
                                         fg="#827268",
                                         background="#E3D5CA",
                                         width=30,
                                         height=1)
        FormSubHeader_label.grid(row=1, column=0, columnspan=3, pady=0, padx=10, sticky='nsew')

        # starting from row 2
        row_offset = 2

        # Labels ! more centered now
        first_name_label = Label(self,
                                 text="First Name",
                                 font=("PMingLiU", 14, "bold"),
                                 fg="#827268",
                                 background="#E3D5CA",
                                 width=30,
                                 height=1)
        first_name_label.grid(row=0+row_offset, column=0, padx=5, pady=5, sticky='e')

        last_name_label = Label(self,
                                 text="Last Name",
                                 font=("PMingLiU", 14, "bold"),
                                 fg="#827268",
                                 background="#E3D5CA",
                                 width=30,
                                 height=1)
        last_name_label.grid(row=1+row_offset, column=0, padx=5, pady=5, sticky='e')

        age_label = Label(self,
                          text="Age (must be over 18)",
                          font=("PMingLiU", 14, "bold"),
                          fg="#827268",
                          background="#E3D5CA",
                          width=30,
                          height=1)
        age_label.grid(row=2+row_offset, column=0, padx=5, pady=5, sticky='e')

        contact_label = Label(self,
                              text="Contact number",
                              font=("PMingLiU", 14, "bold"),
                              fg="#827268",
                              background="#E3D5CA",
                              width=30,
                              height=1)
        contact_label.grid(row=3+row_offset, column=0, padx=5, pady=5, sticky='e')

        email_label = Label(self,
                            text="Email address",
                            font=("PMingLiU", 14, "bold"),
                            fg="#827268",
                            background="#E3D5CA",
                            width=30,
                            height=1)
        email_label.grid(row=4+row_offset, column=0, padx=5, pady=5, sticky='e')

        name_of_cat_label = Label(self,
                                  text="Name of cat looking to adopt",
                                  font=("PMingLiU", 14, "bold"),
                                  fg="#827268",
                                  background="#E3D5CA",
                                  width=30,
                                  height=1)
        name_of_cat_label.grid(row=5+row_offset, column=0, padx=5, pady=5, sticky='e')

        # Entry boxes
        user_first_name = StringVar()
        first_name_entry = ttk.Entry(self, textvariable=user_first_name, font=('PMingLiU', 14, 'normal'))
        first_name_entry.grid(row=0+row_offset, column=1, padx=5, pady=5, sticky='w')

        user_last_name = StringVar()
        last_name_entry = ttk.Entry(self, textvariable=user_last_name, font=('PMingLiU', 14, 'normal'))
        last_name_entry.grid(row=1+row_offset, column=1, padx=5, pady=5, sticky='w')

        user_age = StringVar()
        age_entry = ttk.Entry(self, textvariable=user_age, font=('PMingLiU', 14, 'normal'))
        age_entry.grid(row=2+row_offset, column=1, padx=5, pady=5, sticky='w')

        user_contact = StringVar()
        contact_entry = ttk.Entry(self, textvariable=user_contact, font=('PMingLiU', 14, 'normal'))
        contact_entry.grid(row=3+row_offset, column=1, padx=5, pady=5, sticky='w')

        user_email = StringVar()
        email_entry = ttk.Entry(self, textvariable=user_email, font=('PMingLiU', 14, 'normal'))
        email_entry.grid(row=4+row_offset, column=1, padx=5, pady=5, sticky='w')

        # Combo box
        chosen_cat = StringVar()
        chosen_cat.set("")
        cat_combobox = ttk.Combobox(self, textvariable=chosen_cat, state="readonly", font=('PMingLiU', 14, 'normal'))
        cat_combobox['values'] = cat_names
        cat_combobox.grid(row=5+row_offset, column=1, padx=5, pady=5, sticky='w')

        def save_to_file():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            age_str = age_entry.get()
            contact_str = contact_entry.get()

            # Validation checks
            # checking if first name entry is all letters
            if not re.fullmatch(r'[a-zA-Z]+', first_name):
                name_error = "First and last name must only contain letters."
                messagebox.showerror("Error", name_error)
                return

            # checking if last name entry is all letters
            if not re.fullmatch(r'[a-zA-Z]+', last_name):
                name_error = "First and last name must only contain letters."
                messagebox.showerror("Error", name_error)
                return

            # checking if age entry is all numbers
            if not age_str.isdigit():
                number_error = "Age and contact must only contain numbers."
                messagebox.showerror("error", number_error)
                return

            # checking if age entry is 18 or over
            age = int(age_str)
            if age < 18:
                age_error = "Legally, you must be over 18 to adopt an animal."
                messagebox.showerror("Age error")
                return

            # checking if contact entry is all numbers
            if not contact_str.isdigit():
                number_error = "Age and contact must only contain numbers"
                messagebox.showerror("error", number_error)
                return

            # if all entries pass validation save to json
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "contact": contact_str,
                "email": email_entry.get(),
                "cat": chosen_cat.get()
            }

            with open('user_info.json', 'a') as f:
                json.dump(data, f, indent=4)
            
            messagebox.showinfo("Save Successful!! Meow")

        # Button to save to json file
        save_button = Button(self, text="Save",
                              font=("PMingLiU", 14, "bold"),
                              fg="#827268",
                              bg="#EDEDE9",
                              command=save_to_file)
        save_button.grid(row=8, column=0, columnspan=3, pady=(20, 0), padx=50, sticky='nsew')

        # Button to go back to the Main page 
        back_button = Button(self, text="Menu",
                              font=("PMingLiU", 14, "bold"),
                              fg="#827268",
                              bg="#EDEDE9",
                              command=lambda: controller.show_frame("MainFrame"))
        back_button.grid(row=9, column=0, columnspan=1, pady=100, padx=40, sticky="ew")
        
        # button to go back to adoption page
        back_button = Button(self, text="Go back to cats!",
                              font=("PMingLiU", 14, "bold"),
                              fg="#827268",
                              bg="#EDEDE9",
                              command=lambda: controller.show_frame("AdoptionFrame"))
        back_button.grid(row=9, column=1, columnspan=4, pady=100, padx=(0, 40), sticky="ew")

# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()