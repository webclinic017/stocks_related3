def outer_func(who):
    i=7    
    def inner_func():
        print("Hello  ", who)
    


    def inner_func55(i):
        print("Hello babu ", who,' ',i)
    inner_func()
    inner_func55(i)



outer_func("World!")
