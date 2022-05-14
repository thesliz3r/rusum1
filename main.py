#verilen mailin qiymeti manual input

print("Malin Ilkin Qiymeti:")
malinQiymeti = input()

#print("Rusum:")
#y = input()

#eger 300+dusa malin qiymeti -300$
tax=int(300)
malinQiymeti=int(malinQiymeti)
if malinQiymeti > tax:
    rusum=(malinQiymeti-tax)*0.36
else:
    rusum=0

if rusum > 0:
    print("Malin Rusuma dushen hissesi", rusum, "azn")

#(x-300)*0.36

#(x-300)0.36 +malin ilkin qiymeti

#1.7((x-300)0.36+ malin ilkin qiymeti)

totalDollar = int(malinQiymeti)+int(rusum)

kurs = 1.7

manat= totalDollar * kurs

text = ("Malin Azn Qiymeti:", round(manat, 2) ,"Azn")
text = str(text).upper()

print(text)
