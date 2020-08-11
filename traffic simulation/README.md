
# Traffic simulation


# The Model

This project aims to simulate a simplified road traffic. The simulation provides insights to the relationship between traffic flow and car density, as well as how that changes as more lanes are added to the model. In this simulation, the road is unidirectional and the cars can move to either lane immediately next to them (right or left lane). Finally, this simulation builds upon the traffic model presented by Nagel &

Schreckenberg (1992) and the multi-lane traffic model presented by  Rickert et al. (1996).

As mentioned, the model is an extremely simplified version of a real life traffic scenario; therefore, it holds a few assumptions:

1.  The cars' velocities only assume discrete values

2.  The cars can switch lane to either their left or right lane

3.  There are no roadblocks such as traffic lights, road accidents, etc

4.  All cars are the same, occupying the same amount of space and having the same max and minimum velocities

5.  All the drivers follow the pre-determined rules

6.  There are no pedestrians, bicycles, motorbikes, etc. Only cars

Although the model counts on pre-determined rules to run smoothly, it does take into account some randomness into the model. The reason for that is to simulate some of the randomness that happens in real life such as having a driver taking up a call, road has a hole, etc. Such randomness is taken into account under the probability of a driver to randomly slow down the car and the probability of a driver to randomly not switch lanes even though the rules say he could do so. Additionally, the cars are initialized in random lanes (in the multi-lane scenarios), in random spaces, and with random velocities. It is important to not that, had no randomness being taken into account, the model would be deterministic and not a suitable model to simulate a real-life road traffic, which is also not deterministic.

As per the rules that dictates the simulation, we can divide them up into two categories: lane shift and velocity update.

# Lane Shift

For a car to switch lanes, it must obey the following rules:

1.  The distance between the current car and the nearest car ahead should be less than the current car's velocity plus one;

2.  The distance between the current car and the nearest car ahead on the other lane should be greater than the current car's velocity plus one;

3.  The distance between the current car and the nearest car behind it on the other lane should be greater than the maximum velocity defined in the model;

4.  It satisfies the probability of changing lanes defined in the model

# Velocity Update

For a car to update its velocity, it follows the rules specified below:

1.  If the distance between the current car and the nearest car ahead is greater than the car's current velocity and the current velocity is less than the maximum speed, then the car's velocity is increased by one;

2.  If the distance between the current car and the nearest car ahead is less or equal to the current car's velocity, then its velocity becomes the distance minus 1;

3.  If the random probability of slowing down the car is satisfied, the car's velocity is decreased by one

Finally, the model updates the cars' positions to reflect the updated velocities.

# Analysis

The main metric of analysis for this project will be the traffic flow. In this case, traffic flow is given as the number of cars that leave and re-enter the road per time step. This simulation assumes periodic boundary, so having cars re-entering the road can be seen as a new influx of cars. 

For this analysis, I have run several different simulation trials for every density of cars from 0.05 to 1 at 0.05 intervals to be able to retrieve an average for the traffic flow at every density value. Additionally, I ran such trials under different lane scenarios to compare the results across simulation runs. There is an steady increase in the traffic flow as we add more lanes to the simulation. Additionally, we can also see that the maximum average flow is also achieved at increased density values as we add more lanes to the traffic, with a lower increase rate when compared to the increase rate of the traffic flow itself.

Generally, at extremely low densities, we can see a steady increase in the traffic flow for every simulation until it peaks, then the traffic flow decreases until reaching values very close to 0. This can be explained by the fact that at very low densities, there are not enough cars to leave and re-enter the road, so the flow will not be too high; but as we add more cars to the road, it is harder for them to move forward and therefore it will take longer for them to leave and re-enter the road, decreasing the traffic flow again. The peak happens when there is the perfect balance between the number of cars in the road and how easy it is for them to move forward. As we add more lanes, the cars have more options to move forward and the traffic flow gets higher at increasing higher densities, as we can see by the figures above. The figure below shows the summary of the maximum average traffic flow values per number of lanes in the simulation.

![](https://lh6.googleusercontent.com/Xc8cbKGJ27jj9uefeaVidh4Hu4J_Ng5f3QtJcul4KhHiRliWgOM67r_FDxa95pZ5c1kVLAIqbiVmqQyJGWLqaFgpvCNLd9GUq9Nxv5rnfW6pFUncmhDgSjlp7R2sswsAk5bnea4T)

# References

Nagel, K., Schreckenberg, M. (1992). A cellular automaton model for freeway traffic. Journal de Physique I, 2(12), 2221--2229.
Rickert, M., et al. (1996). Two Lane Traffic Simulations using Cellular Automata. Physica A: Statistical Mechanics and its Applications, 231(4), 534--550. 
