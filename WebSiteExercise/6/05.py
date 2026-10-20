def construction_dict_amis(l):
    a = dict()
    for i in l:
        a[i[0]] = set()
        a[i[1]] = set()

    for i in l:
        a[i[0]].add(i[1])

    return a

print(construction_dict_amis([('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')])
)