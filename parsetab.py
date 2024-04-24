
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA CONNECT DIVIDE EXP LPAREN MINUS NUMBER PLUS RPAREN SETTO STRING TIMES VARIABLE\n    assignment : VARIABLE SETTO expression\n    \n    assignment : VARIABLE SETTO flow\n    \n    flow : VARIABLE CONNECT flow_functions\n    \n    flow_functions : flow_function_call CONNECT flow_functions\n    \n    flow_functions : flow_function_call\n    \n    flow_function_call : VARIABLE LPAREN params RPAREN\n     \n    assignment : expression\n    \n    expression : expression PLUS term\n    \n    expression : expression MINUS term\n    \n    expression : term \n            | string\n    \n    string : STRING\n    \n    term : term TIMES exponent\n    \n    term : term DIVIDE exponent\n    \n    term : exponent\n    \n    exponent : factor EXP factor\n    \n    exponent : factor\n    \n    exponent : LPAREN expression RPAREN\n     \n    factor : NUMBER\n     \n    factor : VARIABLE\n    \n    factor : function_call\n    \n    function_call : VARIABLE LPAREN RPAREN\n    \n    function_call : VARIABLE LPAREN params RPAREN\n    \n    params : params COMMA expression\n        | expression\n    '
    
_lr_action_items = {'VARIABLE':([0,9,12,13,14,15,16,17,18,33,35,40,41,],[2,20,21,20,20,20,20,20,20,36,20,20,36,]),'STRING':([0,9,12,13,35,40,],[7,7,7,7,7,7,]),'LPAREN':([0,2,9,12,13,14,15,16,17,20,21,35,36,40,],[9,13,9,9,9,9,9,9,9,13,13,9,40,9,]),'NUMBER':([0,9,12,13,14,15,16,17,18,35,40,],[10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,5,6,7,8,10,11,20,21,22,23,24,27,28,29,30,31,32,34,37,38,43,44,],[0,-20,-7,-10,-11,-15,-12,-17,-19,-21,-20,-20,-1,-2,-22,-8,-9,-13,-14,-16,-18,-23,-3,-5,-4,-6,]),'SETTO':([2,],[12,]),'EXP':([2,8,10,11,20,21,24,34,],[-20,18,-19,-21,-20,-20,-22,-23,]),'TIMES':([2,4,6,8,10,11,20,21,24,27,28,29,30,31,32,34,],[-20,16,-15,-17,-19,-21,-20,-20,-22,16,16,-13,-14,-16,-18,-23,]),'DIVIDE':([2,4,6,8,10,11,20,21,24,27,28,29,30,31,32,34,],[-20,17,-15,-17,-19,-21,-20,-20,-22,17,17,-13,-14,-16,-18,-23,]),'PLUS':([2,3,4,5,6,7,8,10,11,19,20,21,22,24,26,27,28,29,30,31,32,34,39,],[-20,14,-10,-11,-15,-12,-17,-19,-21,14,-20,-20,14,-22,14,-8,-9,-13,-14,-16,-18,-23,14,]),'MINUS':([2,3,4,5,6,7,8,10,11,19,20,21,22,24,26,27,28,29,30,31,32,34,39,],[-20,15,-10,-11,-15,-12,-17,-19,-21,15,-20,-20,15,-22,15,-8,-9,-13,-14,-16,-18,-23,15,]),'RPAREN':([4,5,6,7,8,10,11,13,19,20,24,25,26,27,28,29,30,31,32,34,39,42,],[-10,-11,-15,-12,-17,-19,-21,24,32,-20,-22,34,-25,-8,-9,-13,-14,-16,-18,-23,-24,44,]),'COMMA':([4,5,6,7,8,10,11,20,24,25,26,27,28,29,30,31,32,34,39,42,],[-10,-11,-15,-12,-17,-19,-21,-20,-22,35,-25,-8,-9,-13,-14,-16,-18,-23,-24,35,]),'CONNECT':([21,38,44,],[33,41,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([0,9,12,13,35,40,],[3,19,22,26,39,26,]),'term':([0,9,12,13,14,15,35,40,],[4,4,4,4,27,28,4,4,]),'string':([0,9,12,13,35,40,],[5,5,5,5,5,5,]),'exponent':([0,9,12,13,14,15,16,17,35,40,],[6,6,6,6,6,6,29,30,6,6,]),'factor':([0,9,12,13,14,15,16,17,18,35,40,],[8,8,8,8,8,8,8,8,31,8,8,]),'function_call':([0,9,12,13,14,15,16,17,18,35,40,],[11,11,11,11,11,11,11,11,11,11,11,]),'flow':([12,],[23,]),'params':([13,40,],[25,42,]),'flow_functions':([33,41,],[37,43,]),'flow_function_call':([33,41,],[38,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> VARIABLE SETTO expression','assignment',3,'p_assignment_assign','translator.py',144),
  ('assignment -> VARIABLE SETTO flow','assignment',3,'p_assignment_flow','translator.py',156),
  ('flow -> VARIABLE CONNECT flow_functions','flow',3,'p_flow_form','translator.py',166),
  ('flow_functions -> flow_function_call CONNECT flow_functions','flow_functions',3,'p_flow_functions','translator.py',181),
  ('flow_functions -> flow_function_call','flow_functions',1,'p_flow_function_single','translator.py',194),
  ('flow_function_call -> VARIABLE LPAREN params RPAREN','flow_function_call',4,'p_flow_function_call','translator.py',201),
  ('assignment -> expression','assignment',1,'p_assignment_expression','translator.py',217),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','translator.py',226),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','translator.py',237),
  ('expression -> term','expression',1,'p_expression_term','translator.py',247),
  ('expression -> string','expression',1,'p_expression_term','translator.py',248),
  ('string -> STRING','string',1,'p_string','translator.py',254),
  ('term -> term TIMES exponent','term',3,'p_term_times','translator.py',261),
  ('term -> term DIVIDE exponent','term',3,'p_term_divide','translator.py',272),
  ('term -> exponent','term',1,'p_term_exponent','translator.py',282),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_exp','translator.py',289),
  ('exponent -> factor','exponent',1,'p_exponent_factor','translator.py',300),
  ('exponent -> LPAREN expression RPAREN','exponent',3,'p_exponent_parent','translator.py',307),
  ('factor -> NUMBER','factor',1,'p_factor_num','translator.py',316),
  ('factor -> VARIABLE','factor',1,'p_factor_id','translator.py',324),
  ('factor -> function_call','factor',1,'p_factor_function_call','translator.py',332),
  ('function_call -> VARIABLE LPAREN RPAREN','function_call',3,'p_function_call_no_params','translator.py',339),
  ('function_call -> VARIABLE LPAREN params RPAREN','function_call',4,'p_function_call_params','translator.py',346),
  ('params -> params COMMA expression','params',3,'p_params','translator.py',356),
  ('params -> expression','params',1,'p_params','translator.py',357),
]
