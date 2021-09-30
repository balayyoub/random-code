import fitz

max_width = 80
file_name = "01-file_name" + ".pdf"
doc = fitz.open(file_name)
f = open(file_name + "_toc.txt", "w", encoding="utf-8")
toc = doc.getToC()
for t in toc:
    while t[0] > 1: 
        t[1] = '    ' + t[1]
        t[0] -= 1
    #t[1] = t[1] + ' '
    #t[2] = ' ' + str(t[2])
    info = (t[1][:(max_width-1)]) if len(t[1]) > (max_width-1) else t[1]
    print(info.ljust(max_width,'.'), t[2], file=f)
