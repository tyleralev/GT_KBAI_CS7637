import numpy as np
from collections import Counter

class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        # Add your code here!
        #
        # The first parameter to this method is a list of diseases, represented as a
        # list of 2-tuples. The first item in each 2-tuple is the name of a disease. The
        # second item in each 2-tuple is a dictionary of symptoms of that disease, where
        # the keys are letters representing vitamin names ("A" through "Z") and the values
        # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
        #
        # The second parameter to this method is a particular patient's symptoms, again
        # represented as a dictionary where the keys are letters and the values are
        # "+", "-", or "0".
        #
        # This method should return a list of names of diseases that together explain the
        # observed symptoms. If multiple lists of diseases can explain the symptoms, you
        # should return the smallest list. If multiple smallest lists are possible, you
        # may return any sufficiently explanatory list.
        labels = []
        training_data = []
        for disease in diseases:
            labels.append(disease[0])
            training_data.append(disease_tests_list(disease[1]))

        neighbors = nearest_neighbors(training_data,labels,disease_tests_list(patient),5, distance=distance_calc)

        disease_probs = vote_distance_weights(neighbors, all_results=True)
        print(disease_probs)
        diagnosis = []
        ruled_out_diseases = []
        for prob in disease_probs[1]:
            if prob[1] > .2:
                diagnosis.append(prob[0])
            elif prob[1] <= .2:
                ruled_out_diseases.append(prob)


        return diagnosis


### Helper Functions ####
def disease_tests_list(disease_dict):
    """Converting disease dictionaries in numpy lists for easier KNN."""
    disease_list = []
    for attr in disease_dict:
        if disease_dict[attr] == "0":
            disease_list.append(0)
        elif disease_dict[attr] == "+":
            disease_list.append(1)
        elif disease_dict[attr] == "-":
            disease_list.append(-1)
        else:
            print("UNKOWN Test Result!!!")
            disease_list.append(None)
    return disease_list

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

def vote_distance_weights(neighbors, all_results=True):
    class_counter = Counter()
    number_of_neighbors = len(neighbors)
    for index in range(number_of_neighbors):
        dist = neighbors[index][1]
        label = neighbors[index][2]
        class_counter[label] += 1 / (dist**2 + 1)
    labels, votes = zip(*class_counter.most_common())
    
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
             class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, votes4winner / sum(votes)
