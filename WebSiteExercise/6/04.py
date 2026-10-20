def substitue(message: str, abreviation):
    for i in abreviation:
        message = message.replace(i+" ", abreviation[i])
    return message