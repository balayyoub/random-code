import fitz

file_name = "01-file_name" + ".pdf"
doc = fitz.open(file_name)
f = open(file_name + "_toc.txt", "x", encoding="utf-8")
toc = doc.getToC()
for t in toc:
    while t[0] > 1: 
        t[1] = '    ' + t[1]
        t[0] -= 1
    #t[1] = t[1] + ' '
    #t[2] = ' ' + str(t[2])
    print(t[1].ljust(80,'.'), t[2], file=f)
