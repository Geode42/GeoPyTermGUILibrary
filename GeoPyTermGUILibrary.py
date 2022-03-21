from colorsys import hsv_to_rgb

show_warnings = True

class __formatting:
	def __init__(self):
		self.__dictionary = {
			'reset': '\33[0m', 'r': '\33[0m',
			'bold': '\33[1m', 'b': '\33[1m',
			'light': '\33[2m', 'l': '\33[2m',
			'italic': '\33[3m', 'i': '\33[3m',
			'underline': '\33[4m', 'u': '\33[4m',
			'blink': '\33[5m',
			'invert': '\33[7m',
			'hide': '\33[8m', 'h': '\33[8m',
			'strikethrough': '\33[9m', 's': '\33[9m',
			'double underline': '\33[21m',
			'reset intensity': '\33[22m', 'rb': '\33[22m', 'rl': '\33[22m',
			'reset italic': '\33[23m', 'ri': '\33[23m',
			'reset underline': '\33[24m', 'ru': '\33[24m',
			'reset blink': '\33[25m',
			'reset invert': '\33[27m',
			'reset hide': '\33[28m',
			'reset strikethrough': '\33[29m', 'rs': '\33[29m',
			'dblack': '\33[30m',
			'dred': '\33[31m',
			'dgreen': '\33[32m',
			'dyellow': '\33[33m',
			'dblue': '\33[34m',
			'dpurple': '\33[35m',
			'dcyan': '\33[36m',
			'dwhite': '\33[37m',
			# '': '\33[38m',  # implemented via function
			'reset color': '\33[39m', 'rc': '\33[39m',
			'background dblack': '\33[m40',
			'background dred': '\33[m41',
			'background dgreen': '\33[m42',
			'background dyellow': '\33[m43',
			'background dblue': '\33[m44',
			'background dpurple': '\33[m45',
			'background dcyan': '\33[m46',
			'background dwhite': '\33[m47',
			# '': '\33[m48',  # implemented via function
			'reset background': '\33[m49', 'rbg': '\33[49m',
			# '': '\33[m58',  # implemented via function
			'reset underline color': '\33[m59', 'ruc': '\33[59m',
			'black': '\33[90m',
			'red': '\33[91m',
			'green': '\33[92m',
			'yellow': '\33[93m',
			'blue': '\33[94m',
			'purple': '\33[95m',
			'cyan': '\33[96m',
			'white': '\33[97m',
			'background black': '\33[100m',
			'background red': '\33[101m',
			'background green': '\33[102m',
			'background yellow': '\33[103m',
			'background blue': '\33[104m',
			'background purple': '\33[105m',
			'background cyan': '\33[106m',
			'background white': '\33[107m',
			}
		for key, value in self.__dictionary.items():
			key = key.replace(' ', '_')
			self.__setattr__(key, value)
	
	def __getitem__(self, key):
		return self.__dictionary[key]
	
	def __contains__(self, item):
		if item in self.__dictionary:
			return True
		return False
	
	def __iter__(self):
		for key, value in self.__dictionary.items():
			return key

f = __formatting()


def color_from_rgb(r, g, b):
	return f'\033[38;2;{r};{g};{b}m'

def color_from_hsv(h, s, v):
	r, g, b = hsv_to_rgb(h, s, v)
	r, g, b = round(r * 255), round(g * 255), round(b * 255)
	return f'\033[38;2;{r};{g};{b}m'

def background_from_rgb(r, g, b):
	return f'\033[48;2;{r};{g};{b}m'

def background_from_hsv(h, s, v):
	r, g, b = hsv_to_rgb(h, s, v)
	r, g, b = round(r * 255), round(g * 255), round(b * 255)
	return f'\033[48;2;{r};{g};{b}m'

def underline_from_rgb(r, g, b):
	return f'\033[58;2;{r};{g};{b}m'

def underline_from_hsv(h, s, v):
	r, g, b = hsv_to_rgb(h, s, v)
	r, g, b = round(r * 255), round(g * 255), round(b * 255)
	return f'\033[58;2;{r};{g};{b}m'

def fprint(text, start='', end=''):
	text = start + text + end

	d = {
		'b': f.bold,
		'i': f.italic,
		'u': f.underline,
		'l': f.light,
		's': f.strikethrough,
		'blink': f.blink,
		'double underline': f.double_underline,
		'red': f.red,
		'green': f.green,
		'yellow': f.yellow,
		'blue': f.blue,
		'purple': f.purple,
		'cyan': f.cyan,
	}

	active_elements = []
	custom_rgb = False

	ineq_text = None
	ending = False
	for i in text:
		if ineq_text is not None and i == '>':
			if ineq_text.startswith('rgb'):
				if ending:
					if custom_rgb:
						for j in active_elements:
							if '\x1b[' in j:
								active_elements.remove(j)
								custom_rgb = False
								print(f.r, end='')
								for j in active_elements:
									print(j, end='')
								ineq_text = None
								ending = False
								break
					else:
						if show_warnings:
							print(f.r + f.red + f'|===== WARNING: Tag {ineq_text} not active =====|' + f.r)
				else:
					color = []
					ineq_text = ineq_text[3:]
					if ineq_text.startswith('('):
						ineq_text = ineq_text[1:]
						if ineq_text.endswith(')'):
							ineq_text = ineq_text[:-1]
							ineq_text = ineq_text.split(',')
							if len(ineq_text) == 3:
								for val in ineq_text:
									val = val.strip(' ')
									if val.isnumeric:
										color.append(int(val))
								active_elements.append(color_from_rgb(color[0], color[1], color[2]))
								custom_rgb = True
								print(f.r, end='')
								for j in active_elements:
									print(j, end='')
								ineq_text = None
								ending = False
			elif ineq_text in d:
				if ending:
					if d[ineq_text] in active_elements:
						active_elements.remove(d[ineq_text])
					else:
						if show_warnings:
							print(f.r + f.red + f'|===== WARNING: Tag {ineq_text} not active =====|' + f.r)
				else:						
					active_elements.append(d[ineq_text])

				print(f.r, end='')
				for j in active_elements:
					print(j, end='')
				ineq_text = None
				ending = False
			else:
				if show_warnings:
					print(f.r + f.red + f'|===== WARNING: Tag {ineq_text} not found =====|' + f.r)

					for j in active_elements:
						print(j, end='')
		elif ineq_text is not None:
			if len(ineq_text) == 0 and i == '/':
				ending = True
			else:
				ineq_text += i
		elif i == '<':
			ineq_text = ''
		else:
			print(i, end='')
	print(end)
