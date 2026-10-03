count = 1
orfdic = {}

def annotation(ORF) : # برای ORF های نهایی ID خودکار می‌سازد.
    global count
    label = f"BGF_00{count}"
    orfdic[ORF] = [label]
    count+=1
    return (label)