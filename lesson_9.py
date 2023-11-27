# ----- 9.1 -------
def my_func( my_list ):
    new_list = []
    for i, el  in enumerate( my_list ):
        if i % 2 == 1:
            new_list.append( el[::-1] )
        else:
            new_list.append( el )
    return new_list

res = my_func( [ "aboba", "4321", "rorwowor", "1234" ] )

print( res )

# ----- 9.2 -------
def only_a( my_list ):
    new_list = []
    for el in my_list:
        if el[0] == "a" or el[0] == "A":
            new_list.append( el )
    return new_list

res = only_a( [ "aboba", "a4321", "rorwowor", "a1234" ] )

print( res )

# ------ 9.3 ------
def filter_by_a( my_list ):
    return list(filter( lambda row: "a" in row, my_list ))

my_list = ["abc", "deg", "asfasf", "jljljlj"]

print( filter_by_a( my_list ) )


# ------ 9.4 ------
def only_string( my_list ):
    new_list = []
    for el in my_list:
        if isinstance( el, str ):
            new_list.append( el )
    return new_list


res = only_string([ "a", 2, "c", 4, "b" ])
print( res )


# ----- 9.5 -------

def only_one( my_list ):
    new_list = []
    for el in my_list:
        if my_list.count( el ) == 1:
            new_list.append( el )
    return new_list

res = only_one( [1,2,1,2,3,4,5] )
print( res )


# ----- 9.6 -------

def concan( row1, row2 ):
    return [ *list(row1), *list(row2) ]

print( concan( "hello", "world" ) )


# ----- 9.7 -------

def only_one_plus( row1, row2 ):
    row1_origin = list(filter( lambda char: row1.count( char ) == 1, list(row1) ))
    row2_origin = list(filter( lambda char: row2.count( char ) == 1, list(row2) ))
    return [ *list(row1_origin), *list(row2_origin) ]

res = only_one_plus( "hello", "wrold" )

print( res )


# ----- 9.8 -------

from random import randint, choice
from string import ascii_lowercase

def create_email( domains, names ):
    rand_string = "".join([ choice( ascii_lowercase )for _ in range( randint(5, 7) ) ])
    return f"{choice(names)}.{randint(100, 999)}@{rand_string}.{choice(domains)}"

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)

print(e_mail)