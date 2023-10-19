from utils import check_if_color_gray_variation
from lxml import etree
import zipfile
import os
import sys
import zipfile


def get_xml_tree(xml_string):
   return etree.ElementTree(etree.fromstring(xml_string))

def get_xml_tree_from_document(doc_xml_file_path):
    return etree.parse(doc_xml_file_path).getroot()


docx_filename=sys.argv[1]
root=get_xml_tree_from_document(docx_filename)


#p_counter=0

body=root[0]
print(len(body.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')))
for i,p in enumerate(body.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')):
    #print(i,p.tag)

    for shd in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd'):

        color=shd.attrib["{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill"]
        print(color)

        if check_if_color_gray_variation(color):
            print(f"line {i+1} grey shade detected in this paragraph removing it")
            body.remove(p)
            break

    for highlight in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}highlight'):

        color=highlight.attrib["{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val"]
        print(color)

        if check_if_color_gray_variation(color):
            print(f"line {i+1} grey shade detected in this paragraph removing it")
            body.remove(p)
            break


#print(len(body.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')))

def generate_output_docx():
    with open(sys.argv[2], 'wb') as f:
        f.write(etree.tostring(root))


        # zip_cmd="zip -r /Users/saurabh/Documents/projects/smtv/docx_grey_remover/word2.docx  *"
        # os.chdir("/Users/saurabh/Documents/projects/smtv/docx_grey_remover/temp/unzip/")
        # #os.system(zip_cmd)

        # filenames = zipfile.ZipFile(docx_filename).namelist()
        # # Now, create the new zip file and add all the filex into the archive
        
        # with zipfile.ZipFile(dst_docx, "w") as docx:
        #     for filename in filenames:
        #         docx.write(os.path.join("/Users/saurabh/Documents/projects/smtv/docx_grey_remover/temp/unzip/",filename), filename)
        # #os.system()



generate_output_docx()