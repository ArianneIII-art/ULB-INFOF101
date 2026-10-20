def prime_numbers(nb):
    if type(nb) != int:
        return None
    elif nb < 0:
        return None
    
    prime_list = []
    i = 2
    while len(prime_list) < nb:
        is_prime = True
        for c in prime_list:
            if i % c == 0:
                is_prime = False
        if is_prime:
            prime_list.append(i)
        i += 1
    return prime_list