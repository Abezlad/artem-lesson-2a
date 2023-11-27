#----- 10.1 -----

def get_domains( filename: str = "" ):
    if filename:
        with open( filename, "r" ) as file:
            data = file.read()
            rows = data.split("\n")
            return list(map( lambda row: row[1:], rows ))

res = get_domains( "domains.txt" )
print( res )

#----- 10.2 -----

def get_names( filename: str = "" ):
    if filename:
        with open( filename, "r" ) as file:
            data = file.read()
            rows = data.split("\n")
            return list(map( lambda row: row.split("\t")[1], rows ))

res = get_names( "names.txt" )
print( res )

#----- 10.3 -----

def get_names( filename: str = "" ):
    if filename:
        dates = []
        with open( filename, "r" ) as file:
            data = file.read()
            rows = data.split("\n")
            for row in rows:
                if "-" in row:
                    dates.append( {"date": row.split( "-" )[0].strip()} )

            return dates

res = get_names( "authors.txt" )
print( res )