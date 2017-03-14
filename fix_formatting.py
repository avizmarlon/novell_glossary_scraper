### Novell Glosary Scraping
## by Marlon Aviz

FILE_PATH = "scraped-data_optmized.txt"
saveTo = "final_data.txt"
handle = open(FILE_PATH, 'r', encoding="utf-8")
c = 0
word = None
definition = []
for line in handle:
	line = line.strip()
	if c == 1:
		word = line
		c = 0
		continue
	if line == "######":
		if len(definition) > 0:
			definition_text = '. '.join(definition)
			shandle = open(saveTo, 'a', encoding='utf-8')
			shandle.write(word + "\t" + definition_text + '\n\n')
			shandle.close()
			definition.clear()
		c = 1
		continue
	if line != "":
		definition.append(line)