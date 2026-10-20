def store_email(liste_mails: list[str]):
    to_return = {}
    for i in range(len(liste_mails)):
        liste_mails[i] = liste_mails[i].split("@")
        to_return[liste_mails[i][1]] = []

    for i in liste_mails:
        to_return[i[1]].append(i[0])
        if "thierry" in to_return[i[1]]:
            to_return[i[1]].remove("thierry")
            to_return.append("thierry")

    return to_return