def includeFig(figName, title, scale = 0.23):
	latexCommand = "\\begin{"+"frame}\n"
	latexCommand += "\\frametitle{"+title+"}\n"
	latexCommand += "\t\\begin{"+"figure}\n"
	latexCommand += "\t\t\\begin{"+"center}\n"
	latexCommand += "\t\t\t\includegraphics[scale="+str(scale)+"]{"+figName+"}\n"
	latexCommand += "\t\t\\end{"+"center}\n"
	latexCommand += "\t\\end{"+"figure}\n"
	

	return latexCommand

def includeEq(i, winNSize, scale = 0.25):
	#latexCommand = "\t\\begin{"+"minipage}{7cm}\n"
	latexCommand = "\\small\n"
	latexCommand += windowsFunction(i)
	#latexCommand += "\t\\end{minipage"+"}\n"
	latexCommand += "\\normalsize\n"
	#latexCommand += "\t\\begin{minipage"+"}{7cm}\n"
	latexCommand += "\t\t\hspace{3cm}"+winNSize+"\n"
	#latexCommand += "\t\\end{minipage"+"}\n"
	latexCommand += "\\end{"+"frame}\n"

	return latexCommand


def includeSection(section):
	return "\section{"+section+"}\n"



def windowsFunction(i):

	latexCommand = "\\begin{equation*" + "}\n"
	if (i in [2, 3, 4]):
		latexCommand += "\tg(t, \\beta) = \left\{\n" 
	else:
		latexCommand += "\tg(t) = \left\{\n" 
	latexCommand +=	"\t\t\\begin{"+"array}{"+"cc}\n"

	if (i==1): #papoulis
		latexCommand +=	"\t\t\t\\frac{"+"1}{\pi}\\vert \\sin{(2\pi t)} \\vert+(1-2\\vert t \\vert )\cos{(2\pi t)}, & \\vert t\\vert \\leq \\frac{1"+"}{2"+"}\\\\\n"
		latexCommand +=	"\t\t\t0, & elsewhere\\\\\n"
	elif(i in [2, 3, 4]): #tukey
		latexCommand += "\t\t\t1, & \\vert t \\vert < \\beta\\\\\n"
		latexCommand +=	"\t\t\t\\frac{1"+"}{2"+"}+\\frac{1"+"}{2"+"}\\cos{"+"(\\frac{2\\pi \\vert t \\vert - \\beta}{1-2\\beta})}, "
		latexCommand += "& \\beta \\leq \\vert t \\vert  \\leq \\frac{1}{2}\\\\ \n"
		latexCommand += "\t\t\t0, & elsewhere\\\\ \n"

	elif(i==5): #bartllet
		latexCommand +=	"\t\t\t1-2\\vert t\\vert, & \\vert t\\vert \\leq \\frac{"+"1}{2"+"}\\\\\n"
		latexCommand +=	"\t\t\t0, & elsewhere\\\\ \n"

	elif(i==6): #box car
		latexCommand +=	"\t\t\t1, & \\vert t\\vert \\leq \\frac{"+"1}{2"+"}\\\\\n"
		latexCommand +=	"\t\t\t0, & elsewhere\\\\\n"

	elif(i==7): #hamming
		latexCommand +=	"\t\t\t0.54+0.46\cos{(2\pi t)}, & \\vert t\\vert \\leq \\frac{"+"1}{2"+"}\\\\\n"
		latexCommand +=	"\t\t\t0, & elsewhere\\\\\n"

	elif(i==8): #hanning
		latexCommand += "\t\t\t\\frac{1"+"}{2"+"}+\\frac{1"+"}{2"+"}\cos{(2\pi t)}, & \\vert t\\vert \\leq \\frac{1"+"}{2"+"}\\\\ \n"
		latexCommand += "0, & elsewhere\\\\ \n"

	latexCommand +=	"\t\t\\end{"+"array}\n"
	latexCommand +=	"\t\\right.\n"
	latexCommand += "\\end{" + "equation*}\n"


	return latexCommand


