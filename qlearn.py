'''
	Q-Learning Algorithm Example

	Results are already normalized 
	Last row in Q is not set.

'''

import random

rooms = [0,1,2,3,4,5]

# Set the number of runs
episodes = 50 

# End State, ie room #
goalState = 5

# Set the learning parameter gamma
gamma = .8


# Rewards Matrix
R = [		#ACTION				
		# 0  1  2  3  4  5     STATE
		[-1,-1,-1,-1,0,-1],		# 0
		[-1,-1,-1,0,-1,100],	# 1
		[-1,-1,-1,0,-1,-1],		# 2
		[-1,0,0,-1,0,-1],		# 3
		[0,-1,-1,0,-1,100],		# 4
		[-1,0,-1,-1,0,100]		# 5
	]

# Initialize matrix Q to zero
Q = [
		#0 1 2 3 4 5
		[0,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,0,0,0,0,0]
	]



for x in range(episodes):
		initRoom = random.choice(rooms)
		while initRoom != goalState:
			possibleActions = []
			for i in range(len(R[initRoom])):
			  if R[initRoom][i] != -1:
			  	possibleActions.append(i)

			randomAction = random.choice(possibleActions)
			nextActions = []
			for i in range(len(R[randomAction])):
			  if R[randomAction][i] != -1:
			  	nextActions.append(i)

			maxQ = 0
			for i in range(len(nextActions)):
				QnextState = Q[randomAction][nextActions[i]]
				if QnextState > maxQ:
					maxQ = QnextState

			Q[initRoom][randomAction] = int(R[initRoom][randomAction] + gamma*maxQ)
			initRoom = randomAction

print(Q)

'''
[
	 [0, 0, 0, 0, 80, 0], 
	 [0, 0, 0, 64, 0, 100], 
	 [0, 0, 0, 64, 0, 0], 
	 [0, 80, 51, 0, 80, 0], 
	 [64, 0, 0, 64, 0, 100], 
	 [0, 0, 0, 0, 0, 0]
 ]

'''

