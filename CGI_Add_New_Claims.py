import cgi

def main():
    form = cgi.FieldStorage()
    clmtid = form.getvalue('id')
    doi = form.getvalue('doi')
    issue_type = form.getvalue('issue_type')
    billed = form.getvalue('billed')
    covered = form.getvalue('covered')
    contents = processInput(clmtid, doi,issue_type,billed,covered)
    print(contents)

def processInput(x, a,b,c,d,e,f,g):
    clmtid = str(x)
    doi = str(a)
    issue_type = str(b)
    billed = str(c)
    covered = str(d)
    vals = [clmtid ,doi,issue_type,billed,covered]
    return fileToStr('try.html').format(**locals())

def fileToStr(FileName):
    fin=open(FileName);
    contents = fin.read();
    fin.close()
    return contents

try:
    print("Content-type: text/html\n\n")
    main()
except:
    cgi.print_exception()
