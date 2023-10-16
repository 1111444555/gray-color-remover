from docx import Document

document = Document('data/sample.docx')
#breakpoint()
for i,paragraph in enumerate(document.paragraphs):
    print(i,paragraph.text)
    
    # if i==7:
    #     breakpoint()    
    #breakpoint()
    if len(paragraph.runs) > 0:
        for run in paragraph.runs:
            if  run.font.highlight_color != None:
                #if paragraph.runs[0].font.highlight_color.value==16:
                if 'GRAY_' in run.font.highlight_color.name:
                    print("testing")
                    paragraph.clear()
                    break
        # skip this


    
    # print(paragraph.style.font.color.type)
    # print(paragraph.style.font.highlight_color)
    # print(paragraph.style.font.size.pt)

document.save("data/output.docx")