if __name__=="__main__":
    
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

    wfg={i:[] for i in prr_adL.keys()}
    for key,val in prr_adL.items():
        for resource in val:
            wfg[key].extend(rap_adL[resource])
        wfg[key]=list(set(wfg[key]))
    print("WFG:",wfg)
