# Vectors2D
It's a small module called to facilitate work with vectors in Python. Adds class Vector2D and operations with vectors in 2 dimensions.
All functions take Vector2D. They also take tuples or lists of int or float with len == 2.
Vectors can be added, subbed, multiplied by other vector or by int/float and more. You can find all the functions of the module below.

---
## Installing
Simply run `pip install vectors2d` from your command line.


## Class:
` Vector2D ` : takes ints, floats, tuple, list when creating. If not given, creates zero vector (0;0). If given only one number, assigns it to "x" coordinate. Also can take other Vector2D object.
### Class methods:
1. `is_zero()` : check if vector is a zero vector.
2. `is_parallel_to(vector)` : check if the vector is parallel to the given vector. Takes Vector2D, list ot tuple.
3. `is_perpendicular_to(vector)` : check if the vector is perpendicular to the given vector. Takes Vector2D, list ot tuple.
4. `is_codirectional_to(vector)` : check if vector is co-directional to the given vector. Takes Vector2D, list ot tuple.


## Global functions:
1. `absolute_vector(vector)` : calculates an absolute value of given vector. Takes Vector2D object, list or tuple. Returns float;
2. `sum_vectors(*vectors)` : returns the sum of all the given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns Vector2D;
3. `sub_vectors(*vectors)` : returns the subtraction of all the given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns Vector2D;
4. `mult_vector(vector, multiplier)` : returns the multiplication of the given vector by the given number (can be int or float). "vector" takes Vector2D object, list and tuple as vector; "multiplier" takes int and float as multiplier. Returns Vector2D;
5. `scalar_mult_vectors(vectors*)` : calculates a scalar multiplication of the given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns float;
6. `get_angle(vector1, vector2)` : returns the angle between the two given vectors in radians. Takes Vector2D objects, lists and tuples in any combination. Returns float;
7. `vector_from_dots(dot1, dot2)` : calculates a vector from the two given dots. Returns Vector2D.

## Examples:
1. **Creating vectors**
   ```
   >>> a = Vector2D(1)  # unit vector a(1;0)
   >>> b = Vector2D(3, 5)  # vector b(3;5)
   >>> c = Vector2D(list)  # vector from list or tuple (must have length 2)
   >>> d = Vector2D(a)  # creates a vector with the same coordinates as the vector a has.
   ```
2. **Getting vector's coorinates**
   1. As a list:
      ```
      >>> a()  # get list of the vector's coordinates
      Output: [1, 0]  
      ```
      > You can use `vector.vector` for the same result
      
   2. Getting exact vector's coordinate:
      ```
      >>> a[0]  # get the "x" coorinate of the vector a
      Output: 1

      >>> b[1]  # get the "y" coordinate of the vector b
      Output: 5
      ```
      > Values also can be changed this way
      
   3. Getting a negative vector:
      ```
      >>> a = Vector2D(3, 2)
      >>> b = -a
      >>> b()
      Output: [-3, -2]
      ```
      
3. **Getting a magnitude (an absolute value) of a vector**
   ```
   >>> abs(a)  # using native Python function
   Output: 1.0
   >>> abs(b)
   Output: 5.830951894845301
   ```
   > Inner function for absolute value is `absolute_vector(vector)`:
   ```
   >>> absolute_vector(a)  # using the function from the module
   Output: 1.0
   >>> absolute_vector(b)
   Output: 5.830951894845301
   ```
