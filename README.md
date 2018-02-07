Installieren von Django.
----------------------------------------------------

1. -Django muss mit Hilfe des "Pip Package-Installers" installiert werden.

   -Dazu führt man den Command "pip install Django" mit der cmd aus.

   -Wenn man sicher sein möchte, dass Django ordnungsgemäß installiert wurde, öffnet man die Python-Shell
    durch Ausführen des Commands "Python " und führt folgenden Test aus: 
   --------------------------------------------------    

    >>> import django
    >>> print(django.get_version())
    
    ------------------------------------------------
    wird nun die Version von Django angezeigt, wurde es erfolgreich installiert.

(für alle Schritte wird vorausgesetzt, dass Python bereits installiert wurde)

Erstellen eines Django Projekts
-----------------------------------------------------

2. -Nun wechselt man mit der cmd in das Verzeichnis, indem man sein Django-Projekt erstellen möchte.

   -Dann wird der Command "django-admin startproject mysite" ausgeführt.

   -Django hat nun den neuen Ordner "mysite" erstellt. Im Anschluss muss mit de cmd in diesen Ordner gewechselt werden.

   -Jetzt führt man den Command "Python manage.py runserver" aus. Unter http://localhost:8000 kann man nun die von Django 
    erstellte Website aufrufen.

Erstellen einer Django App.
------------------------------------------------------

3. -Um eine Website aufzubauen muss eine App erstellt werden. Dies macht man, indem man "python manage.py startapp -Name der App-" 
    mit der cmd ausführt.

   
   -Jetz wechselt man in den Ordner mysite/-Name der App- un fügt dort die Datei "urls.py" hinzu.


   -Dann öffnet man die Datei mysite/mysite/urls.py und ersetzt ihren Code durch Folgendes:
   ---------------------------------------------------

   from django.urls import include, path
   from django.contrib import admin

   urlpatterns = [
       path('-Name der App-/', include('-Name der App-.urls')),
       path('admin/', admin.site.urls),
   ]  

   ----------------------------------------------------
   -Als Nächstes wird die Datei "mysite/-Name der App-/urls.py geöffnet die gerade erstellt wurde
    dort wird folgender Code eingefügt:
   ----------------------------------------------------

   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]

   -----------------------------------------------------
   -Im letzten Schritt muss nun noch der Code der Datei mysite/-Name der App-/views.py durch Folgendes ersetzt werden:
   -----------------------------------------------------

   from django.http import HttpResponse

   def index(request):
       return HttpResponse("##############")

    ----------------------------------------------------
    anstelle der # kann ein belibiger Text ausgegeben werden


    -unter http://localhost/-Name der App- ist nun der Text zusehen
______________________________________________________________________________________________________________________________________
______________________________________________________________________________________________________________________________________




Weitere Funktionen von Django:
------------------------------

	Django Administration:
        ----------------------

	-Um die Django Administration nutzen zu können, die unter http://localhost:8000/admin zufinden ist, muss zunächst
	 ein Superuser erstellt werden. Das kann man, indem man den Command "python manage.py createsuperuser" mit der cmd ausführt.
	 Nun wird man aufgefordert einen Username und ein Passwort anzugeben.


	-Nach dem Erstellen des Superusers kann man nun die Admin-Site nutzen, bei der man sich mit seinen Daten einloggt.


	Django Models erstellen 
  	-----------------------


	-Django-Models werden im Verzeichnis der erstellten App, in der Datei "models.py" erstellt.


	-Um ein neues Model zu erstellen, erstellt man ein Klasse mit einem entsprechenden Namen. Das sieht dann z.B. so aus:


        class Person(models.Model):
	    Name = models.CharField(max_length=20)
	    Nachname = models.CharField(max_length=20, default='Müller')


	Dem Model "Person" werden zwei Felder zugewiesen:

	  -Name: in diesem Feld können bis zu 20 Zeichen enthalten sein

	  -Nachname: in diesem Feld können ebenfals bis zu 20 Zeichen enthalten sein, wird ihm kein Wert zugewiesen 
	   wird standartmäßig der Wert 'Müller' angenommen.


	-Um das Model als SQL-Datenbank nutzen zu können muss man den Command "Python manage.py makemigrations" und direkt danach "python 
	 manage.py migrate" ausführen.


	-Nun kann man über die Admin-Seite neue "Personen" hinzufügen.


	SQL-Queries
	-----------


	-Möchte man sehen welche "Personen" momentan existieren, öffnet man erneut die Python-Shell indem man "python manage.py shell" ausführt
	 und importier das entsprechende Model:

	
	>>> from -Name der App-.models import Person

	
	-Dann muss mann angeben welche "Personen" man angezeigt haben möchte. 
  	>>> Person.objects.all()
	 zeigt alle an.

	
	-Möchte man z.B. nur Personen sehen die mit Nachnamen "Müller" heißen muss man Folgendes tun:

	>>>Person.objects.filter(Nachname='Müller')

	-Außerden kann man die "Personen" auch ordnen indem man "Person.objects.orderd_by() verwendet   




