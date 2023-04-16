# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()
    if ("I" in choice):
        pattern = input()
        text = input()
    elif ("F" in choice):
        print("Input file path")
        path = input()
        path = "./tests/" + path
        f = open(path, "r")
        pattern = f.readline()
        text = f.readline()
        f.close()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    position = []
    patternLength = len(pattern)
    textLength = len(text)
    patternHash = hash(pattern)

    for i in range (textLength - patternLength + 1):
        if hash(text[i:i+patternLength]) == patternHash:
            if text[i:i+patternLength] == pattern:
                position.append(i)
    # and return an iterable variable
    return position


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
