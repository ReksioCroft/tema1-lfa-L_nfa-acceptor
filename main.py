def evaluare( cuv, stare, vizitat ):
    vizitat[stare] = True
    raspuns = False
    if len(cuv) == 0:
        if stare in finale:
            raspuns = True
        else:
            for i in Q[stare]["$"]:
                if vizitat[i] == False:
                    raspuns = raspuns or evaluare( cuv, i, vizitat )
                    if raspuns == True:
                        break
    elif cuv[0] in alfabet:
        for i in Q[stare][ cuv[0] ]:
            raspuns = raspuns or evaluare( cuv[1:], i, [ False for i in range(nrStari) ] )
            if raspuns == True:
                break
        else:
            for i in Q[stare]["$"]:
                raspuns = raspuns or evaluare( cuv, i, vizitat )
                if raspuns == True:
                    break
    return raspuns


fin = open("automat.in")
nrStari = int( fin.readline() )
fin.readline()
alfabet = fin.readline().split()
alfabet.append( "$")
stare0 = int( fin.readline() )
fin.readline()
finale = [ int(x) for x in fin.readline().split() ]
fin.readline()
Q = [ { j : [] for j in alfabet } for i in range(nrStari) ]
for i in fin:
    ls = i.split()
    a = int( ls[0] )
    b = int( ls[2] )
    ch = ls[1]
    ls = Q[a][ch]
    ls.append( b )
    Q[a][ch] = ls
fin.close()

teste = open( "teste.in" )
for i in teste:
    print( evaluare( i.strip(" ,-.;\n"), stare0, [ False for i in range(nrStari) ] ) )
teste.close()
