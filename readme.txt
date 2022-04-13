Modulo 7:

Para esta tarea utilice django junto con gunicorn y Nginx. 

Todo el comando en si fue implementado directo desde la terminal de visual studio code.

El titulo de "Slang Panameño"  y las palabras del mismo.
Para esto utilice los siguientes comandos desde la terminal:

from main.models import Item, Slang
t = Slang(name="Slang Panameño")
t.save()

Luego con las palabras:
t.item_set.create(text="Mopri = Significa primo.", complete=False)
t.item_set.create(text="Chantin: Significa casa", complete=False)
t.item_set.create(text="Ofi/Ofe: Significa si. Ejemplo: Ofi, yo vi esa vaina", complete=False)
t.item_set.create(text="Vaina: Significao cosa. Esta no solo esta en el Slang de PTY.", complete=False)
t.item_set.create(text="Que xopa: Significa como estas. Ejemplo: Que xopa, como has estado?.", complete=False)

Luego de agregar estas palabras a la base de datos se les asigna un ID automaticamente.

Mopri = Significa primo. (id=1)
Chantin: Significa casa (id=2)
Ofi/Ofe: Significa si. Ejemplo: Ofi, yo vi esa vaina (id=3)
Vaina: Significao cosa. Esta no solo esta en el Slang de PTY. (id=4)
Que xopa: Significa como estas. Ejemplo: Que xopa, como has estado?. (id=5)

Para imprimirlos solo hay que ir al archivo de views.py en el archivo main y colocar:

def index(response, name):
    ls = Slang.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return  HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

para imprimir un objeto junto con el titulo de "Slang Panameño"

def index(response, name):
    ls = Slang.objects.get(name=name)
    item = ls.item_set.get(id=1)
    item = ls.item_set.get(id=2)
    item = ls.item_set.get(id=3)
    item = ls.item_set.get(id=4)
    item = ls.item_set.get(id=5)
    return  HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
Para imprimir todos.

Otra forma de hacerlo es con html:

<html>
    <head>
        <title>Slang Panameño</title>
        <body>
            <h1>Slang Panameño</h1>
            <p></p>
            <p></p>
            <p></p>
            <h2>By: Jose Dondis</h2>
            <h2>Cedula: 4-812-1989</h2>
            <p></p>
            <p></p>
            <p></p>
            <p>Mopri = Significa primo.</p>
            <p></p>
            <p>Chantin: Significa casa</p>
            <p></p>
            <p>Ofi/Ofe: Significa si. Ejemplo: Ofi, yo vi esa vaina</p>
            <p></p>
            <p>Vaina: Significao cosa. Esta no solo esta en el Slang de PTY.</p>
            <p></p>
            <p>Que xopa: Significa como estas. Ejemplo: Que xopa, como has estado?.</p>
            <p></p>
            <p></p>

        </body>
    </head>
</html>

para llamar el siguiente archivo hay que colocar:

def base(response):
     return rener(response, "main/base.html, {})

Y listo. Eso seria todo. Todo se puede hacer desde la terminal, por ende cuando se lee el codigo se ve vacio pero realmente es porque en django no es necesario escribir el codigo en los archivos. Desde la terminal es mucho mas facil y rapido

Adjunto hago envio de la captura de pantalla de la prueba de que si funciona el mismo
