Points and Vectors
****
Points:
    - Represent Location
    - Written as (x, y, z)
Vectors:
    - Represent change in location
    - Magnitude and Direction
    - Written as [x
                  y
                  z]
Operating on Vectors:
    - Addition
    - Subtraction
    - Scalar Multiplication

Magnitude and Direction:
    - Magnitude of a vector refers to how much movement it quantifies
    - Direction of a vector refers to where the director's movement is pointed.
    - A unit vector is a vector whose magnitude is 1.
    - A vector's direction can be represented by a unit vector.
    - Normialization is a process of finding a unit vector in the same direction a s given vector. a/[a]

How about multiplying two vectors?
Inner Products:
    - It lets us find the angle between two vectors
    - a.b = |a|*|b|*cos(0)
    - It results a number not a vector
    - 1 <= cos(0)<=1
    - Cauchy Schwarz Inequality
        - a.b <= |a].|b|


**************
gradient descent reference
1. http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html
2. http://mccormickml.com/2014/03/04/gradient-descent-derivation/
3. http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/


************
Gradient Descent Optimizers:
1. Overview of gradient descent optimization algorithms
  http://ruder.io/optimizing-gradient-descent/index.html#whichoptimizertochoose
2. Types of Optimization Algorithms used in Neural Networks and Ways to Optimize Gradient Descent
https://towardsdatascience.com/types-of-optimization-algorithms-used-in-neural-networks-and-ways-to-optimize-gradient-95ae5d39529f


************

Gradient:
   - A vector that is a multi-variable generalization of a derivative(dy/dx)
   - Calculated using partial derivatives

Optimization Algorithms:
  - Help us to minimize(or maximize) an objective function
      - Objective function:
          - A function dependent on the model's internal learnable parameters which are used in computing the target values from the set of predictors
          - Weights and Bias of the neural network are internal learnable parameters

Types of optimization algorithms:
  1. First Order
      - Minimize/Maximize a loss function using its gradient values wrt the parameters
      - Gives us a line tangential to a point on its error surface
      - Example: Gradient Descent
      - Why we need it?
          => Tells us whether the function is decreasing or increasing at a particular point.

  2. Second Order
      - Also called Hessian
      - Minimize/Maximize a loss function
      - A matrix of second order partial derivatives
      - Gives us a quadratic surface which touches the curvature of the error surface.
      - Why we need it?
          => Tells us whether the first derivative is increasing or decreasing.
          => Provides hints regarding function's curvature

Variants of Gradient Descent:
1. Stochastic gradient Descent
2. Minibatch gradient Descent

Algorithms to optimize gradient descent:
1. momentum
2. nesterov accelerated Gradient
3. adagrad
4. adadelta
5. ada

******
Regularization Norms:
1. L1(Lasso)
2. L2(Ridge)(Tikhonov regularization)(Weight Decay)
3. Regularization Term

https://www.quora.com/What-is-the-difference-between-L1-and-L2-regularization-How-does-it-solve-the-problem-of-overfitting-Which-regularizer-to-use-and-when
