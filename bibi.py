
def n_over_m(num, den) :

    if (num == 0): 
        return "0"
 
    initial = num // den 
 
    res = "" 
  
    res += str(initial) 
 
    if (num % den == 0): 
        return res 
 
    res += "."
 
    rem = num % den 
    mp = {} 

    index = 0
    repeating = False
    while (rem > 0 and not repeating) :

        if ( rem in mp): 

            index = mp[rem] 
            repeating = True
            break
         
        else:
            mp[rem] = len(res) 
 
        rem = rem * 10

        temp = rem // den 
        res += str(temp )
        rem = rem % den 

    if (repeating) : 
        res += ")"
        x = res[:index]
        x += "("
        x += res[index:]
        res = x
     
    return res 
 
if __name__ =="__main__":
    N, M = map(int, input().split())
    print(n_over_m(N, M))