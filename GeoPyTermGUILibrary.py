from colorsys import hsv_to_rgb

class __formatting:
	def __init__(self):
		self.__dictionary = {
			'reset': '\33[0m',
			'bold': '\33[1m',
			'light': '\33[2m',
			'italic': '\33[3m',
			'underline': '\33[4m',
			'blink': '\33[5m',
			'invert': '\33[7m',
			'hide': '\33[8m',
			'strikethrough': '\33[9m',
			'double underline': '\33[21m',
			'reset intensity': '\33[22m',
			'reset italic': '\33[23m',
			'reset underline': '\33[24m',
			'reset blink': '\33[25m',
			'reset invert': '\33[27m',
			'reset hide': '\33[28m',
			'reset strikethrough': '\33[29m',
			'dblack': '\33[30m',
			'dred': '\33[31m',
			'dgreen': '\33[32m',
			'dyellow': '\33[33m',
			'dblue': '\33[34m',
			'dpurple': '\33[35m',
			'dcyan': '\33[36m',
			'dwhite': '\33[37m',
			# '': '\33[38m',  # implemented via function
			'reset color': '\33[39m',
			'background dblack': '\33[m40',
			'background dred': '\33[m41',
			'background dgreen': '\33[m42',
			'background dyellow': '\33[m43',
			'background dblue': '\33[m44',
			'background dpurple': '\33[m45',
			'background dcyan': '\33[m46',
			'background dwhite': '\33[m47',
			# '': '\33[m48',  # implemented via function
			'reset background': '\33[m49',
			# '': '\33[m58',  # implemented via function
			'reset underline color': '\33[m59',
			'superscript': '\33[m73',
			'subscript': '\33[74m',
			'reset script': '\33[75m',
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
