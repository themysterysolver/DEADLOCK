from collections import deque
def khan(wfg,n):
    topoSort=[]
    indegree={i:0 for i in wfg.keys()}
    print("INDEGREE BEFORE:",indegree)

    for key,val in wfg.items():
        for v in val:
            indegree[v]=indegree.get(v,0)+1
    print("INDEGREE AFTER:",indegree)
    q=deque([])
    for key,val in indegree.items():
        if val==0:
            q.append(key)
    print("QUEUE:",q)
    if len(q)==0:
        return True
    while q:
        node=q.popleft()
        topoSort.append(node)
        for neighbour in wfg[node]:
            indegree[neighbour]-=1
            if(indegree[neighbour]==0):
                q.append(neighbour)
    return len(topoSort)<n

if __name__=="__main__":
    n=5
    process=[1,2,3,4,5]
    prr_adL={1:[1],
            2:[2,5],
            3:[3],
            4:[4],
            5:[]}
    print("PROCESS-REQUESTING-RESOURCE-ADL",prr_adL)
    
    rap_adL={1:[2],
             2:[3],
             3:[],
             4:[1],
             5:[5]}
    print("RESOURCE-ALLOCATED-PROCESS-ADL",rap_adL)

    wfg={i:[] for i in process}
    for key,val in prr_adL.items():
        for resource in val:
            wfg[key].extend(rap_adL[resource])
        wfg[key]=list(set(wfg[key]))
    print("WFG:",wfg)
    print("HAS CYCLE",khan(wfg,n))
