#Index4x4=
# -------------
# | 0 | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 | 7 |
# -------------
# | 8 | 9 | 10| 11|
# -------------
# | 12| 13| 14| 15|
# -------------

import random

BlockAPosition = 12
BlockBPosition = 13
BlockCPosition = 14
AgentPosition = 15

StartState = []
for i in range(0,16):
    if i==BlockAPosition:
        StartState.append(1)
    elif i==BlockBPosition:
        StartState.append(2)
    elif i==BlockCPosition:
        StartState.append(3)
    elif i==AgentPosition:
        StartState.append(55)
    else:
        StartState.append(0)


def GoalState(State):
    if (State== [55, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0] or 
        State== [0, 55, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 55, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 55, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 55, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 55, 0, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 55, 0, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 55, 2, 0, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 55, 0, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 55, 0, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 55, 3, 0, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 55, 0] or
        State== [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 55]):
            return True


def BoardState(State):
    print ("| %i | %i | %i | %i |" % (State[0], State[1], State[2], State[3]))
    print ("| %i | %i | %i | %i |" % (State[4], State[5], State[6], State[7]))
    print ("| %i | %i | %i | %i |" % (State[8], State[9], State[10], State[11]))
    print ("| %i | %i | %i | %i |" % (State[12], State[13], State[14], State[15]))

def Up (State):
    NewState=State[:]
    Index = NewState.index(55)
    IndexNewPosition = Index-4
    if Index in [0,1,2,3]:
        return None
    else:
        NewState[Index], NewState[IndexNewPosition] = NewState[IndexNewPosition], NewState[Index]
        return NewState
    
def Down (State):
    NewState=State[:]
    Index = NewState.index(55)
    IndexNewPosition = Index+4
    if Index in [12,13,14,15]:
        return None
    else:
        NewState[Index], NewState[IndexNewPosition] = NewState[IndexNewPosition], NewState[Index]
        return NewState
    
def Right (State):
    NewState=State[:]
    Index = NewState.index(55)
    IndexNewPosition = Index+1
    if Index in [3,7,11,15]:
        return None
    else:
        NewState[Index], NewState[IndexNewPosition] = NewState[IndexNewPosition], NewState[Index]
        return NewState

def Left (State):
    NewState=State[:]
    Index = NewState.index(55)
    IndexNewPosition = Index-1
    if Index in [0,4,8,12]:
        return None
    else:
        NewState[Index], NewState[IndexNewPosition] = NewState[IndexNewPosition], NewState[Index]
        return NewState


def CreateNode(State, Parent, Action, Depth, Cost):
	return Node(State, Parent, Action, Depth, Cost)

def ExpandNode (Node, Fringe):
    ExpandFringe=[]
    i=range(4)
    k= random.sample(i,len(i))
    for j in k:
        
        if j==0:
            ExpandFringe.append(CreateNode(Up(Node.State),Node, "UP", Node.Depth+1, 0))
        if j==1:
            ExpandFringe.append(CreateNode(Down(Node.State),Node, "DOWN", Node.Depth+1, 0))
        if j==2:
            ExpandFringe.append(CreateNode(Right(Node.State),Node, "RIGHT", Node.Depth+1, 0))
        else:
            ExpandFringe.append(CreateNode(Left(Node.State),Node, "LEFT", Node.Depth+1, 0))
    
    ExpandFringe = [Node for Node in ExpandFringe if Node.State != None]
    return ExpandFringe


def DFS(Start):
    Fringe = []
    TimeComplexity=0
    Moves = [None]
    Fringe.append( CreateNode( Start, None, None, 0, 0 ) )
    Node=CreateNode( Start, None, None, 0, 0 )
    if GoalState(Node.State)==True:
        return Moves, TimeComplexity
    while True:
        if len( Fringe ) == 0: 
            return None, TimeComplexity
        else:
            Node = Fringe.pop(0)
            
            TimeComplexity+=1
        if GoalState(Node.State) == True:
            Moves=[]
            Configuration = []
            while True:
                Moves.insert(0, Node.Action)
                Configuration.insert(0,Node.State)
                if Node.Depth == 1: 
                    break
                Node = Node.Parent
            BoardState(Start)
            for count in range(0, len(Moves)):
                print(Moves[count])
                BoardState(Configuration[count])
            return Moves, TimeComplexity
        else:
            ExpandFringe = ExpandNode( Node, Fringe )
            ExpandFringe.extend( Fringe )
            Fringe = ExpandFringe
            if TimeComplexity%10000==0:
                print(TimeComplexity)

class Node:
    def __init__( self, State, Parent, Action, Depth, Cost ):
        self.State = State
        self.Parent = Parent
        self.Action = Action
        self.Depth = Depth
        self.Cost = Cost
        
def main():
    Result,Time= DFS(StartState)
    if Result == None:
        print ("No solution found")
    elif Result == [None]:
        print ("The time complexity is:", Time)
        print ("Starting state was the goal")
    else:
        print ("The time complexity is:", Time)
        print ("The goal state was achieved in:", len(Result), " moves")
  
    
    
if __name__ == "__main__":
 main()
    