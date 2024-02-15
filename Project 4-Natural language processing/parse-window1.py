import xml.etree.ElementTree as ET
import numpy as np
import conllu
from sklearn import svm, neighbors
from sklearn import tree as decisionTree
from sklearn.model_selection import KFold, cross_val_score
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
#--------------------------------------------------------------------------------------------------------------------------------------
# The bible text
#--------------------------------------------------------------------------------------------------------------------------------------
# Add the relevant ana information to the vector
def addAna(vectors, ana, i):
    if (ana.find("BASEFORM_BINYAN_PAAL") != -1):
        vectors[i][30] += 1
    if (ana.find("BASEFORM_BINYAN_NIFAL") != -1):
        vectors[i][31] += 1
    if (ana.find("BASEFORM_BINYAN_HIFIL") != -1):
        vectors[i][32] += 1
    if (ana.find("BASEFORM_BINYAN_HUFAL") != -1):
        vectors[i][33] += 1
    if (ana.find("BASEFORM_BINYAN_PIEL") != -1):
        vectors[i][34] += 1
    if (ana.find("BASEFORM_BINYAN_PUAL") != -1):
        vectors[i][35] += 1
    if (ana.find("BASEFORM_BINYAN_HITPAEL") != -1):
        vectors[i][36] += 1
    if (ana.find("BASEFORM_GENDER_MASCULINE") != -1):
        vectors[i][37] += 1
    if (ana.find("BASEFORM_GENDER_FEMININE") != -1):
        vectors[i][38] += 1
    if (ana.find("BASEFORM_NUMBER_PLURAL") != -1):
        vectors[i][39] += 1
    if (ana.find("BASEFORM_NUMBER_SINGULAR") != -1):
        vectors[i][40] += 1
    if (ana.find("BASEFORM_NUMBER_DUAL") != -1):
        vectors[i][41] += 1
    if (ana.find("BASEFORM_PERSON_1") != -1):
        vectors[i][42] += 1
    if (ana.find("BASEFORM_PERSON_2") != -1):
        vectors[i][43] += 1
    if (ana.find("BASEFORM_PERSON_3") != -1):
        vectors[i][44] += 1
    if (ana.find("BASEFORM_PERSON_ANY") != -1):
        vectors[i][45] += 1
    if (ana.find("BASEFORM_POS_VERB") != -1):
        vectors[i][46] += 1
    if (ana.find("BASEFORM_POS_NOUN") != -1):
        vectors[i][47] += 1
    if (ana.find("BASEFORM_POS_ADJECTIVE") != -1):
        vectors[i][48] += 1
    if (ana.find("BASEFORM_POS_NEGATION") != -1):
        vectors[i][49] += 1
    if (ana.find("BASEFORM_POS_ADVERB") != -1):
        vectors[i][50] += 1
    if (ana.find("BASEFORM_POS_CONJUNCTION") != -1):
        vectors[i][51] += 1
    if (ana.find("BASEFORM_POS_INTERJECTION") != -1):
        vectors[i][52] += 1
    if (ana.find("BASEFORM_POS_INTERROGATIVE") != -1):
        vectors[i][53] += 1
    if (ana.find("BASEFORM_POS_PREPOSITION") != -1):
        vectors[i][54] += 1
    if (ana.find("BASEFORM_POS_PROPERNAME") != -1):
        vectors[i][55] += 1
    if (ana.find("BASEFORM_POS_PRONOUN") != -1):
        vectors[i][56] += 1
    if (ana.find("BASEFORM_POS_PARTICIPLE") != -1):
        vectors[i][57] += 1
    if (ana.find("BASEFORM_STATUS_ABSOLUTE") != -1):
        vectors[i][58] += 1
    if (ana.find("BASEFORM_STATUS_CONSTRUCT") != -1):
        vectors[i][59] += 1
    if (ana.find("BASEFORM_TENSE_PAST") != -1):
        vectors[i][60] += 1
    if (ana.find("BASEFORM_TENSE_FUTURE") != -1):
        vectors[i][61] += 1
    if (ana.find("BASEFORM_TENSE_TOINFINITIVE") != -1):
        vectors[i][62] += 1
    if (ana.find("BASEFORM_TENSE_IMPERATIVE") != -1):
        vectors[i][63] += 1
    if (ana.find("BASEFORM_TENSE_BAREINFINITIVE") != -1):
        vectors[i][64] += 1
    if (ana.find("PREFIX_FUNCTION_CONJUNCTION") != -1):
        vectors[i][65] += 1
    if (ana.find("PREFIX_FUNCTION_DEFINITEARTICLE") != -1):
        vectors[i][66] += 1
    if (ana.find("PREFIX_FUNCTION_INTERROGATIVE") != -1):
        vectors[i][67] += 1
    if (ana.find("PREFIX_FUNCTION_PREPOSITION") != -1):
        vectors[i][68] += 1
    if (ana.find("SUFFIX_FUNCTION_ACCUSATIVENOMINATIVE") != -1):
        vectors[i][69] += 1
    if (ana.find("SUFFIX_FUNCTION_POSSESIVEPRONOUN") != -1):
        vectors[i][70] += 1
    if (ana.find("SUFFIX_GENDER_MASCULINE") != -1):
        vectors[i][71] += 1
    if (ana.find("SUFFIX_GENDER_FEMININE") != -1):
        vectors[i][72] += 1
    if (ana.find("SUFFIX_NOMINAL_ENDING") != -1):
        vectors[i][73] += 1
    if (ana.find("SUFFIX_NUMBER_PLURAL") != -1):
        vectors[i][74] += 1
    if (ana.find("SUFFIX_NUMBER_SINGULAR") != -1):
        vectors[i][75] += 1
    if (ana.find("SUFFIX_PERSON_2") != -1):
        vectors[i][76] += 1
    if (ana.find("SUFFIX_PERSON_3") != -1):
        vectors[i][77] += 1
    return vectors

