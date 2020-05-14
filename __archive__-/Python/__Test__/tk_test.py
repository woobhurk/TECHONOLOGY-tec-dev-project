#coding = utf-8

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox

def showHello():
    tkMsgBox.showinfo("InfoBox", "Hello");

new_wnd = tk.Tk();
new_wnd.title("New Window");
print("Hello world!");
print("你好");
new_btn = ttk.Button(new_wnd, text = "New Button", width = 50);
new_btn.config(command = showHello);
new_btn.grid();
new_lbl = ttk.Label(new_wnd, text = "New Label");
new_lbl.grid();
new_wnd.mainloop();
