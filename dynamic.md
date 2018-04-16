Multistage decision problems
******

The key bits of dynamic programming are "overlapping sub-problems" and "optimal substructure". These properties of a problem mean that an optimal solution is composed of the optimal solutions to its sub-problems. For instance, shortest path problems exhibit optimal substructure. The shortest path from A to C is the shortest path from A to some node B followed by the shortest path from that node B to C.

In greater detail, to solve a shortest-path problem you will:

find the distances from the starting node to every node touching it (say from A to B and C)
find the distances from those nodes to the nodes touching them (from B to D and E, and from C to E and F)
we now know the shortest path from A to E: it is the shortest sum of A-x and x-E for some node x that we have visited (either B or C)
repeat this process until we reach the final destination node
Because we are working bottom-up, we already have solutions to the sub-problems when it comes time to use them, by memoizing them.

Remember, dynamic programming problems must have both overlapping sub-problems, and optimal substructure. Generating the Fibonacci sequence is not a dynamic programming problem; it utilizes memoization because it has overlapping sub-problems, but it does not have optimal substructure (because there is no optimization problem involved).

http://mat.gsia.cmu.edu/classes/dynamic/node2.html#SECTION00020000000000000000

Deterministic dynamic:
  function(state, decision)=>immediate payoff, next state
Stochastic dynamic:
  function(probabilistic state || probabilistic decision)=>immediate payoff, next state

decision => sequence of decision steps over time
decision => valuefunction1(state1) + valuefunction2(state2) + ...

Bellman equation:
The significance of Bellman equation is that it gives a way to reason about the maximization the utility of by an agent over a time horizon. Often the problems that we seek to solve are "farming" problems where we seek to maximize the overall utility of a resource over a period of time as opposed to harvesting the resource all at once.

The other way of looking at Bellman's equation is that this is a way of balancing the local exploitation (in the state space) vs exploring more of the state space so that an optimal harvesting policy can be generated. This is applicable in reinforcement learning contexts.

https://joshgreaves.com/reinforcement-learning/understanding-rl-the-bellman-equations/
policy iteration vs value iteration
