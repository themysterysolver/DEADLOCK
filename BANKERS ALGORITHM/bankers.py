def is_safe(process,available,max,alloc):
    path=[]
    n=len(process)
    m=len(available)

    need=[[max[i][j]-alloc[i][j] for j in range(m)] for i in range(n)]

    finish=[False]*n
    safe_seq=[]
    while len(safe_seq)<n:
        found=False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j]<=available[j] for j in range(m)):
                    for j in range(m):
                        available[j]+=alloc[i][j]
                    safe_seq.append(process[i])
                    finish[i]=True
                    found=True
                    break
        if not found:
            break
    if len(safe_seq)==n:
        return "[SAFE]:"+'->'.join(safe_seq)
    else:
        return "[UNSAFE]:NO PATH FOUND!"

if __name__=="__main__":
    process=['P0','P1','P2','P3','P4']
    allocation = [
        [0, 1, 0], 
        [2, 0, 0], 
        [3, 0, 2], 
        [2, 1, 1], 
        [0, 0, 2]  
    ]
    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3] 
    ]
    available = [3, 3, 2]
    print("Is safe:",is_safe(process,available,maximum,allocation))