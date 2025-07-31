from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # Importing Image and ImageTk from pillow to use the images
import os # Importing os to check files

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

# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()
