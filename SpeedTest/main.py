from tkinter import *
from speedtest import Speedtest

def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(download / (10**6), 2)

    download_label.config(text="Скорость загрузки:\n" + str(download_speed) +"MbPs")
    upload_label.config(text="Скорость отдачи:\n" + str(upload_speed) + "MbPs")

root = Tk()

root.title("Speedtest")
root.geometry("300x400")

button = Button(root, text="Старт", font=40, command=test)
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text="Скорость загрузки:\n-", font=35)
download_label.pack(pady=50)
upload_label = Label(root, text="Скорость отдачи:\n-", font=35)
upload_label.pack(pady=10)

root.mainloop()