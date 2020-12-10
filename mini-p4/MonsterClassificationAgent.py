
class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.

        pass

    def solve(self, monster_list, new_monster):
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        #TRUE CATEGORY LISTS
        sizeTrue_list = []
        colorTrue_list = []
        coveringTrue_list = []
        foot_typeTrue_list = []
        leg_countTrue_list = []
        arm_countTrue_list = []
        eye_countTrue_list = []
        horn_countTrue_list = []
        lays_eggsTrue_list = []
        has_wingsTrue_list = []
        has_gillsTrue_list = []
        has_tailTrue_list = []

        ##FALSE CATEGORY LISTS
        sizeFalse_list = []
        colorFalse_list = []
        coveringFalse_list = []
        foot_typeFalse_list = []
        leg_countFalse_list = []
        arm_countFalse_list = []
        eye_countFalse_list = []
        horn_countFalse_list = []
        lays_eggsFalse_list = []
        has_wingsFalse_list = []
        has_gillsFalse_list = []
        has_tailFalse_list = []



        for monster in monster_list:
            if monster[1] == True:
                sizeTrue_list.append(monster[0]['size'])
                colorTrue_list.append(monster[0]['color'])
                coveringTrue_list.append(monster[0]['covering'])
                foot_typeTrue_list.append(monster[0]['foot-type'])
                leg_countTrue_list.append(monster[0]['leg-count'])
                arm_countTrue_list.append(monster[0]['arm-count'])
                eye_countTrue_list.append(monster[0]['eye-count'])
                horn_countTrue_list.append(monster[0]['horn-count'])
                lays_eggsTrue_list.append(monster[0]['lays-eggs'])
                has_wingsTrue_list.append(monster[0]['has-wings'])
                try:
                    has_gillsTrue_list.append(monster[0]['has-gills'])
                except KeyError:
                    has_gillsTrue_list.append(monster[0]['has_gills'])
                
                
                has_tailTrue_list.append(monster[0]['has-tail'])

            elif monster[1] == False:
                sizeFalse_list.append(monster[0]['size'])
                colorFalse_list.append(monster[0]['color'])
                coveringFalse_list.append(monster[0]['covering'])
                foot_typeFalse_list.append(monster[0]['foot-type'])
                leg_countFalse_list.append(monster[0]['leg-count'])
                arm_countFalse_list.append(monster[0]['arm-count'])
                eye_countFalse_list.append(monster[0]['eye-count'])
                horn_countFalse_list.append(monster[0]['horn-count'])
                lays_eggsFalse_list.append(monster[0]['lays-eggs'])
                has_wingsFalse_list.append(monster[0]['has-wings'])
                try:
                    has_gillsFalse_list.append(monster[0]['has-gills'])
                except KeyError:
                    has_gillsFalse_list.append(monster[0]['has_gills'])
                #else:
                #    print("OTHER ERROR FOR HAS GILLS...")
    
                has_tailFalse_list.append(monster[0]['has-tail'])

        print(has_gillsFalse_list)
        print(has_gillsTrue_list)

        prob_list = []   
        prob_list.append(SizeProbAnalysis(self, new_monster['size'], sizeTrue_list, sizeFalse_list))
        prob_list.append(ColorProbAnalysis(self, new_monster['color'], colorTrue_list, colorFalse_list))
        prob_list.append(CoveringProbAnalysis(self, new_monster['covering'], coveringTrue_list, coveringFalse_list))
        prob_list.append(FootTypeProbAnalysis(self, new_monster['foot-type'], foot_typeTrue_list, foot_typeFalse_list))
        prob_list.append(LegCountProbAnalysis(self, new_monster['leg-count'], leg_countTrue_list, leg_countFalse_list))
        prob_list.append(ArmCountProbAnalysis(self, new_monster['arm-count'], arm_countTrue_list, arm_countFalse_list))
        prob_list.append(EyeCountProbAnalysis(self, new_monster['eye-count'], eye_countTrue_list, eye_countFalse_list))
        prob_list.append(HornCountProbAnalysis(self, new_monster['horn-count'], horn_countTrue_list, horn_countFalse_list))
        prob_list.append(LaysEggsProbAnalysis(self, new_monster['lays-eggs'], lays_eggsTrue_list, lays_eggsFalse_list))
        prob_list.append(HasWingsProbAnalysis(self, new_monster['has-wings'], has_wingsTrue_list, has_wingsFalse_list))
        try:
            new_monster_gills = new_monster['has_gills']
        except KeyError:
            new_monster_gills = new_monster['has-gills']
            print('KeyError was caught and remedied')

        prob_list.append(HasGillsProbAnalysis(self, new_monster_gills, has_gillsTrue_list, has_gillsFalse_list))
        prob_list.append(HasTailProbAnalysis(self, new_monster['has-tail'], has_tailTrue_list, has_tailFalse_list))
        
        true_prob = 0
        false_prob = 0

        for prob in prob_list:
           true_prob += prob['true_prob']/12
           false_prob += prob['false_prob']/12

        print('True Probality: ' + str(true_prob))
        print('False Probality: ' + str(false_prob))

        if true_prob > false_prob:
            return True
        elif true_prob < false_prob:
            return False
        elif true_prob == false_prob:
            return False
        else:
            return print('UNKOWN ERROR CALCULATING ANSWER!!!!')


        

        




