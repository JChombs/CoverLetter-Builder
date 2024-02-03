import subprocess
import tkinter as tk
from config import API, COVERLETTERS, JOBDESCRIPTION, WORKEXPERIENCE, EDUCATION

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x700")
        self.root.title("Model Main Menu")
        
        self.destroyed = False
        
        self.label = tk.Label(self.root, text="Cover Letter Builder", font=("Calibri", 40))
        self.label.pack()
        self.Explain = tk.Label(self.root, text="Welcome to the cover letter builder\n", font=("Calibri", 20))
        self.Explain.pack()
        self.Explain2 = tk.Label(self.root, text="Please choose between the two options:\n build a cover letter or edit your information for the model", font=("Calibri", 20))
        self.Explain2.pack()
        self.RunModel = tk.Button(self.root, text='Write a Cover Letter', pady=180, padx=73, font=('Calibri', 20),
                                    command=lambda: self.destroy_and_run(runMenu), fg='white', bg='blue')
        self.RunModel.place(x=420, y=300)

        self.EditEducation = tk.Button(self.root, text='Edit your information', pady=180, padx=73, font=('Calibri', 20),
                                    command=lambda: self.destroy_and_run(RunEdit), fg='white', bg='blue')
        self.EditEducation.place(x=0, y=300)

        self.root.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.root.destroy()
            func()

class EditMenu:
    def __init__(self):
        self.Aroot = tk.Tk()
        self.Aroot.geometry("500x500")
        self.Aroot.title("Model Edit Menu")

        self.destroyed = False
        
        self.label = tk.Label(self.Aroot, text="What Would You Like to Edit?", font=("Calibri", 25))
        self.label.pack()

        self.RunModel = tk.Button(self.Aroot, text='Edit Work Experience', pady=20, padx=71, font=('Calibri', 15),
                                    command=lambda: '', fg='white', bg='blue')
        self.RunModel.place(x=90, y=150)

        self.EditEducation = tk.Button(self.Aroot, text='Edit Education', pady=20, padx=80, font=('Calibri', 15),
                                    command=lambda: '', fg='white', bg='blue')
        self.EditEducation.place(x=110, y=270)

        self.BackButton = tk.Button(self.Aroot, text='Go Back', pady=20, padx=71, font=('Calibri', 15),
                                    command=lambda: self.destroy_and_run(runMain), fg='white', bg='red')
        self.BackButton.place(x=140, y=380)

        self.Aroot.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.Aroot.destroy()
            func()

class RunMenu:
    def __init__(self):
        self.Broot = tk.Tk()
        self.Broot.geometry("800x700")
        self.Broot.title("Run Model")

        self.destroyed = False
        
        self.label = tk.Label(self.Broot, text="Build Cover Letter", font=("Calibri", 40))
        self.label.pack()

        self.RunModelLabel = tk.Label(self.Broot, text='Enter Word Document Name: ', font=('Calibri', 15))
        self.RunModelLabel.place(x=80, y=100)
        self.docxentry = tk.Entry(self.Broot, font=("Callabri",16))
        self.docxentry.place(x=350, y=100)

        self.RunModelLabel = tk.Label(self.Broot, text='Enter Job Description Here: ', font=('Calibri', 15))
        self.RunModelLabel.place(x=280, y=150)
        self.InfoEnter = tk.Text(self.Broot, height=30, width=70)
        self.InfoEnter.place(x=280, y=170)

        self.BackButton = tk.Button(self.Broot, text='Go Back', pady=20, padx=71, font=('Calibri', 15),
                                    command=lambda: self.destroy_and_run(runMain), fg='white', bg='red')
        self.BackButton.place(x=300, y=570)

        self.Broot.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.Broot.destroy()
            func()

def runMain():
    MainMenu()

def RunEdit():
    EditMenu()

def runMenu():
    RunMenu()

def Start():
    runMain()

Start()