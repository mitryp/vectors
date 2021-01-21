## Vectors2D
It's a small module that adds class Vector2D and operations with vectors.
All functions take Vector2D. Also they take tuples or lists with len == 2 of int/float.
Vectors can be added, multiplied by other vector or by int/float and you can get angle between two vectors.
---
# Classes:
` Vector2D ` : takes tuple or list of coordinates with length 2 when creating. If not given, creates zero vector (0;0). Also can take other Vector2D object.


# Functions:
1. `absolute_vector(vector)` : calculates absolute value of given vector. Takes Vector2D object, list or tuple. Returns float;
2. `add_vectors(*vectors)` : adds all the given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns Vector2D;
3. `sub_vectors(*vectors)` : subtracts all the given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns Vector2D;
4. `mult_vector(vector, multiplier)` : multiplies given vector by given number (can be int or float). "vector" takes Vector2D object, list and tuple as vector; "multiplier" takes int and float as multiplier. Returns Vector2D;
5. `scalar_mult_vectors(vectors*)` : calculates scalar multiplication of given vectors. Takes Vector2D objects, lists and tuples in any combination. Returns float;
6. `get_angle(vector1, vector2)` : returns angle between two given vectors in radians. Takes Vector2D objects, lists and tuples in any combination. Returns float;
7. `vector_from_dots(dot1, dot2)` : calculates vector from two given dots. Returns Vector2D.

## TODO list:
- [x] Vector object with 2 coordinates
- [x] Vector operations 
  - [x] Sum
  - [x] Sub
  - [x] Mult by number
  - [x] Mult by vector
  - [ ] Power by number
- [x] Vector calculations
  - [x] Absolute value
  - [x] Angle between vectors
  - [x] Vector from two dots
  - [ ] Is zero
- [ ] Assignment operations
  - [ ] +=
  - [ ] -=
  - [ ] *=
  - [ ] **=
  - [ ] /= (for numbers only)
- [ ] Other
  - [ ] Negative vector (Urgent)
