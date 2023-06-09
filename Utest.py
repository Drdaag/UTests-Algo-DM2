from algo_py.bintree import BinTree
from algo_py import heap

import random

# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader

# My handout
myfile = "MY_FILE.py"
# Load module. Same result as "import mycode"
mycode = SourceFileLoader('mycode', myfile).load_module()

# print(mycode.build_frequency_list("bbaabtttaabtctce"))

def simple_check(name, tru, val):
    test = ("[OK]" if tru == val else "-----------NO")
    print(f"{name} : {test}")
    if(test == "-----------NO"):
        print(f"True : {tru}\nGot  : {val}\n")
        return False
    return True
        
def rand_string_gen(res):
    str_val = ""
    leng = len(res)
    for i in range(leng):
        num = res[i]
        for j in range(num[0]):
            str_val += num[1]
    sr = ''.join(random.sample(str_val, len(str_val)))
    return sr

def get_hauteur_feuilles(B):
    if (B == None) :
        return []
    else :
        res = []
        auxi_get_feuilles(B, res, 0)
        return res

def auxi_get_feuilles(B, L, i):           
    if(B.left == None):
        if(B.right == None):
            return (B.key, i)
    else :
        tmp = auxi_get_feuilles(B.right, L, i+1)
        if (tmp != None):
            L.append(tmp)
        tmp2 = auxi_get_feuilles(B.left, L, i+1)
        if (tmp2 != None):
            L.append(tmp2)

            
def check_scramble_lists(name, L1, L2):
    if(len(L1) != len(L2)):
        print(f"{name} : -----------NO")
        print(f"True : {L1}\nGot  : {L2}\n")
    else:
        i = 0
        leng = len(L1)
        while (i < leng and L1[i] in L2) :
            i += 1
        if (i == leng) :
            print(f"{name} : [OK]")
            return True
        else :
            print(f"{name} : -----------NO")
            print(f"{L1[i]} is not in !")
            print(f"True : {L1}\nGot  : {L2}\n")
            return False
            
            
def mult_scamble_list(name, L, LL):
    for l in LL :
        if(len(l) != len(L)):
                continue
        i = 0
        leng = len(l)
        while (i < leng and l[i] in L) :
            i += 1
        if (i == leng) :
            print(f"{name} : [OK]")
            return True
    print(f"{name} : -----------NO")
    print(f"{l[i]} is not in !")
    print(f"True (and variants): {l}\nGot                : {L}\n")
    return False

def check_freq(x):
    freq = []
    for c in set(x): #set => créait un disctionnaire = {}
       freq.append((x.count(c), x))
    return freq

            
def __tostr(self):
    l, r, t = [], [], []
    middle_left, middle_right = 0, 0
    key = str(self.key)
    len_key = len(key)
    middle = len_key // 2
    len_left, len_right = 0, 0
    if self.left != None:
        l, middle_left = __tostr(self.left)
        key = "_" + key
        len_key += 1
        len_left = len(l[0])
        middle += len_left + 1
    if self.right != None:
        r, middle_right = __tostr(self.right)
        key += "_"
        len_key += 1
        len_right = len(r[0])
    if l == [] and r == []:
        return [key], len_key //2
    t.append( (" " * (middle_left + 1) + "_" * (len_left - middle_left - 1) if l else "") 
                + key 
                + ("_" * (middle_right) + " " * (len_right - middle_right) if r else "")
            )
    t.append( (" " * middle_left + "/" + " " * (len_left - middle_left - 1) if l else "") 
                + " " * len_key 
                + (" " * middle_right + "\\" + " " * (len_right - middle_right - 1) if r else "")
            )
    ll, lr = len(l), len(r)
    t = t + [   ((l[i] if i < ll else " " * len_left) 
                    + " " * len_key
                    + (r[i] if i < lr else " " * len_right) )
                    for i in range(max(ll, lr))
            ]
    return t, middle
                
def print_tree(tree):
    print("".join(e + "\n" for e in __tostr(tree)[0]))

B_Simple = B = BinTree(None, BinTree(
    None, BinTree("t", None, None), BinTree(
                "b", None, None)), BinTree(None, BinTree("a", None, None), BinTree(None, BinTree("c", None, None), BinTree("e", None, None))))

B_medium = BinTree(None,
             BinTree(None, 
                     BinTree(None, 
                             BinTree('m', None, None),
                             BinTree(None,
                                     BinTree(None, 
                                             BinTree('s', None, None),
                                             BinTree('i', None, None)
                                             ),
                                     BinTree('u', None, None)
                                     )
                            ),
                     BinTree('a', None, None)
                     ),
             BinTree(None,
                     BinTree(' ', None, None),
                     BinTree(None,
                             BinTree(None,
                                     BinTree('n', None, None),
                                     BinTree('f', None, None)
                                     ),
                             BinTree('h', None, None)
                             )
                    )
            )   
