#phantom deadlock
import threading
import time
from collections import deque

prr_adL={1:[1],2:[]}
rap_adL={1:[2],2:[1]}
lock=threading.Lock()

def build_wfg():
    wfg={i:[] for i in process}
    for key,val in prr_adL.items():
        for resource in val:
            wfg[key].extend(rap_adL[resource])
        wfg[key]=list(set(wfg[key]))
    print("WFG:",wfg)
    return wfg

def detect_deadlock(wfg):
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

def process2_req():
    time.sleep(1)
    with lock:
        prr_adL[2]=[2]
def process1_release_late():
    time.sleep(5)
    with lock:
        rap_adL[2]=[]

def detection():
    for i in range(5):
        time.sleep(1)
        wfg=build_wfg()
        print("IS THERE DEADLOCK DURING REQ,REPLY:",detect_deadlock(wfg))

if __name__=="__main__":
    n=2
    process=[1,2]
    
    print("PROCESS-REQUESTING-RESOURCE-ADL",prr_adL)
    print("RESOURCE-ALLOCATED-PROCESS-ADL",rap_adL)

    wfg=build_wfg()

    t1=threading.Thread(target=process2_req)
    t2=threading.Thread(target=process1_release_late)
    t3=threading.Thread(target=detection)

    t1.start()
    t2.start()
    t3.start()

    

