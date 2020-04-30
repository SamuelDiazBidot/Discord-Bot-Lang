import sys

tab_count = 0
function_type = ''
token = ''
token_flag = False

def tabs():
    result = ''
    for _ in range(0, tab_count):
        result = result + '\t'
    return result

def run(p):
    global tab_count, function_type, token, token_flag

    if p[0] == 'program':
        return run(p[1]) + '\n' + run(p[2])
    elif p[0] == 'variable':
        var = run(p[1])
        return var + ' = ' + run(p[2])
    elif p[0] == 'binop_exp':
        return run(p[2]) + p[1] + run(p[3])
    elif p[0] == 'if_exp':
        if len(p) > 3:
            original_tab = tabs()
            tab_count += 1
            a = 'if ' + run(p[1]) + ':\n' + tabs() + run(p[2]) + '\n' + original_tab + 'else:\n' + tabs() + run(p[3])
            tab_count -= 1
            return a
        else:
            tab_count += 1
            a = 'if ' + run(p[1]) + ':\n' + tabs() + run(p[2])
            tab_count -= 1
            return a
    elif p[0] == 'try_exp':
        original_tab = tabs()
        tab_count += 1
        a = 'try:\n' + tabs() + run(p[1]) +'\n' + original_tab + "except:\n" + tabs() + run(p[2])
        tab_count -= 1
        return a
    elif p[0] == 'fn':
        function_type = 'fn'
        tab_count += 1
        a = 'def ' + run(p[1]) + ' (' + run(p[2]) + '):\n' + tabs() + run(p[3])
        tab_count -= 1
        return a
    elif p[0] == 'command':
        function_type = 'command'
        function_id = run(p[1])
        tab_count += 1
        command = '@bot.command()\nasync def ' + function_id  + '(ctx,' + run(p[2]) + '):\n' + tabs() + run(p[3]) 
        error = '\n@' + function_id + '.error\nasync def ' + function_id + '_error(ctx,error):\n' + tabs() + 'if isinstance(error, commands.BadArgument):\n'+ tabs() +'\tawait ctx.send(\'Invalid Arguments\')'
        tab_count -= 1
        return command + error
    elif p[0] == 'parameter':
        if p[1] == None:
            return ''
        elif len(p) > 2:
            return run(p[1]) + ',' + run(p[2])
        else:
            return run(p[1])
    elif p[0] == 'body':
        if len(p) > 2:
            return run(p[1]) + '\n' + tabs() + run(p[2]) 
        else:
            return run(p[1])
    elif p[0] == 'return':
        return 'return ' + run(p[1])
    elif p[0] == 'global':
        return 'global ' + run(p[1])
    elif p[0] == 'token':
        token_flag = True
        token = run(p[1])
        return ''
    elif p[0] == 'function_call':
        function_name = run(p[1])
        if function_name == 'send':
            function_name = send(function_type)
        if p[2] == None:
            return function_name + '()'
        else:
            return function_name + '(' + run(p[2]) + ')'
    elif p[0] == 'term_list':
        if len(p) > 2:
            return run(p[1]) + ',' + run(p[2])
        else:
            return run(p[1])
    elif p[0] == 'term_map':
        if len(p) > 3:
            return run(p[1]) + ':' + run(p[2]) + ',' + run(p[3])
        else:
            return run(p[1]) + ':' + run(p[2])
    elif p[0] == 'dict':
        if p[1] == None:
            return '{}'
        else:
            return '{' + run(p[1]) + '}'
    elif p[0] == 'list':
        if p[1] == None:
            return '[]'
        else:
            return '[' + run(p[1]) + ']'
    elif p[0] == 'unop_term':
        return p[1] + run(p[2])
    elif p[0] == 'id':
        return str(p[1])
    elif p[0] == 'number':
        return str(p[1])
    elif p[0] == 'string':
        return str(p[1])
    elif p[0] == 'boolean':
        return str(p[1])

def send(function_type):
    if function_type == 'command':
        return 'await ctx.send'
    else:
        print('Error: cannot call send function on a function')
        sys.exit()

def defaultCodeEnd():
    global token
    return '\nbot.run(' + token + ')'

def makeFile(syntaxTree):
    default_code_begining = 'import discord\n' + 'from discord.ext import commands\n' + 'bot = commands.Bot(command_prefix=\'-\')\n'
    program = default_code_begining + run(syntaxTree) + defaultCodeEnd()
    checkErrors()
    outputCode = open('bot.py', 'w')
    outputCode.write(program)
    outputCode.close()

def checkErrors():
    global token_flag

    if not token_flag:
        print('Missing a token function')
        sys.exit()