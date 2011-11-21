paper.pdf: paper.ps
	ps2pdf paper.ps

paper.ps: paper.dvi
	dvips -o paper.ps paper.dvi

paper.dvi: paper.tex
	latex paper.tex
	latex paper.tex

clean:
	rm -f paper.aux paper.log paper.dvi paper.ps
