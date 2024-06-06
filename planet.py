from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Planet Encyclopidia")

root.minsize(500, 550)
root.maxsize(500, 550)

root.configure(background="lightblue")

Mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open("earth.jpg"))

planets = ['Mercury', 'Venus', 'Earth']
selectedPlanet = StringVar()
dropdown = ttk.Combobox(root, textvariable=selectedPlanet, values=planets)

planet_label = Label(root, bg="lightblue", text="Select Planet")
planet_name_label = Label(root,font=("courier", 18, "bold"), bg="lightblue")
planet_img = Label(root, bg="gold2", borderwidth=2, highlightthickness=5, relief="solid")
planet_gravity_radius = Label(root, font=("castellar"), bg="lightblue")
planet_info = Label(root, font=("courier"), bg="lightblue", wraplength=500)

def get_info():
    planet = selectedPlanet.get()
    
    if(planet == "Mercury") :
        planet_name_label['text'] = planet
        planet_img['image'] = Mercury
        planet_gravity_radius['text']  = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        planet_info["text"] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
    elif(planet == "Earth"):
        planet_name_label['text'] = planet
        planet_img['image'] = Earth
        planet_gravity_radius['text']  = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        planet_info["text"] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
    else:
        planet_name_label['text'] = planet
        planet_img['image'] = Venus
        planet_gravity_radius['text']  = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        planet_info["text"] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
        
button = Button(root, text="Get info", command=get_info)
button.place(relx=0.5, rely=0.18, anchor=CENTER)

planet_label.place(relx=0.2, rely=0.1, anchor=CENTER)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
planet_name_label.place(relx=0.5, rely=0.25, anchor=CENTER)
planet_img.place(relx=0.5, rely=0.5, anchor=CENTER)
planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()