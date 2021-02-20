# Bounded Buffer Problem

No. of Buffers will be bounded , i.e, it'll have a finite number of values.

Buffer is nothing but a place where you can store an item.

Consider there are N no. of Buffers, where each and every buffer can store one value. So the total system can hold N values.

## Variables:

1. mutex: Mutual Exclusion Variable.
    It can have the value 0 or 1.

    When mutex = 1, it means buffer space is free and not occupied by some other process and it can be accessed. The critical section is free from any process access.

2. empty: Number of Empty Buffers

3. full: Number of Full Buffers

Initially,

mutex = 1
empty = N
full = 0

## Pseudo-Code

```
def Producer:
    do{
        ...
        Produce an Empty Item in nextP
        ...
        wait(empty)
        wait(mutex)
        ...
        Add nextP to Buffer
        ...
        signal(mutex)
        signal(full)
    }while(True)

def Consumer:
    do{
        wait(full)
        wait(mutex)
        ...
        Remove an item from Buffer to nextC
        ...
        signal(mutex)
        signal(empty)
        ...
        Consume the item in nextC 
    }while(True)

def wait: It will decrement the value of the variable, if it is already minimum(of that particular variable) it'll hold the process 
def signal:  It will increment the value of the variable, if it is already maximum(of that particular variable) it'll hold the process

```
