variabs = {}
try:
	variabs.update({1:int(input())})
	variabs.update({2:int(input())})
	variabs.update({3:0})
	for i in range(variabs.get(1)):
		for i in range(variabs.get(2)):
			variabs.update({3:variabs.get(3)+ 1})
	print(variabs.get(3))
	input("Code finished.")
except Exception as e:
	print("An exception has occured, check your code again. If you believe the error was caused by a mistake in the language, submit a report on GitHub.")
	input(e)