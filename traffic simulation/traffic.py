#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import numpy
import copy
get_ipython().run_line_magic('matplotlib', 'inline')
import pylab as pl

"""
Class: TrafficSimulation

Attributes:
[float] density: The car density in the road
[int] roadLength: Length of the road
[int] lanes: Total number of lanes
[int] vMax: Maximum velocity a car can have 
[float] slowP: Probability that a car will slow down randomly
[float] changeLaneP: Probability that a car will change lane if it has been assigned to do so

Methods:
__init__(self, density, roadLength,lanes, vMax, slowP, changeLaneP=1): Initializes object
Returns: N/A

initializeState(self,numberOfLanes): Initializes state of the simulation ( road(s) )
Returns: list

update(self): Updates the state of the simulation
Returns: N/A

changeLanes(self,state,lane): Shift cars from one lane to the other if appropriate
Returns: N/A

checkChangeLane(self,state,i,otherLane): Checks if a car should shift lanes
Returns: boolean

updateLane(self,state, lane): Updates cars' velocities and positions 
Returns: N/A

__repr__(self): Overrides how the object should be displayed to the user
Returns: string

assignRandomDensities(self,sumCars,numberOfLanes,totalCars,lane_densities,maxRandom): Assigns random densities 
to each lane
Returns: int

"""
##########################################################################################################################
class TrafficSimulation:
    
    def __init__(self, density, roadLength,lanes, vMax, slowP, changeLaneP=1):
        self.density = density
        self.roadLength = roadLength
        self.lanes = lanes
        self.slowP = slowP
        self.changeLaneP = changeLaneP
        self.vMax = vMax
        self.state = self.initializeState(lanes)
        self.time_step = 0
        self.cumulative_traffic_flow = 0
        
    def initializeState(self,numberOfLanes):
        lanes = list()
        lane_densities= [0] * numberOfLanes
        totalCars = round(self.density * self.roadLength * numberOfLanes)
        
        # If there is only 1 lane, there is no need to divide the total into different portions
        if self.lanes >1:
            sumCars = 0
            maxRandom = totalCars
            if totalCars > self.roadLength:
                maxRandom = self.roadLength
            # Given the total number of cars that should be on the roads,
            # it randomly assigns a portion of the total to each lane
            sumCars = 0
            sumCars = self.assignRandomDensities(sumCars,numberOfLanes,totalCars,lane_densities,maxRandom)
            # in case that the total number of cars is greater than the road length, this will ensure
            # that the cars are distributed throughout the lanes without exceeding each lane's road
            # length
            while totalCars - sumCars > 0:
                sumCars = self.assignRandomDensities(sumCars,numberOfLanes,totalCars-sumCars,lane_densities,(totalCars - sumCars))
        else:
            lane_densities[0]=(int(totalCars))
            
        # For each lane, given its density (defined in the loop above), it
        # will place the cars into random positions within the lane
        for i in range(numberOfLanes):
            l = [-1] * self.roadLength
            carIndexes = numpy.random.choice(range(self.roadLength),
                size=lane_densities[i],replace=False)
            
            # On top of it, will also randomly assign the initial
            # velocity of each car
            for i in carIndexes:
                l[i] = random.randint(0,self.vMax)
            lanes.append(l)

        return lanes
    
    def assignRandomDensities(self,sumCars,numberOfLanes,totalCars,lane_densities,maxRandom):
        currentSum = 0
        # Assigns random cars to each lane, while ensuring
        # that the number os cars assigned to one lane doesn't go over
        # the road length.
        for i in range(numberOfLanes):
            currentCars = random.randint(0,abs(maxRandom-currentSum))
            
            if lane_densities[i] + currentCars < self.roadLength:
                lane_densities[i] += (int(currentCars))
                sumCars += currentCars
                currentSum += currentCars
            else:
                lane_densities[i] += 0
        return sumCars
    
    def update(self):
        
        # If there is more than one lane in the simulation,
        # we go through every lane and check if there are cars
        # in it that should be shifting to another lane
        if self.lanes > 1:
            for i in range(len(self.state)):
                self.changeLanes(self.state[i],i)
        
        # We update every lane, which means updating
        # all the cars' velocities and positions
        # accordingly
        for i in range(len(self.state)):
            self.updateLane(self.state[i],i)
            
        # Update time step count and traffic flow.
        # Here the flow is given as the amount of cars that 
        # go over the boundary; that is, that reach the end of
        # the road and re-enter the road. There is a maximum of
        # self.vMax cars that could do this per update. And for every
        # car that holds a velocity greater than the index it is at currently
        # (from 0 to self.vMax), it means that this car re-entered the road
        # and the cumulative traffic flow variable gets one added to it
        self.time_step += 1
        for j in range(self.lanes):
            for i in range(self.vMax):
                if self.state[j][i] > i:
                    self.cumulative_traffic_flow += 1
    
    
    def changeLanes(self,state,lane):
        # Initialized helper variables
        copyOfState = copy.deepcopy(self.state)
        leftLane = -1
        rightLane = -1
        changeLane = False
        
        # Loops through the whole current lane and
        for i in range(self.roadLength):
            
            #If there is a car in the given index i, carry on:
            if state[i] > -1 and random.random() < self.changeLaneP:
                
                #checks the distance between current car and next nearest car
                distance = 0
                for j in range(i+1, (i+self.roadLength)):
                    if state[(j % self.roadLength)] == -1:
                        distance += 1
                    else:
                        break
                
                # If distance to the nearest car in the same lane is less
                # than the current car's velocity + 1, check if there is enough
                # distance in the line besides it.
                if distance < (state[i] + 1):
                    leftLane = lane - 1
                    rightLane = lane + 1
                    otherLane = -1
                    changeLane = False
                    
                    # If there is only a lane at the left of
                    # the current lane or to the right, pick that one.
                    # If there are lanes on both sides of the current lane,
                    # randomly pick one.
                    if leftLane < 0:
                        otherLane = rightLane
                    elif rightLane > lane:
                        otherLane = leftLane
                    else:
                        otherLane = random.randint(leftLane,rightLane)
                    
                    # Check if there is enough distance to the front and back of the car
                    # meaning that the car can move to the other lane
                    changeLane =  self.checkChangeLane(state,i,otherLane)
                    
                    #if the current lane has two lanes besides it, and the one we just checked
                    # doesn't have enough space to acommodate the current car, check the other one
                    if not changeLane:
                        if (otherLane != rightLane and rightLane < self.lanes):
                            otherLane = rightLane
                            changeLane = self.checkChangeLane(state,i,otherLane)
                        elif (otherLane != leftLane and leftLane >= 0):
                            otherLane = leftLane
                            changeLane = self.checkChangeLane(state,i,otherLane)
                    
                    #If we can change lanes, do so
                    if changeLane:
                        copyOfState[otherLane][i] = state[i]
                        self.state[lane][i] = -1
         
        # After we're done with the lane shifts for the current lane, we update
        # the state of the simulation
        if leftLane != -1 and leftLane >= 0:
            self.state[leftLane] = copy.deepcopy(copyOfState[leftLane])
        if rightLane != -1 and rightLane < self.lanes:
            self.state[rightLane] = copy.deepcopy(copyOfState[rightLane])

            
    def checkChangeLane(self,state,i,otherLane):
        distanceOtherLane = -1
        backDistanceOtherLane = 0
        if otherLane > -1:
            # If this lane is empty, returning True indicates that a
            # car can move there, therefore there is no need to check
            # distances
            if self.state[otherLane] == [-1] * self.roadLength:
                return True
            
            # Given the index of the current car we are looking at, we look at the same
            # index in the other lane and start going forward to see where the 
            # nearest next car is
            for j in range(i, (i+self.roadLength)):
                if self.state[otherLane][(j % self.roadLength)] == -1:
                    distanceOtherLane += 1
                # When we find the nearest car going forward, we try to find the nearest
                # car going backwards (still in the other lane)
                else:
                    # We only look for the nearest car backwards if the forward distance
                    # falls under the rule to shift lane, that is, if the distance
                    # is greater than the car's current velocity plus one
                    if distanceOtherLane > state[i] + 1:
                        backDistanceOtherLane = 0
                        for k in range(i-1, (i-self.roadLength),-1):
                            if self.state[otherLane][(k % self.roadLength)] == -1:
                                backDistanceOtherLane += 1
                            else:
                                # Check if the backwards distance falls under the rule
                                # to shift lanes
                                if backDistanceOtherLane > self.vMax:
                                    return True
                                break
                    else:
                        break
        return False
        
        
    def updateLane(self,state, lane):
        
        for i in range(self.roadLength):
            if state[i] > -1:
                
                # Accelerates car according to the 
                # pre defined rules
                distance = 1
                for j in range(i+1, (i+self.roadLength)):
                    if state[(j % self.roadLength)] == -1:
                        distance += 1
                    else:
                        break          
                        
                if distance > state[i] and state[i] < self.vMax:
                    state[i] += 1

                # Slows car down according to the 
                # pre defined rules
                if distance <= state[i]:
                    state[i] = distance - 1
                
                # Randomly slows car down given the 
                # probability of slowing a car self.slowP
                if state[i] > 0 and random.random() < self.slowP:
                        state[i] -= 1

        # After updating all the cars' velocities, we
        # make sure that they move accordingly
        newstate = [-1] * self.roadLength
        for i in range(self.roadLength):
            if state[i] > -1:
                nextindex = (i + state[i])%self.roadLength 
                newstate[nextindex] = state[i]
            
        self.state[lane] = copy.deepcopy(newstate)
          
        
    def __repr__(self):
        s = "\n"
        for i in range(len(self.state)):
            s += ''.join('.' if x < 0 else str(x) for x in self.state[i])
            s += '\n'
        return s

