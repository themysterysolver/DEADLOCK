#phantom deadlock
if __name__=="__main__":
    n=2
    process=[1,2]
    prr_adL={1:[1],
            2:[]}
    print("PROCESS-REQUESTING-RESOURCE-ADL",prr_adL)
    
    rap_adL={1:[2],
             2:[1]}
    print("RESOURCE-ALLOCATED-PROCESS-ADL",rap_adL)

    wfg={i:[] for i in process}
    for key,val in prr_adL.items():
        for resource in val:
            wfg[key].extend(rap_adL[resource])
        wfg[key]=list(set(wfg[key]))
    print("WFG:",wfg)

    
