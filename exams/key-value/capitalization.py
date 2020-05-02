def capitalize(string: str, rule: list):
    # handle the case longer strings than rule
    if len(rule) < len(string):
        # add a sufficient amount of 
        rule = rule * (len(string) // len(rule) + 1)

    result = []
    # zip() stops when shortest iterable is exhausted
    # thus, the string will be the limiting factor,
    # as was intended
    for char, flag in zip(string, rule):
        # skip non-alphabetic characters
        if not char.isalpha():
            result.append(char)
        elif flag: # truthy
            # capitalize if flag is 1
            result.append(char.upper())
        else: # falsy
            # set to lowercase if flag is 0
            result.append(char.lower())

    return ''.join(result)

