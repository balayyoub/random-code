import fitz

file_name = "01-file_name.pdf"
doc = fitz.open(file_name)
f = open(file_name + "_toc.txt", "x")
toc = doc.getToC()
for t in toc:
    while t[0] > 1: 
        t[1] = '    ' + t[1]
        t[0] -= 1
    print(t[1].ljust(70,'.'), t[2], file=f)