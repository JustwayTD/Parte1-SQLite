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