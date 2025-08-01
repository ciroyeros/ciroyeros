from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title = ("Ejercicio completo con tkinter| Profe: Luis ")
ventana.geometry("400x400")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
numero3 = StringVar()
resultado = StringVar()
numero1.set("")
numero2.set("")
numero2.set("")

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()) + float(numero3.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
def restar():
    try:
       resultado.set(float(numero1.get()) - float(numero2.get()) - float(numero3.get()))
       mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
numero1.set("")
numero2.set("")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()) * float(numero3.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
numero1.set("")
numero2.set("")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()) / float(numero3.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
numero1.set("")
numero2.set("")

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es:{resultado.get()}")
    




marco = Frame(ventana, width=300, height=200)
marco.config(
padx=15,
pady=15,
bd=5,
relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2,justify="center").pack()
Label(marco, text="Tercer número: ").pack()
Entry(marco, textvariable=numero3,justify="center").pack()
Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)
Button(marco, text="Lista", command=lista).pack(side="left", fill=X, expand=YES)

ventana.mainloop()