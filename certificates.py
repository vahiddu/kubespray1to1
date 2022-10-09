import glob
import subprocess

# absolute path to search all text files inside a specific folder
path = r'/etc/kubernetes/pki/*.crt'
files = glob.glob(path)
print(files)

for file in files:
        result = subprocess.run(['echo 'file' |openssl', 'x509', '-in', '/etc/kubernetes/pki/''.crt', '-noout' '-text|grep', 'name'], stdout=subprocess.PIPE)
        result.stdout