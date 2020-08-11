
#Traffic simulation


#The Model

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

#Lane Shift

For a car to switch lanes, it must obey the following rules:

1.  The distance between the current car and the nearest car ahead should be less than the current car's velocity plus one;

2.  The distance between the current car and the nearest car ahead on the other lane should be greater than the current car's velocity plus one;

3.  The distance between the current car and the nearest car behind it on the other lane should be greater than the maximum velocity defined in the model;

4.  It satisfies the probability of changing lanes defined in the model

#Velocity Update

For a car to update its velocity, it follows the rules specified below:

1.  If the distance between the current car and the nearest car ahead is greater than the car's current velocity and the current velocity is less than the maximum speed, then the car's velocity is increased by one;

2.  If the distance between the current car and the nearest car ahead is less or equal to the current car's velocity, then its velocity becomes the distance minus 1;

3.  If the random probability of slowing down the car is satisfied, the car's velocity is decreased by one

Finally, the model updates the cars' positions to reflect the updated velocities.

#Analysis

The main metric of analysis for this project will be the traffic flow. In this case, traffic flow is given as the number of cars that leave and re-enter the road per time step. This simulation assumes periodic boundary, so having cars re-entering the road can be seen as a new influx of cars. 

For this analysis, I have run several different simulation trials for every density of cars from 0.05 to 1 at 0.05 intervals to be able to retrieve an average for the traffic flow at every density value. Additionally, I ran such trials under different lane scenarios to compare the results across simulation runs.

