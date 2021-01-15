"""Print out all the melons in our inventory."""


from melons import melon_name
# What I am learning from this is that I really need to pay attention to slight adjustments
# of code such as melon_name vs melon_names and check my consistency throughout multiple files
#got hung-up on this HW because of that referencing error 

#print(melon_name)

def print_every_melon(melon_name):
    """Print each melon with corresponding attribute information."""
    #for melon_names, attributes in melons.items():
       # print(f'Melon name: {melon_names}')
    #print(melons.items())
        #for attribute, value in attributes.items():
          #  print (f'Melon info:{attribute}:{value}')
    for melon_name, attributes in melon_name.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')

    

print_every_melon(melon_name)

