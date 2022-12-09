## **Save**
We are going to use following python libraries to achieve the task
1. pywebcopy
1. Tkinter Dialogs
### **pywebcopy**
PyWebCopy is a free tool for copying full or partial websites locally onto your hard-disk for offline viewing.
### Run the following command to import this library:
```
pip install pywebcopy
```
***
### **tkinter.simpledialog**
We are going to use ```tkinter.simpledialog``` library for receiving a pop-up dialog-box after saving the response.
### Run the following command to import this library:
```
pip install tkinter.simpledialog
```
***
## The ```save``` Function 
We are going to define a new function "download" for downloading the fetched response.
Inside the download function we are calling the requested function . 
Then by the "save_website"  method of pywebcopy we are downloading response in our local directory.
```
from pywebcopy import save_website
from tkinter import messagebox

def download():
    link = requested()
    save_website( url=link, project_folder="./folder_path")
    messagebox.showinfo("Success!", "Project folder saved.")
```    
- [pywebcopy Documentation](https://pypi.org/project/pywebcopy/)
- [Tkinter Dialogs Documentations](https://docs.python.org/3/library/dialog.html)
