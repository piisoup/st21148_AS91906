'''
    Cat adoption program!
    Made by: Daisy Chamberlain

    V1 = fully functional code, no extensive work on aesthetics
    V2= work on aesthetics with formframe, changed adoptionframe using grids
'''

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # Importing Image and ImageTk from pillow to use the images
import os # Importing os to check files
import json # to write to files
from tkinter import messagebox # for the popups


# Global lists
cat_images = [
    "Images/comet.png",
    "Images/Bratboy.png",
    "Images/Sylvester.png",
    "Images/Simba(1).png",
    "Images/Timtam.JPG",
    "Images/Yoyo.JPG"
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

# class holding all the main stuff
class CatAdoption:
    '''
    Main applications
    '''
    def __init__(self):
        self.root = Tk()
        self.root.title("Adopt A Cat!! :-)")
        self.root.geometry("700x720")

        self.root.resizable(False, False)

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        for F in (MainFrame, AdoptionFrame, FormFrame,):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial frame
        self.show_frame("MainFrame")

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

class MainFrame(Frame):
    # main menu with navigation
    def __init__(self, parent, controller):
        # Set the background color for the MainFrame
        Frame.__init__(self, parent,
                       bg="#D6CCC2")

        style = ttk.Style()
        style.configure("My.TLabel",
                        background="#D6CCC2",
                        font=("PMingLiU", 16, "bold"))

        label = Label(self,
                      text="Find your purrfect match! \n Adopt a cat today!",
                      font=("PMingLiU", 16, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=5)
        label.pack(pady=20, fill='x', padx=10)

        # Button to go to Adoption page
        to_adopt_button = Button(self, text="Go", bg="#EDEDE9",
                                  font=("PMingLiU", 16, "bold"),
                                  fg="#827268",
                                  width=15,
                                  height=2,
                                  command=lambda: controller.show_frame("AdoptionFrame"))
        to_adopt_button.pack(pady=(85, 10), fill='x', padx=40)

        # moved quit button to MainFrame as it's part of the homepage layout
        button_quit = Button(self, text="Exit",
                                  font=("PMingLiU", 14, "bold"),
                                  fg="#827268",
                                  width=15,
                                  height=1,
                                  command=controller.quit_app)
        button_quit.pack(padx=40, fill='x', pady=(0, 10))

# Page which shows cats for adoption
class AdoptionFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#D6CCC2") 

        self.grid_rowconfigure(0, weight=0) 
        self.grid_rowconfigure(1, weight=1) 
        self.grid_rowconfigure(2, weight=1) 
        self.grid_rowconfigure(3, weight=0) 
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.photos = []

        header_label = Label(self,
                             text="Our Adoptable Cats",
                             font=("PMingLiU", 16, "bold"),
                             fg="#827268",
                             background="#E3D5CA",
                             height=2)
        header_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky="ew")

        # placing all the boxes manually !!

        # Cat 1 row 1, column 0
        self.create_cat_box(row=1, col=0, index=0)

        # Cat 2 row 1, column 1
        self.create_cat_box(row=1, col=1, index=1)

        # Cat 3 row 1, column 2
        self.create_cat_box(row=1, col=2, index=2)

        # Cat 4 row 2, column 0
        self.create_cat_box(row=2, col=0, index=3)

        # Cat 5 row 2, column 1
        self.create_cat_box(row=2, col=1, index=4)

        # Cat 6 row 2, column 2
        self.create_cat_box(row=2, col=2, index=5)

        # button to go back to main
        back_button = Button(self, text="Menu",
                             font=("PMingLiU", 14, "bold"),
                             fg="#827268",
                             bg="#EDEDE9",
                             command=lambda: controller.show_frame("MainFrame"))
        back_button.grid(row=3, column=0, columnspan=1, pady=10, padx=40, sticky="ew")

        # go to adoption form 
        back_button = Button(self, text="Go to adopt!",
                             font=("PMingLiU", 14, "bold"),
                             fg="#827268",
                             bg="#EDEDE9",
                             command=lambda: controller.show_frame("FormFrame"))
        back_button.grid(row=3, column=2, columnspan=1, pady=10, padx=40, sticky="ew")

    # creating the boxes for the cats
    def create_cat_box(self, row, col, index):
        rough_box = Frame(self, bg="#E0E0E0", bd=1, relief="solid")
        rough_box.grid(row=row, column=col, padx=10, pady=7, sticky="nsew")

        image_label = Label(rough_box,
                            bg="#C0C0C0",
                            relief="groove")
        image_label.pack(pady=5, padx=5, fill="both", expand=True)

        # putting the dictionaries into a variable
        image_path = cat_images[index]
        current_cat_info = cat_info[index]

        if os.path.exists(image_path):
            try:
                # opening image and changing width
                img = Image.open(image_path)
                target_width = 180
                target_height = 180
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height

                # checks if the target box is wider then the originals image aspect ratio
                if target_width / target_height > aspect_ratio:
                    new_height = target_height
                    new_width = int(new_height * aspect_ratio)

                # if false then box is taller! and changes
                else:
                    new_width = target_width
                    new_height = int(new_width / aspect_ratio)

                # use lanczos as it is a better way to downscale images - keeps quality
                img = img.resize((new_width, new_height), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                self.photos.append(photo)
            except Exception as e:
                # if image is not loading will show LOADING error
                image_label.config(text=f"loading image error {os.path.basename(image_path)}: {e}", bg="red", fg="white", font=("PMingLiU", 8), wraplength=100)
        else:
            # if image file cannot be found, will show orange box and let users know
            image_label.config(text=f"Image cannot be found: {os.path.basename(image_path)}", bg="orange", fg="white", font=("PMingLiU", 8), wraplength=100)

        cat_info_label = Label(rough_box, text=current_cat_info,
                               bg="#EDEDE9",
                               font=("PMingLiU", 10, "bold"),
                               fg="#827268")
        cat_info_label.pack(expand=True, fill="both", pady=(0, 5))

# frame to adopt cats
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
                          text="Age",
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

        user_age = IntVar()
        age_entry = ttk.Entry(self, textvariable=user_age, font=('PMingLiU', 14, 'normal'))
        age_entry.grid(row=2+row_offset, column=1, padx=5, pady=5, sticky='w')

        user_contact = IntVar()
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
            # writing to json file :O
            data = {
            "first_name": first_name_entry.get(),
            "last_name": last_name_entry.get(),
            "age": age_entry.get(),
            "contact": contact_entry.get(),
            "email": email_entry.get(),
            "cat": chosen_cat.get()
            }

            with open('user_info.json', 'w') as f:
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