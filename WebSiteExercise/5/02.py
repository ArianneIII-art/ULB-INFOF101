def est_adn(s):
    if len(s) == 0:
        return False
    
    to_return = True
    for i in range(len(s)):
        if not(s[i] in ['A','T','C','G']):
            to_return = False
    return to_return