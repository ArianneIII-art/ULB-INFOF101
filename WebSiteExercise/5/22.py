def wc(file: str) -> tuple[int]:
    with open(file, encoding="utf-8") as f:
        text = f.read()
    
    line = 0
    word = 0
    pev_alpha = False

    for ch in text:
        if ch == "\n":
            line += 1
        
        if not(pev_alpha) and ch.isalnum():
            word += 1
            pev_alpha = True
        elif not(ch.isalnum()):
            pev_alpha = False

    return len(text), word, line