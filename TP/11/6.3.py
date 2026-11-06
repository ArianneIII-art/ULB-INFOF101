def grouper_utilisateurs(t):
    res = {}
    for i in t:
        i = i.split("@")
        res[i[1]] = res.get(i[1], []) + [i[0]]
    return res


emails = ["alice@ulb.be", "bob@gmail.com", "charlie@ulb.be"]
print(grouper_utilisateurs(emails))
