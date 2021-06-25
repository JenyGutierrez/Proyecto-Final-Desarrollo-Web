import sqlite3

con = sqlite3.connect("catshop.db")
print("La base de datos ha sido abierta")

# tabla para el registro de usuarios
con.execute("create table catUser (idU INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL, email TEXT UNIQUE NOT NULL, telefono INTEGER NOT NULL, pass TEXT UNIQUE NOT NULL)")
print("Tabla de usuarios creada")

# tabla para el producto
con.execute("create table catProductos (idP INTEGER PRIMARY KEY AUTOINCREMENT, imagen TEXT NOT NULL, nombreP TEXT NOT NULL, talla TEXT, precio INTEGER NOT NULL, descripcion TEXT NOT NULL, disponibles INTEGER NOT NULL, categoria TEXT NOT NULL)")
print("Tabla de productos creada")

# tabla para las ubicaciones
con.execute("create table catSucursales (idT INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nombreSucursal TEXT NOT NULL, direccion TEXT NOT NULL, horario TEXT NOT NULL, telefono TEXT NOT NULL)")
print("Tabla de ubicaciones creada")
con.close()