# Add the syntactic function to the vector
def addFunction(vectors, function, i):
    if (function == "Adju"):
        vectors[i][0] += 1
    elif (function == "Cmpl"):
        vectors[i][1] += 1
    elif (function == "Conj"):
        vectors[i][2] += 1
    elif (function == "Eppr"):
        vectors[i][3] += 1
    elif (function == "ExsS"):
        vectors[i][4] += 1
    elif (function == "Exst"):
        vectors[i][5] += 1
    elif (function == "Frnt"):
        vectors[i][6] += 1
    elif (function == "Intj"):
        vectors[i][7] += 1
    elif (function == "IntS"):
        vectors[i][8] += 1
    elif (function == "Loca"):
        vectors[i][9] += 1
    elif (function == "Modi"):
        vectors[i][10] += 1
    elif (function == "ModS"):
        vectors[i][11] += 1
    elif (function == "NCop"):
        vectors[i][12] += 1
    elif (function == "NCoS"):
        vectors[i][13] += 1
    elif (function == "Nega"):
        vectors[i][14] += 1
    elif (function == "Objc"):
        vectors[i][15] += 1
    elif (function == "PrAd"):
        vectors[i][16] += 1
    elif (function == "PrcS"):
        vectors[i][17] += 1
    elif (function == "PreC"):
        vectors[i][18] += 1
    elif (function == "Pred"):
        vectors[i][19] += 1
    elif (function == "PreO"):
        vectors[i][20] += 1
    elif (function == "PreS"):
        vectors[i][21] += 1
    elif (function == "PtcO"):
        vectors[i][22] += 1
    elif (function == "Ques"):
        vectors[i][23] += 1
    elif (function == "Rela"):
        vectors[i][24] += 1
    elif (function == "Subj"):
        vectors[i][25] += 1
    elif (function == "Supp"):
        vectors[i][26] += 1
    elif (function == "Time"):
        vectors[i][27] += 1
    elif (function == "Unkn"):
        vectors[i][28] += 1
    else:
        vectors[i][29] += 1
    return vectors

# Parses most of the tree (except for the syntacticInfo for some reason) to the root object
tree = ET.parse('text.xml')
root = tree.getroot()

# Count the number of psukim
count = 0
for pasuk in root.iter('s'):
    count += 1
glinertLabels = np.zeros(count)
blauLabels = np.zeros(count)
bibleVectors = np.zeros((count, 78))

# Create a dictionary of the word ids to their syntactic function by converting the xml file to a string (since it's not working in ET)
idDict = {}
path = r".\text.xml"
bibleData = open(path, 'r',encoding='utf-8').read()
while (bibleData.find("function=") != -1):
    index = bibleData.find("function=")
    function = bibleData[index+10:index+14]
    bibleData = bibleData[index+19:]
    index = bibleData.find(" ")
    if (bibleData[1:index-1] != id):
        id = bibleData[1:index-1]
    idDict[id] = function

