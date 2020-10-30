"""

you are given a list of commands each command looks like this: 
command are: ADD, SUB, MUL, VALUE VALUE => putting an item in your return array command looks
like: { type: ADD, loc1: number, loc2: number}
resuts array which keeps track of the output 
first command => res[0] 
second command => res[1] 
command.loc1, you can either have a number, or you have an
index '$idx' for example { type: ADD, loc1: 5, loc2: 3}  => 8 
buut {type: ADD, loc1: '$1', loc2: '$2' } =>  add res[1] with res[2]

make a function that returns an array of commands and returns a results array
input: [{ type: VALUE, loc1: 5, loc2: null}, {type: ADD, loc1: '$0', loc2: 3}] 
returns [5, 8]

"""
# can try to develop a graph
"""
probable solution:
1) lenght = len(input) , results= []


"""

def command(command_list):
    lenght = len(command_list)

    results = []

    for command in command_list:
        if command['type'] == "VALUE":
            if isinstance(command['loc1'], str):
                if results[int(command['loc1'][1])]:
                    results.append(results[int(command['loc1'][1])])
                else:
                    results.append(None)
            else:
                results.append(command['loc1'])
        if command['type'] == "ADD":
            if isinstance(command['loc1'], str):
                if results[int(command['type'][1])]:
                    results.append(results[int(command['type'][1])])
                else:
                    results.append(None)