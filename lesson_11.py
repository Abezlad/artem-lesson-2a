# ----- 1 ------

from os import listdir
#import os

def dir_info( dir_path ):
    info = {
        "filenames": [],
        "dirnames": []
    }
    for path in listdir( dir_path ):
        if len(path.split(".")) > 1:
            info["filenames"].append( path )
        else:
            info["dirnames"].append( path )
    return info

res = dir_info( "../" )
print( res )


# ----- 2 ------

def sort_by_alph( to_sort, is_reversed = False ):
    copy_of_dict = to_sort.copy()
    sorted_list = sorted(copy_of_dict["filenames"], key = lambda row: ord(row[0].lower()), reverse=is_reversed )
    copy_of_dict["filenames"] = sorted_list
    return copy_of_dict


res = sort_by_alph( dir_info( "test/" ), True )

print( res )


# ---- 3 -----

def add_new_element( dict_to_update, name ):
    copy_of = dict_to_update.copy()
    if len(name.split(".")) > 1:
        copy_of["filenames"].append( name )
    else:
        copy_of["dirnames"].append( name )
    return copy_of

res = add_new_element( dir_info( "test/" ), "file5" )
print( res )