i = 0
for pasuk in root.iter('s'):
    glinert = int(pasuk.attrib['glinert'])
    blau = int(pasuk.attrib['blau'])
    glinertLabels[i] = glinert
    blauLabels[i] = blau
    hitpaelIndex = 0
    index = -1
    id = ""
    for word in pasuk.iter('w'):
        for m in word.iter('m'):
            # Find the index of the verb with binyan hitpael
            if (m.attrib['ana'].find("BASEFORM_BINYAN_HITPAEL") != -1):
                hitpaelIndex = index+1
        index += 1
    # Adds the relevant vector information for the word before and after the verb with binyan hitpael
    if (root[i][hitpaelIndex-1].text != None):
        # Goes over all the parts of the word-the m tag
        for j in range(len(root[i][hitpaelIndex-1])):
            ana = root[i][hitpaelIndex-1][j].attrib['ana']
            bibleVectors = addAna(bibleVectors, ana, i)
            # Adds the information only once per each id
            if "phraseId" in root[i][hitpaelIndex-1][j].attrib and root[i][hitpaelIndex-1][j].attrib['phraseId'] != id:
                id = root[i][hitpaelIndex-1][j].attrib['phraseId']
                bibleVectors = addFunction(bibleVectors, idDict[id], i)
    if (root[i][hitpaelIndex+1].text != None):
        for j in range(len(root[i][hitpaelIndex+1])):
            ana = root[i][hitpaelIndex+1][j].attrib['ana']
            bibleVectors = addAna(bibleVectors, ana, i)
            if "phraseId" in root[i][hitpaelIndex+1][j].attrib and root[i][hitpaelIndex+1][j].attrib['phraseId'] != id:
                id = root[i][hitpaelIndex+1][j].attrib['phraseId']
                bibleVectors = addFunction(bibleVectors, idDict[id], i)
    i += 1

#--------------------------------------------------------------------------------------------------------------------------------------
# The modern text
#--------------------------------------------------------------------------------------------------------------------------------------

data = open("modern_hebrew.conllu.txt", mode="r", encoding="utf-8")
annotated = data.read()
sentences = conllu.parse(annotated)
upos_set = set()
xpos_set = set()
feats = set()

# Iterate over sentences
for sentence in sentences:
    # Iterate over tokens in each sentence
    for token in sentence:
        # Get upos, xpos, and feats for each token
        upos = token['upos']
        xpos = token['xpos']
        feat_dict = token['feats']

        # Add upos and xpos to their respective sets
        upos_set.add(upos)
        xpos_set.add(xpos)

        # Add feats to the set
        if feat_dict:
            for feat, value in feat_dict.items():
                feats.add((feat, value))

feats = set()

# Iterate over sentences
for sentence in sentences:
    # Iterate over tokens in each sentence
    for token in sentence:
        # Get feats for each token
        feat_dict = token['feats']

        # Add feats to the set
        if feat_dict:
            for feat, value in feat_dict.items():
                feats.add((feat, value))

# Sort feats in ascending order based on the feat key
sorted_feats = sorted(feats, key=lambda x: x[0])

filtered_sentences = []

# Iterate over sentences
for sentence in sentences:
    has_hitpael = False

    # Iterate over tokens in each sentence
    for token in sentence:
        # Get feats for each token
        feat_dict = token['feats']

        # Check if 'HebBinyan' feature exists and has the value 'HITPAEL'
        if feat_dict and 'HebBinyan' in feat_dict and feat_dict['HebBinyan'] == 'HITPAEL':
            has_hitpael = True
            break

    # Add sentence to filtered_sentences only if it has 'HebBinyan' as 'HITPAEL'
    if has_hitpael:
        filtered_sentences.append(sentence)

# Define a map for upos and their corresponding indices in the vector
upos_map = {
    'DET': 66,
    'ADV': 10,
    'X': 28,
    'INTJ': 7,
    'NOUN': 47,
    'AUX': 19,
    'SCONJ': 2,
    'CCONJ': 2,
    'ADJ': 48,
    'PRON': 56,
    'PROPN': 59,
    'VERB': 46,
    'ADP': 68,
    'NUM': 58,
}

# Define a map for xpos and their corresponding indices in the vector
xpos_map = {
    'DET': 66,
    'ADV': 10,
    'X': 28,
    'INTJ': 7,
    'NOUN': 47,
    'AUX': 19,
    'SCONJ': 2,
    'CCONJ': 2,
    'ADJ': 48,
    'PROPN': 59,
    'PRON': 56,
    'VERB': 46,
    'ADP': 68,
    'NUM': 58,
}

