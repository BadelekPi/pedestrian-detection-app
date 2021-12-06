from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# from functions import display_logo, display_textbox, extract_images, display_icon, resize_image, display_images
from tkinter.ttk import Combobox
import time
import os

def quit():
    global root
    root.quit()

def open_file():
    browse_text.set('Wczytywanie...')
    file = askopenfile(parent=root, mode='rb', title='Wybierz plik', filetype=[("Plik .mpg", "*.mpg")])
    if file:
        browse_text.set('Wybrano.')
        browse_btn = Button(root, textvariable=browse_text, command=lambda: open_file(), font=("Helvetica", 12),
                            bg="green", fg="black", height=1, width=12)
        browse_btn.grid(column=1, row=3, pady=5)
        global selected_path
        selected_path = file.name

def open_video():
    cam_text.set('Wczytywanie...')
    time.sleep(1)

def open_cam():
    cam_enable = 1

def display_logo(url, row, column):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)

def start_detection(selected_model, selected_path, selected_resolution):
    if selected_resolution == "1920x1080":
        resolution_width = 1920
        resolution_hight = 1080

    elif selected_resolution == "1280x720":
        resolution_width = 1280
        resolution_hight = 720

    elif selected_resolution == "640x360":
        resolution_width = 640
        resolution_hight = 360

    if selected_model == "Faster-RCNN v1 640x640":
        if selected_resolution == "1920x1080": resolution = [1920, 1080]
        os.chdir("C:/Object_detection_faster_rcnn/models-master/research/")
        command = 'python testowo.py {} {} {}'.format(selected_path, resolution_width, resolution_hight)
        os.system(command)

    elif selected_model == "SSD EfficientDet D0 512x512":
        os.chdir("C:/Object_detection_efficientdet/windows_v1.8.0/models-master/research")
        command = 'python testowo.py'
        os.system(command)

    elif selected_model == "SSD MobileNet v1 640x640":
        os.chdir("C:/Object_detection_mobile/models-master/research")
        command = 'python testowo.py'
        os.system(command)

root = Tk()
root.geometry('+%d+%d'%(350,10)) #place GUI at x=350, y=10
root.title('Praca inżynierska Badełek Piotr')
root.iconbitmap("wat_logo.ico")

#header area - logo & name
header = Frame(root, width=495, height=300, bg="white")
header.grid(columnspan=3, rowspan=2, row=0, column=0)

#main content area - text and image extraction
main_content = Frame(root, width=501, height=355, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=4, row=3)

icon = Image.open("app_header.png")

icon = ImageTk.PhotoImage(icon)
icon_label = Button(image=icon, width=495, height=300)
icon_label.image = icon
icon_label.grid(column=0, row=0, columnspan=3, rowspan=2)

# Browse source button
source_text = Label(root, text="Wybierz źródło detekcji:", font=("Helvetica", 12, "bold"), bg="#20bebe", fg="black")
source_text.grid(column=0, row=3, pady=5)

# Browse video Button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Helvetica",12), bg="#20bebe", fg="black", height=1, width=12)
browse_text.set("Z pliku video")
browse_btn.grid(column=1, row=3, pady=5)
selected_path = 0

# Camera button
cam_text = StringVar()
cam_btn = Button(root, textvariable=cam_text, command=lambda:open_video(), font=("Helvetica",12), bg="#20bebe", fg="black", height=1, width=12)
cam_text.set("Kamera")
cam_btn.grid(column=2, row=3, pady=5)

# Neural network model browse
nn_text = Label(root, text="Wybierz model sieci:", font=("Helvetica", 12, "bold"), bg="#20bebe", fg="black")
nn_text.grid(column=0, row=4)
selected_model = StringVar()

suwak = Combobox(root, textvariable=selected_model, state="readonly")
suwak['values'] = ("SSD EfficientDet D0 512x512", "Faster-RCNN v1 640x640", "SSD MobileNet v1 640x640")
suwak.grid(row=4, column=1, columnspan=2)


# Resolution browse
selected_resolution = StringVar()
res_text = Label(root, text="Wybierz rozdzielczość obrazu:", font=("Helvetica", 12, "bold"), bg="#20bebe", fg="black")
res_text.grid(column=0, row=5)
suwak = Combobox(root, textvariable=selected_resolution, state="readonly")
suwak['values'] = ("1920x1080", "1280x720", "640x360")
suwak.grid(row=5, column=1, columnspan=2)


#Start detection button
start_text = StringVar()
start_btn = Button(root, textvariable=start_text, font=("Raleway",12), bg="green", fg="white", height=1, width=15, command=lambda:start_detection(selected_model.get(), selected_path,
                                                                                                                                                  selected_resolution.get()))
start_text.set("Rozpocznij detekcje")
start_btn.grid(row=6, column=0, columnspan=3)


root.mainloop()

