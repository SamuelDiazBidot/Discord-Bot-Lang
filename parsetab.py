
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BINARY_OPERATOR BOOLEAN CATCH COMMAND ELSE FLOAT FN GLOBAL ID IF INTEGER RET SIGN STRING TOKEN TRY UNITARY_OPERATOR\n    run : program\n    \n    program : program function\n            | program function_call\n            | program python_function_call\n            | program variable\n            | program token\n            | function\n            | function_call\n            | python_function_call\n            | variable\n            | token\n    \n    function : FN id '(' parameter ')' '{' body '}'\n             | COMMAND id '(' parameter ')' '{' body '}'\n    \n    token : TOKEN '(' string ')'\n    \n    function_call : id '(' term_list ')' \n    \n    python_function_call : '.' id '(' term_list ')'\n    \n    parameter : id ',' parameter\n              | id\n              | empty\n    \n    body : body exp\n         | body variable\n         | body return\n         | body global\n         | body function_call\n         | body python_function_call\n         | function_call\n         | python_function_call\n         | exp\n         | variable\n         | return\n         | global\n    \n    exp : term binop exp\n        | term\n        | IF exp '{' body '}' ELSE '{' body '}'\n        | IF exp '{' body '}'\n        | TRY '{' body '}' CATCH '{' body '}'\n    \n    variable : id '=' exp \n    \n    return : RET id\n    \n    global : GLOBAL term_list\n    \n    term_map : term ':' term ',' term_map\n             | term ':' term\n    \n    term_list : term_list ',' term\n              | term\n    \n    term : unop term\n         | number\n         | boolean\n         | string\n         | function_call\n         | id\n         | list\n         | dict\n         | empty\n    \n    unop : SIGN\n         | UNITARY_OPERATOR\n    \n    binop : SIGN\n          | BINARY_OPERATOR\n    \n    dict : '{' term_map '}'\n         | '{' empty '}'\n    \n    list : '[' term_list ']'\n    \n    number : FLOAT\n           | INTEGER\n    \n    boolean : BOOLEAN\n    \n    string : STRING\n    \n    id : ID\n    \n    empty :\n    "
    
