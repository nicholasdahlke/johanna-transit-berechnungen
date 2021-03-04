import math
#Definitionen

msgDlg ("Bitte Achten Sie darauf, dass sie die Deutsch Kommas als Punkte schreiben!")
Rs = input ("Wie groß ist der Radius des Sterns den Sie beobachten?") #Sternradius - Literatur
F = math.sqrt(input ("Wie groß ist Ihre gemessene Transittiefe?"))#Wurzel aus Transittiefe - Lichtkurve
G = 6.673*10**-11 #Gravitationskonstante - Literatur
Ms = input ("Welche Masse beträgt der Stern, den Sie beobachten?") #Masse des Sterns - Literatur
P = float (input("Was ist die Periodendauer des Exolaneten in sekunden?")) #Periondendauer - Literatur
Pmin = P/60 #Periodendauer in min
D = input ("Wie lange hat der Transit gedauert?") #Transitdauer - Lichtkurve
Rjup = 6.911*10**7
AE = 1.496*10**11
pi = 3.14

#Radius des Planeten
print "Radius des Planeten:"
Rp = Rs*F
print Rp, "Meter"
print "Gerundet:",(int(Rp)), "Meter"
print "In Vielfachen des Jupiters:"
print Rp/Rjup, "Meter"
print "--------------------"
#Abstand Planet-Stern

print "Abstand Planet-Stern:"
a = ((G*Ms*P**2)/(4*pi**2))**(1.0/3.0)
print a, "Meter"
print "in AE:", a/AE
print "--------------------"

#Inklination
#Breitengrad
drad = math.acos((((D*pi*a)/Pmin)-Rp)/Rs)
ddeg=(drad*180)/pi
print "Breitengrad:",ddeg, "°"
irad = math.acos(Rs*math.sin(drad)/a)
ideg= (irad*180)/pi
print "Inklination:", ideg, "°"