![](https://lh5.googleusercontent.com/XBA-3d5q16fMuONcthOXIJ_8dX7Ne-_XL4npUg7WkiEnwtHSHjDkDrzj5WBVeaHXQWouTri8AzxzL4xvB6CCNABihbbhtI_Bp3S6169B-ZVbCtNeJK_5LzhGW1NGGGkr2MWcvewG)![](https://lh5.googleusercontent.com/WzgQkxLSM5fJCI69WvmJIC9fKEdsWxhyg9-lxsyf4ZOT0cnxbP6r8ATjuQ3YLxJ21ZyE4dZrol_Juwwmq9_UyIU3ryGrTvVKRttotRyXCiaaXLI47PfHUUcMuOFDWHBfzAPfsRvD)

![](https://lh3.googleusercontent.com/StngwDj5X8kt0wA3l7UbYh9Np9IykrbQBZ0yWECzBl9LSKF19fKfIXcJRolWh9tc9FzLoKy0XMybm3zos4kOTCdjhinFBSJbNPOexx7-3Pt82UJYz31yv8yurjN1TOtU5n9vh6K7)

![](https://lh3.googleusercontent.com/Fn7QLB5yz4NHyhhERn-zXslMgYI9txmaVJA_SwdGt68CA69K-pRODCFgTor1Uth_54cj9Mnxpx0d5BGj_UEQnV5PfBxCk1SQ7pmlItYseX_hs-gaOA6yt7qDyiEZfyURKFwZjigV)![](https://lh6.googleusercontent.com/uodaEOr2NpH4kFpaCJYSJ_MTI80X8Ekdj_q5lOhSXdVB5eETL1DzCjGnnKQdeNELm5XDgNDKRMUXhnWI5FYSg8dmOOYHq3T57e6sHi_bg5X82ePirO1mShhJos6UZa3bhE5K7BHs)

![](https://lh6.googleusercontent.com/n9-CiIncsBvAQgMfqsTLlAr72z2sfXIWiORf19b0ZC10k6wcaMvRO6BgZortYDZBEH7hyPbxZRaBHAtpz81wZLUJK5ZOI_NfX4cAWiIYGc10BtskLAZonOImA4Ddp0udQaV1Hm8r)![](https://lh4.googleusercontent.com/p0SDnNbyXctsCW8juu_DP422J7xzswJHYFc36brEHRVHCKvJZddiYYCg5SshFNnm90mAbglg0qzkVLVbl7pEF08ZKvrps7JA2dglbafGgOvY_VGZXALUh6OIedDrnugeB0NnNMh7)          

![](https://lh6.googleusercontent.com/A9YUCcvXClmi4rkYcvOeqSWr5ie6sfsvQYQvjQOOGFZc-1_TuSLiizTbkJCGTpV6KdxrGeWcnzRidIuGexzxn9W_oiimdf1oAAUKvnYRhfbiYctJJbq-GgthQaokQoVPsGEFxfi_)![](https://lh4.googleusercontent.com/vvT38CXk-f_zyrVdz-yLzfwj6m7sLIVyWAWyhIa_FVy4yVLg34VvpOH3Y15-hNGpWHYT1aUc6pcVTw9KhKK6leNaqcreKCC5CIP3iWLv27I4zTEhQy5A0q-OGV3k5Xx4vZvRfuWb)     

![](https://lh3.googleusercontent.com/vM6qa3jwlaKBKxkUeS_Arm6k7Do7IRGEQZ7nBNeh1o_zZluN7Jwia3iO4VVNKu7aMXgM9PpHXC3ZM-ZK__HZwfsPW5qmXipwhT7wVh6un2DykJGvpZbY2UfsbSFG6r3cqE0VqsiF)![](https://lh6.googleusercontent.com/mWq_GSSBtWQFXUdqA2WoCFyAABW8sxHcarI5sV2enPh2ulYZMRK7CCwQfmCCOPVzhOstaPOYzTHYqjbV6jDSiT-QfjJt62csIMYy5qM_RmRHAPnnQQ_B93Nw8y9meaAlEDjQbTtO)

![](https://lh4.googleusercontent.com/5MWEIdaC5yJ_gTftNpSRZwHXjqcZ3Bj1Y2X4b3kffSTG08eE7fo--OWDJiX_kAVK7Cm8KpyAqWeRsTb5L9RycKQ-BYd0zwB3rOPxxCZDY0ELeyGtBsQSW2myALy0wzNZ030_E4pr)![](https://lh3.googleusercontent.com/nG0IDOAuU_yFf41_0XHuPTi6qhPdvahWkWfKP9liGDI0z6ld_9ZF4Irnud3vrZeYnNe_XNq7gfS3tK0aRG7QUxJoN4BPy16cQA2lSyLxWAKwW7-y4GfhIYqg52dgdbGCz-HMBtPx)

It is possible to see that there is an steady increase in the traffic flow as we add more lanes to the simulation. Additionally, we can also see that the maximum average flow is also achieved at increased density values as we add more lanes to the traffic, with a lower increase rate when compared to the increase rate of the traffic flow itself.

Generally, at extremely low densities, we can see a steady increase in the traffic flow for every simulation until it peaks, then the traffic flow decreases until reaching values very close to 0. This can be explained by the fact that at very low densities, there are not enough cars to leave and re-enter the road, so the flow will not be too high; but as we add more cars to the road, it is harder for them to move forward and therefore it will take longer for them to leave and re-enter the road, decreasing the traffic flow again. The peak happens when there is the perfect balance between the number of cars in the road and how easy it is for them to move forward. As we add more lanes, the cars have more options to move forward and the traffic flow gets higher at increasing higher densities, as we can see by the figures above. The figure below shows the summary of the maximum average traffic flow values per number of lanes in the simulation.

![](https://lh6.googleusercontent.com/Xc8cbKGJ27jj9uefeaVidh4Hu4J_Ng5f3QtJcul4KhHiRliWgOM67r_FDxa95pZ5c1kVLAIqbiVmqQyJGWLqaFgpvCNLd9GUq9Nxv5rnfW6pFUncmhDgSjlp7R2sswsAk5bnea4T)

#References

Nagel, K., Schreckenberg, M. (1992). A cellular automaton model for freeway traffic. Journal de Physique I, 2(12), 2221--2229.

Rickert, M., et al. (1996). Two Lane Traffic Simulations using Cellular Automata. Physica A: Statistical Mechanics and its Applications, 231(4), 534--550. 