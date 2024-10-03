def shoot_or_retail(word):
    #initial counter
    countS = 0
    countR = 0
    sumR = 0
    sumS = 0
    #start iteration
    for letter in range(0,len(word)-1):
        status="not ok" #initial array
        #check 2 consecutive number
        if word[letter]== "R":
            countR = countR+1
            sumR = sumR+1
            #caseRS
            if word[letter+1]=="S":
                if word[len(word)-1] == "S":
                    countS =countS +1
                    sumS = sumS+1
                status="ok" 
                countR = 0
                countS = 0
                if (word[0]=="R" or word[len(word)-1] == "S"):
                    break
                continue
            #caseRR
            elif word[letter+1]=="R":
                if word[len(word)-1] == "R":
                    countR =countR +1
                    sumR = sumR+1
                if (word[0]=="R" or word[len(word)-1] == "S"):
                    break
                status="ok"
                continue
        
        elif word[letter]=="S":
            countS =countS +1
            sumS = sumS+1
            #caseSS
            if word[letter+1]=="S":
                if word[len(word)-1] == "S":
                    countS =countS +1
                    sumS = sumS+1
                if (word[0]=="R" or word[len(word)-1] == "S"):
                    break
                status="ok"
                continue
            #caseSR
            elif word[letter+1]=="R":
                if word[len(word)-1] == "R":
                    countR =countR +1
                    sumR = sumR+1
                if (word[0]=="R" or word[len(word)-1] == "S"):
                    break
                status="ok"
                continue
    
    
    #check and summary print
    if status=="ok"and countR>=countS:  
        if sumR >= sumS :
            print("Good Boy")
    else:
        print("Bad Boy")



shoot_or_retail("SRSSRRR") #Good boy
shoot_or_retail("RSSRR")   #Bad boy
shoot_or_retail("SSSRRRRS") #Bad boy
shoot_or_retail("SRRSSR")  #Bad boy
shoot_or_retail("SSRSRR") #Good boy
print("==================")
shoot_or_retail("SSSSSS") #Bad boy
shoot_or_retail("RRRRRR") #Bad boy
shoot_or_retail("SRSRSR") #Good boy
print("==================")
shoot_or_retail("SRRRSSR") #Bad boy
shoot_or_retail("SSRRRSS") #Bad boy
shoot_or_retail("SSSRRRSR")#Good boy