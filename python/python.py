import sys

integer = int(1)
fl = float(1.0)
character = str('c')
boolean = bool(True)
liste = list(['1', '2', '3', '4'])

def get_entry():
	return input(f'Entrer valeur:')

def pprint():
	print(f'Integer: {integer}\n')
	print(f'Float: {fl}\n')
	print(f'String: {character}\n')
	print(f'Boolean: {boolean}\n')
	print(f'Liste: {liste}\n')
	print(f'Entree: {entree}\n')

def comp():
	if entree > 18446744073709551614:
		print('Taille maximum\n')
	else:
		print('OK\n')

def switch():
	match entree:
		case "Boolean":
			print('Type Boolean\n')
		case "Intger":
			print('Type int\n')
		case "Float":
			print('Type float\n')
		case "List":
			print('Type list\n')
		case other:
			print('Type inconnu')

class val:
	def __init__(self, name, value, ttype: str):
		self.name = name
		self.value = value
		self.ttype = ttype

	def get_type(self):
		print (f'{self.name} is of type {self.ttype}\n')

	def get_value(self):
		print (f'{self.name} is equal to {self.value}\n')

	def get_name(self):
		print (f'{self.name}\n')

if __name__ == "__main__":
	integer = val("Integer", 1, int)
	fl = val("Float", 1.0, float)

#print(f'Integer name: {integer.name}\n')
#print(f'Integer size: {integer.size}\n')
integer.get_value()
integer.get_name()
integer.get_type()

print(f'{integer.value}')

fl.get_value()
fl.get_name()
fl.get_type()

fl.size = sys.getsizeof(fl.value)

print(f'{fl.value}')

entree = val("input", float(get_entry()), float)
print(f'Entree egal: {entree.value}')
print(type(entree.value))
print(f'{entree.ttype}')