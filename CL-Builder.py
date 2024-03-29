import subprocess
import tkinter as tk
from tkinter import messagebox
from config import API, COVERLETTERS, JOBDESCRIPTION, WORKEXPERIENCE, EDUCATION, MODEL

wrok = WORKEXPERIENCE
jobe = EDUCATION
descript = JOBDESCRIPTION
mdoel = MODEL

### WORK IN PROGRESS

class MainMenu():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x820")
        self.root.title("Model Main Menu")
        
        self.destroyed = False
        
        self.label = tk.Label(self.root, text="Cover Letter Builder", font=("Calibri", 40))
        self.label.pack()
        self.Explain = tk.Label(self.root, text="Welcome to the cover letter builder\n", font=("Calibri", 20))
        self.Explain.pack()
        self.Explain2 = tk.Label(self.root, text="Please choose between the two options:\n build a cover letter or edit your information for the model", font=("Calibri", 20))
        self.Explain2.pack()
        self.RunModel = tk.Button(self.root, text='Write a Cover Letter', pady=180, padx=70, font=('Calibri', 20),
                                    command=lambda: self.destroy_and_run(runMenu), fg='white', bg='blue')
        self.RunModel.place(x=420, y=300)

        self.EditEducation = tk.Button(self.root, text='Edit your information', pady=180, padx=70, font=('Calibri', 20),
                                    command=lambda: self.destroy_and_run(RunEdit), fg='white', bg='blue')
        self.EditEducation.place(x=2, y=300)
        
        self.Disclaimer = tk.Label(self.root, text="DISCLAIMER: This is an AI model, they are not always accurrate\n Please check and review its work", font=("Calibri", 11))
        self.Disclaimer.place(x=0, y=750)

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
                                  command=lambda: self.destroy_and_run(editWork), fg='white', bg='blue')
        self.RunModel.place(x=90, y=150)

        self.EditEducation = tk.Button(self.Aroot, text='Edit Education', pady=20, padx=80, font=('Calibri', 15),
                                       command=lambda: self.destroy_and_run(editEducation), fg='white', bg='blue')
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
        self.Broot.geometry("750x850")
        self.Broot.title("Run Model")

        self.destroyed = False
        
        self.label = tk.Label(self.Broot, text="Build Cover Letter", font=("Calibri", 40))
        self.label.pack()

        self.RunModelLabel = tk.Label(self.Broot, text='Enter Word Document Name: ', font=('Calibri', 15))
        self.RunModelLabel.place(x=80, y=100)
        self.docxentry = tk.Entry(self.Broot, font=("Callabri",16))
        self.docxentry.place(x=350, y=100)

        self.RunModelLabel = tk.Label(self.Broot, text='Enter Job Description Here: ', font=('Calibri', 15))
        self.RunModelLabel.place(x=70, y=150)
        self.InfoEnter = tk.Text(self.Broot, height=30, width=80)
        self.InfoEnter.place(x=78, y=180)

        self.BackButton = tk.Button(self.Broot, text='Go Back', pady=20, padx=50, font=('Calibri', 12),
                                    command=lambda: self.destroy_and_run(runMain), fg='white', bg='red')
        self.BackButton.place(x=20, y=770)

        def show_popup():
            popup_window = tk.Toplevel(self.Broot)
            popup_window.title("Completion")
            label = tk.Label(popup_window, text="Cover Letter built!")
            label.pack(pady=15)
            close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
            close_button.pack(pady=10)

        def runnit(x, y):
            with open(descript, 'w') as file:
                file.write(x)
            command = ['python', MODEL, '--docName', y]
            subprocess.run(command)
            show_popup()
            self.destroy_and_run(runMain)

        self.runbutt = tk.Button(self.Broot, text='Build Cover-Letter', pady=25, padx=60, font=('Calibri', 15),
                         command=lambda: runnit(self.InfoEnter.get("1.0", tk.END), self.docxentry.get()), fg='white', bg='blue')
        self.runbutt.place(x=230, y=700)

        self.Broot.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.Broot.destroy()
            func()

