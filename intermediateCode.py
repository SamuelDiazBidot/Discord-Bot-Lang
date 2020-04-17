tab_count = 0

def tabs():
    result = ''
    for _ in range(0, tab_count):
        result = result + '\t'
    return result

def run(p):
    global tab_count

    default_code_begining = 'import discord\n' + 'from discord.ext import commands\n' + 'client = discord.Client()\n' + 'bot = commands.Bot(command_prefix=\'$\')\n'
    default_code_end = '\nclient.run(\'your token here\')'

    if p[0] == 'program':
        if len(p) > 2:
            return  default_code_begining + run(p[1]) + '\n' + run(p[2]) + default_code_end
        else:
            return default_code_begining + run(p[1]) + default_code_end
    elif p[0] == 'variable':
        return run(p[1]) + ' = ' + run(p[2])
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
        tab_count += 1
        a = 'def ' + run(p[1]) + ' (' + run(p[2]) + '):\n' + tabs() + run(p[3])
        tab_count -= 1
        return a
    elif p[0] == 'command':
        tab_count += 1
        a = '@bot.command()\nasync def ' +  run(p[1]) + '(ctx,' + run(p[2]) + '):\n' + tabs() + run(p[3]) + '\nbot.add_command(' + run(p[1]) + ')\n'
        tab_count -= 1
        return a
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
    elif p[0] == 'function_call':
        if p[2] == None:
            return run(p[1]) + '()'
        else:
            return run(p[1]) + '(' + run(p[2]) + ')'
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

def makeFile(syntaxTree):
    program = run(syntaxTree)
    outputCode = open('bot.py', 'w')
    outputCode.write(program)
    outputCode.close()