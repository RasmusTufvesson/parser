
import item_parser
import json

def parse(item_holder = None, json_file = None, file = None):
    if json_file != None:
        with open(json_file, "r") as f:
            out = json.loads(f.read())
        
    elif item_holder != None:
        out = eval(item_holder)#dict(item_holder)
    
    else:
        raise ValueError("no item holder or json file assigned")

    out = item_parser.parse(out)

    if file == None:
        print (out)
    else:
        if file != None:
            with open(file, "w") as f:
                file.write(json.dumps(out))

import argh

argh.dispatch_command(parse)