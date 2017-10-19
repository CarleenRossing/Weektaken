bestand = open("/home/carleen/Documenten/Protein seq sus scrofa.fasta", 'r').readlines()[1:]

seq = ''
regels = 0


for line in bestand:
    seq = seq + line
    regels = regels + 1

print(len(seq))


aantalD = float(seq.count('D'))
aantalE = float(seq.count('E'))
aantalR = float(seq.count('R'))
aantalK = float(seq.count('K'))
aantalN = float(seq.count('N'))
aantalA = float(seq.count('A'))
aantalC = float(seq.count('C'))
aantalQ = float(seq.count('Q'))
aantalG = float(seq.count('G'))  
aantalH = float(seq.count('H'))
aantalI = float(seq.count('I'))
aantalL = float(seq.count('L'))
aantalM = float(seq.count('M'))
aantalF = float(seq.count('F'))
aantalP = float(seq.count('P'))
aantalS = float(seq.count('S'))
aantalT = float(seq.count('T'))
aantalV = float(seq.count('V'))  
aantalY = float(seq.count('Y'))
aantalW = float(seq.count('W'))


print("het aantal D", aantalD) 
print("het aantal E", aantalE)
print("het aantal R", aantalR)
print("het aantal K", aantalK)
print("het aantal N", aantalN)
print("het aantal A", aantalA)
print("het aantal C", aantalC)
print("het aantal Q", aantalQ)
print("het aantal G", aantalG)
print("het aantal H", aantalH)
print("het aantal I", aantalI)
print("het aantal L", aantalL)
print("het aantal M", aantalM)
print("het aantal F", aantalF)
print("het aantal P", aantalP)
print("het aantal S", aantalS)
print("het aantal T", aantalT)
print("het aantal V", aantalV)
print("het aantal Y", aantalY)
print("het aantal W", aantalW)

gewichtD = aantalD * 133.104 
gewichtE = aantalE * 174.131
gewichtR = aantalR * 174.203
gewichtK = aantalK * 146.189
gewichtN = aantalN * 132.11
gewichtA = aantalA * 89.094
gewichtC = aantalC * 121.154
gewichtQ = aantalQ * 146.146
gewichtG = aantalG * 75.067
gewichtH = aantalH * 155.156
gewichtI = aantalI * 131.175
gewichtL = aantalL * 131.175
gewichtM = aantalM * 149.208
gewichtF = aantalF * 165.192
gewichtP = aantalP * 115.132
gewichtS = aantalS * 105.093
gewichtT = aantalT * 119.119
gewichtV = aantalV * 117.148
gewichtY = aantalY * 181.191
gewichtW = aantalW * 204.228

totaalgewicht = gewichtD + gewichtE + gewichtR + gewichtK + gewichtN + gewichtA + gewichtC + gewichtQ + gewichtG + gewichtH + gewichtI + gewichtL + gewichtM + gewichtF + gewichtP + gewichtS + gewichtT + gewichtV + gewichtY + gewichtW
correctie = 18.016 * len(seq)
totaal_gewicht = totaalgewicht - correctie
print(format(totaal_gewicht, '.3f'))

#water keer de lengte



