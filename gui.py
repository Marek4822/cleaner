from tkinter import filedialog
from tkinter import messagebox
import ttkbootstrap as ttk
import os
import shutil
from extensions import *

class App():
    def __init__(self):
        super().__init__()
        self = ttk.Window(
            title="Cleaner",
            size=(700, 350),
            themename='darkly',
            resizable=(False, False)
        )
        self.cleaner = Cleaner(self)
        self.mainloop()


class Cleaner(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(10, 10))
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.directory = ''
        self.widgets()


    def widgets(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

        style = ttk.Style()
        style.configure('success.TButton', font=('arial', 14))

        open_label = ttk.Label(self, text='Folder Cleaner', font='arial 30' ) #Label
        path_label = ttk.Label(self, text='Path:', font='arial 16') #Label
        self.path_entry = ttk.Entry(self, font=('arial 14')) #Entry
        open_button = ttk.Button(self, text='Open',  command=self.open_folder, bootstyle='success') #Button
        clear_button = ttk.Button(self, text='Clear', command=self.clear, bootstyle='success') #Button

        open_label.grid(row=0, column=0, sticky='',columnspan=3) #Label
        path_label.grid(row=1, column=0, sticky='nw') #Label
        self.path_entry.grid(row=1, column=0, sticky='ew', columnspan=2) #Entry
        open_button.grid(row=1, column=2, sticky='ew') #Button
        clear_button.grid(row=2, column=0, sticky='', columnspan=3) #Button


    def open_folder(self):
        self.directory = filedialog.askdirectory()
        self.path_entry.delete(0, 'end')
        self.path_entry.insert(0, self.directory)

    def get_path(self):
        main_path = self.directory
        return main_path

    def create_folders(self, main_path):
        os.chdir(main_path)
        for folders in list_dir:
            if not os.path.exists(folders):
                os.mkdir(folders)
            else:
                continue

    def del_empty_folders(self):
        for folders in list_dir:
            if len(os.listdir(folders)) == 0:
                shutil.rmtree(folders)
            else:
                continue

    def move_files_extension(self, main_path, file_extension, sub_path):
        counter = 1
        for file in os.listdir(main_path):
            if any(file.endswith(extension)
                for extension in file_extension):
                destination_path = os.path.join(sub_path, file)
                while os.path.exists(destination_path):
                    filename_parts = os.path.splitext(file)
                    destination_path = os.path.join(sub_path, f"{filename_parts[0]} ({counter}){filename_parts[1]}")
                    counter += 1
                shutil.move(os.path.join(main_path, file), destination_path)


    def move_files_other(self, main_path, sub_path):
        counter = 1
        for file in os.listdir(main_path):
            if os.path.isfile(os.path.join(main_path, file)):
                destination_path = os.path.join(sub_path, file)
                while os.path.exists(destination_path):
                    filename_parts = os.path.splitext(file)
                    destination_path = os.path.join(sub_path, f"{filename_parts[0]} ({counter}){filename_parts[1]}")
                    counter += 1
                shutil.move(os.path.join(main_path, file), destination_path)


    def clear(self):
        main_path = self.get_path()
        if main_path:
            try: 
                document_path = (rf"{main_path}\Documents")
                image_path = (rf"{main_path}\Image")
                audio_path = (rf"{main_path}\Music")
                video_path = (rf"{main_path}\Video")
                program_path = (rf"{main_path}\Programs")
                compressed_path = (rf'{main_path}\Compressed')
                other_path = (rf"{main_path}\Others")
                list_path = [image_path, video_path, audio_path, document_path, program_path, compressed_path]
                
                self.create_folders(main_path)
                counter = 0
                for _ in range(6):
                    self.move_files_extension(main_path, list_extension[counter], list_path[counter])
                    counter +=1
                self.move_files_other(main_path, other_path)
                self.del_empty_folders()
                messagebox.showinfo('Success', f'Your directory: {main_path} has been cleared!')

            except Exception as e:
                print(f'Error Occurred: {e}')
                messagebox.showerror('Error', f'Error Occurred: {e}')
        else:
            messagebox.showerror('Error', 'Please choose path to your directory!')

App()