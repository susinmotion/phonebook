import sys, os

def create_phonebook(phonebook):
#create a new phonebook
	filename="%s.txt" % phonebook
	if os.path.exists(filename):
		print "that file already exists!"
		quit()
	with open(filename, 'w') as f:
		pass
def add_entry(firstname, lastname, number, phonebook):
#add a new name and number
	filename="%s.txt" % phonebook
	if not os.path.exists(filename):
		print "that phonebook does not exist"
		quit()
	with open(filename, 'a') as f:
		f.write("%s\t%s\t%s\n" %(firstname, lastname, number))

def update(name, number):
#update an existing name with a new number
	pass
def lookup(phonebook, name):
	filename="%s.txt" % phonebook
	if not os.path.exists(filename):
		print "that phonebook does not exist"
		quit()
	with open(filename, 'r') as f:
		for line in f:
			if line.split().pop(0)==name:
				print line
# look up a number from a name
	pass
def reverse_lookup(number):
#look up a name given a number
	pass
def remove(name):
# remove the entry for a given name
	pass

if __name__=='__main__':
	args=sys.argv[:]
	script=args.pop(0)
	if not args:
		print "please enter a command"
		quit()
	command=args.pop(0)

	command_funcs={
		'create': create_phonebook,
		'add': add_entry,
		'reverse-lookup': reverse_lookup,
		'lookup': lookup,
		'remove': remove,
		'update':update
	}
	if command not in command_funcs:
		print "please enter a valid command"
		quit()
	func=command_funcs[command]

	command_arguments={
		'create': "phonebook name",
		'add': "first name, last name, number and phonebook name",
		'reverse-lookup': "phone number",
		'lookup': "phonebook name and name",
		'remove': "name",
		'update': "name and number"
	}
	try:
		func(*args)
	except:
		print command, "requires", command_arguments[command]
		quit()
