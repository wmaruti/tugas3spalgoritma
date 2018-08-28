# tentukan batas bilangan prima yang akan dicari
Angka = int(input('Jumlah bilangan : '))

#perulangan untuk mengecek bilangan prima
for num in range(2,42):
    prima = True
    for i in range(2,num):
        if (num%i==0):
            prima = False
    if prima:
       print (num)
