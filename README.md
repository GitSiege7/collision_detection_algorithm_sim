# Collision Detection Algorithm Simulation
An interactive minimal particle simulation that displays the differences in performance between three different collision detection algorithms.

##Three Algorithms
###Brute Force (B-F) (default)
####Algorithm Explanation
The brute force algorithm utilizes the very simple, and inefficient, method of simply checking every particle against every other particle in the simulation. Though for small numbers of particles (likely less than two hundred) this may suffice with a decent processing power, it quickly grows slow and unstable with higher quantities of bodies.

This algorithm works well with small numbers of bodies and is very easy to implement. Simply iterate a collision detection function over every pair of bodies in the simulation.

####Observations
You'll notice when using this algorithm that it is slow... but it is consistent. Due to it's simplicity and independence from partitioning tricks (more on those in the next algorithm), this algorithm performs relatively similar whether the bodies are dense and in close proximity, or spread across the screen evenly.

####Time Complexity
This implementation has a time complexity of *O(n^2)*, given that n is the number of bodies in the simulation.


###Sweep & Prune (S&P)
####Algorithm Explanation
The sweep and prune algorithm uses a more thoughtful approach to determining which bodies could need to be compared for collision detection.

Beyond a certain distance, we can guarantee that two bodies will not collide because they are simply too far away to. The B-F algorithm checked this by going through each pair and checking its distance... very... slowly. But if we isolate and sort all of the balls by one axis, x or y, we can determine if it is possible for them to collide. Since the hard-coded resolution for this project has an aspect ratio of 16:9, it makes more sense to me to sort by the x axis since it is longer, allowing for a higher chance of space between any two balls. This is important for the complexity of this algorithm.



####Observations


####Time Complexity


###Grid Space Partitioning (GRID)
####Algorithm Explanation


####Observations


####Time Complexity
