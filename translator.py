import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt
from library import *

# ---------- Graph variables --------------------------
parseGraph = None
draw = True
fileImport = True
NODE_COUNTER = 0

#---------- Description -------------------------------
# This program is a simple lexer that can handle
# basic arithmetic operations and variable assignment.
# It also has a symbol table to store the values of
# the variables.

#---------- List of tokens ----------------------------

tokens =(
    'NUMBER',
    "VARIABLE",
    "SETTO",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EXP",
    "LPAREN",
    "RPAREN",
    "COMMA",
    "STRING",
    "CONNECT"


)

#---------- Regular expressions -----------------------

t_PLUS = r'\+'
t_SETTO = r'='
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'\->'

#---------- Symbol table ------------------------------
symbol_table = dict()

# ---------- Predefined functions ----------------------
def printP():
    print("Hello, World!")

def printP2(num):
    print("Hello, World! " + str(num))

#---------- node functions -----------------------------
def add_node(attr):
    global parseGraph
    global NODE_COUNTER
    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1

    return parseGraph.nodes[NODE_COUNTER - 1]
    

#---------- Dictionary of reserved words --------------
symbol_table["pi"] = 3.14159265359 # Predefined values
symbol_table["e"] = 2.71828182846 # Predefined values
symbol_table["phi"] = 1.61803398875 # Predefined values
symbol_table["tau"] = 6.28318530718 # Predefined values
symbol_table["gamma"] = 0.5772156649 # Predefined values
symbol_table["inf"] = float('inf') # Predefined values
symbol_table["nan"] = float('nan') # Predefined values
symbol_table["true"] = 1 # Predefined values
symbol_table["false"] = 0 # Predefined values
symbol_table["print"] = print # Predefined values
symbol_table["printP"] = printP # Predefined values
symbol_table["printP2"] = printP2 # Predefined values
symbol_table["exit"] = "exit" # Predefined values
symbol_table["symbols"] = "symbols" # Predefined values
symbol_table["max"] = max              # Predefined values

symbol_table["load_image"] = load_image # Predefined values
symbol_table["save_image"] = save_image # Predefined values
symbol_table["show_image"] = show_image # Predefined values
symbol_table["gen_matrix"] = gen_matrix # Predefined values
symbol_table["gen_vector"] = gen_vector # Predefined values
symbol_table["my_mean"] = my_mean # Predefined values
symbol_table["my_sum"] = my_sum # Predefined values
symbol_table["my_median"] = my_median # Predefined values
symbol_table["my_std"] = my_std # Predefined values
symbol_table["my_max"] = my_max # Predefined values
symbol_table["my_min"] = my_min # Predefined values
symbol_table["my_sin"] = my_sin # Predefined values
symbol_table["my_cos"] = my_cos # Predefined values
symbol_table["my_tan"] = my_tan # Predefined values
symbol_table["histogram"] = histogram # Predefined values
symbol_table["canny_edge"] = canny_edge # Predefined values
symbol_table["gray_scale"] = gray_scale # Predefined values

#---------- Ignored characters ------------------------



#---------- Regular expressions as functions ----------

def t_NUMBER(t):
    r'\d+\.?\d*'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t




def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t
#---------- Boilerplate code --------------------------

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Error")
    t.lexer.skip(1)

#---------- Building the lexer -----------------------------
    
lexer = lex.lex()

#---------- Parsing rules ----------------------------------
def p_assignment_assign(p):
    '''
    assignment : VARIABLE SETTO expression
    '''
    node = add_node({"type":"ASSIGN", "label":"=", "value":""})
    node_variable = add_node({"type":"VARIABLE_ASSIGN", "label":f"VAR_{p[1]}", "value":p[1]})
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

# ---------- Assignment flow -----------------------------

def p_assignment_flow(p):
    '''
    assignment : VARIABLE SETTO flow
    '''
    node = add_node({"type":"ASSIGN", "label":"=", "value":""})
    node_variable = add_node({"type":"VARIABLE_ASSIGN", "label":f"VAR_{p[1]}", "value":p[1]})
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_flow_form(p):
    '''
    flow : VARIABLE CONNECT flow_functions
    '''
    ff = p[3][0]
    connections = parseGraph.neighbors(ff["counter"])
    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            c["type"] = "VARIABLE"
            c["label"] = f"VAR_{p[1]}"
            c["value"] = p[1]
            break
    p[0] = p[3][-1]

