# Dining Philosopher Problem 

N philosophers seated around a circular table. There is one chopstick between each philosopher. 

A philosopher must pick up its two nearest chopsticks in order to eat.

A philosopher must pick up first one chopstick, then the second one, not both at once.

## Using Semaphores

Each chopstick is governed by a mutual exclusion semaphore that prevents any other philosopher from picking up the chopstick when it is already in use by another philosopher.

```
semaphore chopstick[5]; // initialized to 1
```

Each philosopher grabs/picks-up a chopstick 'i' by P(chopstick[i]) 

Each philosopher releases/puts-down a chopstick 'i' by V(chopstick[i])

### Pseudo-Code

```
while(1) {
// obtain the two chopsticks to my immediate right and left
P(chopstick[i]);
P(chopstick[(i+1)%N];
// eat
// release both chopsticks
V(chopstick[(i+1)%N];
V(chopstick[i]);
}
```

### DeadLock

Each philosopher grabs its right chopstick first causes each semaphore’s value to decrement to '0' each philosopher then tries to grab its left chopstick.

Each semaphore’s value is already '0', so each process will block on the left chopstick’s semaphore.

These processes will never be able to resume by themselves - we have deadlock!

Some deadlock-free solutions:

1. Allow at most 4 philosophers at the same table when there are 5 resources.
2. Odd philosophers pick first left then right, while even philosophers pick first right then left
3. Allow a philosopher to pick up chopsticks only if both are free. This requires protection of critical sections to test if both chopsticks are free before grabbing them.


#### Note : Semaphore is a signalling approach, while monitor or mutex is a lock based approach.

Semaphores: wait() & signal()
Monitor/Mutex: acquire() & release()

A monitor ensures that only one process/thread at a time can be active within a monitor.

If two processes want to access the monitor, then access is mutually exclusive and only one process at a time can modify the value of counter.

## [Using Monitors](https://rosettacode.org/wiki/Dining_philosophers#Python) 

```
monitor DP 
{
    status state[5];
    condition self[5];
    
    Pickup(int i) {
        state[i] = hungry;
        test(i);
        if(state[i]!=eating) self[i].wait;
    }
    Putdown(int i) {
        state[i] = thinking;
        test((i+1)%5);
        test((i-1)%5);
    }

    test(int i) {
        if (state[(i+1)%5] != eating && state[(i-1)%5] != eating && state[i] == hungry) {
        state[i] = eating;
        self[i].signal();
        }
    }
    init() {
        for i = 0 to 4
        state[i] = thinking;
    }
} // end of monitor
```

Deadlock is avoided by never waiting for a fork while holding a fork (locked): 

Procedure is to do block while waiting to get first fork, and a nonblocking acquire of second fork.  If failed to get second fork, release first fork, swap which fork is first and which is second and retry until getting both.