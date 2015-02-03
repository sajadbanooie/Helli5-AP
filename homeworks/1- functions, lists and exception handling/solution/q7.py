# question 7 solution


try:
    f = open("test.txt", "r")
    try:
        g = f.readlines()
        g = [int(z) for z in g]
        print sum(g)*1./len(g)
    except:
        print "empty file"
except:
    print "file not found"
    
