from sqlite3.dbapi2 import connect
from flask import *
import sqlite3
# from sqlalchemy import text

app = Flask(__name__)

# LLAMADO A LAS PAGINAS
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogos.html")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

#CONSULTA DE USUARIOS
@app.route("/consultarUsuarios")  
def consultar():
    con = sqlite3.connect("catshop.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("SELECT * FROM catUser")  
    rows = cur.fetchall()
    cur.close()     
    return render_template("consultarUsuarios.html", filas = rows)

# CONSULTA DE USUARIOS PARA LA SECCION DE POSTRES
@app.route("/reposteria")  
def reposteria():
    con = sqlite3.connect("catshop.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("SELECT imagen, nombreP, precio, disponibles FROM catProductos WHERE categoria = 'postres' ")  
    rows = cur.fetchall()
    cur.close()     
    return render_template("reposteria.html", filas = rows)

# FUNCION PARA BORRAR LOS USUARIOS
@app.route('/borrar')
def borrar():
    identificador = request.args.get('my_var', 'nop')
    
    conn = sqlite3.connect("catshop.db")
    conn.execute("DELETE FROM catUser WHERE idU = ?", (identificador))
    conn.commit()
    # UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'table_name';
    # conn.execute("UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'catUser' ")
    conn.close()
    return render_template("index.html")

#FUNCION PARA MOSTRAR LAS SUCURSALES
@app.route("/sucursales")  
def sucursales():
    con = sqlite3.connect("catshop.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("SELECT nombreSucursal, direccion, horario, telefono FROM catSucursales")  
    rows = cur.fetchall()
    cur.close()     
    return render_template("sucursales.html", filas = rows)

# FUNCION PARA INGRESAR LOS USUARIO
@app.route("/registro", methods = ["POST", "GET"])
def guardarDatos():
    msg = "msg"
    con = sqlite3.connect("catshop.db")
    
    if request.method == "POST":
        try:
            nombre = request.form["nombreRegistro"]
            apellidoR = request.form["apeRegistro"]
            email = request.form["correoRegistro"]
            telefono = request.form["telefonoRegistro"]
            contra = request.form["contra"]
            print(nombre, apellidoR, email, telefono, contra)
            
            cur = con.cursor()
            cur.execute("INSERT INTO catUser (nombre, apellido, email, telefono, pass) VALUES (?,?,?,?,?)", (nombre, apellidoR, email, telefono, contra))
            con.commit()
            msg = "Usuario agregado"
            
        except:
            msg = "No se agrego el usuario"
            con.rollback()
        finally:
            con.close()
            return render_template("registrar.html", msg = msg)