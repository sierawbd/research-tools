#!/usr/bin/env python
#THIS REQUIRES THAT bibutils IS INSTALLED ON YOUR MACHINE

"""
Usage:
./bib2word2010.py [Input files]
"""

import sys
import fileinput
import os

if __name__ == '__main__':
  #input a BibTex .bib file
  fnames = sys.argv[1:]

  #run bibutils functions to convert to Word XML
  os.system("cat " + ' '.join(fnames) + " > TEMPOUT0.bib")
  os.system("bib2xml TEMPOUT0.bib > TEMPOUT1.xml")
  os.system("xml2wordbib TEMPOUT1.xml > TEMPOUT2.xml")
  os.system("rm TEMPOUT1.xml")

  #clean up for Word 2010 formatting
  f1 = open('TEMPOUT2.xml', 'r')
  for line in f1:
    line = line.replace("ArticleInAPeriodical", "JournalArticle")
    line = line.replace("PeriodicalName", "JournalName")
    line = line.replace("Proceedings", "ConferenceProceedings")
    print line,
  f1.close()
  #os.system("rm TEMPOUT0.bib TEMPOUT2.xml")
