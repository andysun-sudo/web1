import cgi
import uuid

def main():
    form = cgi.FieldStorage()
    clmtid = uuid.uuid4().hex[:8]
    name = form.getvalue('name')
    gender = form.getvalue('gender')
    dob = form.getvalue('DOB')
    ssn = form.getvalue('SSN')
    smoking = form.getvalue('smoking')
    allegies = form.getvalue('allegies')
    medical_conditions = form.getvalue('medical conditions')
    contents = processInput(clmtid, name,gender,dob,ssn,smoking,allegies, medical_conditions)
    print(contents)

def processInput(x, a,b,c,d,e,f,g):
    clmtid = str(x)
    name = str(a)
    gender = str(b)
    dob = str(c)
    ssn = str(d)
    smoking = str(e)
    allegies = str(f)
    medical_conditions = str(g)
    vals = [clmtid, name,gender,dob,ssn,smoking,allegies, medical_conditions]
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
