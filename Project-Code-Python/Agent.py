# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops, ImageOps
import numpy as np

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        value = -1
        
        if problem.problemSetName == 'Basic Problems D':
            if problem.name == 'Basic Problem D-11':
                print(f'Working on {problem.problemSetName}, {problem.name}')
                print('---------------------------')

                if problem.problemType == '2x2':
                    print(problem.problemType)

                    if problem.hasVerbal == True:
                        print('VERBAL ANALYSIS')
                        #problem_dict = verbal2x2dicts(self, problem)
                        
                        #DONT TOUCH THIS IS GOOD
                        #problem_analysis = VerbalProblemAnalysis1(self, problem_dict)

                        #value = problem_analysis['problem_ans']
                        #print(value)
                        
                        print('---------------------------')

                    if problem.hasVisual == True:
                        print('VISUAL ANALYSIS')
                        problem_dict = Visual2x2ProblemDict(self, problem)
                        ans_list = Visual2x2AnswerList(self, problem_dict)
                        value = Visual2x2AnswerAnalyzer(self, ans_list)
                        print(value)
                        print('--------------------------------------------')
                elif problem.problemType == '3x3':
                    print(problem.problemType)
                    if problem.hasVerbal == True:
                        print('VERBAL ANALYSIS')
                    if problem.hasVisual == True:
                        print('VISUAL ANALYSIS')
                        #print(Visual3x3ProblemDict(self, problem))
                        #problem_dict = Visual3x3ProblemAnalysisDict(self, problem)
                        fig_a = Image.open(problem.figures['A'].visualFilename, mode='r').convert('1')
                        fig_b = Image.open(problem.figures['B'].visualFilename, mode='r').convert('1')
                        fig_c = Image.open(problem.figures['C'].visualFilename, mode='r').convert('1')
                        fig_d = Image.open(problem.figures['D'].visualFilename, mode='r').convert('1')
                        fig_e = Image.open(problem.figures['E'].visualFilename, mode='r').convert('1')
                        fig_f = Image.open(problem.figures['F'].visualFilename, mode='r').convert('1')
                        fig_g = Image.open(problem.figures['G'].visualFilename, mode='r').convert('1')
                        fig_h = Image.open(problem.figures['H'].visualFilename, mode='r').convert('1')

                        ans_img_strs = ['1','2','3','4','5','6','7','8']

                        answer_list = []

                        fig_ans = Image.open(problem.figures['7'].visualFilename, mode='r').convert('1')

                        #print(VisualAndOrXORComps(self, fig_a, fig_b, fig_c))
                        #print(VisualAndOrXORComps(self, fig_d, fig_e, fig_f))
                        #print(VisualAndOrXORComps(self, fig_g, fig_h, fig_ans))

                        #diff_fig = ImageChops.difference(fig_g,fig_h)
                        #diff_conv = diff_fig.convert('L')
                        #diff_inv = ImageOps.invert(diff_conv)
                        #final_inv = diff_inv.convert('1')
                        #print(rms_diff(final_inv,fig_ans))

                        #print(VisualImagePixelComp(self, fig_a,fig_b))

                        for img_str in ans_img_strs:
                            print('------------------------------')
                            print('------------------------------')
                            print(problem.figures[img_str].visualFilename)
                            print('------------------------------')
                            print('------------------------------')
                            answ_fig = Image.open(problem.figures[img_str].visualFilename, mode='r').convert('1')

                            horz = HorzProbAnalysisVisual3x3(self, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, answ_fig)
                            vert = VertProbAnalysisVisual3x3(self, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, answ_fig)
                            diag = DiagProbAnalysisVisual3x3(self, fig_a, fig_b, fig_f, fig_e, fig_d, fig_h, answ_fig)


                            tot = np.sum([horz,vert,diag])

                            answer_list.append((int(img_str),tot))

                        


                        print(answer_list)
                        answer = min(answer_list, key=lambda n: (n[1], -n[0]))
                        print(answer)

                        value = answer[0]
                
                else:
                    pass
            else:
                pass
        else:
            pass

        return value

#####VERBAL FUNCTIONS#######
def VerbalNoChange(self, fig_problem_dict1, fig_problem_dict2):

    if 'shape' in fig_problem_dict1 and 'shape' in fig_problem_dict2:
       if fig_problem_dict1['shape'] != fig_problem_dict2['shape']:
           return False
    if 'size' in fig_problem_dict1 and 'size' in fig_problem_dict2:
       if fig_problem_dict1['size'] != fig_problem_dict2['size']:
           return False
    if 'fill' in fig_problem_dict1 and 'fill' in fig_problem_dict2:
       if fig_problem_dict1['fill'] != fig_problem_dict2['fill']:
           return False
    if 'angle' in fig_problem_dict1 and 'angle' in fig_problem_dict2:
       if fig_problem_dict1['angle'] != fig_problem_dict2['angle']:
           return False
    if 'alignment' in fig_problem_dict1 and 'alignment' in fig_problem_dict2:
       if fig_problem_dict1['alignment'] != fig_problem_dict2['alignment']:
           return False

    #####NEED TO COME BACK AND FIGURE THIS ONE OUT#########
    #if 'inside' in fig_problem_dict1 and 'inside' in fig_problem_dict2:
    #   if fig_problem_dict1['inside'] != fig_problem_dict2['inside']:
    #       return False
    return True

def VerbalRotationCalc(self, fig_problem_dict1, fig_problem_dict2):
    rotation = 0
    if 'angle' in fig_problem_dict1 and 'angle' in fig_problem_dict2:
       if fig_problem_dict1['angle'] != fig_problem_dict2['angle']:
           angleX = int(fig_problem_dict1['angle'])
           angleY = int(fig_problem_dict2['angle'])
           if (angleY - angleX - 180) < 0:
                angle_diff = angleY - angleX
                rotation = angle_diff/20
           if (angleY - angleX - 180) > 0:
                angle_diff = angleX - angleY + 180
                rotation = angle_diff/20
       
    return rotation

def VerbalReflection(self, fig_problem_dict1, fig_problem_dict2):
    if 'fill' in fig_problem_dict1 and 'fill' in fig_problem_dict2:
        if fig_problem_dict1['fill'] == fig_problem_dict2['fill']:
            #if 'shape' in fig_problem_dict1 and 'shape' in fig_problem_dict2:
        #if fig_problem_dict1['shape'] == fig_problem_dict2['shape']:
            if 'angle' in fig_problem_dict1 and 'angle' in fig_problem_dict2:
                if fig_problem_dict1['angle'] != fig_problem_dict2['angle']:
                    angleX = int(fig_problem_dict1['angle'])
                    angleY = int(fig_problem_dict2['angle'])
                    if abs(angleY - angleX) == 90 or abs(angleY - angleX) == 270:
                        return True
            if 'alignment' in fig_problem_dict1 and 'alignment' in fig_problem_dict2:
                if fig_problem_dict1['alignment'] != fig_problem_dict2['alignment']:
                    alignmentX = fig_problem_dict1['alignment']
                    alignmentY = fig_problem_dict2['alignment']
                    alignX1, alignX2 = alignmentX.split('-')
                    alignY1, alignY2 = alignmentY.split('-')
                    if alignX1 == alignY1 and alignX2 != alignY2:
                        return True
                    if alignX2 == alignY2 and alignX1 != alignY1:
                        return True
    return False

