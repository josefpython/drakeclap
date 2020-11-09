#!/usr/bin/env python3
import responsivepathing as rp
#set add1 comma input endline set add1 add1 comma input endline for get add1 endline for get add1 add1 endline set add1 add1 add1 comma add1 add1 add1 plus1 endline endstatement endline  endstatement endline print get add1 add1 add1 endline 


class Decoder:
	def __init__(self, input_file, output_file):		
		self.f = open(rp.here(output_file), "w")
		self.finp = open(rp.here(input_file), "r")
		
		self.tabs = 1
		self.input_string = str(finp.read())
		self.f.writelines("variabs = {}\ntry:\n")
		self.tabstring = ""

	def get(args):
		return( "variabs.get(" + str(args) + ")" )

	def set_(args_string):
		global tabstring
		global tabs
		tabstring = ""
		for x in range(tabs):
			tabstring = tabstring + "\t"

		#args_string = add1 comma input
		args = args_string.split(" comma ")

		p1args = args[0].split(" ")
		p1int = 0
			
		for arg in p1args:
			if arg == "add1":
				p1int= p1int + 1
			elif arg == "sub1":
				p1int= p1int - 1

		try:
			p2args = args[1].split(" ")

			p2int = 0
			p2plusint = 0

			if(p2args[0]=="input"):
				p2int = "int(input())"

			elif(p2args[0]=="get"):
				for arg in p2args:
					if arg == "add1":
						p2int= p2int + 1
					elif arg == "sub1":
						p2int = p2int - 1
					elif arg == "plus1":
						p2plusint = p2plusint + 1
					elif arg == "minus1":
						p2plusint = p2plusint - 1

				p2int = get(p2int)       

			else:
				for arg in p2args:
					if arg == "add1":
						p2int= p2int + 1
					elif arg == "sub1":
						p2int = p2int - 1

			operator = ""
			if p2plusint > 0:
				operator = "+ " + str(p2plusint)
			elif p2plusint < 0:
				operator = str(p2plusint)

		except IndexError:
			p2int = 0
			operator = ""


		f.writelines(tabstring + "variabs.update({" + str(p1int) + ":" + str(p2int) + operator + "})\n")

	def print_(args_string):
		global tabstring
		global tabs
		tabstring = ""
		for x in range(tabs):
			tabstring = tabstring + "\t"

		args = args_string.split(" ")
		idofvar = 0

		if args[0] == "get":

			for arg in args:
				if arg == "add1":
					idofvar = idofvar + 1
				elif arg == "sub1":
					idofvar = idofvar - 1        

			idofvar = get(idofvar)

		else:

			for arg in args:
				if arg == "add1":
					idofvar = idofvar + 1
				elif arg == "sub1":
					idofvar = idofvar - 1
		
		f.writelines(tabstring + "print(" + str(idofvar) + ")\n")

	def if_(args_string):
		global tabstring
		global tabs
		tabstring = ""
		for x in range(tabs):
			tabstring = tabstring + "\t"

		args = args_string.split(" comma ")
		p1args = args[0].split(" ")
		p1int = 0
		p2args = args[1].split(" ")
		p2int = 0

		if p1args[0] == "get":

			for arg in p1args:
				if arg == "add1":
					p1int= p1int + 1
				elif arg == "sub1":
					p1int= p1int - 1

			p1int = get(p1int)
        

		else:
			for arg in p1args:
				if arg == "add1":
					p1int= p1int + 1
				elif arg == "sub1":
					p1int= p1int - 1

		if p2args[0] == "get":

			for arg in p2args:
				if arg == "add1":
					p2int= p2int + 1
				elif arg == "sub1":
					p2int= p2int - 1

			p2int = get(p2int)
			

		else:
			for arg in p1args:
				if arg == "add1":
					p2int= p2int + 1
				elif arg == "sub1":
					p2int= p2int - 1

		f.writelines(tabstring + "if " + str(p1int) + " == " + str(p2int) + ":\n")
		tabs = tabs + 1

	def for_(args_string):
		global tabstring
		global tabs
		tabstring = ""
		for x in range(tabs):
			tabstring = tabstring + "\t"

		args = args_string.split(" comma ")
		p1args = args[0].split(" ")
		p1int = 0

		if p1args[0] == "get":

			for arg in p1args:
				if arg == "add1":
					p1int= p1int + 1
				elif arg == "sub1":
					p1int= p1int - 1

			p1int = get(p1int)
			

		else:
			for arg in p1args:
				if arg == "add1":
					p1int= p1int + 1
				elif arg == "sub1":
					p1int= p1int - 1

		f.writelines(tabstring + "for i in range(" + str(p1int) + "):\n")
		tabs = tabs + 1


commands = input_string.split(" endline ")

for command in commands:
    base = command.split(" ")[0]
    if base == "set":
        set_(command.split("set ")[1])
    elif base == "print":
        print_(command.split("print ")[1])
    elif base == "for":
        for_(command.split("for ")[1])
    elif base == "if":
        if_(command.split("if ")[1])
    elif base == "endstatement":
        tabs = tabs - 1
    elif base == "else":
        tabstring = ""
        for x in range(tabs):
            tabstring = tabstring + "\t"
        
        f.writelines(tabstring + "else:\n")
        tabs = tabs + 1

f.writelines('\tinput("Code finished.")\n')
f.writelines('except Exception as e:\n\tprint("An exception has occured, check your code again. If you believe the error was caused by a mistake in the language, submit a report on GitHub.")\n\tinput(e)')
