def a(**kwargs):
    result=[{'a':'3' , 'b':'4' , 'c':'7', 'd':'0'},{'a':'3' , 'b':'5' , 'c':'8', 'd':'1'}]
    #found =0
    for dic in result:
        if dic['a'] == '3':
            found = 0
            for key,value in kwargs.items():
                if dic[key] == value:
                    found = found + 1
                else:
                    found = 0
		print "******"
		print found
		print "******"
            if len(kwargs) == found:
                break
    if len(kwargs) !=  found:
        print "error"
a(c='8',b='4')        
