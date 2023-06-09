import copy
import re
from binarytree import build, build2, Node


# HuffPair definition: it is similar to dictionary item, but can be used in logical operations like int (per value)
# which is important for sorting the list; for printing it can be parsed as a string in a readable form.
class HuffPair():
    def __init__(self, key, value) -> None:
        self._key = key
        self._value = value

    def __lt__(self, other):
        return self._value < other
    
    def __eq__(self, other):
        return self._value == other
    
    def __gt__(self, other):
        return self._value > other
    
    def __str__(self):
        return self._key+":"+str(self._value)

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

# Function for quick drawing of the (sub)tree, that is tree consisting of both int's and HuffPairs
def regenerate_visual_tree(sub_tree):
    visual_tree = []
    for i in sub_tree:
        visual_tree.append(str(i))

    print(visual_tree)
    print(build2(visual_tree))

def regenerate_list_only(sub_tree):
    visual_tree = []
    for i in sub_tree:
        visual_tree.append(str(i))

    print(visual_tree)

# Text snippets
# text = input("Enter text for encoding:")
# text = ("The most merciful thing in the world, I think, is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, each straining in its own direction, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age.")
# Longer text snippet
# text = ("The most merciful thing in the wold, I think, is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, each straining in its own direction, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age. Theosophists have guessed at the awesome grandeur of the cosmic cycle wherein our world and human race form transient incidents. They have hinted at strange survivals in terms which would freeze the blood if not masked by a bland optimism. But it is not from them that there came the single glimpse of forbidden aeons which chills me when I think of it and maddens me when I dream of it. That glimpse, like all dread glimpses of truth, flashed out from an accidental piecing together of separated things—in this case an old newspaper item and the notes of a dead professor. I hope that no one else will accomplish this piecing out; certainly, if I live, I shall never knowingly supply a link in so hideous a chain. I think that the professor, too, intended to keep silent regarding the part he knew, and that he would have destroyed his notes had not sudden death seized him. My knowledge of the thing began in the winter of 1926–27 with the death of my grand-uncle George Gammell Angell, Professor Emeritus of Semitic Languages in Brown University, Providence, Rhode Island. Professor Angell was widely known as an authority on ancient inscriptions, and had frequently been resorted to by the heads of prominent museums; so that his passing at the age of ninety-two may be recalled by many. Locally, interest was intensified by the obscurity of the cause of death. The professor had been stricken whilst returning from the Newport boat; falling suddenly, as witnesses said, after having been jostled by a nautical-looking negro who had come from one of the queer dark courts on the precipitous hillside which formed a short cut from the waterfront to the deceased’s home in Williams Street. Physicians were unable to find any visible disorder, but concluded after perplexed debate that some obscure lesion of the heart, induced by the brisk ascent of so steep a hill by so elderly a man, was responsible for the end. At the time I saw no reason to dissent from this dictum, but latterly I am inclined to wonder—and more than wonder. As my grand-uncle’s heir and executor, for he died a childless widower, I was expected to go over his papers with some thoroughness; and for that purpose moved his entire set of files and boxes to my quarters in Boston. Much of the material which I correlated will be later published by the American Archaeological Society, but there was one box which I found exceedingly puzzling, and which I felt much averse from shewing to other eyes. It had been locked, and I did not find the key till it occurred to me to examine the personal ring which the professor carried always in his pocket. Then indeed I succeeded in opening it, but when I did so seemed only to be confronted by a greater and more closely locked barrier. For what could be the meaning of the queer clay bas-relief and the disjointed jottings, ramblings, and cuttings which I found? Had my uncle, in his latter years, become credulous of the most superficial impostures? I resolved to search out the eccentric sculptor responsible for this apparent disturbance of an old mans peace of mind.")
# Text trivial
text = "AABCBAD"

# Text cleaning
text_cleaned = clean_text(text)
# print("Text (crude): "+ text)

# print("Text (formatted): "+ text_cleaned)

