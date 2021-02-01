parser_items = {
"root": ".",
"file_mid": "├── FILE",
"file_end": "└── FILE",
"indent": "│   ",
"empty_indent": "    ",
"newline": "\n"
}

item_holders = [
    dict,
    list,
    tuple
]



#items = [
#    str,
#    int,
#    float
#]

def find_in_dict(d, f):
    count = 0
    for i in d:
        if i == f:
            return count, i
        count += 1
    return None

""" def make_indents(number, find_, len_):
    global parser_items
    op = ""
    for ind in range(number):
        if find_<len_:
            op += parser_items["empty_indent"]
        else:
            op += parser_items["indent"]
    return op """

def indentation(number_of_indents: int, ended_indents: dict):
    global parser_items
    ind = ""
    for i in range(number_of_indents):
        if ended_indents.get(i, True) == False:
            ind += parser_items["empty_indent"]
        else:
            ind += parser_items["indent"]
    return ind

def parse(item_holder, indents = 0, ended_indents: dict = {}):
    global parser_items, item_holders
    #print (item_holders)
    if type(item_holder) not in item_holders:
        raise TypeError(f"{type(item_holder).__name__} not a valid item holder")
    if indents == 0:
        output = parser_items["root"] + parser_items["newline"]
    else:
        output = parser_items["newline"]
    num = 0
    for file in item_holder:
        f = find_in_dict(item_holder, file)[0]
        le = len(item_holder)-1
        if f<le:
            output += indentation(indents, ended_indents) + parser_items["file_mid"].replace("FILE", file) #parser_items["indent"]*indents
        else:
            output += indentation(indents, ended_indents) + parser_items["file_end"].replace("FILE", file) #parser_items["indent"]*indents
            ended_indents[indents] = False
            #print ("end of indent number", indents)
        if type(item_holder[file]) in item_holders:
            if len(item_holder[file]) != 0:
                ended_indents[indents + 1] = True
                output += parse(item_holder[file], indents + 1)
        #if indents == 0:
        if num != le:
            output += parser_items["newline"]
        num += 1
    return output