# Define a map for feats and their corresponding indices in the vector
feats_map = {
    'Aspect=Prog': 62,
    'Case=Gen': 70,
    'Case=Acc': 68,
    'Definite=Def': 66,
    'Definite=Cons': 59,
    'Foreign=Yes': 28,
    'Gender=Masc': 37,
    'Gender=Fem,Masc': 38,
    'Gender=Fem': 38,
    'HebBinyan=HUFAL': 33,
    'HebBinyan=PUAL': 35,
    'HebBinyan=HITPAEL': 36,
    'HebBinyan=NITPAEL': 36,
    'HebBinyan=PIEL': 34,
    'HebBinyan=PAAL': 30,
    'HebBinyan=NIFAL': 31,
    'HebBinyan=HIFIL': 32,
    'Mood=Imp': 63,
    'NumType=Ord': 1,
    'NumType=Card': 18,
    'Number=Plur,Sing': 39,
    'Number=Sing': 40,
    'Number=Dual': 41,
    'Number=Plur': 39,
    'Person=3': 44,
    'Person=1': 42,
    'Person=2': 43,
    'Polarity=Pos': 5,
    'Polarity=Neg': 14,  # If UPOS is ADV then 14, else-49
    'Prefix=Yes': 59,
    'Tense=Pres': 64,
    'Tense=Fut': 61,
    'Tense=Past': 60,
    'VerbForm=Inf': 62,
}

# Initialize an empty list to store the vectors
modernVectors = []
y_vector = []
# Iterate over sentences
for sentence in filtered_sentences:
    y_vector.append(int(sentence.metadata['y_vector']))
    has_hitpael = False  # Flag to check if 'HebBinyan=HITPAEL' is present in the sentence

    # Iterate over tokens in the sentence
    for i, token in enumerate(sentence):
        feat_dict = token.get('feats')
        if feat_dict and 'HebBinyan' in feat_dict and feat_dict['HebBinyan'] == 'HITPAEL':
            has_hitpael = True
            break  # If 'HebBinyan=HITPAEL' found, no need to check further

    if has_hitpael:
        # Initialize a vector of zeros with a length of 71 (including the center word 'HebBinyan=HITPAEL')
        vector = np.zeros(78)

        # Get the index of the HITPAEL token in the sentence
        hitpael_index = i

        # Define a helper function to check if the token at the given index contains a specific feature

        def contains_feature(index, feature_type, feature_map):
          if 0 <= index < len(sentence):
              token = sentence[index]
              feat_value = token.get(feature_type)
              if feat_value:
                  # Check if feat_value is a dictionary or a string
                  if isinstance(feat_value, dict):
                      for feat_key, feat_val in feat_value.items():
                          if feat_key + '=' + feat_val in feature_map:
                              return True
                  elif isinstance(feat_value, str):
                      # Split the string into separate features
                      feat_list = feat_value.split('|')  # Assuming features are separated by '|'
                      for feat in feat_list:
                          if feat in feature_map:
                              return True
          return False


        # Print the token before the HITPAEL verb
        if hitpael_index > 0:
            token_before = sentence[hitpael_index - 1]
            upos_before = token_before.get('upos')
            xpos_before = token_before.get('xpos')
            feats_before = token_before.get('feats')

        # Print the token after the HITPAEL verb
        if hitpael_index < len(sentence) - 1:
            token_after = sentence[hitpael_index + 1]
            upos_after = token_after.get('upos')
            xpos_after = token_after.get('xpos')
            feats_after = token_after.get('feats')

        # Check if the tokens before HITPAEL contains each possible upos, xpos, and feats
        if contains_feature(hitpael_index - 1, 'upos', upos_map):
            feature_value = sentence[hitpael_index - 1]['upos']
            vector[upos_map[feature_value]] += 1

        if contains_feature(hitpael_index - 1, 'xpos', xpos_map):
            feature_value = sentence[hitpael_index - 1]['xpos']
            vector[xpos_map[feature_value]] += 1

        if contains_feature(hitpael_index - 1, 'feats', feats_map):
            for feat in sentence[hitpael_index - 1]['feats']:
                if feat in feats_map:
                    feature_value = feat
                    vector[feats_map[feature_value]] += 1

        # Check if the tokens after HITPAEL contains each possible upos, xpos, and feats
        if contains_feature(hitpael_index + 1, 'upos', upos_map):
            feature_value = sentence[hitpael_index + 1]['upos']
            vector[upos_map[feature_value]] += 1

        if contains_feature(hitpael_index + 1, 'xpos', xpos_map):
            feature_value = sentence[hitpael_index + 1]['xpos']
            vector[xpos_map[feature_value]] += 1

        if contains_feature(hitpael_index + 1, 'feats', feats_map):
            for feat in sentence[hitpael_index + 1]['feats']:
                if feat in feats_map:
                    feature_value = feat
                    vector[feats_map[feature_value]] += 1

        # Mark the center word 'HebBinyan=HITPAEL'
        vector[feats_map['HebBinyan=HITPAEL']] += 1
        # Append the vector to the list of vectors
        modernVectors.append(vector)

