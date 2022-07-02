def solve(s):
    ans,charCnt,lo,hi,odd,even = [],[0 for i in range(256)],0,len(s)-1,0,True
    for c in s:
        charCnt[ord(c)] += 1 
    for i in range(256):
        if charCnt[i]%2 != 0:
            odd += 1

    if(len(s)%2 != 0):
        if(odd == 1):
            ans = ['' for i in range(len(s))]
            for i in range(256):
                if charCnt[i]%2 != 0:
                    charCnt[i] -= 1
                    ans[len(s)//2] = chr(i)
                while(charCnt[i] > 0):
                    ans[lo] = chr(i)
                    ans[hi] = chr(i)
                    lo,hi = lo+1,hi-1
                    charCnt[i] -= 2

    else:
        i = 0
        while i < 256 and even:
            even = charCnt[i]%2 == 0
            i += 1
        #print(even)
        if(even):#todas las letras deben estar un numero par de veces
            ans = ['' for i in range(len(s))]
            for i in range(256):
                while(charCnt[i] > 0):
                    
                    ans[lo] = chr(i)
                    ans[hi] = chr(i)
                    lo,hi = lo+1,hi-1
                    charCnt[i] -= 2


    return ans

def main():
    line = input()
    ans = solve(line)
    print(-1 if len(ans) == 0 else "".join(ans))


main()