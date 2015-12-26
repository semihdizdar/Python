disk_sayisi = input("Disk sayısını giriniz : ")

def degistir(n,x,z,y):

    if (n>1):

        degistir(n-1, x, y, z)

        degistir(1, x, z, y)

        degistir(n-1, y, z, x)

    else:

        print "Diski",x, "çubuğundan", z, "çubuğuna koy"

            



def hanoi(disk):

    if (disk <= 0):

        print "Disklerin sayısı sıfırdan küçük olamaz ! "

    else:

         degistir(disk,"A", "C" , "B")

   





hanoi(disk_sayisi)

        