def p_flow_functions(p):
    '''
    flow_functions : flow_function_call CONNECT flow_functions
    '''
    connections = parseGraph.neighbors(p[3][0]["counter"])

    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            parseGraph.add_edge(c["counter"], p[1]["counter"])
            break
    p[0] = [p[1]] + p[3]

def p_flow_function_single(p):
    '''
    flow_functions : flow_function_call
    '''
    p[0] = [p[1]]


def p_flow_function_call(p):
    '''
    flow_function_call : VARIABLE LPAREN params RPAREN
    '''
    node = add_node({"type":"FLOW_FUNCTION_CALL", "label":f"ff_{p[1]}", "value":p[1]})
    pending_node = add_node({"type":"PENDING_NODE", "label":"PENDING", "value":""})
    parseGraph.add_edge(node["counter"], pending_node["counter"])

    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    
    p[0] = node
    


#---------- Assignment expression -------------------------
def p_assignment_expression(p):
    ''' 
    assignment : expression
    '''
    
    p[0] = p[1]
    

#---------- Expression PLUS ------------------------------------
def p_expression_plus(p):
    """
    expression : expression PLUS term
    """

    node = add_node({"type":"PLUS", "label":"+", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

#---------- Expression MINUS -----------------------------------
def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    node = add_node({"type":"MINUS", "label":"-", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

#---------- Expression Term -------------------------------------
def p_expression_term(p):
    """
    expression : term 
            | string
    """
    p[0] = p[1]

def p_string(p):
    '''
    string : STRING
    '''
    p[0] = add_node({"type":"STRING", "label":f"STR_{p[1]}", "value":p[1]})

#---------- Term Times ------------------------------------------
def p_term_times(p):
    '''
    term : term TIMES exponent
    '''
    node = add_node({"type":"TIMES", "label":"*", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

#---------- Term Divide ------------------------------------------
def p_term_divide(p):
    '''
    term : term DIVIDE exponent
    '''
    node = add_node({"type":"DIVIDE", "label":"/", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

def p_term_exponent(p):
    '''
    term : exponent
    '''
    p[0] = p[1]

#---------- Exponent Exponent ---------------------------
def p_exponent_exp(p):
    '''
    exponent : factor EXP factor
    '''
    node = add_node({"type":"POWER", "label":"POW", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

#---------- Exponent Factor -----------------------------
def p_exponent_factor(p):
    '''
    exponent : factor
    '''
    p[0] = p[1]

#---------- Parentheses ---------------------------------
def p_exponent_parent(p):
    '''
    exponent : LPAREN expression RPAREN
    '''
    node = add_node({"type":"GROUP", "label":"{}", "value":""})
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

#---------- Factor --------------------------------------
def p_factor_num(p):
    ''' 
    factor : NUMBER
    '''
    p[0] = add_node({"type":"NUMBER", "label":f"NUM_{p[1]}", "value":p[1]})


#---------- Variable assignment -------------------------
def p_factor_id(p):
    ''' 
    factor : VARIABLE
    '''
    p[0] = add_node({"type":"VARIABLE", "label":f"VAR_{p[1]}", "value":p[1]})
    

#---------- Function call ------------------------------
def p_factor_function_call(p):
    '''
    factor : function_call
    '''
    p[0] = p[1]


def p_function_call_no_params(p):
    '''
    function_call : VARIABLE LPAREN RPAREN
    '''
    p[0] = add_node({"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]})


def p_function_call_params(p):
    '''
    function_call : VARIABLE LPAREN params RPAREN
    '''
    print(p[3])
    node = add_node({"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]})
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_params(p):
    '''
    params : params COMMA expression
        | expression
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

#---------- parse tree ---------------------------------
def execute_parse_tree(tree):
    root = tree.nodes[0]
    root_id = 0
    res = visit_node(tree, root_id, -1)
    if(type(res)== int or type(res) == float):
        print(f"Result: {res}")

# ---------- Visit node function -------------------------

def visit_node(tree, node_id, from_id):
    children = tree.neighbors(node_id)
    res= []
    for c in children:
        if(c != from_id):
            res.append(visit_node(tree, c, node_id))



    current_node = tree.nodes[node_id]
    print( f"From Node {node_id}", res)

    if current_node["type"] == "ROOT":
        return res[0]
    
    if current_node["type"] == "ASSIGN":
        symbol_table[res[0]] = res[1]
        return res[1]
    
    if current_node["type"] == "NUMBER":
        return current_node["value"]
    
    if current_node["type"] == "STRING":
        return current_node["value"]

    if current_node["type"] == "VARIABLE_ASSIGN":
        return current_node["value"]
    
    if current_node["type"] == "PLUS":
        return res[0] + res[1]
    
    if current_node["type"] == "VARIABLE":
        return symbol_table[current_node["value"]]
    
    if current_node["type"] == "MINUS":
        return res[0] - res[1]
    
    if current_node["type"] == "TIMES":
        return res[0] * res[1]
    
    if current_node["type"] == "DIVIDE":
        return res[0] / res[1]
    
    if current_node["type"] == "POWER":
        return pow(res[0], res[1])
    
    if current_node["type"] == "GROUP":
        return res[0]
    
    if current_node["type"] == "PENDING_NODE":
        return res[0]
    
    if current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "FLOW_FUNCTION_CALL":
        v = current_node["value"]
        print("**** HERE Function call: ", v, " ****")
        if v in symbol_table:
            fn = symbol_table[v]
            if callable(fn):
                try:
                    res = fn(*res)
                    return res
                except Exception as e:
                    print("Error in function call", e)
                    return "Error"
                
            else:
                print(f"Error function {v}, IS NOT of type function")
                return "Error"
        else:
            fn = search_cv2(v)
            if fn is not None:
                try :
                    res = fn(*res)
                    return res
                
                except Exception as e:
                    print("HERE *** Error in function call", e, v," FN: " ,fn," RES: ", res)
                    return "Error"
                else:
                    print("Error function", v, "not found")
                    return "Error"
            else:
                print("Error function", v, "not found")
                return "Error"
#---------- Error handling ------------------------------
def p_error(p):
    print("Syntax error on input ", p)


#---------- Building the parser ------------------------

parser = yacc.yacc()

# ---------- Reading the file --------------------------

# IMPORTANT NOTICE: TO TEST A FILE IMPORT SET THE VARIABLE fileImport TO TRUE

# The text file is a file with a list of commands, each command is separated by a new line
if fileImport: # If the file import variable is set to True
    with open("test.txt", "r") as f: # Open the file
        lines = f.readlines() # Read the lines of the file

    for line in lines: # Iterate over each command of the file
        NODE_COUNTER = 0 # Reset the node counter
        parseGraph = nx.Graph() # Reset the graph
        root = add_node({"type":"ROOT", "label":"ROOT"}) # Add the root node
        result = parser.parse(line) # Parse the line
        parseGraph.add_edge(root["counter"], result["counter"]) # Add the edge between the root and the result
        labels = nx.get_node_attributes(parseGraph, 'label') # Get the labels of the nodes
        if (draw): # Draw the graph if it is set to True
            nx.draw(parseGraph,labels=labels, with_labels=True, font_weight='bold') # Draw the graph
            plt.show() # Show the plot

        execute_parse_tree(parseGraph) # Execute the parse tree

#---------- Testing the lexer -------------------------

while True:
    try:
        data = input("input>> ")
        if(data == "exit"):
            break
        if(data == "symbols"):
            print(symbol_table)
            continue

        
    except EOFError:
        break
    
    if not data: continue
    NODE_COUNTER = 0
    parseGraph = nx.Graph()
    root = add_node({"type":"ROOT", "label":"ROOT"})
    result = parser.parse(data)
    parseGraph.add_edge(root["counter"], result["counter"])
    labels = nx.get_node_attributes(parseGraph, 'label')
    if (draw):
        nx.draw(parseGraph,labels=labels, with_labels=True, font_weight='bold')
        plt.show()

    execute_parse_tree(parseGraph)


print("Finished, accepted input.")
