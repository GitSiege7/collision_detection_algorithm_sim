# Collision Detection Algorithm Simulation
An interactive minimal particle simulation that displays the differences in performance between three different collision detection algorithms.

### Note on use
I recommend reading through each one of these explanations about the algorithms before attempting to observe them as you will be able to better see their differences.

#### Controls
- 0 - toggles HUD (in case you just wanna watch the pretty colors)
- 1 - activates B-F algorithm
- 2 - activates S&P algorithm
- 3 - activates GRID algorithm
- ARROW KEYS - changes the direction of simulated gravity (default: down)
- SPACE - turns off simulated gravity

## Three Algorithms
### Brute Force (B-F) (default)
#### Algorithm Explanation
The brute force algorithm utilizes the very simple, and inefficient, method of simply checking every particle against every other particle in the simulation. Though for small numbers of particles (likely less than two hundred) this may suffice with a decent processing power, it quickly grows slow and unstable with higher quantities of bodies.

This algorithm works well with small numbers of bodies and is very easy to implement. Simply iterate a collision detection function over every pair of bodies in the simulation.

#### Observations
You'll notice when using this algorithm that it is slow... but it is consistent. Due to it's simplicity and independence from partitioning tricks (more on those in the next algorithm), this algorithm performs relatively similar whether the bodies are dense and in close proximity, or spread across the screen evenly.

#### Time Complexity
This implementation has a time complexity of **O(n^2)**, given that n is the number of bodies in the simulation.


### Sweep & Prune (S&P)
#### Algorithm Explanation
The sweep and prune algorithm uses a more thoughtful approach to determining which bodies could need to be compared for collision detection.

Beyond a certain distance, we can guarantee that two bodies will not collide because they are simply too far away to. The B-F algorithm checked this by going through each pair and checking its distance... very... slowly. But if we isolate and sort all of the particles by one axis, x or y, we can determine if it is possible for them to collide. Since the hard-coded resolution for this project has an aspect ratio of 16:9, it makes more sense to me to sort by the x axis since it is longer, allowing for a higher chance of space between any two balls. This is important for the complexity of this algorithm.

First, the particles are sorted by their chosen axis, in our case the x axis. Then, each particle is compared with the ones following them in the list, and if their x coordinates intersect (accounting for their radius) they are grouped together to be checked for collisions. Because no matter the y coordinate of the two particles, if their x coordinates don't overlap, we can guarantee they don't collide, greatly eliminating unnecessary checks. So if one particle is compared with the one after it and they overlap, they are added to a list together and the active checking range is expanded to contain both of them, and the next particle is checked against this active range. If that particle overlaps the new active range, it is added and the active range is further expanded until no particle is found overlapping in that active range. A new active range begins with the next particle not yet in any list (it has no need to go back and check the ones added to the last active range). Each active range is then iterated through independently and collision-checked.

#### Observations
For a disperse, even field of particles, there are noticeable performance increases when using S&P rather than B-F. The drawback, however, comes with the instability of the algorithm. When the particles are grouped tightly against the left or right wall, the x coordinates of the balls are compact leading to many more checks, and performance as bad or worse than the B-F algorithm. The reason it is often worse in this case is the additional processing required not just for the excessive collision checks, but also for the memory and processing of storing all the data necessary for the S&P algorithm that mostly turns out to be worthless.

#### Time Complexity
The time complexity of the sweep and prune algorithm is typically around **O(nlog(n))**, but tanks to **O(n^2)** in the case discussed in the observations section.

### Grid Space Partitioning (GRID)
#### Algorithm Explanation
Now we're talking. This algorithm runs circles around the other two.

Space partitioning, with logic similar to the sweep and prune algorithm, aims to search the screen space, divide up particles by their position in that space, and eliminate checks between particles too far apart to possibly collide. The way it does this, however, is by dividing the screen into a grid and assigning each particle to a square in that grid (I'll call it a space) based on it's position. Then, checking each particle in a space against every particle in the eight spaces surrounding it and the one it is in.

This algorithm improves on the last in that it narrows down the collision checks by both axes instead of just one. By checking only the particles in the surrounding spaces, no two particles with significantly different x coordinates or y coordinates will be collision-checked, vastly improving the performance of the simulation with higher particle counts.

#### Observations
Overall, the performance difference between this algorithm and the two before is night and day. The algorithm is much more stable compared to the S&P algorithm, and much more performant than the B-F algorithm (and the S&P).
Naturally, it does have limitations, and can slow down with more bodies and highly dense areas resulting in more checks. Like the S&P algorithm, it performs best when the particles are evenly dispersed.

#### Time Complexity
The average time complexity for space partitioning is **O(n)** assuming evenly distributed particles. 

It is also worth noting the memory complexity, as the grid is stored as a list[of lists[of lists[]]]. My implementation creates grids 10px, meaning 160x90 lists, or 14,400 lists, and relatively little of that space is actually used.

## Cloning & Requirements
### Requirements
- [Python3](python.org)
- [pygame](https://www.pygame.org/wiki/GettingStarted) 2.6.1 or newer
- [uv](https://github.com/astral-sh/uv)

### Cloning
To clone:
```
git clone https://github.com/GitSiege7/collision_detection_algorithm_sim
cd collision_detection_algorithm_sim
```

To run:
```
./run.sh
```
