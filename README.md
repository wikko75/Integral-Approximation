# Integral-Approximation
Using the **Monte Carlo** method. <br><br>
## Algorithm steps: <br>
1. Generate independently and uniformly **n** points from a rectangle **[a, b] x [0, M]** for a given ***M*** **>= sup{ f(x) : x ∈ [a,b] }** <br>
2. Count a number of generated points that lay under the curve of a function **f(x)** <br>
    A point **(x, y)** lies under the curve of **f(x)** if **y <= f(x)** ( = **C** ) <br>
3. The approximation is **C/n * ( b−a ) * M**, where **( b−a ) * M** is an area of the rectangle <br>

## Sample Result:<br>
- **f(x) = x^1/3**
- **a = 0**<br> **b = 8**<br> **M = 3** <br><br>Which gives: **[0, 8] x [0, 3]**<br><br>
- **Blue points** - repeats of the algorithm for given **n**
- **Red points** - average value of repeats for given **n** <br><br>
![Figure_2](https://user-images.githubusercontent.com/102422062/221363288-fa1acd0f-5729-44c2-b541-58e29be28c7f.png) <br>

- The **actual** value of such integral of **f(x)** is **12**!