# ------------------------------------------------------------------------------------------
# B = bintree.BinTree("1", bintree.BinTree("2", bintree.BinTree("3", None, None), None), bintree.BinTree("4", bintree.BinTree("5", None, None), None))
# print(print__str__(B))    
            
            
        
# build_frequency_list
print("\n---------build_frequency_list---------")   
print()  
# simple
res = [(4, 'a'), (4, 'b'), (2, 'c'), (1, 'e'), (5, 't')]
val = mycode.build_frequency_list("bbaabtttaabtctce")
check_scramble_lists("build_frequency_list_simple", res, val)

# medium
res = [(15, ' '), (12, 'a'), (4, 'f'), (9, 'h'), (2, 'i'), (4, 'm'), (4, 'n'), (1, 's'), (4, 'u')]
val = mycode.build_frequency_list("um ah human huffman is fun i am a fan ha ha ha ha ha ha")
check_scramble_lists("build_frequency_list_medium", res, val)


# empty
res = []
val = mycode.build_frequency_list("")
check_scramble_lists("build_frequency_list_empty", res, val)

# complex
res = [(74, 'f'), (1, 'h'), (54, 'k'), (40, 'j'), (4, 's'), (1, 'l'), (29, 'z'), (2, 'e'), (16, 'p'), (4, 'd')]
val = mycode.build_frequency_list("fffhkkffjjfkfjfjfkkkkfkfjfkfsslskfjfkfszfjkfjkfkfkfjfkepjfepzfjjfkdkdjfdkdfjzpjfkfkfjzpkfkfjkzpfkzfjkfffjfkfkfkfjffjfzpzpzzkfjfjfkkzzkjfzkpfkjfkfjfjfjfjfjfkzpkzzppzkfjzpfjkffjfkzpkfjzkfkfkzjfkzkfjkzpfzkfzjfzkzpkjfzkfjpfjfkzfk")
check_scramble_lists("build_frequency_list_complex", res, val)

# build_Huffman_tree
print("\n---------build_Huffman_tree---------")  
print()
print("-----------------------------------------------------")
print("PLUSIEURS ARBRES SONT POSSIBLES POUR UNE MEME LISTE")
print("L'important, chaque feuille est a la bonne hauteur !")
print("SAUF LES FEUILLES DE MEME FREQ, QUI PEUVENT SE SWITCH")
print("         ET DONC PAS AVOIR LA MEME HAUTEUR")
print("-----------------------------------------------------")
print()

# Simple
res = mycode.build_Huffman_tree([(4, 'a'), (4, 'b'), (2, 'c'), (1, 'e'), (5, 't')])
# print(res)
# haut_res = [('t', 2), ('a', 2), ('b', 2), ('c', 3), ('e', 3)]
B = BinTree(None, BinTree(
    None, BinTree("t", None, None), BinTree(
                "b", None, None)), BinTree(None, BinTree("a", None, None), BinTree(None, BinTree("c", None, None), BinTree("e", None, None))))
# B = BinTree(None, BinTree(None, BinTree(None, BinTree("e", None, None), BinTree("c", None, None)), BinTree("b", None, None)), BinTree(None, BinTree("a", None, None), BinTree("t", None, None)))
haut = get_hauteur_feuilles(res)
haut_res = get_hauteur_feuilles(B)
test = check_scramble_lists("build_Huffman_tree_simple", haut, haut_res)
if (not test):
    # print(haut)
    print("True :")
    print_tree(B)
print("Got :")
print_tree(res)
    
# Medium
res = mycode.build_Huffman_tree([(15, ' '), (12, 'a'), (4, 'f'), (9, 'h'), (2, 'i'), (4, 'm'), (4, 'n'), (1, 's'), (4, 'u')])
[(15, ' '), (12, 'a')]
# print(res)
# haut_res = [('t', 2), ('a', 2), ('b', 2), ('c', 3), ('e', 3)]
B = BinTree(None,
             BinTree(None, 
                     BinTree(None, 
                             BinTree('m', None, None),
                             BinTree(None,
                                     BinTree(None, 
                                             BinTree('s', None, None),
                                             BinTree('i', None, None)
                                             ),
                                     BinTree('u', None, None)
                                     )
                            ),
                     BinTree('a', None, None)
                     ),
             BinTree(None,
                     BinTree(' ', None, None),
                     BinTree(None,
                             BinTree(None,
                                     BinTree('n', None, None),
                                     BinTree('f', None, None)
                                     ),
                             BinTree('h', None, None)
                             )
                    )
            )
