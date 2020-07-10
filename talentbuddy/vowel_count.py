def count_vowels(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    count = 0
    vowels = ['a','e','i','o','u']
    
    for i in xrange(len(s)):
        print "Index: %d" % i
        if s[i].lower() in vowels: 
           print s[i]
           count += 1
            
    print count

count_vowels("It is Sunny Day")
count_vowels("iGet Some")

