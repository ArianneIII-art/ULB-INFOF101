n = int(input())

if not(n%2):
    print("erreur")
    exit()

for i in range(n):
    base_str = "X "
    zero_str = "- "
    s = base_str*n
    s = s[:i*len(base_str)] + zero_str + s[(i+1)*len(base_str):]
    s = s[:(n-i-1)*len(base_str)] + zero_str + s[(n-i)*len(base_str):]
    print(s)