# Convert the list of vectors to a numpy array
modernVectors = np.array(modernVectors)
modernLabels = np.array(y_vector)

kernels = ['linear', 'poly', 'rbf', 'sigmoid']
neighborNums = [5,7,9]
criteria = ['gini', 'entropy']

# Split the data into training and testing sets
totalVectors = np.concatenate((bibleVectors, modernVectors), axis=0)
totalLabels = np.concatenate((glinertLabels, modernLabels), axis=0)
def calculateCrossValidation(kernels, neighborNums, criteria, bibleVectors, glinertLabels, modernVectors,
                             modernLabels, totalVectors, totalLabels):
    print("\nBible:\n")
    for kernel in kernels:
        clf = svm.SVC(kernel=kernel, decision_function_shape='ovo')
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, bibleVectors, glinertLabels, cv = k_folds)
        print(f"SVM with {kernel} kernel F score: {scores.mean():.2f}")
    for neighbor in neighborNums:
        clf = neighbors.KNeighborsClassifier(n_neighbors=neighbor)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, bibleVectors, glinertLabels, cv = k_folds)
        print(f"{neighbor}-nearest neighbors F score: {scores.mean():.2f}")
    for criterion in criteria:
        clf = decisionTree.DecisionTreeClassifier(criterion=criterion)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, bibleVectors, glinertLabels, cv = k_folds)
        print(f"Decision tree with criterion {criterion} F score: {scores.mean():.2f}")
    print("\nModern Hebrew:\n")
    for kernel in kernels:
        clf = svm.SVC(kernel=kernel, decision_function_shape='ovo')
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, modernVectors, modernLabels, cv = k_folds)
        print(f"SVM with {kernel} kernel F score: {scores.mean():.2f}")
    for neighbor in neighborNums:
        clf = neighbors.KNeighborsClassifier(n_neighbors=neighbor)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, modernVectors, modernLabels, cv = k_folds)
        print(f"{neighbor}-nearest neighbors F score: {scores.mean():.2f}")
    for criterion in criteria:
        clf = decisionTree.DecisionTreeClassifier(criterion=criterion)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, modernVectors, modernLabels, cv = k_folds)
        print(f"Decision tree with criterion {criterion} F score: {scores.mean():.2f}")
    print("\nTotal:\n")
    for kernel in kernels:
        clf = svm.SVC(kernel=kernel, decision_function_shape='ovo')
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, totalVectors, totalLabels, cv = k_folds)
        print(f"SVM with {kernel} kernel F score: {scores.mean():.2f}")
    for neighbor in neighborNums:
        clf = neighbors.KNeighborsClassifier(n_neighbors=neighbor)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, totalVectors, totalLabels, cv = k_folds)
        print(f"{neighbor}-nearest neighbors F score: {scores.mean():.2f}")
    for criterion in criteria:
        clf = decisionTree.DecisionTreeClassifier(criterion=criterion)
        k_folds = KFold(n_splits=10)
        scores = cross_val_score(clf, totalVectors, totalLabels, cv = k_folds)
        print(f"Decision tree with criterion {criterion} F score: {scores.mean():.2f}")
print("Morphology and syntax:")
calculateCrossValidation(kernels, neighborNums, criteria, bibleVectors, glinertLabels, modernVectors,
                             modernLabels, totalVectors, totalLabels)
print("--------------------------------------------------------------")
print("Morphology only:")
calculateCrossValidation(kernels, neighborNums, criteria, bibleVectors[:,30:], glinertLabels, modernVectors[:,30:],
                             modernLabels, totalVectors[:,30:], totalLabels)
print("--------------------------------------------------------------")
print("Syntax only:")
calculateCrossValidation(kernels, neighborNums, criteria, bibleVectors[:,:30], glinertLabels, modernVectors[:,:30],
                             modernLabels, totalVectors[:,:30], totalLabels)