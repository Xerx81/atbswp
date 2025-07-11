spam = ["apples", "bananas", "cherries", "dates"] 

def list_to_string(items):
    if len(items) == 0:
        print("")
    elif len(items) == 1:
        print(items[0])
    elif len(items) == 2:
        print(f"{items[0]} and {items[1]}.")
    else:
        print(", ".join(items[:-1]) + f", and {items[-1]}.")

list_to_string(spam)
