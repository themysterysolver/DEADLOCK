### DEADLOCK SIMULATION AND DETECTION🔍
- This repo focus on 2 algorithms to detect deadlock from `WFG`(*wait-for-graph*) and a small `JAVA` program that creates a deadlock between *2 threads* and detecting with JAVA tools. 
- We have implemented **2** algorithm in `py` to detect *deadlock* in a ds system
  - Wait for graph analysis🕸️
    - `wfg.py` has a ***cycle** in it which is the system for `NOTES/TC1.jpeg`
    - `wfgWithoutCycle.py` ***doesn't*** have a cycle which is in `NOTES/TC2.jpeg`  
  - Chandy-Misra-Haas-Edge_chasing_algorithm⭕
    -  `Chandy-Misra-Haas-Edge_chasing_algorithmTC1.py` has cycle
    - `Chandy-Misra-Haas-Edge_chasing_algorithmTC2.py` doens't have cycle
- `DEADLOCK CREATION/Deadlock.java` created a deadlock using threads which is viewd with help of `jps` and `jstack`
### 📁REPO STRUCTURE
```.
├── Chandy-Misra-Haas-Edge_chasing_algorithmTC1.py
├── Chandy-Misra-Haas-Edge_chasing_algorithmTC2.py
├── DEADLOCK CREATION
│   ├── Deadlock.java
│   ├── out
│   │   └── production
│   │       └── DEADLOCK CREATION
│   │           ├── Deadlock.class
│   │           └── the_making.md
│   └── the_making.md
├── NOTES
│   ├── KHAN'S ALGORITHM.jpg
│   ├── TC1.jpeg
│   └── TC2.jpeg
├── the_making.md
├── wfg.py
└── wfgWithoutCycle.py
```
