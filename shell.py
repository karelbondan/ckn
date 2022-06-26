import ckn
import re

while True:
	text = input('ckn > ')
	check = re.findall(r'^\w+.ckn$', text)
	# text[0] == "#" is to avoid having the lexer only detecting EOF which will result in error,
	# because comments are skipped. 
	if text.strip() == "" or text[0] == "#":
		continue
	elif check:
		try:
			with open(text, encoding='utf-8') as f:
				text_copy = text
				text = ""
				for lines in f: 
					text += lines.replace("\n", ";")
		except FileNotFoundError as e: 
			print(f"FileNotFound: No file with name \"{text}\" found. Please put your source code in this directory.")
			continue
	result, error = ckn.run(f'<{check[0]}>' if check else '<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))