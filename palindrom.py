 #Recursive veri yapısı ile palindrom örneği
 #Python 2.x
 
def palind(kelime):
    kelime = list(kelime)
    if len(kelime) > 1:
        if kelime.pop(0) != kelime.pop():
            print "Palindrom bir kelime değildir !"
        else:
            return palind(kelime)
    else:
        print  "Evet Palindrom bir kelime"
        

word = raw_input("Palindrom mu ? : ")
palind(word)            
