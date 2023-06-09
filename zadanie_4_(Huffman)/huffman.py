import copy
import re


# Node object definition: it stores pointers to its right & left children nodes - None by default
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

# TODO: Adding function for iterating thru NodeTree and making it into the list with None's would enable
# to visualizing this code with binarytree library (see branch "Kodowanie_Huffmana_Na_Brudno")

# Data cleaning funcitons
def clean_text(crude):
    return re.sub(r'[\W_]', '', crude)

def check_if_exists_in_dict(char, dict):
    for obj in dict:
        if obj == char:
            return True
    return False

# Function to check if the given list represents min-heap or not
def checkMinHeap(A, i):
 
    # if `i` is a leaf node, return true as every leaf node is a heap
    if 2*i + 2 > len(A):
        return True
 
    # if `i` is an internal node
 
    # recursively check if the left child is a heap
    left = (A[i] <= A[2*i + 1]) and checkMinHeap(A, 2*i + 1)
 
    # recursively check if the right child is a heap (to avoid the list index out
    # of bounds, first check if the right child exists or not)
    right = (2*i + 2 == len(A)) or (A[i] <= A[2*i + 2]
                                    and checkMinHeap(A, 2*i + 2))
 
    # return true if both left and right child are heaps
    return left and right

# Main function implementing huffman coding
def huffman_encoding(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_encoding(l, True, binString + '0'))
    d.update(huffman_encoding(r, False, binString + '1'))
    return d

# Text snippets
text = input("Enter text for encoding:")
text = ("The most merciful thing in the world, I think, is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, each straining in its own direction, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age.")
# Longer text snippet
# text = ("The most merciful thing in the wold, I think, is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, each straining in its own direction, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age. Theosophists have guessed at the awesome grandeur of the cosmic cycle wherein our world and human race form transient incidents. They have hinted at strange survivals in terms which would freeze the blood if not masked by a bland optimism. But it is not from them that there came the single glimpse of forbidden aeons which chills me when I think of it and maddens me when I dream of it. That glimpse, like all dread glimpses of truth, flashed out from an accidental piecing together of separated things—in this case an old newspaper item and the notes of a dead professor. I hope that no one else will accomplish this piecing out; certainly, if I live, I shall never knowingly supply a link in so hideous a chain. I think that the professor, too, intended to keep silent regarding the part he knew, and that he would have destroyed his notes had not sudden death seized him. My knowledge of the thing began in the winter of 1926–27 with the death of my grand-uncle George Gammell Angell, Professor Emeritus of Semitic Languages in Brown University, Providence, Rhode Island. Professor Angell was widely known as an authority on ancient inscriptions, and had frequently been resorted to by the heads of prominent museums; so that his passing at the age of ninety-two may be recalled by many. Locally, interest was intensified by the obscurity of the cause of death. The professor had been stricken whilst returning from the Newport boat; falling suddenly, as witnesses said, after having been jostled by a nautical-looking negro who had come from one of the queer dark courts on the precipitous hillside which formed a short cut from the waterfront to the deceased’s home in Williams Street. Physicians were unable to find any visible disorder, but concluded after perplexed debate that some obscure lesion of the heart, induced by the brisk ascent of so steep a hill by so elderly a man, was responsible for the end. At the time I saw no reason to dissent from this dictum, but latterly I am inclined to wonder—and more than wonder. As my grand-uncle’s heir and executor, for he died a childless widower, I was expected to go over his papers with some thoroughness; and for that purpose moved his entire set of files and boxes to my quarters in Boston. Much of the material which I correlated will be later published by the American Archaeological Society, but there was one box which I found exceedingly puzzling, and which I felt much averse from shewing to other eyes. It had been locked, and I did not find the key till it occurred to me to examine the personal ring which the professor carried always in his pocket. Then indeed I succeeded in opening it, but when I did so seemed only to be confronted by a greater and more closely locked barrier. For what could be the meaning of the queer clay bas-relief and the disjointed jottings, ramblings, and cuttings which I found? Had my uncle, in his latter years, become credulous of the most superficial impostures? I resolved to search out the eccentric sculptor responsible for this apparent disturbance of an old mans peace of mind.")
# Text trivial
# text = 'BCAADDDCCACACAC'

# Text cleaning
text_cleaned = clean_text(text)
print("Text (crude): "+ text)

print("Text (formatted): "+ text_cleaned)

# Python dictionary structure is used, where key is a unique char and value is the number of occurences; dict is predefined as empty
signs = dict()

# Analyze text & populate the dict
for char in text_cleaned:
    if check_if_exists_in_dict(char, signs):
        signs.update({char: signs[char]+1})
    else:
        signs.update({char: 1})

        
sorted_signs = {k: v for k, v in sorted(signs.items(), key=lambda item: item[1])}
sorted_signs_list = list(sorted_signs.values())
print("Ordered dictionary: "+str(sorted_signs))
# Verification of the min heap
if checkMinHeap(sorted_signs_list, 0):
    print("[OK] The list above represent proper min heap!")
else:
    print("[ERROR] The list above is NOT a proper min heap!")
    exit

sorted_signs_list_of_tuples = sorted(signs.items(), key=lambda x: x[1], reverse=True)

nodes = sorted(signs.items(), key=lambda x: x[1], reverse=True)

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_encoding(nodes[0][0])

print('\n Char | Huffman code ')
print('----------------------')
for (char, frequency) in sorted_signs_list_of_tuples:
    print(' %-4r |%12s' % (char, huffmanCode[char]))