class EditWorkMenu:
    def __init__(self):
        self.Kroot = tk.Tk()
        self.Kroot.geometry("750x850")
        self.Kroot.title("Edit Work Experience")

        self.destroyed = False
        self.file_mode_var = tk.StringVar()  # Fix: Use self.

        self.klabel = tk.Label(self.Kroot, text="Choose to either", font=("Calibri", 30))
        self.klabel.pack()
        self.eidt = tk.Label(self.Kroot, text='add on to file:', font=("Calibri", 20))
        self.eidt.place(x=25, y=60)
        self.overw = tk.Label(self.Kroot, text='Overwrite File:', font=("Calibri", 20))
        self.overw.place(x=550, y=60)

        def WriteorAdd(x):
            filevar = x
            self.InfEnter.config(state='normal')
            return filevar

        self.addbutt = tk.Button(self.Kroot, text='Add', pady=20, padx=90, font=('Calibri', 14),
                                 command=lambda: self.file_mode_var.set(WriteorAdd('a')), fg='white', bg='blue')
        self.addbutt.place(x=25, y=95)

        self.overbutt = tk.Button(self.Kroot, text='Overwrite', pady=20, padx=90, font=('Calibri', 14),
                                  command=lambda: self.file_mode_var.set(WriteorAdd('w')), fg='white', bg='blue')
        self.overbutt.place(x=470, y=95)

        self.InfEnter = tk.Text(self.Kroot, height=30, width=85, state='disabled')
        self.InfEnter.place(x=40, y=180)

        self.BackButton = tk.Button(self.Kroot, text='Go Back', pady=20, padx=50, font=('Calibri', 12),
                                    command=lambda: self.destroy_and_run(RunEdit), fg='white', bg='red')
        self.BackButton.place(x=20, y=770)

        def show_popup():
            popup_window = tk.Toplevel(self.Kroot)
            popup_window.title("Task Completion")
            label = tk.Label(popup_window, text="Work Experience information changed")
            label.pack(pady=15)
            close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
            close_button.pack(pady=10)
        
        def Writefile(filename, mode):
            show_popup()
            with open(filename, mode) as file:
                file.write(self.InfEnter.get("1.0", tk.END))
            self.destroy_and_run(RunEdit)
            
            

        self.runbutt = tk.Button(self.Kroot, text='Edit Info', pady=25, padx=60, font=('Calibri', 15),
                                 command=lambda: Writefile(WORKEXPERIENCE, self.file_mode_var.get()), fg='white', bg='blue')
        self.runbutt.place(x=270, y=700)

        self.Kroot.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.Kroot.destroy()
            func()

class EditEduMenu:
    def __init__(self):
        self.Kroot = tk.Tk()
        self.Kroot.geometry("750x850")
        self.Kroot.title("Edit Education")

        self.destroyed = False
        self.file_mode_var = tk.StringVar()

        def WriteorAdd(x):
            filevar = x
            self.InfEnter.config(state='normal')
            return filevar

        self.klabel = tk.Label(self.Kroot, text="Choose to either", font=("Calibri", 30))
        self.klabel.pack()
        self.eidt = tk.Label(self.Kroot, text='add on to file:', font=("Calibri", 20))
        self.eidt.place(x=25, y=60)
        self.overw = tk.Label(self.Kroot, text='Overwrite File:', font=("Calibri", 20))
        self.overw.place(x=550, y=60)

        self.addbutt = tk.Button(self.Kroot, text='Add', pady=20, padx=90, font=('Calibri', 14),
                                 command=lambda: self.file_mode_var.set(WriteorAdd('a')), fg='white', bg='blue')
        self.addbutt.place(x=25, y=95)
        self.overbutt = tk.Button(self.Kroot, text='Overwrite', pady=20, padx=90, font=('Calibri', 14),
                                  command=lambda: self.file_mode_var.set(WriteorAdd('w')), fg='white', bg='blue')
        self.overbutt.place(x=470, y=95)

        self.InfEnter = tk.Text(self.Kroot, height=30, width=85, state='disabled')
        self.InfEnter.place(x=40, y=180)

        self.BackButton = tk.Button(self.Kroot, text='Go Back', pady=20, padx=50, font=('Calibri', 12),
                                    command=lambda: self.destroy_and_run(RunEdit), fg='white', bg='red')
        self.BackButton.place(x=20, y=770)

        def show_popup():
            popup_window = tk.Toplevel(self.Kroot)
            popup_window.title("Task Completion")
            label = tk.Label(popup_window, text="Education information changed")
            label.pack(pady=15)
            close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
            close_button.pack(pady=10)
        
        def Writefile(filename, mode):
            show_popup()
            with open(filename, mode) as file:
                file.write(self.InfEnter.get("1.0", tk.END))
            self.destroy_and_run(RunEdit)

        self.runbutt = tk.Button(self.Kroot, text='Edit Info', pady=25, padx=60, font=('Calibri', 15),
                                 command=lambda: Writefile(EDUCATION, self.file_mode_var.get()), fg='white', bg='blue')
        self.runbutt.place(x=270, y=700)

        self.Kroot.mainloop()

    def destroy_and_run(self, func):
        if not self.destroyed:
            self.destroyed = True
            self.Kroot.destroy()
            func()


def runMain():
    MainMenu()

def RunEdit():
    EditMenu()

def runMenu():
    RunMenu()

def editWork():
    EditWorkMenu()

def editEducation():
    EditEduMenu()

def Start():
    runMain()

Start()