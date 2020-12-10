def ProbGenerator(sheep_count, wolf_count):
    generator_options = [(0,1),(1,0),(1,1),(2,0),(0,2)]
    gen_list = []
    for gen in generator_options:
        if ((sheep_count - gen[0]) >= 0) and ((wolf_count - gen[1]) >= 0):
            gen_list.append(gen)

        else:
            pass

    return gen_list

def ProbTester(gen_list, cur_sheep, cur_wolves, opp_sheep, opp_wolves):
    playable_moves = []
    for move in gen_list:
        if 
        if ((cur_sheep - move[0]) == 0)  and ((cur_wolves - move[1]) == 0):
            playable_moves.append(move)

        else:
            pass

    return playable_moves