# Python dictionary structure is used, where key is a unique char and value is the number of occurences; dict is predefined as empty
signs = dict()

# Analyze text & populate the dict
for char in text_cleaned:
    if check_if_exists_in_dict(char, signs):
        signs.update({char: signs[char]+1})
    else:
        signs.update({char: 1})
    
# print("###" * 50)
# print("Unordered dictionary: "+str(signs))

# Now a Min Heap will be created; rules for it:
# 1. Parent is always smaller than its children
# 2. Between elements in each next layers there are no empty leaves
# 3. Every layer but the last one must be full

# For a typical array-stored heap convention, a min to max sorted
# array/list is a proper min heap. Here, I'll use built-in
# sort functionality for that.

sorted_signs = {k: v for k, v in sorted(signs.items(), key=lambda item: item[1])}
sorted_signs_list = list(sorted_signs.values())
# print("###" * 50)
# print("Ordered dictionary: "+str(sorted_signs))
# print("Ordered list: "+str(sorted_signs_list))

# Binarytree library is used for visualization
# print("###" * 50)
root_numeral = build(sorted_signs_list)
# print(root_numeral)

# print("###" * 50)
# Verification of the min heap
# if checkMinHeap(sorted_signs_list, 0):
#     print("The list above represent proper min heap")
# else:
#     print("The list above is NOT a proper min heap!")
#     exit

# A bit more visual fireworks: tree with letter representations
sorted_signs_formatted = list(sorted_signs.items())
sorted_signs_formatted_list = copy.deepcopy(sorted_signs_formatted)
for i, s in enumerate(sorted_signs_formatted):
    letter = str(sorted_signs_formatted[i][0])
    num = str(sorted_signs_formatted[i][1])
    new = letter+":"+num
    sorted_signs_formatted[i] = new
    
print(sorted_signs_formatted)
root_formatted = build2(sorted_signs_formatted)
# print(root_formatted)

# List-based implementation

# Reverse-sort frequency dictionary by value (descending)
huffman_input =  dict(sorted(sorted_signs.items(), key=lambda item: item[1], reverse=True))
huffman_keys = list(huffman_input)
print(huffman_input)
# Test - get key and value of a one pair from list
# print(huffman_keys[len(huffman_input)-1])
# print(huffman_input[huffman_keys[len(huffman_input)-1]])

# Creating tree nodes
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


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
# # Get least frequent ones values
# list_pointer = 1
# last_one = huffman_input[huffman_keys[len(huffman_input)-list_pointer]]
# list_pointer += 1
# second_one = huffman_input[huffman_keys[len(huffman_input)-list_pointer]]
# # Add sum before them
# print("Huffman coding tree creation starts here.")
# root = Node(last_one + second_one)
# # print("Tree was initalized with "+str(sum)+", which is a sum of last & second last node values.")
# # print(sub_tree)
# pair = HuffPair(key=huffman_keys[len(huffman_input)-list_pointer] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer]])
# root.values.append(pair)
# print(root)
# exit
# # print("Last node, "+str(pair)+", was added to the list.")
# # regenerate_visual_tree(sub_tree)
# pair2 = HuffPair( key=huffman_keys[len(huffman_input)-list_pointer+1] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer+1]])
# sub_tree.append(pair2)
# # print("Second last node, "+str(pair)+", was added to the list.")
# regenerate_visual_tree(sub_tree)
# ############################################
# print("Initial tree structure has been finalized.")

# list_pointer += 1
# pair = HuffPair(key=huffman_keys[len(huffman_input)-list_pointer] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer]])
# new_tree = []
# # Sum always go to the new root
# root = Node(pair._value + sub_tree[0])
# if pair._value > sub_tree[0]:
#     root.right = Node(sub_tree)
#     root.left = Node(pair._value)
# else:
#     root.left = Node(sub_tree)
#     root.right = Node(pair._value)

