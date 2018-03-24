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

import math

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
print(StartState)

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
        #print (NewState)
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
    ExpandFringe.append(CreateNode(Up(Node.State),Node, "UP", Node.Depth+1, f(Node,h(Node.State))))
    ExpandFringe.append(CreateNode(Down(Node.State),Node, "DOWN", Node.Depth+1, f(Node,h(Node.State))))
    ExpandFringe.append(CreateNode(Right(Node.State),Node, "RIGHT", Node.Depth+1, f(Node,h(Node.State))))
    ExpandFringe.append(CreateNode(Left(Node.State),Node, "LEFT", Node.Depth+1, f(Node,h(Node.State))))
    ExpandFringe = [Node for Node in ExpandFringe if Node.State != None] 
    return ExpandFringe


#def h(State):
#    misplaced=0
#    if State[5] != 1:
#        misplaced-=1
#    if State[9] != 2:
#        misplaced-=1
#    if State[13] != 3:
#        misplaced-=1
#    print(misplaced,"misplaced score")
#    return misplaced

def h(State):
    Misplaced=0
    Distance=0

    if State[5] != 1:
        Misplaced+=1
        Distance += math.fabs(State.index(1)-5)
    if State[9] != 2:
        Misplaced+=1
        Distance += math.fabs(State.index(2)-9)
    if State[13] != 3:
        Misplaced+=1
        Distance += math.fabs(State.index(3)-13)
    
    Heuristic=Distance+Misplaced
    print(Heuristic)
    return Heuristic

def f(Node, h):
    f = (Node.Depth + h)
    return f 
    
    
def Astar(Start):
    Fringe = []
    TimeComplexity=0
    Moves = [None]
    
    
    Node=CreateNode( Start, None, None, 0, h(Start))
    Fringe.append( Node )
    if GoalState(Node.State)==True:
        return Moves, TimeComplexity
    while True:
        if len( Fringe ) == 0: 
            return None, TimeComplexity
        else:
            if len(Fringe)>1:
                Fringe = sorted(Fringe, key=lambda Node: Node.Cost)
            Node = Fringe.pop(0)
            TimeComplexity+=1
            BoardState(Node.State)
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
            Fringe.extend(ExpandNode(Node, Fringe))
            print(TimeComplexity)
       

class Node:
    def __init__(self, State, Parent, Action, Depth, Cost):
        self.State = State
        self.Parent = Parent
        self.Action = Action
        self.Depth = Depth
        self.Cost = Cost
        
def main():
    Result,Time= Astar(StartState)
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
    