def VerbalTransformsCalcs(self,transforms):
    trans_points = transforms['points']
    if 'no_change' in transforms:
        if transforms['no_change'] == True:
            trans_points += 10
    if 'shape_trans' in transforms:
        if transforms['shape_trans']['shape_change'] == True:
            trans_points += 5
            if transforms['shape_trans']['initial_shape'] == 'right_triangle' and transforms['shape_trans']['change_shape'] == 'square':
                trans_points += 1
    if 'size_trans' in transforms:
        if transforms['size_trans']['size_change'] == True:
            trans_points += 4
            #if transforms['shape_trans']['initial_shape'] == 'right_triangle' and transforms['shape_trans']['change_shape'] == 'square':
            #    trans_points += 2
    if 'fill_trans' in transforms:
        if transforms['fill_trans']['fill_change'] == True:
            trans_points += 1
    if 'angle_trans' in transforms:
        if transforms['angle_trans']['angle_change'] == True:
            if transforms['angle_trans']['angle_reflection'] == True:
                trans_points += 7
                if 'rotation_pts' in transforms['angle_trans']:
                    if transforms['angle_trans']['rotation_pts'] != 0:
                        trans_points += abs(transforms['angle_trans']['rotation_pts'])
            if transforms['angle_trans']['angle_reflection'] == False:
                if 'rotation_pts' in transforms['angle_trans']:
                    if transforms['angle_trans']['rotation_pts'] != 0:
                        trans_points += transforms['angle_trans']['rotation_pts']
    if 'inside_trans' in transforms:
        if transforms['inside_trans']['inside_change'] == True:
            trans_points += 4
    if 'alignment_trans' in transforms:
        if transforms['alignment_trans']['alignment_change'] == True:
            trans_points += 4
            if transforms['alignment_trans']['top_bottom_trans'] == True:
                trans_points += 2
            if transforms['alignment_trans']['left_right_trans'] == True:
                trans_points += 2    
    if 'above_trans' in transforms:
        if transforms['above_trans']['above_change'] == True:
            trans_points += 1
    return trans_points


def VerbalPointsCalcs(self, fig_problem_dict1, fig_problem_dict2):
    points = 0
    if len(fig_problem_dict1) == len(fig_problem_dict2):
        for a, b in zip(fig_problem_dict1, fig_problem_dict2):
            transforms={}
            change_points = 0
            if 'shape' in a and 'shape' in b:
                if a['shape'] == b['shape']:
                    change_points += 1
                if a['shape'] != b['shape']:
                    shape_trans=dict(
                        shape_change=True,
                        initial_shape = a['shape'],
                        change_shape = b['shape']
                    )
                    transforms['shape_trans'] = shape_trans
            if 'size' in a and 'size' in b:
                if a['size'] == b['size']:
                    change_points += 1
                if a['size'] != b['size']:
                    size_trans=dict(
                        size_change=True,
                        initial_size = a['size'],
                        change_size = b['size']
                    )
                    transforms['size_trans'] = size_trans
            if 'fill' in a and 'fill' in b:
                if a['fill'] == b['fill']:
                    change_points += 1
                if a['fill'] != b['fill']:
                    fill_trans=dict(
                        fill_change=True
                    )
                    transforms['fill_trans'] = fill_trans
            if 'angle' in a and 'angle' in b:
                if a['angle'] == b['angle']:
                    change_points += 1
                    angle_trans=dict(
                        angle_change=False
                    )
                    transforms['angle_trans'] = angle_trans
                #putting rotation function where we are already needing angle
                if a['angle'] != b['angle']:
                    rotation_pts = VerbalRotationCalc(self, a, b)
                    angle_reflection = VerbalReflection(self, a, b)
                    angle_trans=dict(
                        angle_change=True,
                        angle_reflection=angle_reflection,
                        rotation_pts=rotation_pts
                    )
                    transforms['angle_trans'] = angle_trans
            if 'inside' in a and 'inside' in b:
                if a['inside'] == b['inside']:
                    change_points += 1
                if a['inside'] != b['inside']:
                    inside_trans=dict(
                        inside_change = True
                    )
                    transforms['inside_trans'] = inside_trans
            if 'alignment' in a and 'alignment' in b:

                if a['alignment'] == b['alignment']:
                    change_points += 1
                if a['alignment'] != b['alignment']:
                    apart1, apart2 = a['alignment'].split('-')
                    bpart1, bpart2 = b['alignment'].split('-')
                    alignment_change = True
                    if apart1 == bpart1:
                        top_bottom_trans = False
                    if apart1 != bpart1:
                        top_bottom_trans = True
                    if apart2 == bpart2:
                        left_right_trans = False
                    if apart2 != bpart2:
                        left_right_trans = True
                    
                    alignment_trans=dict(
                        alignment_change=alignment_change,
                        top_bottom_trans=top_bottom_trans,
                        left_right_trans=left_right_trans
                    )
                    transforms['alignment_trans'] = alignment_trans
            if 'above' in a and 'above' in b:
                if a['above'] == b['above']:
                    change_points += 1
                if a['above'] != b['above']:
                    above_change=True
                
                    above_trans=dict(
                        above_change=above_change
                    )
                    transforms['above_trans'] = above_trans
            
            transforms['no_change'] = VerbalNoChange(self, a, b)
            transforms['points'] = change_points
            print(transforms)
            compare_points = VerbalTransformsCalcs(self,transforms)
            points += compare_points
            #print('-----------------------')
    return points

def VerbalProblemAnalysis(self, problem_dict):

    ab_points = VerbalPointsCalcs(self, problem_dict["figA"], problem_dict["figB"])
    ac_points = VerbalPointsCalcs(self, problem_dict["figA"], problem_dict["figC"])
    #VerbalPointsCalcs(self,problem_dict["figB"],problem_dict["fig3"])
    c1_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig1"])
    c2_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig2"])
    c3_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig3"])
    c4_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig4"])
    c5_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig5"])
    c6_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig6"])

    b1_points = VerbalPointsCalcs(self,problem_dict["figB"], problem_dict["fig1"])
    b2_points = VerbalPointsCalcs(self,problem_dict["figB"], problem_dict["fig2"])
    b3_points = VerbalPointsCalcs(self,problem_dict["figB"],problem_dict["fig3"])
    b4_points = VerbalPointsCalcs(self,problem_dict["figB"], problem_dict["fig4"])
    b5_points = VerbalPointsCalcs(self,problem_dict["figB"], problem_dict["fig5"])
    b6_points = VerbalPointsCalcs(self,problem_dict["figB"], problem_dict["fig6"])

    abc_points = ab_points + ac_points

    fig1_points = c1_points + b1_points
    fig2_points = c2_points + b2_points
    fig3_points = c3_points + b3_points
    fig4_points = c4_points + b4_points
    fig5_points = c5_points + b5_points
    fig6_points = c6_points + b6_points

    problem_points = dict(
        fig1_points = fig1_points,
        fig2_points = fig2_points,
        fig3_points = fig3_points,
        fig4_points = fig4_points,
        fig5_points = fig5_points,
        fig6_points = fig6_points
    )

    #calculates the figure with minimum points away from abc_points
    key, value = min(problem_points.items(), key=lambda kv : abs(kv[1] - abc_points))
    
    problem_ans = VerbalProblemAnswerCalc(self, key)

    problem_anlysis = dict(
       abc_points = abc_points,
       problem_points = problem_points, 
       problem_value = value,
       problem_key = key,
       problem_ans = problem_ans
    )

    return problem_anlysis

def VerbalProblemAnalysis1(self, problem_dict):

    ab_points = VerbalPointsCalcs(self, problem_dict["figA"], problem_dict["figB"])
    #ac_points = VerbalPointsCalcs(self, problem_dict["figA"], problem_dict["figC"])

    c1_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig1"])
    c2_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig2"])
    c3_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig3"])
    c4_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig4"])
    c5_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig5"])
    c6_points = VerbalPointsCalcs(self,problem_dict["figC"], problem_dict["fig6"])

    fig1_points = c1_points
    fig2_points = c2_points
    fig3_points = c3_points
    fig4_points = c4_points
    fig5_points = c5_points
    fig6_points = c6_points

    problem_points = dict(
        fig1_points = fig1_points,
        fig2_points = fig2_points,
        fig3_points = fig3_points,
        fig4_points = fig4_points,
        fig5_points = fig5_points,
        fig6_points = fig6_points
    )

    #calculates the figure with minimum points away from abc_points
    key, value = min(problem_points.items(), key=lambda kv : abs(kv[1] - ab_points))
    
    problem_ans = VerbalProblemAnswerCalc(self, key)

    problem_anlysis = dict(
       ab_points = ab_points,
       problem_points = problem_points, 
       problem_value = value,
       problem_key = key,
       problem_ans = problem_ans
    )

    return problem_anlysis

def VerbalProblemAnswerCalc(self, key):
    global answer

    if key == 'fig1_points':
        answer = 1
    elif key == 'fig2_points':
        answer = 2
    elif key == 'fig3_points':
        answer = 3
    elif key == 'fig4_points':
        answer = 4
    elif key == 'fig5_points':
        answer = 5
    elif key == 'fig6_points':
        answer = 6
    else:
        answer = -1

    return answer