# print(root)
# print(pair._value)
# print(sub_tree[0])
# if sub_tree[0] < pair._value:
#     # Add another leaf on the LEFT; order: New_root, New_leaf, sub_tree
    # new_tree = []
    # new_tree.append(pair._value + sub_tree[0])
#     new_tree.append(pair)
#     new_tree.extend(sub_tree)
#     sub_tree = new_tree
#     regenerate_visual_tree(new_tree)
# else:
#     # Add another leaf on the RIGHT; order: 
#     new_tree = []
#     new_tree.append(pair._value + sub_tree[0])
#     new_tree.append(sub_tree[0])
    
# list_pointer += 1
# pair = HuffPair(key=huffman_keys[len(huffman_input)-list_pointer] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer]])
# new_sum = huffman_input[huffman_keys[len(huffman_input)-list_pointer]] + sum
# sum = new_sum
# new_tree = []
# new_tree.append(new_sum)
# new_tree.append(pair)
# new_tree.extend(sub_tree)
# sub_tree = new_tree
# sub_tree.sort(reverse=True)
# regenerate_visual_tree(sub_tree)

# list_pointer += 1
# pair = HuffPair(key=huffman_keys[len(huffman_input)-list_pointer] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer]])
# new_sum = huffman_input[huffman_keys[len(huffman_input)-list_pointer]] + sum
# sum = new_sum
# new_tree = []
# new_tree.append(new_sum)
# new_tree.append(pair)
# new_tree.extend(sub_tree)
# sub_tree = new_tree
# sub_tree.sort(reverse=True)
# regenerate_visual_tree(sub_tree)

# root = build2([2, 5, None, 3, None, 1, 4])

# print(root)
# # new_tree.append(pair)
# sub_tree.sort(reverse=True)
# print("Now, another smallest value is added to the tree, which is "+str(pair)+". Please note that the tree will be also sorted:")
# regenerate_list_only(sub_tree)
# sum += huffman_input[huffman_keys[len(huffman_input)-list_pointer]]
# sub_tree.append(sum)
# print("Sum was increased by the value of the last HuffPair inserted. It was added to the tree and tree has been sorted.")
# sub_tree.sort(reverse=True)
# regenerate_visual_tree(sub_tree)

# Generate codes


# regenerate_visual_tree(sub_tree)

# list_pointer += 1
# pair = HuffPair(key=huffman_keys[len(huffman_input)-list_pointer] , value=huffman_input[huffman_keys[len(huffman_input)-list_pointer]])
# sub_tree.append(pair)
# sub_tree.sort(reverse=True)
# regenerate_visual_tree(sub_tree)


# Tree structure definition
# class NodeTree(object):

#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right

#     def children(self):
#         return(self.left, self.right)
    
#     def nodes(self):
#         return (self.left, self.right)
    
#     def __str__(self):
#         return '%s_%s' % (self.left, self.right)
    
# # Huffman code tree impl
# def huffman_code_tree(node, left=True, binString=''):
#     if type(node) is str:
#         return {node: binString}
#     (l, r) = node.children()
#     d = dict()
#     d.update(huffman_code_tree(1, True, binString + "0"))
#     d.update(huffman_code_tree(r, False, binString + '1'))
#     return d

# sorted_signs_formatted_list_copy = copy.deepcopy(sorted_signs_formatted_list)

# while len(sorted_signs_formatted_list) > 1:
#     (key1, c1) = sorted_signs_formatted_list[-1]
#     (key2, c2) = sorted_signs_formatted_list[-2]
#     sorted_signs_formatted_list = sorted_signs_formatted_list[:-2]
#     node = NodeTree(key1, key2)
#     sorted_signs_formatted_list.append((node, c1 + c2))

#     sorted_signs_formatted_list = sorted(sorted_signs_formatted_list, key=lambda x: x[1], reverse=True)

# huffmanCode = huffman_code_tree(sorted_signs_formatted_list[0][0])

# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in sorted_signs_formatted_list_copy:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))