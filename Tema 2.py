import string
# Declaratia unui sir copiat de pe internet
sir_articol=' O contabilă de la MAE este acuzată că a plătit salarii false iubitului ei și fiului acestuia, deși nu erau angajați la minister.'
# Imparte sirul in 2 parti egale
jumatate=len(sir_articol)//2
prima_parte=sir_articol[:jumatate]
a_doua_parte=sir_articol[jumatate:]
# In prima parte
# Transformarea toate literele in majuscule
prima_parte=prima_parte.upper
# Elimină toate spațiile goale de la începutul și finalul șirului
prima_parte=prima_parte.stripp
# In a doua parte
# Inverseaza ordinea caracterelor
a_doua_parte=a_doua_parte[::-1]
# Transformă prima literă în majusculă
a_doua_parte=a_doua_parte.capitalize()
# Elimină toate caracterele de punctuație (., ,, !, ?) din această parte
a_doua_parte=a_doua_parte.translate(str.maketrans('','',string.punctuation))
# Combină cele două părți și afișează rezultatul
rezultat=prima_parte+a_doua_parte
print(rezultat)