#####VISUAL FUNCTIONS####### 
###########GENERAL VISUAL FUNCTIONS########### 
def image_similarity_pct(self, image1, image2):
    """Calculates Image similarity between by comparing images pixel by pixel."""
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."
    
    pairs = zip(image1.getdata(), image2.getdata())
    if len(image1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = image1.size[0] * image1.size[1] * 3

    return (100 - (dif / 255.0 * 100) / ncomponents)

def rms_diff(image_1, image_2):
    """Calculates the root-mean-square difference between the images."""
    assert image_1.mode == image_2.mode, "Different kinds of images."
    assert image_1.size == image_1.size, "Different sizes."
    diff = ImageChops.difference(image_1, image_2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = np.sqrt(sum_of_squares/float(image_1.size[0] * image_1.size[1]))
    return rms



def VisualNoChange(self, image1, image2):
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."

    return rms_diff(image1, image2)

def VisualHorzReflection(self, image1, image2):
    """Calculating RMS Difference of Horizontal Reflection between the two images."""
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."
        
    return rms_diff(image1, image2.transpose(Image.FLIP_LEFT_RIGHT)) 

def VisualVertReflection(self, image1, image2):
    """Calculating RMS Difference of Horizontal Reflection between the two images."""
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."

    return rms_diff(image1, image2.transpose(Image.FLIP_TOP_BOTTOM))

def VisualRotationCalc(self,image1, image2):
    rotation_dict=[]
    rotation=45
    while rotation >= 45 and rotation < 360:
        img_simil = rms_diff(image1.rotate(rotation), image2)
        rotation_degree = str(rotation)
        rotation_rec = dict(
            img_rotation=rotation_degree,
            rotation_score=img_simil
            )
        rotation_dict.append(rotation_rec)
        
        rotation +=  45
        
    return rotation_dict

def VisualImagePixelComp(self, image1, image2):
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."

    im1 = np.asarray(image1.convert('L'))
    im2 = np.asarray(image2.convert('L'))

    im1_black = ((im1 == 0).astype(int)).sum()
    im1_white = ((im1 == 255).astype(int)).sum()

    im2_black = ((im2 == 0).astype(int)).sum()
    im2_white = ((im2 == 255).astype(int)).sum()

    im1_fill_pct = im1_black/(im1_black+im1_white)
    im2_fill_pct = im2_black/(im2_black+im2_white)

    ##DARK PIXEL RATIO CHANGE
    fill_diff = im2_fill_pct-im1_fill_pct

    ##INTERSECTION PIXEL RATIO INCLUDING WHITE & BLACK PIXELS##
    ipr = image_similarity_pct(self, image1, image2)

    ##INTERSECTION PIXEL RATIO OF JUST THE DARK PIXELS
    intersect_img = ImageChops.logical_or(image1, image2)
    intersect_array = np.asarray(intersect_img.convert('L'))
    intersect_black = ((intersect_array == 0).astype(int)).sum()
    intersect_white = ((intersect_array == 255).astype(int)).sum()

    dpir = intersect_black/(intersect_white+intersect_black)
    
    return dict(
        #im1_black=im1_black,
        #im1_white=im1_white,
        #im1_fill_pct=im1_fill_pct,
       # im2_black=im2_black,
        #im2_white=im2_white,
        #im2_fill_pct=im2_fill_pct,
        dpr=fill_diff,
        #ipr=ipr,
        dpir=dpir
    )
def VisualImgCompAffinityTransforms(self, image1, image2):
    ##### No Change Comparison #####
    noChange_Thresh = 99.5
    img_sim = image_similarity_pct(self, image1, image2)
    if img_sim >= noChange_Thresh:
        noChangeVal = 500
    elif img_sim < noChange_Thresh:
        noChangeVal = 0
    else:
        print('Error calculating Image Visual No Change Score')

    return dict(
        vis_noChange = noChangeVal
    )

def VisualRowAffinityTransforms(self, image1, image2, image3):
    """Provides Dictionary of all Image Affinity Transformations."""
    assert image1.mode == image2.mode == image3.mode, "Different kinds of images."
    assert image1.size == image1.size == image3.size, "Different sizes."

    ###ROW VISUAL NO CHANGE###
    noChange_Threshold = .25
    noChange_12 = VisualNoChange(self, image1, image2)
    noChange_23 = VisualNoChange(self, image2, image3)
    noChange_diff = noChange_12 - noChange_23
    if abs(noChange_diff) < noChange_Threshold:
        aff_NoChange = 500
    elif abs(noChange_diff) > noChange_Threshold:
        aff_NoChange = 0 
    else:
        print('Error Calculating Row Visual No Change Transform')

    ###ROW HORZ REFLECTION####
    horzReflect_Threshold = .25
    horzReflect_12 = VisualHorzReflection(self, image1, image2)
    horzReflect_23 = VisualHorzReflection(self, image2, image3)
    horzReflect_diff = horzReflect_12 - horzReflect_23
    if abs(horzReflect_diff) < horzReflect_Threshold:
        aff_HorzReflect = 500
    elif abs(horzReflect_diff) > horzReflect_Threshold:
        aff_HorzReflect = 0 
    else:
        print('Error Calculating Row Visual Horizontal Reflection Transform')

    ###ROW VERT REFLECTION####
    vertReflect_Threshold = 11
    vertReflect_12 = VisualVertReflection(self, image1, image2)
    vertReflect_23 = VisualVertReflection(self, image2, image3)
    vertReflect_diff = vertReflect_12 - vertReflect_23
    if abs(vertReflect_diff) < vertReflect_Threshold:
        aff_VertReflect = 500
    elif abs(vertReflect_diff) > vertReflect_Threshold:
        aff_VertReflect = 0 
    else:
        print('Error Calculating Row Visual Vertical Reflection Transform')

    #vizRotations = VisualRotationCalc(self,image1, image2)

    affTrans_totScore = aff_NoChange + aff_HorzReflect + aff_VertReflect

    return dict(
        viz_noChange=aff_NoChange,
        vizHorzReflect=aff_HorzReflect,
        vizVertReflect=aff_VertReflect,
        #vizRotations=vizRotations,
        affTransTotScore=affTrans_totScore
    )

def otherRowComps(self, image1, image2, image3):
    """Calculating other row patterns."""
    ###Calculating image1 to image3 Horizontal Reflection###
    horzReflect_Threshold = 25
    horzReflect_13 = VisualHorzReflection(self, image1, image3)
    if horzReflect_13 <= horzReflect_Threshold:
        im1_im3_HorzReflect = 250
    elif horzReflect_13 > horzReflect_Threshold:
        im1_im3_HorzReflect = 0 
    else:
        print('Error Calculating Image1 to Image3 Visual Horizontal Reflection Transform')

    ##Calculating image1 to image3 Vertical Reflection###
    vertReflect_Threshold = 25
    vertReflect_13 = VisualVertReflection(self, image1, image3)
    if vertReflect_13 <= vertReflect_Threshold:
        im1_im3_VertReflect = 250
    elif vertReflect_13 > vertReflect_Threshold:
        im1_im3_VertReflect = 0 
    else:
        print('Error Calculating Image1 to Image3 Visual Vertical Reflection Transform')

    ####Compares ROW Dark Pixel Ratio(DPR) Derivative and gives it a score###
    dpr_threshold = .008
    imgComp_12 = VisualImagePixelComp(self, image1, image2)
    imgComp_23 = VisualImagePixelComp(self, image2, image3)

    imgComp_diff = imgComp_12['dpr'] - imgComp_23['dpr']

    if abs(imgComp_diff) <= dpr_threshold:
        dprRow_score = 500
    elif abs(imgComp_diff) > dpr_threshold:
        dprRow_score = 0
    else:
        print('Error Calculating DPR Row Derivative Score')
    
    ##Subtracting and Adding dark Pixels for Third Image 
    im1 = np.asarray(image1.convert('L'))
    im2 = np.asarray(image2.convert('L'))
    im3 = np.asarray(image3.convert('L'))

    im1_black = ((im1 == 0).astype(int)).sum()
    im2_black = ((im2 == 0).astype(int)).sum()
    im3_black = ((im3 == 0).astype(int)).sum()

    sub_12dark = im1_black - im2_black
    add_12dark = im1_black + im2_black
    
    pixel_sub_thresh = 25
    if abs(im3_black - sub_12dark) <= pixel_sub_thresh:
        pixel_sub_score = 500
    elif abs(im3_black - sub_12dark) > pixel_sub_thresh:
        pixel_sub_score = 0 
    else:
        print('Error Calculating Pixel Subtraction Score!!!')

    pixel_add_thresh = 25
    if abs(im3_black - add_12dark) <= pixel_add_thresh:
        pixel_add_score = 500
    elif abs(im3_black - add_12dark) > pixel_add_thresh:
        pixel_add_score = 0 
    else:
        print('Error Calculating Pixel Subtraction Score!!!')
    

    tot_otherComps = im1_im3_HorzReflect + im1_im3_VertReflect + dprRow_score #+ pixel_sub_score + pixel_add_score

    return dict(
        horzReflect_13 = im1_im3_HorzReflect,
        vertReflect_13 = im1_im3_VertReflect,
        dprRow_score = dprRow_score,
        pixel_sub_score = pixel_sub_score,
        pixel_add_score = pixel_add_score,
        tot_otherComps = tot_otherComps
    )
    


def VisualAndOrXORComps(self, image1, image2, image3):
    assert image1.mode == image2.mode == image3.mode, "Different kinds of images."
    assert image1.size == image2.size == image3.size, "Different sizes."

    ### AND Comparison Img1 & Im2 compared to image 3 RMS ###
    im_and12 = ImageChops.logical_and(image1,image2)
    #im_and12.show()
    andComp12_3 = rms_diff(im_and12, image3)
    andComp_thresh = 50
    if andComp12_3 <= andComp_thresh:
        andComp12_3_val = 500
    elif andComp12_3 > andComp_thresh:
        andComp12_3_val = 0
    else:
        print('Error Calculating andComp12_3 Value')

    ### OR Comparison Img1 & Im2 compared to image 3 RMS ###
    im_or12 = ImageChops.logical_or(image1, image2)
    #im_or12.show()
    orComp12_3 = rms_diff(im_or12, image3)
    orComp_thresh = 50
    if orComp12_3 <= orComp_thresh:
        orComp12_3_val = 500
    elif orComp12_3 > orComp_thresh:
        orComp12_3_val = 0
    else:
        print('Error Calculating orComp12_3 Value')

    ### XOR Comparison Img1 & Im2 compared to image 3 RMS ###
    im_xor12 = ImageChops.logical_xor(image1, image2)
    #im_xor12.show()

    inv_im = im_xor12.convert('L')
    inverted_xor = ImageOps.invert(inv_im)

    final_xor = inverted_xor.convert('1')
    #final_xor.show()
    xorComp12_3 = rms_diff(final_xor, image3)

    xorComp_thresh = 50
    if xorComp12_3 <= xorComp_thresh:
        xorComp12_3_val = 500
    elif xorComp12_3 > xorComp_thresh:
        xorComp12_3_val = 0
    else:
        print('Error Calculating xorComp12_3 Value')

    total_score = andComp12_3_val + orComp12_3_val + xorComp12_3_val

    return dict(
        andComp12_3 = andComp12_3,
        orComp12_3 = orComp12_3,
        xorComp12_3 = xorComp12_3,
        total_score = total_score
    )

def RowToRowComps(self, image1, image2, image3, image4, image5, image6, image7, image8, fig_ans):
    """Calculating Row to ROw Comps, SameImage Across Rows."""
    ###First Row Images###
    diff_fig1 = ImageChops.difference(image1, image2)
    diff_fig2 = ImageChops.difference(image2, image3)
    
    ###Second Row Images###
    diff_fig3 = ImageChops.difference(image4, image5)
    diff_fig4 = ImageChops.difference(image5, image6)

    ###Third Row Images###
    diff_fig5 = ImageChops.difference(image7, image8)
    diff_fig6 = ImageChops.difference(image8,fig_ans)

    
    tot1_image = ImageChops.logical_or(diff_fig1,diff_fig2)
    tot2_image = ImageChops.logical_or(diff_fig3,diff_fig4)
    tot3_image = ImageChops.logical_or(diff_fig5,diff_fig6)

    #tot1_image.show()
    #tot2_image.show()
    #tot3_image.show()

    row12_simil = rms_diff(tot1_image, tot2_image)
    row23_simil = rms_diff(tot2_image, tot3_image)
    #print(row12_simil)
    #print(row23_simil)

    combinedRow_imgThresh = 7
    if abs(row12_simil-row23_simil) <= combinedRow_imgThresh:
        combinedRow_ImgsScore = abs(row12_simil-row23_simil)

    elif abs(row12_simil-row23_simil) > combinedRow_imgThresh:
        combinedRow_ImgsScore = 0
    else:
        print('Error Calculating the Combined Image Row Score!')

    return dict(
        row12_simil = row12_simil,
        row23_simil = row23_simil,
        combinedRow_ImgsScore = combinedRow_ImgsScore
    )



def VisualImageComparison(self, image1, image2):
    assert image1.mode == image2.mode, "Different kinds of images."
    assert image1.size == image1.size, "Different sizes."

    return dict(
        #rms_diff = rms_diff(image1, image2),
        pixel_comp = VisualImagePixelComp(self, image1, image2),
        affinity_transforms = VisualImgCompAffinityTransforms(self, image1, image2),
        ) 

######### VISUAL 2x2 PROBLEM FUNCTIONS #############    
def Visual2x2ProblemDict(self, problem):
    figa = Image.open(problem.figures['A'].visualFilename).convert('RGB')
    figb = Image.open(problem.figures['B'].visualFilename).convert('RGB')
    figc = Image.open(problem.figures['C'].visualFilename).convert('RGB')
    fig1 = Image.open(problem.figures['1'].visualFilename).convert('RGB')
    fig2 = Image.open(problem.figures['2'].visualFilename).convert('RGB')
    fig3 = Image.open(problem.figures['3'].visualFilename).convert('RGB')
    fig4 = Image.open(problem.figures['4'].visualFilename).convert('RGB')
    fig5 = Image.open(problem.figures['5'].visualFilename).convert('RGB')
    fig6 = Image.open(problem.figures['6'].visualFilename).convert('RGB')
    
    """-----Probelem set FigA & FigB, FigC Comparison-----."""
    abc_analysis = dict(
        horz_comp = VisualImageComparison(self, figa, figb),
        vert_comp = VisualImageComparison(self, figa, figc),
        diag_comp = VisualImageComparison(self, figb, figc)
    )
    answer_analysis = []
    """-----FigC & FigB, Fig1 Comparison-----."""
    ans_1 = dict(
        horz_comp = VisualImageComparison(self, figc, fig1),
        vert_comp = VisualImageComparison(self, figb, fig1),
        diag_comp = VisualImageComparison(self, figa, fig1)
    )
    answer_analysis.append({'ans_1':ans_1})

    """-----FigC & FigB, Fig2 Comparison-----."""
    ans_2 = dict(
        horz_comp = VisualImageComparison(self, figc, fig2),
        vert_comp = VisualImageComparison(self, figb, fig2),
        diag_comp = VisualImageComparison(self, figa, fig2)
    )
    answer_analysis.append({'ans_2':ans_2})
    """-----FigC & FigB, Fig3 Comparison-----."""
    ans_3 = dict(
        horz_comp = VisualImageComparison(self, figc, fig3),
        vert_comp = VisualImageComparison(self, figb, fig3),
        diag_comp = VisualImageComparison(self, figa, fig3)
    )
    answer_analysis.append({'ans_3':ans_3})

    """-----FigC & FigB, Fig4 Comparison-----."""
    ans_4 = dict(
        horz_comp = VisualImageComparison(self, figc, fig4),
        vert_comp = VisualImageComparison(self, figb, fig4),
        diag_comp = VisualImageComparison(self, figa, fig4)
    )
    answer_analysis.append({'ans_4':ans_4})

    """-----FigC & FigB, Fig5 Comparison-----."""
    ans_5 = dict(
        horz_comp = VisualImageComparison(self, figc, fig5),
        vert_comp = VisualImageComparison(self, figb, fig5),
        diag_comp = VisualImageComparison(self, figa, fig5)
    )
    answer_analysis.append({'ans_5':ans_5})
    """-----FigC & FigB, Fig6 Comparison-----."""
    ans_6 = dict(
        horz_comp = VisualImageComparison(self, figc, fig6),
        vert_comp = VisualImageComparison(self, figb, fig6),
        diag_comp = VisualImageComparison(self, figa, fig6)
    )
    answer_analysis.append({'ans_6':ans_6})

    problem_analysis = dict(
        abc_analysis=abc_analysis,
        answer_analysis=answer_analysis
    )

    return problem_analysis

def Visual2x2ProceduralAnalysis(self, abc_analysis, fig):
    """This determines if the answer figures pass the procedural tests of the problemset."""

    """These are the procedural Horizontal comparisons."""
    if abc_analysis['horz_comp']['vis_unchanged'] == fig['horz_comp']['vis_unchanged']:
        if abc_analysis['horz_comp']['vis_horz_reflect'] == fig['horz_comp']['vis_horz_reflect']:
            if abc_analysis['horz_comp']['vis_vert_reflect'] == fig['horz_comp']['vis_vert_reflect']:
                if abc_analysis['horz_comp']['vis_fill_comp']['fill_change'] == fig['horz_comp']['vis_fill_comp']['fill_change']:
                    if abc_analysis['horz_comp']['vis_rotation'] != [] and fig['horz_comp']['vis_rotation'] != []:
                        for prob_rot, fig_rot in zip(abc_analysis['horz_comp']['vis_rotation'], fig['horz_comp']['vis_rotation']):
                            if prob_rot['img_rotation'] == fig_rot['img_rotation']:
                                print("Passed Horz Procedural Comp")
                                horz_pass = True
                            else:
                                print('Failed vert rot comp...')
                                horz_pass = False
                    elif abc_analysis['horz_comp']['vis_rotation'] == [] and fig['horz_comp']['vis_rotation'] == []:
                        print("Passed Horz Procedural Comp")
                        horz_pass = True
                    else:
                        print('Failed horz blank rot comp...')
                        horz_pass = False
                else:
                    print('Failed horz fill change comp...')
                    horz_pass = False
            else:
                print('Failed horz vert reflection comp...')
                horz_pass = False
        else:
            print('Failed horz horz reflection comp...')
            horz_pass = False
    else:
        print('Failed horz unchanged comp...')
        horz_pass = False

    """These are the procedural Vertical comparisons."""
    if abc_analysis['vert_comp']['vis_unchanged'] == fig['vert_comp']['vis_unchanged']:
        if abc_analysis['vert_comp']['vis_horz_reflect'] == fig['vert_comp']['vis_horz_reflect']:
            if abc_analysis['vert_comp']['vis_vert_reflect'] == fig['vert_comp']['vis_vert_reflect']:
                if abc_analysis['vert_comp']['vis_fill_comp']['fill_change'] == fig['vert_comp']['vis_fill_comp']['fill_change']:
                    if abc_analysis['vert_comp']['vis_rotation'] != [] and fig['vert_comp']['vis_rotation'] != []:
                        for prob_rot, fig_rot in zip(abc_analysis['vert_comp']['vis_rotation'], fig['vert_comp']['vis_rotation']):
                            if prob_rot['img_rotation'] == fig_rot['img_rotation']:
                                print("Passed Vert Procedural Comp")
                                vert_pass = True
                            else:
                                print('Failed vert rot comp...')
                                vert_pass = False
                    elif abc_analysis['vert_comp']['vis_rotation'] == [] and fig['vert_comp']['vis_rotation'] == []:
                        print("Passed Vert Procedural Comp")
                        vert_pass = True
                    else:
                        print('Failed vert blank rot comp...')
                        vert_pass = False
                else:
                    print('Failed vert fill change comp...')
                    vert_pass = False
            else:
                print('Failed vert vert reflection comp...')
                vert_pass = False
        else:
            print('Failed vert horz reflection comp...')
            vert_pass = False
    else:
        print('Failed vert unchanged comp...')
        vert_pass = False
    
    """These are the procedural Diagonal comparisons."""
    if abc_analysis['diag_comp']['vis_unchanged'] == fig['diag_comp']['vis_unchanged']:
        if abc_analysis['diag_comp']['vis_horz_reflect'] == fig['diag_comp']['vis_horz_reflect']:
            if abc_analysis['diag_comp']['vis_vert_reflect'] == fig['diag_comp']['vis_vert_reflect']:
                if abc_analysis['diag_comp']['vis_fill_comp']['fill_change'] == fig['diag_comp']['vis_fill_comp']['fill_change']:
                    if abc_analysis['diag_comp']['vis_rotation'] != [] and fig['diag_comp']['vis_rotation'] != []:
                        for prob_rot, fig_rot in zip(abc_analysis['diag_comp']['vis_rotation'], fig['diag_comp']['vis_rotation']):
                            if prob_rot['img_rotation'] == fig_rot['img_rotation']:
                                diag_pass = True
                                print("Passed Diag Procedural Comp")
                            else:
                                print('Failed diag rot comp...')
                                diag_pass = False
                    elif abc_analysis['diag_comp']['vis_rotation'] == [] and fig['diag_comp']['vis_rotation'] == []:
                        diag_pass = True
                        print("Passed Diag Procedural Comp")
                    else:
                        print('Failed diag blank rot comp...')
                        diag_pass = False
                else:
                    print('Failed diag fill change comp...')
                    diag_pass = False
            else:
                print('Failed diag vert reflection comp...')
                diag_pass = False
        else:
            print('Failed diag horz reflection comp...')
            diag_pass = False
    else:
        print('Failed diag unchanged...')
        diag_pass = False
    
    answer = dict(
        horz_pass=horz_pass,
        vert_pass=vert_pass,
        diag_pass=diag_pass
    )
    return answer

def Visual2x2AnswerList(self, problem_analysis):
    answer_list = []
    i=0
    while i <= 5:
        ans = ('ans_' + str(i+1))
        fig = problem_analysis['answer_analysis'][i][ans]
        proc_comp = Visual2x2ProceduralAnalysis(self, problem_analysis['abc_analysis'], fig)
        
        if ((proc_comp['horz_pass'] == True) and (proc_comp['vert_pass'] == True) and (proc_comp['diag_pass'] == True)):
            answer_list.append(problem_analysis['answer_analysis'][i])
        elif ((proc_comp['horz_pass'] != True) or (proc_comp['vert_pass'] != True) or (proc_comp['diag_pass'] != True)):
            pass
        else:
            print('UNKNOWN ERROR EVALUATING PROCEDURAL CRITERIA!!!!')
        
        i+=1

    return answer_list

def Visual2x2AnswerAnalyzer(self, answr_list):
    global answer

    if len(answr_list) == 1:
        for obj in answr_list:
            for k in obj:
                key = k
    

    if key == 'ans_1':
        answer = 1
    elif key == 'ans_2':
        answer = 2
    elif key == 'ans_3':
        answer = 3
    elif key == 'ans_4':
        answer = 4
    elif key == 'ans_5':
        answer = 5
    elif key == 'ans_6':
        answer = 6
    else:
        answer = -1
        print('COULDNT FIND AN ANSWER!!!!')

    return answer

######### VISUAL 3x3 PROBLEM FUNCTIONS #############  
def Visual3x3RowDict(self, image1, image2, image3, row2rowCompsVal):

    row_list=[]

    ##ROW DICTIONARIES
    aff_transforms = VisualRowAffinityTransforms(self, image1, image2, image3)
    otherRow_comps = otherRowComps(self, image1, image2, image3)
    andorxor_comps = VisualAndOrXORComps(self, image1, image2, image3)

    img_1and2_comp = VisualImageComparison(self, image1, image2)
    img_1and2_comp['aff_transforms'] = aff_transforms
    img_1and2_comp['otherRow_comps'] = otherRow_comps
    img_1and2_comp['andorxor_comps'] = andorxor_comps
    img_1and2_comp['row2row_comps'] = dict(
        combinedRow_ImgVal = row2rowCompsVal,
    )


    img_2and3_comp = VisualImageComparison(self, image2, image3)
    img_2and3_comp['aff_transforms'] = aff_transforms
    img_2and3_comp['otherRow_comps'] = otherRow_comps
    img_2and3_comp['andorxor_comps'] = andorxor_comps
    img_2and3_comp['row2row_comps'] = dict(
        combinedRow_ImgVal = row2rowCompsVal,
    )
    

    row_list.append(img_1and2_comp)
    row_list.append(img_2and3_comp)

    return row_list

def Visual3x3RowValuesList(self, row_dict):

    """Puts Values from row_dict into a list for use in KNN."""
    row_list = []
    for item in row_dict:
        values_list = []
        #Basic Image comparison Info
        #values_list.append(item['rms_diff'])

        #Pixel Comparison Info
        values_list.append(item['pixel_comp']['dpr'])
        #values_list.append(item['pixel_comp']['ipr'])
        values_list.append(item['pixel_comp']['dpir'])

        #Affinity Transforms Info
        #values_list.append(item['aff_transforms']['viz_noCHange'])
        #values_list.append(item['aff_transforms']['vizHorzReflect'])
        #values_list.append(item['aff_transforms']['vizVertReflect'])
        values_list.append(item['aff_transforms']['affTransTotScore'])

        #Other Row Comparisons
        #values_list.append(item['otherRow_comps']['horzReflect_13'])
        #values_list.append(item['otherRow_comps']['vertReflect_13'])
        values_list.append(item['otherRow_comps']['tot_otherComps'])

        #andorxor Row Comparisons
        #values_list.append(item['andorxor_comps']['andComp12_3'])
        #values_list.append(item['andorxor_comps']['orComp12_3'])
        #values_list.append(item['andorxor_comps']['xorComp12_3'])
        values_list.append(item['andorxor_comps']['total_score'])

        #Row To Row Comparisons
        #values_list.append(item['row2row_comps']['row12_simil'])
        #values_list.append(item['row2row_comps']['row23_simil'])
        #values_list.append(item['row2row_comps']['combinedRow_ImgsScore'])
        values_list.append(item['row2row_comps']['combinedRow_ImgVal'])


        row_list.append(values_list)


    return row_list

def ImgCompValuesList(self, img_dict):
    """Puts Values from Image Comparison Dict into a list for use in KNN."""
    img_list = []
    #Basic Image comparison Info
    #img_list.append(img_dict['rms_diff'])
    
    #Pixel Comparison Info
    img_list.append(img_dict['pixel_comp']['dpr'])
    #img_list.append(img_dict['pixel_comp']['ipr'])
    img_list.append(img_dict['pixel_comp']['dpir'])

    #Affinity Transformations Info
    img_list.append(img_dict['affinity_transforms']['vis_noChange'])
    #img_list.append(img_dict['affinity_transforms']['vizHorzReflect'])
    #img_list.append(img_dict['affinity_transforms']['vizVertReflect'])
    #img_list.append(img_dict['affinity_transforms']['vizVertReflect'])
    #for item in img_dict['affinity_transforms']['vizRotations']:
    #    img_list.append(item['rotation_score'])


    return img_list


def HorzProbAnalysisVisual3x3(self, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, fig_ans):
    """Caclculates the Average distance of Test Answer away from Existing HORZ Relationships."""
    print('Horizontal Row Comparison!!!!!')
    #Getting rows right for KNN Lists (work better with numbers in a list)

    ##Horizontal Row to Row Relationships##
    row2rowComps = RowToRowComps(self, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, fig_ans)

    #True Relationships
    row1_dict = Visual3x3RowDict(self, fig_a, fig_b, fig_c, row2rowComps['row12_simil'])
    row2_dict = Visual3x3RowDict(self, fig_d, fig_e, fig_f, row2rowComps['row23_simil'])

    #False Relationships
    ####NONE YET####

    print(row1_dict)
    print(row2_dict)

    #Test Answer Case
    test_dict = Visual3x3RowDict(self, fig_g, fig_h, fig_ans, row2rowComps['row23_simil'])
    print('---------TEST DICT--------')
    print(test_dict)
    test_list = Visual3x3RowValuesList(self, test_dict)

    #Training Data and labels set up to include false cases as well... NOW REALLY ONLY CONCERNED ON DISTANCES FROM TWO CORRECT PATTERNS
    labels = ['True','True','True','True']
    training_data = Visual3x3RowValuesList(self, row1_dict) + Visual3x3RowValuesList(self, row2_dict)


    #Calculating K Nearest Neighbors 
    neighbors = nearest_neighbors(training_data, labels, test_list[1], 4, distance=distance_calc)
    print('-----Nearest Neighbors Results-----')
    print(neighbors)

    total_true_dist = 0
    for neighbor in neighbors:
        total_true_dist += neighbor[1]

    return total_true_dist/4

def VertProbAnalysisVisual3x3(self, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, fig_ans):
    """Caclculates the Average distance of Test Answer away from Existing VERT Relationships."""
    print('Vertical Row Comparison!!!!!')
    #Getting rows right for KNN Lists (work better with numbers in a list)
    
    ##Vertical Row to Row Relationships##
    row2rowComps = RowToRowComps(self, fig_a, fig_d, fig_g, fig_b, fig_e, fig_h, fig_c, fig_f, fig_ans)

    #True Relationships
    row1_dict = Visual3x3RowDict(self, fig_a, fig_d, fig_g, row2rowComps['row12_simil'])
    row2_dict = Visual3x3RowDict(self, fig_b, fig_e, fig_h, row2rowComps['row12_simil'])

    #False Relationships
    ####NONE YET####

    print(row1_dict)
    print(row2_dict)
    
    #Test Answer Case
    test_dict = Visual3x3RowDict(self, fig_c, fig_f, fig_ans, row2rowComps['row23_simil'])
    print('---------TEST DICT--------')
    print(test_dict)
    test_list = Visual3x3RowValuesList(self, test_dict)

    #Training Data and labels set up to include false cases as well... NOW REALLY ONLY CONCERNED ON DISTANCES FROM CORRECT PATTERNS
    labels = ['True','True','True','True']
    training_data = Visual3x3RowValuesList(self, row1_dict) + Visual3x3RowValuesList(self, row2_dict)

    #Calculating K Nearest Neighbors 
    neighbors = nearest_neighbors(training_data, labels, test_list[0], 4, distance=distance_calc)
    print('-----Nearest Neighbors Results-----')
    print(neighbors)

    total_true_dist = 0
    for neighbor in neighbors:
        total_true_dist += neighbor[1]


    return total_true_dist/4

def DiagProbAnalysisVisual3x3(self, fig_a, fig_b, fig_f, fig_e, fig_d, fig_h, fig_ans):
    """Calculates the Average distance of Test Answer away from Existing DIAG Relationships."""
    print('Diagonal Row Comparison!!!!!')
    #Getting rows right for KNN Lists (work better with numbers in a list)
    ae_dict = VisualImageComparison(self, fig_a, fig_e)
    bf_dict = VisualImageComparison(self, fig_b, fig_f)
    dh_dict = VisualImageComparison(self, fig_d, fig_h)

    #False Relationships
    ####NONE YET####

    print(ae_dict)
    print(bf_dict)
    print(dh_dict)
    
    #Test Answer Case
    test_dict = VisualImageComparison(self, fig_e, fig_ans)
    print('---------TEST DICT--------')
    print(test_dict)
    test_list = ImgCompValuesList(self, test_dict)

    #Training Data and labels set up to include false cases as well... NOW REALLY ONLY CONCERNED ON DISTANCES FROM CORRECT PATTERNS
    labels = ['True','True','True']
    training_data = []
    training_data.append(ImgCompValuesList(self, ae_dict))
    training_data.append(ImgCompValuesList(self, bf_dict))
    training_data.append(ImgCompValuesList(self, dh_dict))

    #Calculating K Nearest Neighbors 
    neighbors = nearest_neighbors(training_data, labels, test_list, 3, distance=distance_calc)
    print('-----Nearest Neighbors Results-----')
    print(neighbors)

    total_true_dist = 0
    for neighbor in neighbors:
        total_true_dist += neighbor[1]


    return total_true_dist/3

def Visual3x3ProblemAnalysis(self, problem):
    print('Calculating Problem Analysis Dict...')
    ##Problem Set Images###
    fig_a = Image.open(problem.figures['A'].visualFilename).convert('RGB')
    fig_b = Image.open(problem.figures['B'].visualFilename).convert('RGB')
    fig_c = Image.open(problem.figures['C'].visualFilename).convert('RGB')
    fig_d = Image.open(problem.figures['D'].visualFilename).convert('RGB')
    fig_e = Image.open(problem.figures['E'].visualFilename).convert('RGB')
    fig_f = Image.open(problem.figures['F'].visualFilename).convert('RGB')
    fig_g = Image.open(problem.figures['G'].visualFilename).convert('RGB')
    fig_h = Image.open(problem.figures['H'].visualFilename).convert('RGB')

    horz_comp = dict(
        row_1 = Visual3x3RowDict(self, fig_a, fig_b, fig_c),
        row_2 = Visual3x3RowDict(self, fig_d, fig_e, fig_f)
        )

    vert_comp = dict(
        col_1 = Visual3x3RowDict(self, fig_a, fig_d, fig_g),
        col_2 = Visual3x3RowDict(self, fig_b, fig_e, fig_h)
    )

    diag_comp = dict(
        diag = Visual3x3RowDict(self, fig_c, fig_e, fig_g)
    )
    problem_analysis = dict(
        horz_comp=horz_comp,
        vert_comp=vert_comp,
        diag_comp=diag_comp 
    )
    return problem_analysis



def Visual3x3AnswerAnalysisDict(self, fig_name, fig_ans, fig_a, fig_c, fig_e, fig_f, fig_g, fig_h):
    print(fig_name)
    print('Calculating Answer Analysis dict...')
    horz_comp = Visual3x3RowDict(self, fig_g , fig_h, fig_ans)
    vert_comp = Visual3x3RowDict(self, fig_c , fig_f, fig_ans)
    diag_comp = Visual3x3RowDict(self, fig_a , fig_e, fig_ans)

    answer_analysis = dict(
        fig_name=fig_name,
        horz_comp=horz_comp,
        vert_comp=vert_comp,
        diag_comp=diag_comp 
    )

    return answer_analysis

def Visual3x3ProblemAnswersDict(self, problem, problem_analysis_dict):
    fig_a = Image.open(problem.figures['A'].visualFilename).convert('RGB')
    fig_c = Image.open(problem.figures['C'].visualFilename).convert('RGB')
    fig_e = Image.open(problem.figures['E'].visualFilename).convert('RGB')
    fig_f = Image.open(problem.figures['F'].visualFilename).convert('RGB')
    fig_g = Image.open(problem.figures['G'].visualFilename).convert('RGB')
    fig_h = Image.open(problem.figures['H'].visualFilename).convert('RGB')

    i=3
    answer_dict = []
    #while i <= 8:
    answ = 'fig_'+ str(i)
    ans_fig =  Image.open(problem.figures[str(i)].visualFilename).convert('RGB')
    ans_dict = Visual3x3AnswerAnalysisDict(self, answ, ans_fig, fig_a, fig_c, fig_e, fig_f, fig_g, fig_h)
    if Visual3x3ProceduralAnalysis(self, problem_analysis_dict, ans_dict) == True:
        print(answ + ' Was Added to the answer_dict...' )
        answer_dict.append(ans_dict)
    elif Visual3x3ProceduralAnalysis(self, problem_analysis_dict, ans_dict) == False:
        print(answ + ' Failed Proecedural Analysis and is being Skiped....' )
        pass
    else:
        print('There was an error determining if fig should be added to answer_dict...')
    
    #i+=1

    return answer_dict

def Visual3x3ProblemDict(self, problem):
    problem_analysis = Visual3x3ProblemAnalysisDict(self, problem)

    answer_dict = Visual3x3ProblemAnswersDict(self, problem, problem_analysis)

    problem_dict = dict(
        problem_analysis=problem_analysis,
        answers=answer_dict
    )
    return problem_dict

###KNN Formulas
def distance_calc(instance1, instance2):
    """Calculates distance between two Numpy Arrays."""
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)

    return np.linalg.norm(instance1 - instance2)

def nearest_neighbors(training_set, labels, test_instance, k, distance=distance_calc):
    distances = []
    for index in range(len(training_set)):
        dist = distance_calc(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors


######General Procedural Functions######
def ProceduralUnchanged(unchanged_a, unchanged_b):
    if unchanged_a == unchanged_b:
        return True
    elif unchanged_a != unchanged_b:
        return False
    else:
        print('UNKNOWN ERROR PROCEDURAL CALCULATING NO CHANGE!!!!!!!!')

def ProceduralHorzReflect(horz_reflect_a, horz_reflect_b):
    if horz_reflect_a == horz_reflect_b:
        return True
    elif horz_reflect_a != horz_reflect_b:
        return False
    else:
        print('UNKNOWN ERROR PROCEDURAL CALCULATING Horz Reflection!!!!!!!!')

def ProceduralVertReflect(vert_reflect_a, vert_reflect_b):
    if vert_reflect_a == vert_reflect_b:
        return True
    elif vert_reflect_a != vert_reflect_b:
        return False
    else:
        print('UNKNOWN ERROR PROCEDURAL CALCULATING Vert Reflection!!!!!!!!')

def ProceduralFillChange(fill_change_a, fill_change_b):
    if fill_change_a == fill_change_b:
        return True
    elif fill_change_a != fill_change_b:
        return False
    else:
        print('UNKNOWN ERROR PROCEDURAL CALCULATING Fill Change!!!!!!!!')

def ProceduralRotation(rotation_a, rotation_b):
    if rotation_a != [] and rotation_b != []:
        for prob_rot, fig_rot in zip(rotation_a, rotation_b):
            if prob_rot['img_rotation'] == fig_rot['img_rotation']:
                return True
            else:
                return False
    elif rotation_a == [] and rotation_b == []:
        return True
    else:
        print('UNKNOWN ERROR PROCEDURAL CALCULATING Rotation Comparison!!!!!!!!')

##### VISUAL 3x3 Procedural Functions #######
def Visual3x3ImageProceduralComp(image_comp1, image_comp2):
    if ProceduralUnchanged(image_comp1['vis_unchanged'], image_comp2['vis_unchanged']) == True:
        if ProceduralHorzReflect(image_comp1['vis_horz_reflect'], image_comp2['vis_horz_reflect']) == True:
            if ProceduralVertReflect(image_comp1['vis_vert_reflect'], image_comp2['vis_vert_reflect']) == True:
                if ProceduralFillChange(image_comp1['vis_fill_comp']['fill_change'], image_comp2['vis_fill_comp']['fill_change']) == True:
                    return True
                    #if ProceduralRotation(image_comp1['vis_rotation'], image_comp2['vis_rotation']) == True:
                    #    return True
                    #elif ProceduralRotation(image_comp1['vis_rotation'], image_comp2['vis_rotation']) == False:
                    #    return False
                    #else:
                    #    print('Unknown Error while comparing Image Rotation!!')
                elif ProceduralFillChange(image_comp1['vis_fill_comp']['fill_change'], image_comp2['vis_fill_comp']['fill_change']) == False:
                    return False
                else:
                    print('Unknown Error while comparing Image Fill Change!!')
            elif ProceduralVertReflect(image_comp1['vis_vert_reflect'], image_comp2['vis_vert_reflect']) == False:
                return False
            else:
                print('Unknown Error while comparing Image Vert Reflection!!')
        elif ProceduralHorzReflect(image_comp1['vis_horz_reflect'], image_comp2['vis_horz_reflect']) == False:
            return False
        else:
            print('Unknown Error while comparing Image Horz Reflection!!')
    else: #ProceduralUnchanged(image_comp1['vis_unchanged'], image_comp2['vis_unchanged']) == False:
        return False
    #else:
    #    print('Unknown Error while comparing Image No Change!!')    

def Visual3x3ProceduralHorz(self, problem_horz, answer_horz):
    if (
        (Visual3x3ImageProceduralComp(answer_horz['img_1and2_comp'], problem_horz['row_1']['img_1and2_comp']) == True)
        and
        (Visual3x3ImageProceduralComp(answer_horz['img_1and2_comp'], problem_horz['row_2']['img_1and2_comp']) == True)
        ):
        if (
            (Visual3x3ImageProceduralComp(answer_horz['img_2and3_comp'], problem_horz['row_1']['img_2and3_comp']) == True)
            and
            (Visual3x3ImageProceduralComp(answer_horz['img_2and3_comp'], problem_horz['row_2']['img_2and3_comp']) == True)
            ):
            if (
                (Visual3x3ImageProceduralComp(answer_horz['img_1and3_comp'], problem_horz['row_1']['img_1and3_comp']) == True)
                and
                (Visual3x3ImageProceduralComp(answer_horz['img_1and3_comp'], problem_horz['row_2']['img_1and3_comp']) == True)
                ):
                return True
            elif (
                (Visual3x3ImageProceduralComp(answer_horz['img_1and3_comp'], problem_horz['row_1']['img_1and3_comp']) == False)
                and
                (Visual3x3ImageProceduralComp(answer_horz['img_1and3_comp'], problem_horz['row_2']['img_1and3_comp']) == False)
                ):
                return False
            else:
                print('Unknown Failure for Calculating Image 1 & 3 Procedural Comp!!')
        elif (
            (Visual3x3ImageProceduralComp(answer_horz['img_2and3_comp'], problem_horz['row_1']['img_2and3_comp']) == False)
            and
            (Visual3x3ImageProceduralComp(answer_horz['img_2and3_comp'], problem_horz['row_2']['img_2and3_comp']) == False)
            ):
            return False
        else:
            print('Unknown Failure for Calculating Image 2 & 3 Procedural Comp!!')
    elif (
        (Visual3x3ImageProceduralComp(answer_horz['img_1and2_comp'], problem_horz['row_1']['img_1and2_comp']) == False)
        and
        (Visual3x3ImageProceduralComp(answer_horz['img_1and2_comp'], problem_horz['row_2']['img_1and2_comp']) == False)
        ):
        return False
    else:
        print('Unknown Failure for Calculating Image 1 & 2 Procedural Comp!!')

def Visual3x3ProceduralVert(self, problem_vert, answer_vert):
    if (
        (Visual3x3ImageProceduralComp(answer_vert['img_1and2_comp'], problem_vert['col_1']['img_1and2_comp']) == True)
        and
        (Visual3x3ImageProceduralComp(answer_vert['img_1and2_comp'], problem_vert['col_2']['img_1and2_comp']) == True)
        ):
        if (
            (Visual3x3ImageProceduralComp(answer_vert['img_2and3_comp'], problem_vert['col_1']['img_2and3_comp']) == True)
            and
            (Visual3x3ImageProceduralComp(answer_vert['img_2and3_comp'], problem_vert['col_2']['img_2and3_comp']) == True)
            ):
            if (
                (Visual3x3ImageProceduralComp(answer_vert['img_1and3_comp'], problem_vert['col_1']['img_1and3_comp']) == True)
                and
                (Visual3x3ImageProceduralComp(answer_vert['img_1and3_comp'], problem_vert['col_2']['img_1and3_comp']) == True)
                ):
                return True
            elif (
                (Visual3x3ImageProceduralComp(answer_vert['img_1and3_comp'], problem_vert['col_1']['img_1and3_comp']) != True)
                and
                (Visual3x3ImageProceduralComp(answer_vert['img_1and3_comp'], problem_vert['col_2']['img_1and3_comp']) != True)
                ):
                return False
            else:
                print('Unknown Failure for Calculating Image 1 & 3 Procedural Comp!!')
        elif (
            (Visual3x3ImageProceduralComp(answer_vert['img_2and3_comp'], problem_vert['col_1']['img_2and3_comp']) != True)
            and
            (Visual3x3ImageProceduralComp(answer_vert['img_2and3_comp'], problem_vert['col_2']['img_2and3_comp']) != True)
            ):
            return False
        else:
            print('Unknown Failure for Calculating Image 2 & 3 Procedural Comp!!')
    elif (
        (Visual3x3ImageProceduralComp(answer_vert['img_1and2_comp'], problem_vert['col_1']['img_1and2_comp']) != True)
        and
        (Visual3x3ImageProceduralComp(answer_vert['img_1and2_comp'], problem_vert['col_2']['img_1and2_comp']) != True)
        ):
        return False
    else:
        print('Unknown Failure for Calculating Image 1 & 2 Procedural Comp!!')

def Visual3x3ProceduralDiag(self, problem_diag, answer_diag):
    if Visual3x3ImageProceduralComp(answer_diag['img_1and2_comp'], problem_diag['diag']['img_1and2_comp']) == True:
        if Visual3x3ImageProceduralComp(answer_diag['img_2and3_comp'], problem_diag['diag']['img_2and3_comp']) == True:
            if Visual3x3ImageProceduralComp(answer_diag['img_1and3_comp'], problem_diag['diag']['img_1and3_comp']) == True:
                return True
            elif Visual3x3ImageProceduralComp(answer_diag['img_1and3_comp'], problem_diag['diag']['img_1and3_comp']) != True:
                return False
            else:
                print('Unknown Failure for Calculating Image 1 & 3 Procedural Comp!!')
        elif Visual3x3ImageProceduralComp(answer_diag['img_2and3_comp'], problem_diag['diag']['img_2and3_comp']) != True:
            return False
        else:
            print('Unknown Failure for Calculating Image 2 & 3 Procedural Comp!!')
    elif Visual3x3ImageProceduralComp(answer_diag['img_1and2_comp'], problem_diag['diag']['img_1and2_comp']) != True:
        return False
    else:
        print('Unknown Failure for Calculating Image 1 & 2 Procedural Comp!!')

def Visual3x3ProceduralAnalysis(self, problem_dict, answer_dict):
    print('Calulating Answer Figures Procedural Analysis')
    if Visual3x3ProceduralHorz(self, problem_dict['horz_comp'], answer_dict['horz_comp']) == True:
        if Visual3x3ProceduralVert(self, problem_dict['vert_comp'], answer_dict['vert_comp']) == True:
            if Visual3x3ProceduralDiag(self, problem_dict['diag_comp'], answer_dict['diag_comp']) == True:
                return True
            elif Visual3x3ProceduralDiag(self, problem_dict['diag_comp'], answer_dict['diag_comp']) == False:
                return False
            else:
                print('UNKNOWN ERROR CALCULATING DIAG PROCEDURAL COMP!!!!')
        elif Visual3x3ProceduralVert(self, problem_dict['vert_comp'], answer_dict['vert_comp']) == False:
            return False
        else:
            print('UNKNOWN ERROR CALCULATING VERT PROCEDURAL COMP!!!!')
    elif Visual3x3ProceduralHorz(self, problem_dict['horz_comp'], answer_dict['horz_comp']) == False:
        return False
    else:
        print('UNKNOWN ERROR CALCULATING HORZ PROCEDURAL COMP!!!!')


#####General Functions######
def verbal2x2dicts(self, problem):
    figureAdict  =  []
    for obj in problem.figures["A"].objects:
        for letter in obj:
            figureAdict.append(problem.figures["A"].objects[letter].attributes)

    figureBdict  =  []
    for obj in problem.figures["B"].objects:
        for letter in obj:
            figureBdict.append(problem.figures["B"].objects[letter].attributes)

    figureCdict  =  []
    for obj in problem.figures["C"].objects:
        for letter in obj:
            figureCdict.append(problem.figures["C"].objects[letter].attributes)

    figure1dict  =  []
    for obj in problem.figures["1"].objects:
        for letter in obj:
            figure1dict.append(problem.figures["1"].objects[letter].attributes)
    
    figure2dict  =  []
    for obj in problem.figures["2"].objects:
        for letter in obj:
            figure2dict.append(problem.figures["2"].objects[letter].attributes)
    
    figure3dict  =  []
    for obj in problem.figures["3"].objects:
        for letter in obj:
            figure3dict.append(problem.figures["3"].objects[letter].attributes)
    
    figure4dict  =  []
    for obj in problem.figures["4"].objects:
        for letter in obj:
            figure4dict.append(problem.figures["4"].objects[letter].attributes)
    
    figure5dict  =  []
    for obj in problem.figures["5"].objects:
        for letter in obj:
            figure5dict.append(problem.figures["5"].objects[letter].attributes)

    figure6dict  =  []
    for obj in problem.figures["6"].objects:
        for letter in obj:
            figure6dict.append(problem.figures["6"].objects[letter].attributes)
    
    problem_dict = dict(
        figA=figureAdict, 
        figB=figureBdict,
        figC=figureCdict, 
        fig1=figure1dict,
        fig2=figure2dict,
        fig3=figure3dict,
        fig4=figure4dict,
        fig5=figure5dict,
        fig6=figure6dict
    )

    return problem_dict

