Algorithms & Data Structures for Beginners - NeetCode
# Arrays
## RAM - Random Access Memory
    - waht is the array structure?
        - Byte = 8bits(0 or 1)
        - RAM = Random Access Memory --> Addressable Memory + Value
        - Array = Contiguous Memory
        - Arrays = ASCII Table + 1byte = 8bits = 2^8 = 256

## Static Arrays
    - Reading Data, Writing Data
    - MyArray = [1,3,5] --> RAM = value(1, 3, 5) + address(0, 4, 8) 
        - 0(1) --> Constant Time --> Random Access Memory
        - i = 0 --> MyArray[0] = 1
        - for / while loop --> O(n) --> Linear Time
        - Static Array = Fixed Size
        - Dynamic Array = Resizable Array 
    - Warst Case Time Complexity = O(n)

| Operation                | Big-O Time |
|:-------------------------|-----------:|
| reading/ writing element |       O(1) |
| Insert/Remove End        |       O(1) |
| Insert Middle            |       O(n) | 
| Remove Middle            |       O(n) | 

## Dynamic Arrays
    - python --> myArr = []
    - Java --> List<Integer> myArr = new ArrayList<Integer>();
    - Offerated System
    - increase system --> alocate system : O(n)
    - Amortized Time Complexity = O(1)
    - Warst Case Time Complexity = O(n)
    - size 8 Array -> 15 <= 2 * 8 
        - This means O(2 * n) = O(n)

## Stacks
| Operation     | Big-O Time |
|:--------------|-----------:|
| Push          |       O(1) |
| Pop           |       O(1) |
| Peek / Top    |       O(1) | 

    - LIFO - Last In First Out
