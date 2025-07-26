def combine_lists(list1, list2):
    result = []
    used2 = [False] * len(list2)

    for item1 in list1:
        pos1 = item1["positions"]
        len1 = pos1[1] - pos1[0]
        merged = False

        for i, item2 in enumerate(list2):
            if used2[i]:
                continue

            pos2 = item2["positions"]
            len2 = pos2[1] - pos2[0]

            start = max(pos1[0], pos2[0])
            end = min(pos1[1], pos2[1])
            overlap = end - start

            if overlap > 0 and (overlap > len1 / 2 or overlap > len2 / 2):
                
                result.append({
                    "positions": pos1,
                    "values": item1["values"] + item2["values"]
                })
                used2[i] = True
                merged = True
                break

        if not merged:
            result.append(item1)

   
    for i, item2 in enumerate(list2):
        if not used2[i]:
            result.append(item2)

    
    return sorted(result, key=lambda x: x["positions"][0])
    



