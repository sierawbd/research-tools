import sys
import requests
 
def doi2bib(doi):
    """
    Return a bibTeX string of metadata for a given DOI.
    """
 
    url = "http://dx.doi.org/" + doi
 
    headers = {"accept": "application/x-bibtex"}
    r = requests.get(url, headers = headers)
 
    return r.text

doi = sys.argv[1]
filename=doi.replace('/','_')+'.bib'
f=open(filename,'w')
print >>f, doi2bib(doi)
f.close()

