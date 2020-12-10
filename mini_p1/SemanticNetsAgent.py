from functions import *
class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
	    #the initial number of sheep and wolves as integers,
	    #and return a list of 2-tuples that represent the moves
	    #required to get all sheep and wolves from the left
	    #side of the river to the right.

        end_sheep = 0
        end_wolves = 0
        boat_postion = 0
        moves_list = []

        while (initial_sheep + initial_wolves) > 0:
            if boat_postion == 0:
                gen_list = ProbGenerator(initial_sheep, initial_wolves)

                moves = ProbTester(gen_list, initial_sheep, initial_wolves, end_sheep, end_wolves)
                

                sheep_moved = moves[0][0]
                wolves_moved = moves[0][1]
                move = (sheep_moved, wolves_moved)
                moves_list.append(move)

                initial_sheep -= sheep_moved
                initial_wolves -= wolves_moved

                end_sheep += sheep_moved
                end_wolves += wolves_moved

                boat_postion = 1

            elif boat_postion == 1:
                gen_list = ProbGenerator(end_sheep, end_wolves)

                ProbTester(gen_list, end_sheep, end_wolves, intial_sheep, initial_wolves)

                sheep_moved = moves[0][0]
                wolves_moved = moves[0][1]
                move = (sheep_moved, wolves_moved)
                moves_list.append(move)

                end_sheep -= sheep_moved
                end_wolves -= wolves_moved

                initial_sheep += sheep_moved
                initial_wolves += wolves_moved

                boat_postion = 0
                
            #print(initial_sheep+initial_wolves)

        return moves_list



test_agent = SemanticNetsAgent()

print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
#print(test_agent.solve(3, 3))
#print(test_agent.solve(5, 3))
#print(test_agent.solve(6, 3))
#print(test_agent.solve(7, 3))
#print(test_agent.solve(5, 5))