haut = get_hauteur_feuilles(res)
haut_res = [[('h', 3), ('f', 4), ('n', 4), (' ', 2), ('a', 2), ('u', 4), ('i', 5), ('s', 5), ('m', 3)], #m
            [('h', 3), ('m', 4), ('n', 4), (' ', 2), ('a', 2), ('u', 4), ('i', 5), ('s', 5), ('f', 3)], #f
            [('h', 3), ('m', 4), ('f', 4), (' ', 2), ('a', 2), ('u', 4), ('i', 5), ('s', 5), ('n', 3)], #n
            [('h', 3), ('m', 4), ('f', 4), (' ', 2), ('a', 2), ('n', 4), ('i', 5), ('s', 5), ('u', 3)]] #u
test = mult_scamble_list("build_Huffman_tree_medium", haut, haut_res)
if (not test):
    # print(haut)
    print("True :")
    print_tree(B)
print("Got :")
print_tree(res)

# Empty
res = mycode.build_Huffman_tree([])
# print(res)
# haut_res = [('t', 2), ('a', 2), ('b', 2), ('c', 3), ('e', 3)]
B = None
haut = get_hauteur_feuilles(res)
haut_res = get_hauteur_feuilles(B)
test = check_scramble_lists("build_Huffman_tree_empty", haut, haut_res)
if (not test):
    # print(haut)
    print("True :")
    print("None")
    print("Got :")
    print(res)
    
print("\n---------encode_data---------")      
    
# encode_data
print()
# simple
val = mycode.encode_data(B_Simple, "bbaabtttaabtctce")
res = '01011010010000001010010011000110111'
simple_check("encode_data_simple", res, val)
 
    
# Medium
val = mycode.encode_data(B_medium, "um ah human huffman is fun i am a fan ha ha ha ha ha ha")
res = '001100010011111011100110000111001011100111101110100001110010001010010010110100111100100010110010001001101101011100101110110111011011101101110110111011011101'
simple_check("encode_data_medium", res, val)

# Empty
val = mycode.encode_data(B_medium, "")
res = ""
simple_check("encode_data_empty", res, val)   

# Not Found
try :
    val = mycode.encode_data(B_medium, "ha ha fun Z")
    print("encode_data_not_found : -----------NO")
    print(f"True : Raise Exception\nGot  : {val}\n")
except:
     print("encode_data_not_found : [OK]")
 
 
  
    
# decode_data
print("\n---------decode_data---------")
print() 

# Simple
val = mycode.decode_data(B_Simple, "01011010010000001010010011000110111")
res = 'bbaabtttaabtctce'
simple_check("decode_data_simple", res, val)

# Medium
val = mycode.decode_data(B_medium, "001100010011111011100110000111001011100111101110100001110010001010010010110100111100100010110010001001101101011100101110110111011011101101110110111011011101")
res = 'um ah human huffman is fun i am a fan ha ha ha ha ha ha'
simple_check("decode_data_medium", res, val)

# Empty
val = mycode.decode_data(B_medium, "")
res = ""
simple_check("decode_data_empty", res, val)   

# Not Found
try :
    val = mycode.encode_data(B_medium, "001")
    print("decode_data_not_found : -----------NO")
    print(f"True : Raise Exception\nGot  : {val}\n")
except:
     print("decode_data_not_found : [OK]")


# encode_tree
print("\n---------encode_tree---------")
print() 
# Simple
val = mycode.encode_tree(B_Simple)
res = '0010111010010110001001011000010101100011101100101'
simple_check("encode_tree_simple", res, val)

# Medium
val = mycode.encode_tree(B_medium)
res = '00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000'
simple_check("encode_tree_medium", res, val)

# Empty
print(f"encode_tree_empty : [NOT PRECISED IN THE SUBJECT]\nGot : {mycode.encode_tree(BinTree(None, None, None))}")


# decode_tree
print("\n---------decode_tree---------")
print("/!\\ DEPEND DE ENCODE, A CHECKER DANS LE DOUTE ! /!\\")
print() 

# Simple
enc = "0010111010010110001001011000010101100011101100101"
res = mycode.decode_tree(enc)
val = mycode.encode_tree(res)
test = simple_check("decode_tree_simple", enc, val)
if (not test):
    print("True :")
    print_tree(B_Simple)
    print("Got :")
    print_tree(res)

