def fun(dates):
    for i in range(0, len(dates)-1):
        for j in range(0, len(dates)-i-1):
            if dates[j]["year"] > dates[j+1]["year"]:
                temp = dates[j]
                dates[j] = dates[j+1]
                dates[j+1] = temp
            elif dates[j]["year"] == dates[j+1]["year"]:
                if dates[j]["month"] > dates[j+1]["month"]:
                    temp = dates[j]
                    dates[j] = dates[j + 1]
                    dates[j + 1] = temp
                elif dates[j]["month"] == dates[j+1]["month"]:
                    if dates[j]["day"] > dates[j+1]["day"]:
                        temp = dates[j]
                        dates[j] = dates[j + 1]
                        dates[j + 1] = temp
    return dates

