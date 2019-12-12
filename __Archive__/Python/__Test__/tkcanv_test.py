#encoding = utf-8
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk();
root.wm_geometry('800x700+200+200');
wndcanv = tk.Canvas(root, width = 800, height = 700);
wndcanv.pack();
wndcanv.config(scrollregion = (-400, -200, 100, 100));
x = y = 0;
while (x < 800):
    wndcanv.create_line(x, 0, x, 600);
    x += 10;
wndcanv.create_polygon((-100, 0, 0, 300, 40, 120), smooth = 'true', splinesteps = 100);

root.mainloop();
