#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    Line 1 => O(1)
    Line 2 => O(n * n * n) => O(n ^ 3)
    Line 3 => O(1)

    Adding it all up => O(n ^ 3 + 2) => O(n ^ 3)
    => Cubic Time

b)
    Line 1 => O(1)
    Line 2 => O(n)
    Line 3 => O(1)
    Line 4 => O(n * n)
    Line 5 => O(1)
    Line 6 => O(1)

    Adding it all up => O(n ^ 2 + n + 4) => O(n ^ 2)
    => Quadratic Time

c)
    Line 2 => O(1)
    Line 3 => O(1)
    Line 5 => O(1 + n)

    Adding it all up => O(n + 3) => O(n)
    => Linear Time

## Exercise II

a)  Algorithm

    1. Declare a function *find_floor_f* that takes an argument *n_story*
    2. Initiate a variable *current_story* to 0
    3. Write a while loop to loop until *current_story is equal to n_story*
    4. In the while loop check *if egg will be broken if dropped*
    5. *If broken* return current_story that is the value of f

b) Runtime complexity

    Line 1 => O(1)
    Line 2 => O(1)
    Line 3 => O(n)
    Line 4 => O(1)
    Line 5 => O(1)

    Add it up => O(n + 4) => O(n)
    => Linear Time
