import re


delims = [
    [["""<markup><b><span size=\\\"12288\\\">""", """<"""],
    ["""<markup><b><span size=\\\"12288\\\"><span foreground=\\\"#000000\\\">""", """<"""]],

    [["<markup><b><span size=\\\"8847\\\">", """<"""]],

    [["""<markup><b><span size=\\\"8847\\\">""", """<"""]]
]


def find_all_between(text, start, end):
    found = []
    index = 0
    start_index = text[index:].find(start)
    while start_index != -1:
        start_pos = index + start_index + len(start)
        end_index = text[start_pos:].find(end)
        if end_index != -1:
            end_pos = start_pos + end_index
            index = end_pos + len(end)
            found.append(text[start_pos:end_pos])
        start_index = text[index:].find(start)
    return found


for floor in range(1,4):
    with open(f"{floor}.xcf", mode="rb") as f:
        # convert bytes to string, ignoring encoding
        text = f.read().decode("ascii", "backslashreplace")

        # For each set of delimiters, find all the text between them
        items = []
        for delimset in delims[floor-1]:
            itemset = find_all_between(text, delimset[0], delimset[1])
            items.extend(itemset)

        items = list(set(items))

        newitems = []
        for item in items:
            # re.split for "\\n", " / ", or " "
            for newitem in re.split(r"\\n| / | ", item):
                newitems.append(newitem)

        newitems = [item for item in newitems if item != ""]

        # alphabetize
        newitems.sort()

        # save each item in newtimes to a line in a txt file
        with open(f"Extracted/{floor}.txt", mode="w") as f:
            for item in newitems:
                f.write(item + "\n")
            f.close()