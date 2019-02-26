#!/usr/bin/env python

if __name__ == '__main__':
	import sys

if len(sys.argv) == 1:
    downloaded_dir = input(str('Enter a directory to download your GIT-Project: '))
else:
    filename = sys.argv[1]

table = SymbolTable()
parser = Parser(sys.argv[1])
parser.advance()
line = 0

while parser.hasMoreCommands():
    if parser.commandType() == 'L_COMMAND':
        table.addEntry(parser.symbol(), line)
    else:
        line += 1

    parser.advance()

code = Code()
parser = Parser(downloaded_dir)
parser.advance()

var_stack = 16

while parser.hasMoreCommands():
    cmd_type = parser.commandType()

    if cmd_type == 'A_COMMAND':
        number = 32768

        try:
            addr = int(parser.symbol())
        except:
            if table.contains(parser.symbol()):
                addr = table.getAddress(parser.symbol())
            else:
                table.addEntry(parser.symbol(), var_stack)
                addr = var_stack
                var_stack += 1

        bin_number = bin(number | addr)[3:]
        assembly = '0' + bin_number
        print(assembly)
    elif cmd_type == 'C_COMMAND':
        assembly = '111'
        assembly += code.comp(parser.comp())
        assembly += code.dest(parser.dest())
        assembly += code.jump(parser.jump())
        print(assembly)
    parser.advance()