#####Monster Category Probability Calculation Functions######
def SizeProbAnalysis(self, monster_size, sizeTrue_list, sizeFalse_list):
    """Calculates Probality of monster based on size from Test cases from monster_list"""
    if monster_size == 'large':
        return ProbCalc('large', sizeTrue_list, sizeFalse_list)
    elif monster_size == 'huge':
        return ProbCalc('huge', sizeTrue_list, sizeFalse_list)
    elif monster_size == 'tiny':
        return ProbCalc('tiny', sizeTrue_list, sizeFalse_list)
    elif monster_size == 'medium':
        return ProbCalc('medium', sizeTrue_list, sizeFalse_list)
    else:
        print('SIZE is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def ColorProbAnalysis(self, monster_color, colorTrue_list, colorFalse_list):
    """Calculates Probality of monster based on color from Test cases from monster_list"""
    if monster_color == 'black':
        return ProbCalc('black', colorTrue_list, colorFalse_list)
    elif monster_color == 'white':
        return ProbCalc('white', colorTrue_list, colorFalse_list)
    elif monster_color == 'blue':
        return ProbCalc('blue', colorTrue_list, colorFalse_list)
    elif monster_color == 'red':
        return ProbCalc('red', colorTrue_list, colorFalse_list)
    elif monster_color == 'gray':
        return ProbCalc('gray', colorTrue_list, colorFalse_list)
    elif monster_color == 'purple':
        return ProbCalc('purple', colorTrue_list, colorFalse_list)
    else:
        print('Color is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def CoveringProbAnalysis(self, monster_covering, coveringTrue_list, coveringFalse_list):
    """Calculates Probality of monster based on covering from Test cases from monster_list"""
    if monster_covering == 'fur':
        return ProbCalc('fur', coveringTrue_list, coveringFalse_list)
    elif monster_covering == 'scales':
        return ProbCalc('scales', coveringTrue_list, coveringFalse_list)
    else:
        print('Covering is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def FootTypeProbAnalysis(self, monster_foot_type, foot_typeTrue_list, foot_typeFalse_list):
    """Calculates Probality of monster based on foot_type from Test cases from monster_list"""
    if monster_foot_type == 'paw':
        return ProbCalc('paw', foot_typeTrue_list, foot_typeFalse_list)
    elif monster_foot_type == 'foot':
        return ProbCalc('foot', foot_typeTrue_list, foot_typeFalse_list)
    elif monster_foot_type == 'none':
        return ProbCalc('none', foot_typeTrue_list, foot_typeFalse_list)
    elif monster_foot_type == 'talon':
        return ProbCalc('talon', foot_typeTrue_list, foot_typeFalse_list)
    else:
        print('foot_type is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def LegCountProbAnalysis(self, monster_leg_count, leg_countTrue_list, leg_countFalse_list):
    """Calculates Probality of monster based on leg_count from Test cases from monster_list"""
    if monster_leg_count == 2:
        return ProbCalc(2, leg_countTrue_list, leg_countFalse_list)
    elif monster_leg_count == 1:
        return ProbCalc(1, leg_countTrue_list, leg_countFalse_list)
    elif monster_leg_count == 0:
        return ProbCalc(0, leg_countTrue_list, leg_countFalse_list)
    else:
        print('leg_count is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def ArmCountProbAnalysis(self, monster_arm_count, arm_countTrue_list, arm_countFalse_list):
    """Calculates Probality of monster based on arm_count from Test cases from monster_list"""
    if monster_arm_count == 4:
        return ProbCalc(4, arm_countTrue_list, arm_countFalse_list)
    elif monster_arm_count == 3:
        return ProbCalc(3, arm_countTrue_list, arm_countFalse_list)
    elif monster_arm_count == 8:
        return ProbCalc(8, arm_countTrue_list, arm_countFalse_list)
    elif monster_arm_count == 6:
        return ProbCalc(6, arm_countTrue_list, arm_countFalse_list)
    else:
        print('arm_count is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def EyeCountProbAnalysis(self, monster_eye_count, eye_countTrue_list, eye_countFalse_list):
    """Calculates Probality of monster based on eye_count from Test cases from monster_list"""
    if monster_eye_count == 2:
        return ProbCalc(2, eye_countTrue_list, eye_countFalse_list)
    elif monster_eye_count == 8:
        return ProbCalc(8, eye_countTrue_list, eye_countFalse_list)
    else:
        print('eye_count is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def HornCountProbAnalysis(self, monster_eye_count, eye_countTrue_list, eye_countFalse_list):
    """Calculates Probality of monster based on eye_count from Test cases from monster_list"""
    if monster_eye_count == 2:
        return ProbCalc(2, eye_countTrue_list, eye_countFalse_list)
    elif monster_eye_count == 8:
        return ProbCalc(8, eye_countTrue_list, eye_countFalse_list)
    else:
        print('eye_count is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def LaysEggsProbAnalysis(self, monster_lays_eggs, lays_eggsTrue_list, lays_eggsFalse_list):
    """Calculates Probality of monster based on eye_count from Test cases from monster_list"""
    if monster_lays_eggs == True:
        return ProbCalc(True, lays_eggsTrue_list, lays_eggsFalse_list)
    elif monster_lays_eggs == False:
        return ProbCalc(False, lays_eggsTrue_list, lays_eggsFalse_list)
    else:
        print('lays_eggs is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def HasWingsProbAnalysis(self, monster_has_wings, has_wingsTrue_list, has_wingsFalse_list):
    """Calculates Probality of monster based on has_wings from Test cases from monster_list"""
    if monster_has_wings == True:
        return ProbCalc(True, has_wingsTrue_list, has_wingsFalse_list)
    elif monster_has_wings == False:
        return ProbCalc(False, has_wingsTrue_list, has_wingsFalse_list)
    else:
        print('has_wings is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def HasGillsProbAnalysis(self, monster_has_gills, has_gillsTrue_list, has_gillsFalse_list):
    """Calculates Probality of monster based on has_gills from Test cases from monster_list"""
    if monster_has_gills == True:
        return ProbCalc(True, has_gillsTrue_list, has_gillsFalse_list)
    elif monster_has_gills == False:
        return ProbCalc(False, has_gillsTrue_list, has_gillsFalse_list)
    else:
        print('has_gills is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def HasTailProbAnalysis(self, monster_has_tail, has_tailTrue_list, has_tailFalse_list):
    """Calculates Probality of monster based on has_tail from Test cases from monster_list"""
    if monster_has_tail == True:
        return ProbCalc(True, has_tailTrue_list, has_tailFalse_list)
    elif monster_has_tail == False:
        return ProbCalc(False, has_tailTrue_list, has_tailFalse_list)
    else:
        print('has_tail is not in monster_list UNKOWN!!')
        return dict(
            true_prob=0,
            false_prob=0
        )

def ProbCalc(value, trueList, falseList):
    """Calculates the probality of of true and false based on values"""
    true_vals = trueList.count(value)
    false_vals = falseList.count(value)
    total_vals = true_vals + false_vals
    true_prop = true_vals/total_vals
    false_prob = false_vals/total_vals
    return dict(
        true_prob=true_prop,
        false_prob=false_prob
    )