_lr_action_items = {'FN':([0,2,3,4,5,6,7,13,14,15,16,17,18,21,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,57,62,63,64,69,73,74,75,77,90,108,111,115,119,120,],[8,8,-7,-8,-9,-10,-11,-64,-2,-3,-4,-5,-6,-65,-49,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-44,-65,-55,-56,-14,-59,-57,-58,-32,-16,-35,-12,-13,-36,-34,]),'COMMAND':([0,2,3,4,5,6,7,13,14,15,16,17,18,21,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,57,62,63,64,69,73,74,75,77,90,108,111,115,119,120,],[10,10,-7,-8,-9,-10,-11,-64,-2,-3,-4,-5,-6,-65,-49,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-44,-65,-55,-56,-14,-59,-57,-58,-32,-16,-35,-12,-13,-36,-34,]),'.':([0,2,3,4,5,6,7,13,14,15,16,17,18,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,56,57,62,63,64,66,69,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,111,114,115,116,117,118,119,120,],[11,11,-7,-8,-9,-10,-11,-64,-2,-3,-4,-5,-6,-65,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-65,-44,-65,-55,-56,11,-14,-42,-59,-57,-58,-32,11,11,-28,-29,-30,-31,-26,-27,-49,-65,-16,11,11,-20,-21,-22,-23,-24,-25,-49,-38,-39,11,11,-35,11,-12,11,-13,11,11,11,-36,-34,]),'TOKEN':([0,2,3,4,5,6,7,13,14,15,16,17,18,21,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,57,62,63,64,69,73,74,75,77,90,108,111,115,119,120,],[12,12,-7,-8,-9,-10,-11,-64,-2,-3,-4,-5,-6,-65,-49,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-44,-65,-55,-56,-14,-59,-57,-58,-32,-16,-35,-12,-13,-36,-34,]),'ID':([0,2,3,4,5,6,7,8,10,11,13,14,15,16,17,18,20,21,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,55,56,57,62,63,64,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,114,115,116,117,118,119,120,],[13,13,-7,-8,-9,-10,-11,13,13,13,-64,-2,-3,-4,-5,-6,13,13,13,-49,-43,13,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,13,13,-37,-33,13,13,13,-15,13,-44,13,-55,-56,13,-14,13,-42,-59,-57,-58,13,-32,13,13,-28,-29,-30,-31,-26,-27,-49,13,13,-16,13,13,-20,-21,-22,-23,-24,-25,-49,-38,-39,13,13,13,-35,13,-12,13,-13,13,13,13,-36,-34,]),'$end':([1,2,3,4,5,6,7,13,14,15,16,17,18,21,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,57,62,63,64,69,73,74,75,77,90,108,111,115,119,120,],[0,-1,-7,-8,-9,-10,-11,-64,-2,-3,-4,-5,-6,-65,-49,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-44,-65,-55,-56,-14,-59,-57,-58,-32,-16,-35,-12,-13,-36,-34,]),'(':([9,12,13,19,22,23,26,86,102,],[20,24,-64,25,49,50,20,20,20,]),'=':([9,13,86,102,],[21,-64,21,21,]),')':([13,20,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,49,50,51,52,53,54,55,56,57,67,68,70,72,73,74,75,91,],[-64,-65,-65,-49,55,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-65,-65,69,-18,71,-19,-15,-65,-44,89,90,-65,-42,-59,-57,-58,-17,]),',':([13,20,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,50,52,55,56,57,58,68,72,73,74,75,76,88,93,104,],[-64,-65,-49,56,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-65,-65,70,-15,-65,-44,56,56,-42,-59,-57,-58,-65,-65,107,56,]),'SIGN':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,37,37,-49,-43,37,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,37,37,-37,63,37,37,-15,37,-44,37,-55,-56,37,-42,-59,-57,-58,37,-32,37,37,-28,-29,-30,-31,-26,-27,-49,37,-16,37,37,-20,-21,-22,-23,-24,-25,-49,-38,-39,37,37,37,-35,37,37,37,37,37,-36,-34,]),'BINARY_OPERATOR':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,55,56,57,62,63,64,66,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,114,116,117,118,119,120,],[-64,-65,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,64,-65,-15,-65,-44,-65,-55,-56,-65,-42,-59,-57,-58,-32,-65,-65,-28,-29,-30,-31,-26,-27,-49,-65,-16,-65,-65,-20,-21,-22,-23,-24,-25,-49,-38,-39,-65,-65,-35,-65,-65,-65,-65,-65,-36,-34,]),'}':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,55,56,57,59,60,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,93,94,96,97,98,99,100,101,102,103,104,105,106,108,110,112,114,116,117,118,119,120,],[-64,-65,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-65,-37,-33,-15,-65,-44,74,75,-65,-55,-56,-65,-42,-59,-57,-58,-65,-32,-65,95,-28,-29,-30,-31,-26,-27,-49,-65,-16,-65,-41,108,-20,-21,-22,-23,-24,-25,-49,-38,-39,-65,111,-35,115,-40,-65,-65,119,120,-36,-34,]),'IF':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,55,56,57,62,63,64,66,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,114,116,117,118,119,120,],[-64,47,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,47,-15,-65,-44,47,-55,-56,47,-42,-59,-57,-58,-32,47,47,-28,-29,-30,-31,-26,-27,-49,-65,-16,47,47,-20,-21,-22,-23,-24,-25,-49,-38,-39,47,47,-35,47,47,47,47,47,-36,-34,]),'TRY':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,55,56,57,62,63,64,66,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,114,116,117,118,119,120,],[-64,48,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,48,-15,-65,-44,48,-55,-56,48,-42,-59,-57,-58,-32,48,48,-28,-29,-30,-31,-26,-27,-49,-65,-16,48,48,-20,-21,-22,-23,-24,-25,-49,-38,-39,48,48,-35,48,48,48,48,48,-36,-34,]),'RET':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,56,57,62,63,64,66,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,114,116,117,118,119,120,],[-64,-65,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-65,-44,-65,-55,-56,87,-42,-59,-57,-58,-32,87,87,-28,-29,-30,-31,-26,-27,-49,-65,-16,87,87,-20,-21,-22,-23,-24,-25,-49,-38,-39,87,87,-35,87,87,87,87,87,-36,-34,]),'GLOBAL':([13,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,55,56,57,62,63,64,66,72,73,74,75,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,108,110,114,116,117,118,119,120,],[-64,-65,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-37,-33,-15,-65,-44,-65,-55,-56,88,-42,-59,-57,-58,-32,88,88,-28,-29,-30,-31,-26,-27,-49,-65,-16,88,88,-20,-21,-22,-23,-24,-25,-49,-38,-39,88,88,-35,88,88,88,88,88,-36,-34,]),'UNITARY_OPERATOR':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,38,38,-49,-43,38,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,38,38,-37,-33,38,38,-15,38,-44,38,-55,-56,38,-42,-59,-57,-58,38,-32,38,38,-28,-29,-30,-31,-26,-27,-49,38,-16,38,38,-20,-21,-22,-23,-24,-25,-49,-38,-39,38,38,38,-35,38,38,38,38,38,-36,-34,]),'FLOAT':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,39,39,-49,-43,39,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,39,39,-37,-33,39,39,-15,39,-44,39,-55,-56,39,-42,-59,-57,-58,39,-32,39,39,-28,-29,-30,-31,-26,-27,-49,39,-16,39,39,-20,-21,-22,-23,-24,-25,-49,-38,-39,39,39,39,-35,39,39,39,39,39,-36,-34,]),'INTEGER':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,40,40,-49,-43,40,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,40,40,-37,-33,40,40,-15,40,-44,40,-55,-56,40,-42,-59,-57,-58,40,-32,40,40,-28,-29,-30,-31,-26,-27,-49,40,-16,40,40,-20,-21,-22,-23,-24,-25,-49,-38,-39,40,40,40,-35,40,40,40,40,40,-36,-34,]),'BOOLEAN':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,41,41,-49,-43,41,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,41,41,-37,-33,41,41,-15,41,-44,41,-55,-56,41,-42,-59,-57,-58,41,-32,41,41,-28,-29,-30,-31,-26,-27,-49,41,-16,41,41,-20,-21,-22,-23,-24,-25,-49,-38,-39,41,41,41,-35,41,41,41,41,41,-36,-34,]),'STRING':([13,20,21,24,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,42,42,42,-49,-43,42,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,42,42,-37,-33,42,42,-15,42,-44,42,-55,-56,42,-42,-59,-57,-58,42,-32,42,42,-28,-29,-30,-31,-26,-27,-49,42,-16,42,42,-20,-21,-22,-23,-24,-25,-49,-38,-39,42,42,42,-35,42,42,42,42,42,-36,-34,]),'[':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,55,56,57,62,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,117,118,119,120,],[-64,43,43,-49,-43,43,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,43,43,-37,-33,43,43,-15,43,-44,43,-55,-56,43,-42,-59,-57,-58,43,-32,43,43,-28,-29,-30,-31,-26,-27,-49,43,-16,43,43,-20,-21,-22,-23,-24,-25,-49,-38,-39,43,43,43,-35,43,43,43,43,43,-36,-34,]),'{':([13,20,21,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,55,56,57,62,63,64,65,66,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,92,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,114,116,117,118,119,120,],[-64,44,44,-49,-43,44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,44,44,-37,-33,44,66,44,-15,44,-44,44,-55,-56,78,44,92,-42,-59,-57,-58,44,-32,44,44,-28,-29,-30,-31,-26,-27,-49,44,105,-16,44,44,-20,-21,-22,-23,-24,-25,-49,-38,-39,44,44,44,-35,114,44,116,44,44,44,44,-36,-34,]),']':([13,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,55,56,57,58,72,73,74,75,],[-64,-49,-43,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-65,-15,-65,-44,73,-42,-59,-57,-58,]),':':([13,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,55,57,60,61,73,74,75,107,],[-64,-49,-65,-45,-46,-47,-48,-50,-51,-52,-53,-54,-60,-61,-62,-63,-65,-15,-44,-52,76,-59,-57,-58,-65,]),'CATCH':([95,],[109,]),'ELSE':([108,],[113,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'run':([0,],[1,]),'program':([0,],[2,]),'function':([0,2,],[3,14,]),'function_call':([0,2,20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[4,15,33,33,33,33,33,33,33,33,33,84,33,84,100,33,84,100,84,100,33,100,84,84,100,100,]),'python_function_call':([0,2,66,78,79,92,94,105,106,110,114,116,117,118,],[5,16,85,85,101,85,101,85,101,101,85,85,101,101,]),'variable':([0,2,66,78,79,92,94,105,106,110,114,116,117,118,],[6,17,81,81,97,81,97,81,97,97,81,81,97,97,]),'token':([0,2,],[7,18,]),'id':([0,2,8,10,11,20,21,25,29,43,44,47,49,50,56,62,66,70,76,78,79,87,88,92,94,105,106,107,110,114,116,117,118,],[9,9,19,22,23,26,26,52,26,26,26,26,52,26,26,26,86,52,26,86,102,103,26,86,102,86,102,26,102,86,86,102,102,]),'term_list':([20,43,50,88,],[27,58,68,104,]),'term':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[28,46,57,28,61,46,28,72,46,46,93,46,46,28,46,46,46,46,61,46,46,46,46,46,]),'unop':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'number':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'boolean':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'string':([20,21,24,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[32,32,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'list':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'dict':([20,21,29,43,44,47,50,56,62,66,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'empty':([20,21,25,29,43,44,47,49,50,56,62,66,70,76,78,79,88,92,94,105,106,107,110,114,116,117,118,],[36,36,54,36,36,60,36,54,36,36,36,36,54,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'exp':([21,47,62,66,78,79,92,94,105,106,110,114,116,117,118,],[45,65,77,80,80,96,80,96,80,96,96,80,80,96,96,]),'parameter':([25,49,70,],[53,67,91,]),'term_map':([44,107,],[59,112,]),'binop':([46,],[62,]),'body':([66,78,92,105,114,116,],[79,94,106,110,117,118,]),'return':([66,78,79,92,94,105,106,110,114,116,117,118,],[82,82,98,82,98,82,98,98,82,82,98,98,]),'global':([66,78,79,92,94,105,106,110,114,116,117,118,],[83,83,99,83,99,83,99,99,83,83,99,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> run","S'",1,None,None,None),
  ('run -> program','run',1,'p_run','lexerParser.py',80),
  ('program -> program function','program',2,'p_program','lexerParser.py',88),
  ('program -> program function_call','program',2,'p_program','lexerParser.py',89),
  ('program -> program python_function_call','program',2,'p_program','lexerParser.py',90),
  ('program -> program variable','program',2,'p_program','lexerParser.py',91),
  ('program -> program token','program',2,'p_program','lexerParser.py',92),
  ('program -> function','program',1,'p_program','lexerParser.py',93),
  ('program -> function_call','program',1,'p_program','lexerParser.py',94),
  ('program -> python_function_call','program',1,'p_program','lexerParser.py',95),
  ('program -> variable','program',1,'p_program','lexerParser.py',96),
  ('program -> token','program',1,'p_program','lexerParser.py',97),
  ('function -> FN id ( parameter ) { body }','function',8,'p_function','lexerParser.py',106),
  ('function -> COMMAND id ( parameter ) { body }','function',8,'p_function','lexerParser.py',107),
  ('token -> TOKEN ( string )','token',4,'p_token','lexerParser.py',113),
  ('function_call -> id ( term_list )','function_call',4,'p_function_call','lexerParser.py',119),
  ('python_function_call -> . id ( term_list )','python_function_call',5,'p_python_function_call','lexerParser.py',125),
  ('parameter -> id , parameter','parameter',3,'p_parameter','lexerParser.py',131),
  ('parameter -> id','parameter',1,'p_parameter','lexerParser.py',132),
  ('parameter -> empty','parameter',1,'p_parameter','lexerParser.py',133),
  ('body -> body exp','body',2,'p_body','lexerParser.py',142),
  ('body -> body variable','body',2,'p_body','lexerParser.py',143),
  ('body -> body return','body',2,'p_body','lexerParser.py',144),
  ('body -> body global','body',2,'p_body','lexerParser.py',145),
  ('body -> body function_call','body',2,'p_body','lexerParser.py',146),
  ('body -> body python_function_call','body',2,'p_body','lexerParser.py',147),
  ('body -> function_call','body',1,'p_body','lexerParser.py',148),
  ('body -> python_function_call','body',1,'p_body','lexerParser.py',149),
  ('body -> exp','body',1,'p_body','lexerParser.py',150),
  ('body -> variable','body',1,'p_body','lexerParser.py',151),
  ('body -> return','body',1,'p_body','lexerParser.py',152),
  ('body -> global','body',1,'p_body','lexerParser.py',153),
  ('exp -> term binop exp','exp',3,'p_exp','lexerParser.py',162),
  ('exp -> term','exp',1,'p_exp','lexerParser.py',163),
  ('exp -> IF exp { body } ELSE { body }','exp',9,'p_exp','lexerParser.py',164),
  ('exp -> IF exp { body }','exp',5,'p_exp','lexerParser.py',165),
  ('exp -> TRY { body } CATCH { body }','exp',8,'p_exp','lexerParser.py',166),
  ('variable -> id = exp','variable',3,'p_variable','lexerParser.py',181),
  ('return -> RET id','return',2,'p_return','lexerParser.py',187),
  ('global -> GLOBAL term_list','global',2,'p_global','lexerParser.py',193),
  ('term_map -> term : term , term_map','term_map',5,'p_term_map','lexerParser.py',199),
  ('term_map -> term : term','term_map',3,'p_term_map','lexerParser.py',200),
  ('term_list -> term_list , term','term_list',3,'p_term_list','lexerParser.py',209),
  ('term_list -> term','term_list',1,'p_term_list','lexerParser.py',210),
  ('term -> unop term','term',2,'p_term','lexerParser.py',219),
  ('term -> number','term',1,'p_term','lexerParser.py',220),
  ('term -> boolean','term',1,'p_term','lexerParser.py',221),
  ('term -> string','term',1,'p_term','lexerParser.py',222),
  ('term -> function_call','term',1,'p_term','lexerParser.py',223),
  ('term -> id','term',1,'p_term','lexerParser.py',224),
  ('term -> list','term',1,'p_term','lexerParser.py',225),
  ('term -> dict','term',1,'p_term','lexerParser.py',226),
  ('term -> empty','term',1,'p_term','lexerParser.py',227),
  ('unop -> SIGN','unop',1,'p_unop','lexerParser.py',236),
  ('unop -> UNITARY_OPERATOR','unop',1,'p_unop','lexerParser.py',237),
  ('binop -> SIGN','binop',1,'p_binop','lexerParser.py',243),
  ('binop -> BINARY_OPERATOR','binop',1,'p_binop','lexerParser.py',244),
  ('dict -> { term_map }','dict',3,'p_dict','lexerParser.py',250),
  ('dict -> { empty }','dict',3,'p_dict','lexerParser.py',251),
  ('list -> [ term_list ]','list',3,'p_list','lexerParser.py',257),
  ('number -> FLOAT','number',1,'p_number','lexerParser.py',263),
  ('number -> INTEGER','number',1,'p_number','lexerParser.py',264),
  ('boolean -> BOOLEAN','boolean',1,'p_boolean','lexerParser.py',270),
  ('string -> STRING','string',1,'p_string','lexerParser.py',276),
  ('id -> ID','id',1,'p_id','lexerParser.py',282),
  ('empty -> <empty>','empty',0,'p_empty','lexerParser.py',288),
]