##########################################################################################################################
# End of TrafficSimulation Class
##########################################################################################################################

# Simulates traffic according to density and number of lanes    
def runSimulation(roadLength,lanes, vMax, slowP,totalTrials=100,updatePerTrial=50,printLastTrialPerDensity=True):    

    densities = []
    flow_mean = []
    
    # Runs simulation for every density between 0.05 and 1 at 0.05 intervals 
    for density in numpy.arange(0.05,1,0.05):
        for trial in range(totalTrials):
            trials = numpy.empty([totalTrials])
            sim = TrafficSimulation(density,roadLength,lanes, vMax, slowP)
            # Only prints the state of the simulation for the last trial of every density
            # if printLastTrialPerDensity is set to True
            if printLastTrialPerDensity and trial == totalTrials-1:
                print("\n\n")
                print("------------------------------------------")
                print("Last trial for Simulation at density:",density)
                print("------------------------------------------")
            for i in range(updatePerTrial):
                sim.update()
                if printLastTrialPerDensity and trial == totalTrials-1:
                    print(sim)
            # For every run, we add up the traffic flow per time step count
            # to compare against other densities and lanes afterwards
            trials[trial] = (sim.cumulative_traffic_flow / sim.time_step)
        densities.append(density)
        flow_mean.append(numpy.mean(trials))

    # Make sures that the relevant information on the simulation
    # is displayed to the user
    pl.plot(densities,flow_mean)
    pl.xlabel('Traffic density')
    pl.ylabel('Average traffic flow')
    pl.show();
    maxN = (numpy.max(flow_mean))
    print("Max value for average flow of",round(maxN,2),"was achieved at density:",round(densities[flow_mean.index(maxN)],2))
    
    return maxN

# Sets up the parameters for the simulation
lanesToTry = 10
lanesList = list()
for i in range(1,lanesToTry+1):
    print("\nSimulation with",i,"lane(s)")
    lanesList.append(runSimulation(60,i, 5, 0.4,printLastTrialPerDensity=False))

pl.plot(lanesList)
pl.xlabel('Number of Lanes')
pl.ylabel('Max flow achieved')
pl.show();

