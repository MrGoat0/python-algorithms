def solve(line):
    ans,i,ok,N = [c for c in line],0,True,len(line)
    while ok:
        i,ok = 0,False
        ans = [c for c in ans if c != 'X']
        #print("d")
        N = len(ans)
        #print("".join(ans))
        while i < N:
            j,cnt,canR = i+1,1,0
            #print("".join(ans))
            if(ans[i] != 'X'):
                while j < N and ans[i] == ans[j]: 
                    cnt,j = cnt+1,j+1
                if(cnt > 1):
                    ok = True
                    if(cnt%3 == 0):
                        canR = cnt-(cnt//3)
                    elif(cnt%2 == 0):
                        canR = cnt
                    else:
                        canR = cnt-1
                    n = i+canR
                    while i < n:
                        ans[i],i = 'X',i+1
                    #ans = ans[i:n]
            i = j
    print('"'+"".join(ans)+'"')
line = input()
solve(line)