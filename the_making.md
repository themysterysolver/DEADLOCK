## PROBLEM STATEMENT
##### Simulation of Deadlock Detection:

- Write a program in Python, Java, or C++ to simulate deadlock detection in a distributed system. The program should:
    - Accept input for processes, resources, and wait-for relationships.
    -  Implement a deadlock detection algorithm (e.g., ***wait-for graph analysis*** or ***Chandy-Misra-Haas***).
    - Output whether a deadlock exists and the processes involved.
---
## NOTES
- **RAG**:Resource allocation graph have both `P` *process* node and `R` *resouce*  node,which involves deetcing cycle when resouce have *multiple instances*. 
<br>
- **WFG**:Wait for graph just gives dependecny relationship between `P` with the removal of `R` in ***RAG***.This involves detection when `R` has a *single instance*.
<br>
- **Wait for Graph analysis** simpy talks about *deadlock detection* with existance of **cycle** in *wait for* relation.
    - we can use ***topological sort*** to detect cycles using `KAHN'S ALGORITHM` which uses `BFS`.
---
### KHAN'S ALGORITHM
- what is `Topo sort?`
    - It is the *linear ordering* of `vertices` in a `DAG`such that every node `u` appears beofre `v` in ordering `u->v`.
    - Only possible for graph with no cycles
- **KHAN'S ALGORITHM**:
    - **STEP-1**:Compute the `indegree` of all the vertices.
    - **STEP-2**:Node with **0** indegree is added to the `q`(***queue***).
    - **STEP-3**:`deq` a node,reduce the indgree of neighbours.
        - if the indegree of neighbours become zero add them to `q`
    - **STEP-4**:len(TOPO_SORT)\<len(VERTICES) then we have **cycle**
---

### CHANDY MISRA HAAS
##### EDGE CHASING ALGORITHM
- It is a algorithm which works with `probe`.
- Let's take  a `wfg`,here each *process* `p` can belong to any sites `Si`.
- A probe is passed down form process `pi` to `pj` (***pi-->pj***)
- A probe is defined as a `triplet tuple`=>`(i,j,k)`
    - **i**=>initator process
    - **j**=>sender process
    - **k**=> reciver process
- We said we get a ***loop*** if $i==k$.
---