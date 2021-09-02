from translate import Translator
import os
translator= Translator(to_lang="ja")
try:
	execution_path=os.getcwd()
	with open (f"{execution_path}\\Hi.txt",mode='r', encoding="utf-8") as my_file:
		text=my_file.read()
		translation = translator.translate(text)
		with open (f"{execution_path}\\Hi_to_japanese.txt",mode='w', encoding="utf-8") as my_file2:
			my_file2.write(translation)

except FileNotFoundError as err:
	print('Please Enter the correct path')

except IOError as err:
	print("IO error found")
	raise err