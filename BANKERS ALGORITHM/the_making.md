## BANLER'S ALGORITHM
- Developed by `Edsger Wybe Dijkstra`
- why the name ***banker's algorithm?***
---
## ALGORITHM

1. **Initialization:**
   - Let **Work** and **Finish** be vectors of length **m** and **n** respectively, where:
     - **m** = number of available resources.
     - **n** = number of processes.
   - Set **Work = Available**, meaning **Work** is initialized with the currently available resources.
   - Set **Finish[i] = false** for all processes, indicating that no process has completed initially.

2. **Find an index `i` such that:**
   - **a.** **Finish[i] == false** (The process has not finished yet).
   - **b.** **Need[i] ≤ Work** (The remaining resource requirements of process `i` can be met with the currently available resources in `Work`).
   
   If such an index `i` exists, proceed to step 3. If no such process exists, go to step 4.

3. **Work and Finish Update:**
   - **Work = Work + Allocation[i]**: Add the resources allocated to process `i` to the **Work** vector, representing that the resources held by process `i` are now available for use by other processes.
   - **Finish[i] = true**: Mark process `i` as finished, as it can now complete its execution.
   - Go back to step 2.

4. **Check for Safe or Unsafe State:**
   - If **Finish[i] == true** for **all processes** `i`, then the system is in a **safe state**, meaning it is possible to allocate resources and all processes can eventually complete.
   - If **Finish[i] == false** for **all processes**, then the system is in an **unsafe state**, meaning some processes cannot complete, and there is a possibility of a **deadlock**.
---