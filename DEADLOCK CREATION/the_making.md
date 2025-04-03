## DEADLOCK DETECTION IN JAVA
- Run the `Deadlock.java` program
- What happens in the program is that `t1` thread acquires `obj1` and waits for `t2` to acquire `obj2` now which won't be accessible for `t1` after sleep
- Similarly it happens for `t2`
- we can detect deadlock with help of certain tools
  - **`jps` command**:java process status gived ***PID** along with *class Name*
  - **`jstack <PID>` command**:gives you all thread running in for that `PID`