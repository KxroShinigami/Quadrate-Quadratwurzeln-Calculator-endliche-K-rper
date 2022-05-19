#--> Quadrate-Quadratwurzeln-Calc-in-endlichen-Koerpern
#-> Dieser Rechner berechnet, ob die eingegebene Zahl in dem Körper ein Quadrat ist und entsprechend deren Quadratwurzeln und somit auch die Punkte auf der elliptischen Kurve, falls vorhanden
#-> Input:
# x = zu untersuchende Zahl im Körper
# p = Primzahl des Körpers
# b = Zahl, welche kein Quadrat im körper ist

import math # für den gcd / ggT
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Easy Peasy Lemon's Squeezy")

def quadrate_quadratwurzeln(x, p):
    Quadrat_teiler = int((p-1)/2)

    if(pow(x, Quadrat_teiler, p) == 1):
        print("\nDie eingegebene Zahl ist ein Quadrat.")

        if((p+1)%4 == 0):
            print("\n4 | p+1: ")
            w1 = pow(x, int((p+1)/4), p)
            w2 = p - w1

            print("\nDie Quadratwurzel w1 ist: ", w1, " \nund die Quadratwurzel w2 ist: ", w2)
            return 1

        elif((p-1)%4 == 0):
            print("\n4 | p-1: ") 
            # 2^l *t
            temp_pow = len(format(int((p-1)/2), 'b'))-1
            temp_gcd = pow(2, temp_pow)
            l_temp = math.gcd(int((p-1)/2), temp_gcd) # l_temp = 2^l
            l = len(format(l_temp, 'b'))-1 # aus 2^l muss die Position des most-significant-bit (Bit am weitesten links) geholt werden für das l
            t = int(((p-1)/2)/l_temp) # (p-1)/2 durch 2^l teilen, damit t raus kommt.

            try: # b
                print("\nPlease enter a valid Integer: ")
                b = int(input("b: "))
            except Exception as e:
                print("\nError: ", e)

            if(pow(b, Quadrat_teiler, p) != p-1 and pow(b, Quadrat_teiler, p) != -1): 
                    print("\nb muss ein Nicht-Quadrat sein!")
                    return 0
            
            n = 0
            
            for i in range(l):
                c = (pow(x, pow(2, l-(i+1), p) * t, p) * pow(b, n, p))%p

                print("\nc", i, ": ", c)

                if(c == 1): 
                    n = int(n/2)
                else: 
                    n = int(n/2 + (p-1)/4)
                
                print("\nn", i, ": ", n)
            
            a = (pow(x, int((t+1)/2), p) * pow(b, n, p))%p

            w1 = a
            w2 = p - a

            print("\nDie Quadratwurzel w1 ist: ", w1, " \nund die Quadratwurzel w2 ist: ", w2)

        else:
            print("\n\nSomething is wrong...i can feel it...")
            return 0
    else:
        print("\nDie eingegebene Zahl ist kein Quadrat.")
        return 0
    

# Input:
try: # x
        print("\nPlease enter a valid Integer: ")
        x = int(input("x: "))
except Exception as e:
        print("\nError: ", e)

try: # p
        print("\nPlease enter a valid prime: ")
        p = int(input("p: "))
except Exception as e:
        print("\nError: ", e)

# Aufrufen der Funktion
quadrate_quadratwurzeln(x, p)