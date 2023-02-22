
Program je napisan u programskom jeziku C++(source python) koristeći OpenCV biblioteke. Program snima videozapis s zadane kamerice i stvara prozor naziva "slika". Zatim stvara trake za praćenje kako bi kontrolirao položaj okvira i vrijednosti praga za obradu slike.

Unutar petlje while, program čita okvire s kamere i dobiva položaje traka. Zatim crta pravokutni okvir s četiri linije oko odabrane područja okvira. Program stvara klon okvira, a okvir se smanjuje s kloniranog okvira pomoću položaja i veličine okvira.

Program prikazuje klonirani okvir s pravokutnim okvirom i također smanjeni okvir. Korisnik može premještati okvir pomoću traka, a program će ažurirati položaj okvira i njegovu veličinu prema potrebi. Ako korisnik pritisne tipku "w", program ulazi u petlju za obradu smanjenog okvira. Unutar petlje program snima novi okvir iz kamere i crta okvir oko istog položaja kao i prethodni okvir.

Korisnik može zatim pritisnuti tipku "t" da pozove funkciju "glavni" ili "e" da pozove funkciju "kontroler". Ako korisnik pritisne tipku "q", program će se zaustaviti i vratiti u funkciju "glavni".

"Funkcija glavni" nije definirana u kodu, pa nije jasno što radi. Funkcija "kontroler" vraća vektor s x-položajem, y-položajem i vrijednosti praga za obradu slike. Program tada koristi ove vrijednosti za ažuriranje položaja okvira u okviru.

Općenito, program omogućuje korisniku odabir područja okvira i obradu tog područja zasebno. Korisnik može kontrolirati položaj i veličinu okvira, kao i vrijednosti praga za obradu slike. Program također omogućuje korisniku pozivanje drugih funkcija za obradu odabranog područja.
