from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # Importing Image and ImageTk from pillow to use the images
import os # Importing os to check files

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
        # Adjusted geometry to better accommodate the grid of cat images
        self.root.geometry("700x720")

        self.root.resizable(False, False)

        # Container for all frames - this will hold your MainFrame and other content frames
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

        FormHeader_label = Label(self,
                      text="Adoption Form!",
                      font=("PMingLiU", 20, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=2)
        FormHeader_label.pack(pady=(20, 0), fill='x', padx=10)

        FormSubHeader_label = Label(self,
                      text="All Information Kept Private.",
                      font=("PMingLiU", 8, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        FormSubHeader_label.pack(pady=0, fill='x', padx=10)

        # Labels
        first_name_label = Label(self,
                      text="First Name",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        first_name_label.pack()

        last_name_label = Label(self,
                      text="Last Name",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        last_name_label.pack()

        age_label = Label(self,
                      text="Age",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        age_label.pack()

        contact_label = Label(self,
                      text="Contact number",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        contact_label.pack()

        email_label = Label(self,
                      text="Email address",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        email_label.pack()

        name_of_cat_label = Label(self,
                      text="Name of cat looking to adopt",
                      font=("PMingLiU", 14, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=1)
        name_of_cat_label.pack()

        # Entry boxes
        user_first_name=StringVar()
        first_name_entry=ttk.Entry(self, textvariable = user_first_name, font = ('PMingLiU',14,'normal'))
        first_name_entry.pack()

        user_last_name=StringVar()
        last_name_entry=ttk.Entry(self, textvariable = user_last_name, font = ('PMingLiU',14,'normal'))
        last_name_label.pack()

        user_age=IntVar()
        age_entry=ttk.Entry(self, textvariable = user_age, font = ('PMingLiU',14,'normal'))
        age_entry.pack()


        user_contact=IntVar()
        contact_entry=ttk.Entry(self, textvariable = user_contact, font = ('PMingLiU',14,'normal'))
        contact_entry.pack()

        user_email=StringVar()
        email_entry=ttk.Entry(self, textvariable = user_email, font = ('PMingLiU',14,'normal'))
        email_entry.pack()

        #combo box
        chosen_cat=StringVar()
        chosen_cat.set("")
        cat_combobox = ttk.Combobox(self, textvariable=chosen_cat, state="readonly", font= ('PMingLiU', 14, 'normal'))
        cat_combobox['values'] = cat_names
        cat_combobox.pack()

        # grid!
        first_name_label.grid(row=0, column=0)
        first_name_entry.grid(row=0, column=1)
        last_name_label.grid(row=1, column=0)
        last_name_entry.grid(row=1, column=1)
        age_label.grid(row=2, column=0)
        age_entry.grid(row=2, column=1)
        contact_label.grid(row=3, column=0)
        contact_entry.grid(row=3, column=1)
        email_label.grid(row=4, column=0)
        email_entry.grid(row=4, column=1)
        name_of_cat_label.grid(row=5, column=0)
        cat_combobox.grid(row=5, column=1)




# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()
