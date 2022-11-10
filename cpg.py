import pypdfium2 as pdfium
import os
from glob import iglob
import shutil

file_path = os.path.abspath(__file__)
split_path = file_path.split('\\')
directory = split_path[:-1]
rootdir_glob = ('\\').join(directory)+"\**\*"
print(rootdir_glob)

# file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]

file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]

for f in file_list:
    check = f.split('.')
    ext = check.pop()
    if ext!='pdf':
        continue

    f_split_path = f.split('\\')

    f_name_raw = f_split_path.pop()
    f_name_split = f_name_raw.split()
    f_name_done = f_name_split[0:6]
    f_name = (" ").join(f_name_done)

    f_root_directory = ('\\').join(f_split_path)
    f_split_path[0] = "g:"
    f_dest_directory = ('\\').join(f_split_path)
    f_dest_directory = f_dest_directory+"\\"+f_name


    pdf = pdfium.PdfDocument(f)
    page = pdf.get_page(0)
    image = page.render_to(pdfium.BitmapConv.pil_image)
    if not os.path.exists(f_dest_directory):
        os.makedirs(f_dest_directory)
    image.save(f_dest_directory+"\\"+f_name+"_0.png")
    page = pdf.get_page(1)
    image = page.render_to(pdfium.BitmapConv.pil_image)
    if not os.path.exists(f_dest_directory):
        os.makedirs(f_dest_directory)
    image.save(f_dest_directory+"\\"+f_name+"_1.png")

    
