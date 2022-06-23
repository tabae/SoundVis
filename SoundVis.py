from turtle import color
import sounddevice as sd
import numpy as np
import datetime
import time
import tkinter
import threading

def reflesh():
    duration = 60
    def callback(indata, frames, time, status):
        val = np.sqrt(np.mean(indata**2))
        ratio = max(0.0, min(1.0, val / 0.03))
        x = min(90, ratio * 90)
        print(ratio)
        R = - (0xFF - 0x55) * ratio + 0xFF
        G = - (0xFF - 0xAA) * ratio + 0xFF
        B = - (0xFF - 0xAA) * ratio + 0xFF
        color_code = '#{:02X}{:02X}{:02X}'.format(int(R), int(G), int(B))
        print(color_code)
        canvas.delete("all")
        canvas.create_oval(5+x,5+x,195-x,195-x,fill=color_code)

    with sd.InputStream(
            channels=1, 
            dtype='float32', 
            callback=callback
        ):
        sd.sleep(int(duration * 1000))
     
canvas = tkinter.Canvas(master=None, width=200, height=200)
canvas.pack()

thread = threading.Thread(target=reflesh, daemon=True)
thread.start()

canvas.mainloop()