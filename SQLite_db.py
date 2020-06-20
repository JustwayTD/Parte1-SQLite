# Actividad: Elaborar una aplicación de línea de comandos en Python que sirva cuyo propósito sea mantener un diccionario de palabras 
# del slang panameño (xopa, mopri, otras). Las palabras y su significado deben ser almacenadas dentro de una base de datos 
# SQLite. Las opciones dentro del programa deben incluir como mínimo: 
# a) Agregar nueva palabra, c) Editar palabra existente, d) Eliminar palabra existente, e) Ver listado de palabras,
#  f) Buscar significado de palabra, g) Salir
import sqlite3

conn = sqlite3.connect('Slang.db')

c =conn.cursor()
# c.execute("CREATE TABLE slangs ( word text ,meaning text)")
def agregar(word1,palabraS):
    """Adds a new word to our data base"""
    word1 = word1.strip()
    palabraS = palabraS.strip()
    with conn:
        c.execute("INSERT INTO slangs values(:word, :meaning)",{"word": word1, "meaning" :palabraS})
    print("Cool! La palabra ",word1,"ha sido añadida")
def menu():
    """Menú principal del programa """
    opc = int(input("Bienvenido Fren! ¿Que vamos a hacer hoy?\n1) Agregar nueva palabra \n2) Editar palabra existente \n3) Eliminar alguna palabra existente \n4) Ver listado de palabras \n5) Buscar significado de palabra \n6) Salir\n"))
    return opc
def editaMoh(wordto,newmean):
    """Edits an already existing word from our database"""
    wordto.strip()
    newmean.strip()
    with conn:
        c.execute("UPDATE slangs SET meaning = :newmean WHERE word = :wordto AND meaning = :newmean",{"wordto" :wordto,"newmean" :newmean})
    print("La palabra: ", wordto," ha sido actualizada")
def eliminaMoh (word):
    """Deletes certain word from our database"""
    with conn:
        c.execute("DELETE from slangs WHERE word = :word AND meaning = :meaning",{"word" :word.word,"meaning" :word.meaning})
def urbanDic():
    """Shows all elements from my database slangs"""
    with conn:
        c.execute("SELECT * FROM slangs")
        return c.fetchall()
def whatIsLove(babyDont):
    """Shows a Description of a certain word"""
    babyDont.strip()
    print("la palabra es:", babyDont)
    with conn:
        c.execute("SELECT * FROM slangs WHERE meaning = :meaning",{"meaning" :babyDont})
    return c.fetchall()

if __name__=="__main__":
    choo = menu()
    if choo == 1:
        palabra1 = input("Cual sera la palabra a agregar?\n")
        palabra2 = input("Y que significa eso?\n")
        agregar(palabra1,palabra2)
    elif choo == 2:
        palabra1 = input ("Cual palabra quieres editar?\n")
        palabra2 = input("Cual sera el nuevo significado?\n")
        editaMoh(palabra1,palabra2)
    elif choo == 3:
        palabra1 = input("Que palabra quieres eliminar?\n")
        eliminaMoh(palabra1)
    elif choo == 4:
        palabras = urbanDic()
        for palabras in palabras:
            print(palabras)
    elif choo == 5:
        palabra1 = input("De que palabra quieres el significado (case sensitive)")
        palabras = whatIsLove(palabra1)
        for palabras in palabras:
            print("Significa:", palabras)
