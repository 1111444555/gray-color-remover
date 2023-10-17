from utils import check_if_color_gray_variation
from lxml import etree
import zipfile
import os
import sys

# def get_word_xml(docx_filename):
#    with open(docx_filename) as f:
#       zip = zipfile.ZipFile(f)
#       xml_content = zip.read('word/document.xml')
#    return xml_content


def get_xml_tree(xml_string):
   return etree.ElementTree(etree.fromstring(xml_string))

def get_xml_tree_from_document(doc_xml_file_path):
    return etree.parse(doc_xml_file_path).getroot()


docx_filename="word/document.xml"
root=get_xml_tree_from_document(docx_filename)


p_counter=0

for element in root.iter():
    #print(element.tag)
    #if "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p" in element.tag:
    if '</w:p' in etree.tostring(element).decode():
        #breakpoint()
        p_counter=p_counter+1
        


        for e in element.iter():


            if "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr" in e.tag:

                if "shd" in e:
                    breakpoint()
                for item in e.iter():

                    if "shd" in item:
                        breakpoint()


                    if "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd" in item.tag:
                        #print("testiin")
                        color=item.attrib["{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill"]
                        #print(color,item,item.getparent().getparent().getparent())
                        print(color)

                        if check_if_color_gray_variation(color):
                            item.getparent().getparent().getparent().remove(item.getparent().getparent())


                    if item.tag =="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}highlight":
                        color=item.attrib["{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val"]
                        #print("11111")
                        print(color)
                        #print(color,item,item.getparent().getparent())
                        if check_if_color_gray_variation(color):
                            item.getparent().getparent().getparent().remove(item.getparent().getparent())

print(p_counter)


with open('temp/unzip/word/document.xml', 'wb') as f:
    f.write(etree.tostring(root))

os.system("cd /Users/saurabh/Documents/projects/smtv/docx_grey_remover/temp/unzip/Users/saurabh/Documents/projects/smtv/docx_grey_remover/temp/unzip")
os.system("zip -r ../../word2.docx  *")