4. **Operations with vectors**
   1. Addition
      ```
      >>> c = a + b  # using the mathematical operator  # returns Vector2D
      >>> c()
      Output: [4, 5]
      ```
      > Inner function for addition is `sum_vectors(*vectors)`:
      ```
      >>> c = sum_vectors(a, b)  # using the function of the module  # returns Vector2D
      >>> c()
      Output: [4, 5]
      ```
      > You can use `+=` with another vector to change the vector directly:
      ```
      >>> a += b  # adding b to a and assigning result to a
      >>> a()
      Output: [4, 5]
      ```
      
   2. Subtraction
      ```
      >>> c = b - a  # using the mathematical operator  # returns Vector2D
      >>> c()
      Output: [2, 5]
      ```
      > Inner function for substraction is `sub_vectors(*vectors)`:
      ```
      >>> c = sub_vectors(b, a)  # using the function of the module  # returns Vector2D
      >>> c()
      Output: [2, 5]
      ```
      > You can use `-=` with other vector to change vector directly
      
   3. Multiplication
      1. By other vector:
      ```
      >>> a * b  # scalar multiplication of the vectors using mathematical operator
      Output: 3.0  # returns float
      ```
      > Inner function for scalar multiplication is `scalar_mult_vectors(*vectors)`:
      ```
      >>> scalar_mult_vectors(a, b)  # using function of the module
      Output: 3.0
      ```
      **Note that while you are using mathematical operators to multiply vectors you can't use it more than once in a row, because you can't multiply float by Vector2D:**
      ```
      >>> a * b * c
      Output:
         TypeError: unsupported operand type(s) for *: 'float' and 'Vector2D'
      ```
      > Code `a * (b * c)` will multiply the vector a by a cross product of the vectors b and c. If you need to get cross product of more than two vectors at once, you must use `scalar_mult_vectors(a, b, c)` instead.
      
      2. By number:
      ```
      >>> c = b * 2  # using mathematical operator  # returns Vector2D
      >>> c()
      Output: [6, 10]
      ```
      > Inner function for multiplication by number is `mult_vector(vector, modifier)`:
      ```
      >>> c = mult_vector(b, 3)  # returns Vector2D
      >>> c()
      Output: [9, 15]
      ```
      > You can use `*=` *only* with other vector to change vector directly
      
   4. Getting angle between vectors:
      ```
      >>> get_angle(a, b)  # returns angle between vectors in radians
      Output: 1.0303768265243125
      ```
      *Returns angle in radians*
      
5. **Boolean operations**
   1. Check if vector is zero vector:
      ```
      >>> a = Vector2D(0, 0)
      >>> a.is_zero()
      Output: True
      
      >>> b = Vector2D(1, 2)
      >>> b.is_zero()
      Output: False
      ```
      
   2. Check if vector is parallel with other vector:
      ```
      >>> a = Vector2D(1, 0)
      >>> b = Vector2D(-3, 0)
      >>> a.is_parallel_to(b)  # takes Vector2D, list or tuple
      Output: True
      
      >>> c = Vector2D(3, 7)
      >>> c.is_parallel_to(b)
      Output: False
      ```
   3. Check if vector is perpendicular with other vector:
      ```
      >>> a = Vector2D(3, 0)
      >>> b = Vector2D(0, 4)
      a.is_perpendicular_to(b)
      Output: True
      
      >>> c = Vector2D(1, 5)
      >>> c.is_perpendicular_to(b)
      Output: False
      ```
      

### TODO list:
- [x] Two-dimensional vector class
- [x] Vector operations 
  - [x] Sum
  - [x] Sub
  - [x] Mult by number
  - [x] Scalar multilpication with vector
  - [ ] Power by number
- [x] Vector calculations
  - [x] Absolute value - `absolute_vector()`
  - [x] Angle between vectors - `get_angle()`
  - [x] Vector from two dots - `vector_from_dots()`
  - [x] Is zero - `vector.is_zero()`
  - [x] Is (not) parallel - `vector.is_parallel_to()`
  - [x] Is perpendicular - `vector.is_perpendicular_to()`
  - [x] Is co-directional - `vector.is_codirectional_to()`
- [x] Assignment operations
  - [x] +=
  - [x] -=
  - [x] \*= (only for numbers)
  - [ ] \**=
  - [ ] /= (only for numbers)
- [x] Other
  - [x] Negative vector
