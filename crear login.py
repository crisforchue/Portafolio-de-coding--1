import customtkinter 

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('350x300') #Crean la ventana principal de la applicacion, ademas de definir el tamano

def login():

    print("Te haz loggeado exitosamente!") #Una vez el usuario se haya loggeado exitosamente aparecera este mensaje en su pantalla

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True) #el "CTKFrame" crea el contenedor dento del root (ventana principal). Pady y padx asignant el tamamno, "fill" hace que se expanda horzontal y vertical, y "expand true" hace que ocupe todo el espacio posible.

label = customtkinter.CTkLabel(master=frame, text='Login') #CTkLabel crear el "Login" dentro del contenedor. Igual con el "Username, password"
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login) #Aca, el parametro del login se associan a la funcion inicial que hicimos.
button.pack(pady=12, padx=10)

root.mainloop() #Aca hace que todo funcione, yay
