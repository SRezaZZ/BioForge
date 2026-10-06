def annotation(orfs):
    orfdic = {}
    count = 1

    for orf in orfs:
        if count <= 9:
            label = f"BFG_00{count}"
        elif count <= 99:
            label = f"BFG_0{count}"
        elif count <= 999:
            label = f"BFG_{count}"
        else:
            label = "no space for id"

        orf["ID"] = label
        orfdic[label] = orf
        count += 1

    return orfs