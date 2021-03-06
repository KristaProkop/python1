
#if list item is string, print the first letter, string length times, in lowercase
#if the list item is a number, print *, number times

def draw_stars(my_list):
    for element in my_list:
        if type(element) is str:
            print element[0].lower()*len(element)
        elif type(element) is int:
            print "*"*element
        else:
            print "Invalid list item"


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
y = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
draw_stars(y)

#test edge case with boolean list item
z = [False, "Tom", 7]  
draw_stars(z)
