def agregar():
     conn=sqlite3.connect("deportistas")
     nombre=input("ingrese nombre")
     apellido=input("ingrese su apellido")
     edad=input("ingrese su edad")
     telefono=("ingrese su numero de telefono")
     insert
     conn.execute('''INSERT INTO deportistas (nombre, apellido, edad, telefono)VALUES ( '%s' , '%s' , '%s', '%s', '%s')'''%(nombre, apellido,edad, telefono))
     conn.commit()
     conn.close()

def modificar ():
          nombre=input("ingrese su nombre")
          apellido("ingrese su apellido")
          aql="update deportistas set apellido=?Where nombre=?",
          conn.execute(sql,(apellido,nombre))
          conn.commit()
          conn.close()
