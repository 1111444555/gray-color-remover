# Gray color remover

# Dependencies
lxml

### This program takes in input docx as input and produces output docx as output

# Status
tested on sample.docx works fine
but for some reason docx cannot be saved from temporary xml file in python (same command works in terminal)

# To run

```
input_docx=data/sample.docx
output_docx=data/output.docx

mkdir src_doc
unzip $input_docx
cp -r src_doc dst_doc

python3 main.py src_doc/word/document.xml  dst_doc/word/document.xml

cd dst_doc
zip -r ../output.docx *





```