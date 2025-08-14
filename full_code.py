from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # Importing Image and ImageTk from pillow to use the images
import os # Importing os to check files

# Global list of cat images
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
        Frame.__init__(self, parent, bg="#D6CCC2") # background colour

        # Configure grid rows and columns to be responsive
        self.grid_rowconfigure(0, weight=0) # Header row - fixed size
        self.grid_rowconfigure(1, weight=1) # First row of cat boxes - stretches
        self.grid_rowconfigure(2, weight=1) # Second row of cat boxes - stretches
        self.grid_rowconfigure(3, weight=0) # Buttons row - fixed size
        self.grid_columnconfigure(0, weight=1) # Columns expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # prevent garbage collection
        self.photos = []

        # Header label for the Adoption page
        header_label = Label(self,
                             text="Our Adoptable Cats",
                             font=("PMingLiU", 16, "bold"),
                             fg="#827268",
                             background="#E3D5CA",
                             height=2)
        header_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky="ew")

        for r in range(2):
                    for c in range(3):
                        rough_box = Frame(self, bg="#E0E0E0", bd=1, relief="solid")
                        rough_box.grid(row=r + 1, column=c, padx=10, pady=7, sticky="nsew")

                        image_label = Label(rough_box,
                                            bg="#C0C0C0",
                                            relief="groove")
                        image_label.pack(pady=5, padx=5, fill="both", expand=True)

                        # Getting the images and info from the global lists
                        cat_index = (r * 3 + c) % len(cat_images)  
                        image_path = cat_images[cat_index]
                        current_cat_info = cat_info[cat_index] # get the cats information! using same for consistancy

                        if os.path.exists(image_path):
                            try:
                                img = Image.open(image_path)
                                target_width = 180
                                target_height = 180

                                img_width, img_height = img.size
                                aspect_ratio = img_width / img_height

                                if target_width / target_height > aspect_ratio:
                                    new_height = target_height
                                    new_width = int(new_height * aspect_ratio)
                                else:
                                    new_width = target_width
                                    new_height = int(new_width / aspect_ratio)

                                img = img.resize((new_width, new_height), Image.LANCZOS)
                                photo = ImageTk.PhotoImage(img)
                                image_label.config(image=photo)
                                self.photos.append(photo)
                            except Exception as e:
                                print(f"loading image error {image_path}: {e}")
                                image_label.config(text=f"Error with image: {os.path.basename(image_path)}", bg="red", fg="white", font=("PMingLiU", 8), wraplength=100)
                        else:
                            image_label.config(text=f"Image cannot be found: {os.path.basename(image_path)}", bg="orange", fg="white", font=("PMingLiU", 8), wraplength=100)

                        # Label for the cat information
                        cat_info_label = Label(rough_box, text=current_cat_info,
                                            bg="#EDEDE9",
                                            font=("PMingLiU", 10, "bold"),
                                            fg="#827268")
                        cat_info_label.pack(expand=True, fill="both", pady=(0,5))

                # Button to go back to the Main page
                    back_button = Button(self, text="Back to Main",
                                    font=("PMingLiU", 14, "bold"),
                                    fg="#827268",
                                    bg="#EDEDE9",
                                    command=lambda: controller.show_frame("MainFrame"))
                    back_button.grid(row=3, column=0, columnspan=1, pady=10, padx=40, sticky="ew")

                # button to go to adoption form page
                    back_button = Button(self, text="Go to adopt!",
                                    font=("PMingLiU", 14, "bold"),
                                    fg="#827268",
                                    bg="#EDEDE9",
                                    command=lambda: controller.show_frame("FormFrame"))
                    back_button.grid(row=3, column=2, columnspan=1, pady=10, padx=40, sticky="ew")

# page which allows users to adopt
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


# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()

