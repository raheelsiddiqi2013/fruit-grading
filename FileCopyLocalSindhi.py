import os
import shutil

src_dir1="C:\\My Data\\My research\\Fruit Grading System\\Datasets\\Guava Dataset\\Guava Dataset\\Local Sindhi\\Green"
src_dir2="C:\\My Data\\My research\\Fruit Grading System\\Datasets\\Guava Dataset\\Guava Dataset\\Local Sindhi\\Mature Green"
src_dir3="C:\\My Data\\My research\\Fruit Grading System\\Datasets\\Guava Dataset\\Guava Dataset\\Local Sindhi\\Ripe"

dst_dir="C:\\My Data\\My research\\Fruit Grading System\\Datasets\\Guava Dataset\\ThreeGuavaSpecies\\Train\\LocalSindhi"
counter=1

src_files=os.listdir(src_dir1)
for file_name in src_files:
    print(file_name)
    full_file_name=os.path.join(src_dir1,file_name)
    dst_file_name=str(counter)+".jpg"
    full_dst_file_name=os.path.join(dst_dir,dst_file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name,full_dst_file_name)
    counter=counter+1

src_files=os.listdir(src_dir2)
for file_name in src_files:
    print(file_name)
    full_file_name=os.path.join(src_dir2,file_name)
    dst_file_name=str(counter)+".jpg"
    full_dst_file_name=os.path.join(dst_dir,dst_file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name,full_dst_file_name)
    counter=counter+1

src_files=os.listdir(src_dir3)
for file_name in src_files:
    print(file_name)
    full_file_name=os.path.join(src_dir3,file_name)
    dst_file_name=str(counter)+".jpg"
    full_dst_file_name=os.path.join(dst_dir,dst_file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name,full_dst_file_name)
    counter=counter+1
