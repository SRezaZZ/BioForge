count = 1
orfdic = {}

def annotation(ORF) : # برای ORF های نهایی ID خودکار می‌سازد.
    global count
    if count <= 9 :
        label = f"BGF_00{count}"
        orfdic[ORF] = [label]
        count+=1
        return (label)
    elif count <= 99 :
        label = f"BGF_0{count}"
        orfdic[ORF] = [label]
        count+=1
        return (label)
    elif count <= 999 :
        label = f"BGF_{count}"
        orfdic[ORF] = [label]
        count+=1
        return (label)
    else :
        return ("no space for id")
