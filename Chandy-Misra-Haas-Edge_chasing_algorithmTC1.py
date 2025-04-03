from collections import deque
def edge_chasing(wfg,n,initiator):
    q=deque([])
    for v in wfg[initiator]:
        q.append((initiator,initiator,v))
    print("INITIAL PROBE Q:",list(q))
    while q:
        l=len(q)
        print("Q:",q)
        for _ in range(l):
            init,u,v=q.popleft()
            if init==v:
                return True
            for dest_v in wfg[v]:
                q.append((init,v,dest_v))
    return False

if __name__=="__main__":
    n=5
    process=[1,2,3,4,5]
    prr_adL={1:[1],
            2:[3,4,5],
            3:[5],
            4:[2]}
    print("PROCESS-REQUESTING-RESOURCE-ADL",prr_adL)
    
    rap_adL={1:[2],
             2:[1],
             3:[5],
             4:[3],
             5:[4]}
    print("RESOURCE-ALLOCATED-PROCESS-ADL",rap_adL)

    wfg={i:[] for i in process}
    for key,val in prr_adL.items():
        for resource in val:
            wfg[key].extend(rap_adL[resource])
        wfg[key]=list(set(wfg[key]))
    print("WFG:",wfg)

    initiator=1

    print("HAS CYCLE",edge_chasing(wfg,n,initiator))
