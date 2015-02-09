#
from optparse import OptionParser

#
def count_words (stopwords, text):
	# split text on whitespace regardless of length
	raw_words = text.split (None)

	words = dict()
	for word in raw_words:
		if word in stopwords:
			continue

		if not words.has_key (word):
			words[word] = 0

		words[word] = words[word] + 1

	return words

class PreParser ():
	def parse (self, f):
		text = ""
		for line in f.xreadlines ():
			if "\n" == line[0]:
				continue

			line_text = line.strip ().lower ()
			line_text = line_text.replace (".", " ")
			line_text = line_text.replace (",", " ")
			line_text = line_text.replace ("?", " ")
			line_text = line_text.replace ("!", " ")
			line_text = line_text.replace ("(", " ")
			line_text = line_text.replace (")", " ")
			line_text = line_text.replace (":", " ")
			line_text = line_text.replace (";", " ")

			if "-" == line_text[-1:]:
				line_text = line_text[:-1]
			else:
				line_text = line_text + " "

			text = text + line_text

		return text

def main ():
	option_parser = OptionParser ()
	option_parser.add_option ('-s', '--stopword-file',
		dest='stopwordfile',
		help='File containing stop words.')
	option_parser.add_option ('-f', '--input-file',
		dest='filename',
		help='File to read.')
	(options, args) = option_parser.parse_args ()

	stopwords = dict ()
	with open (options.stopwordfile) as f:
		parts = f.read ().split (None)
		for part in parts:
			if not stopwords.has_key (part):
				stopwords[part] = True

	text = ""
	with open (options.filename) as f:
		text = PreParser ().parse (f)

	words = count_words (stopwords, text)

	for word in sorted (words, key=words.get, reverse=True):
		print word, words[word]

if __name__ == "__main__":
	main ()
