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
```
from pywebcopy import save_website
from tkinter import messagebox

def download():
    lnk = requested()
    save_website( url=lnk, project_folder="./saved_website/")
    messagebox.showinfo("Success!", "Project folder saved.")
```    
- [pywebcopy Documentation](https://pypi.org/project/pywebcopy/)
- [Tkinter Dialogs Documentations](https://docs.python.org/3/library/dialog.html)