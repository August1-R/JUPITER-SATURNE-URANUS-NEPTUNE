import time
nombreTest = 0
print (time.asctime(time.localtime(time.time())))  # Afficher la date en format lisible



for N in range(0,10):
    #print("A")
    for E in range(0,10):
        #print("BB")
        if N != E:
            for U in range(0,10):
                #print("BBB")
                if U != N and U !=E:
                    for J in range(0, 10):
                        #print("CCCC")
                        if J != N and J !=E and J != U:
                            for R in range(0, 10):
                                #print("DDDDD")
                                if R != N and R != E and R != U and R != J:
                                    for S in range(0, 10):
                                        #print("E")
                                        if S != N and S != E and S != U and S != J and S != R:
                                            for P in range(0, 10):
                                                #print("F")
                                                if P != N and P != E and P != U and P != J and P != R and P != S:
                                                    for I in range(0, 10):
                                                        #print("G")
                                                        if I != N and I != E and I != U and I != J and I != R and I != S and I != P:
                                                            for T in range(0, 10):
                                                                #print("H")
                                                                if T != N and T != E and T != U and T != J and T != R and T != S and T != P and T != I:
                                                                    for A in range(0, 10):
                                                                        #print("I")
                                                                        if A != N and A != E and A != U and A != J and A != R and A != S and A != P and A != I and A != T:
                                                                            nombreTest += 1
                                                                            #print("titi")
                                                                            JUPITER = int(str(J) + str(U) + str(P) + str(I) + str(T) + str(E) + str(R))
                                                                            SATURNE = int(str(S) + str(A) + str(T) + str(U) + str(R) + str(N) + str(E))
                                                                            URANUS = int(str(U) + str(R) + str(A) + str(N) + str(U) + str(S))
                                                                            NEPTUNE = int(str(N) + str(E) + str(P) + str(T) + str(U) + str(N)+ str(E))
                                                                            if JUPITER + SATURNE + URANUS == NEPTUNE:
                                                                                print(time.asctime(time.localtime(time.time())))  # Afficher la date en format lisible
                                                                                print(nombreTest)
                                                                                print("La solution est : ", " N=", N," E=", E, "U=", U," J=", J, " R=", R," S=", S, " P=", P," I=", I, " T=", T," A=", A)
print(time.asctime(time.localtime(time.time())))
print(nombreTest)