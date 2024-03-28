# import input_data
import gzip
import tarfile
import os

gz_file_path = 'data_set/t10k-images-idx3-ubyte.gz'
# gz_file_path = 'data_set/t10k-labels-idx1-ubyte.gz'

extractor_folder = 'extractor_files'


with gzip.open(gz_file_path, 'rb') as f:
    file_content = f.read()

print(file_content)
print(type(file_content))
# if not os.path.exists(extractor_folder):
#     os.makedirs(extractor_folder)

# with open(gz_file_path, 'rb') as gz_ref:  r'C:\Users\Administrator\Desktop\Opencv\data_set\t10k-images-idx3-ubyte.gz'
#     gz_ref.write(extractor_folder)
# gz_ref = tarfile.open(gz_file_path, 'r')
# gz_ref.extractall(extractor_folder)

print(f'文件已解压到{extractor_folder}')