# Medium
enc = "00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000"
res = mycode.decode_tree(enc)
val = mycode.encode_tree(res)
test = simple_check("decode_tree_medium", enc, val)
if (not test):
    print("True :")
    print_tree(B_medium)
    print("Got :")
    print_tree(res)


# to_binary
print("\n---------to_binary---------")
print()

# data_Simple
encData = "01011010010000001010010011000110111"
           
res = mycode.to_binary(encData)
tru = ('Z@¤Æ\x07', 5)
simple_check("to_binary_data_simple", tru, res)


# data_Medium
encData = "001100010011111011100110000111001011100111101110100001110010001010010010110100111100100010110010001001101101011100101110110111011011101101110110111011011101"
res = mycode.to_binary(encData)
tru = ('1>æ\x1c¹î\x87"\x92ÓÈ²&×.Ý»ví\r', 4)
simple_check("to_binary_data_medium", tru, res)

# tree_Simple
encTree = "0010111010010110001001011000010101100011101100101"
res = mycode.to_binary(encTree)
tru = ('.\x96%\x85c²\x01', 7)
simple_check("to_binary_tree_simple", tru, res)

# tree_Medium
encTree = "00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000"
res = mycode.to_binary(encTree)
tru = ('\x16ÒçiºØR\x02Ýf´\x00', 7)
simple_check("to_binary_tree_medium", tru, res)

# no_align
encTree = "00010110"
res = mycode.to_binary(encTree)
tru = ('\x16', 0)
simple_check("to_binary_tree_no_align", tru, res)

# from_binary
print("\n---------from_binary---------")
print()

# data_Simple
tru = "01011010010000001010010011000110111"
res = mycode.from_binary('Z@¤Æ\x07', 5)
simple_check("from_binary_data_simple", tru, res)


# data_Medium
tru = "001100010011111011100110000111001011100111101110100001110010001010010010110100111100100010110010001001101101011100101110110111011011101101110110111011011101"
res = mycode.from_binary('1>æ\x1c¹î\x87"\x92ÓÈ²&×.Ý»ví\r', 4)
simple_check("from_binary_data_medium", tru, res)

# tree_Simple
tru = "01011010010000001010010011000110111"
        
res = mycode.from_binary('Z@¤Æ\x07', 5)
simple_check("from_binary_tree_simple", tru, res)

# tree_Medium
tru = "00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000"
res = mycode.from_binary('\x16ÒçiºØR\x02Ýf´\x00', 7)
simple_check("from_binary_tree_medium", tru, res)


# compress/decompress
print("\n---------compress/decompress---------")
print()

# Simple
tru = "bbaabtttaabtctce"
tmp = mycode.compress(tru)
val = mycode.decompress(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
simple_check("FINAL_compress_simple", tru, val)

# Medium
tru = "um ah human huffman is fun i am a fan ha ha ha ha ha ha"
tmp = mycode.compress(tru)
val = mycode.decompress(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
simple_check("FINAL_compress_medium", tru, val)

# Complex
tru = "um ah human huffman is fun i am a fan ha ha ha ha ha ha MDR- Il est plus LONG ET EST COMPLEXE MDR"
tmp = mycode.compress(tru)
val = mycode.decompress(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
simple_check("FINAL_compress_complex", tru, val)




# RANDOM TESTS (may be unstable)
print("\n+---------RANDOM TESTS---------+")
print("|    May be unstable, don't    |")
print("|  consider them if the others |")
print("|         are not [OK]         |")
print("+------------------------------+\n")

# build_frequency_list
# simple
a = random.randint(1,5)
b = random.randint(1,5)
c = random.randint(1,5)
e = random.randint(1,5)
t = random.randint(1,5)
res = [(a, 'a'), (b, 'b'), (c, 'c'), (e, 'e'), (t, 't')]
sr = rand_string_gen(res)
val = mycode.build_frequency_list(sr)
check_scramble_lists("rand_build_frequency_list_simple", res, val)

# complex
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
e = random.randint(1,20)
t = random.randint(1,20)
h = random.randint(1,20)
k = random.randint(1,20)
l = random.randint(1,20)
m = random.randint(1,20)
p = random.randint(1,20)
res = [(a, 'a'), (b, 'b'), (c, 'c'), (e, 'e'), (t, 't'), (h, 'h'), (k, 'k'), (l, 'l'), (m, 'm'), (p, 'p')]
sr = rand_string_gen(res)
val = mycode.build_frequency_list(sr)
check_scramble_lists("rand_build_frequency_list_complex", res, val)
