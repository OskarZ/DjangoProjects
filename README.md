Installieren von Django.
----------------------------------------------------

1. -Django muss mit Hilfe des "Pip Package-Installers" installiert werden.

   -Dazu f�hrt man den Command "pip install Django" mit der cmd aus.

   -Wenn man sicher sein m�chte, dass Django ordnungsgem�� installiert wurde, �ffnet man die Python-Shell
    durch Ausf�hren des Commands "Python " und f�hrt folgenden Test aus: 
   --------------------------------------------------    

    >>> import django
    >>> print(django.get_version())
    
    ------------------------------------------------
    wird nun die Version von Django angezeigt, wurde es erfolgreich installiert.

(f�r alle Schritte wird vorausgesetzt, dass Python bereits installiert wurde)

Erstellen eines Django Projekts
-----------------------------------------------------

2. -Nun wechselt man mit der cmd in das Verzeichnis, indem man sein Django-Projekt erstellen m�chte.

   -Dann wird der Command "django-admin startproject mysite" ausgef�hrt.

   -Django hat nun den neuen Ordner "mysite" erstellt. Im Anschluss muss mit de cmd in diesen Ordner gewechselt werden.

   -Jetzt f�hrt man den Command "Python manage.py runserver" aus. Unter http://localhost:8000 kann man nun die von Django 
    erstellte Website aufrufen.

Erstellen einer Django App.
------------------------------------------------------

3. -Um eine Website aufzubauen muss eine App erstellt werden. Dies macht man, indem man "python manage.py startapp -Name der App-" 
    mit der cmd ausf�hrt.

   
   -Jetz wechselt man in den Ordner mysite/-Name der App- un f�gt dort die Datei "urls.py" hinzu.


   -Dann �ffnet man die Datei mysite/mysite/urls.py und ersetzt ihren Code durch Folgendes:
   ---------------------------------------------------

   from django.urls import include, path
   from django.contrib import admin

   urlpatterns = [
       path('-Name der App-/', include('-Name der App-.urls')),
       path('admin/', admin.site.urls),
   ]  

   ----------------------------------------------------
   -Als N�chstes wird die Datei "mysite/-Name der App-/urls.py ge�ffnet die gerade erstellt wurde
    dort wird folgender Code eingef�gt:
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

	-Um die Django Administration nutzen zu k�nnen, die unter http://localhost:8000/admin zufinden ist, muss zun�chst
	 ein Superuser erstellt werden. Das kann man, indem man den Command "python manage.py createsuperuser" mit der cmd ausf�hrt.
	 Nun wird man aufgefordert einen Username und ein Passwort anzugeben.


	-Nach dem Erstellen des Superusers kann man nun die Admin-Site nutzen, bei der man sich mit seinen Daten einloggt.


	Django Models erstellen 
  	-----------------------


	-Django-Models werden im Verzeichnis der erstellten App, in der Datei "models.py" erstellt.


	-Um ein neues Model zu erstellen, erstellt man ein Klasse mit einem entsprechenden Namen. Das sieht dann z.B. so aus:


        class Person(models.Model):
	    Name = models.CharField(max_length=20)
	    Nachname = models.CharField(max_length=20, default='M�ller')


	Dem Model "Person" werden zwei Felder zugewiesen:

	  -Name: in diesem Feld k�nnen bis zu 20 Zeichen enthalten sein

	  -Nachname: in diesem Feld k�nnen ebenfals bis zu 20 Zeichen enthalten sein, wird ihm kein Wert zugewiesen 
	   wird standartm��ig der Wert 'M�ller' angenommen.


	-Um das Model als SQL-Datenbank nutzen zu k�nnen muss man den Command "Python manage.py makemigrations" und direkt danach "python 
	 manage.py migrate" ausf�hren.


	-Nun kann man �ber die Admin-Seite neue "Personen" hinzuf�gen.


	SQL-Queries
	-----------


	-M�chte man sehen welche "Personen" momentan existieren, �ffnet man erneut die Python-Shell indem man "python manage.py shell" ausf�hrt
	 und importier das entsprechende Model:

	
	>>> from -Name der App-.models import Person

	
	-Dann muss mann angeben welche "Personen" man angezeigt haben m�chte. 
  	>>> Person.objects.all()
	 zeigt alle an.

	
	-M�chte man z.B. nur Personen sehen die mit Nachnamen "M�ller" hei�en muss man Folgendes tun:

	>>>Person.objects.filter(Nachname='M�ller')

	-Au�erden kann man die "Personen" auch ordnen indem man "Person.objects.orderd_by() verwendet   




