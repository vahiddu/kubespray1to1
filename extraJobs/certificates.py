import glob
import os

# absolute path to search all text files inside a specific folder
path = r'/etc/kubernetes/pki/*.crt'
files = glob.glob(path)

for file in files:
    print(os.path.basename(file))
    os.system('openssl x509 -in ' + file + ' -noout -text | grep Not')
