# Kubespray Installation
Kubespray ile 1 master 1 worker cluster üzerinde metallb,argocd,prometheus-stack kurulumunu `vagrant up` komutu ile direkt ayağa kaldırabilmek için geliştirilmiş bir projedir.

İlk önce aşağıdaki komutlar ile kubespray kurulumunun yönetileceği macos ortamı hazırlanır.

```ShellSession
brew install python && alias python=python3 && python -m pip install --upgrade pip && alias pip=pip3 && brew install vagrant && brew install kubectl && brew install helm &&brew install git && cd ~/ && git clone https://github.com/kubernetes-sigs/kubespray.git && cd kubespray && pip3 install -r requirements.txt && cd contrib/inventory_builder && pip3 install -r requirements.txt
```
Parallels yüklemek için 
`brew install --cask parallels`
Virtualbox yüklemek için 
`brew install --cask virtualbox && brew install --cask virtualbox-extension-pack`

Vagrant dosyasında 1 master(+etcd) ve 1 worker oluşturmak için aşağıdaki komutu default Vagrantfile'ı overwrite etmek için kullanacağız.

```ShellSession
cat <<EOF > ~/kubespray/vagrant/config.rb
\$os = "ubuntu2004arm"
\$num_instances = 2
\$instance_name_prefix = "k8s"
\$vm_memory = 4096
\$vm_cpus = 4
\$subnet = "172.18.8"
\#$subnetHost = "172.16.100"
\$etcd_instances = 1
\$kube_master_instances = 1
\$kube_node_instances = 1
\#$ansible_tags = ["apps", "ingress-controller"]
\$inventory = "inventory/mycluster"
EOF
```
Aşağıdaki komut ile hosts.yml dosyası oluşturup ardından vi ile master ve worker node olacakları belirliyoruz.

```ShellSession
cp -r inventory/sample inventory/mycluster
declare -a IPS=(172.18.8.101 172.18.8.102)
KUBE_CONTROL_HOSTS=1 CONFIG_FILE=inventory/mycluster/hosts.ini python3 contrib/inventory_builder/inventory.py ${IPS[@]}
```
Ardından vagrant up komutu ile çalıştırıyoruz. 

ssh fatal error durumunda aşağıdakiler yapılabilir 
- ansible_host ipleri makine içinden bakılarak inventory/mycluster/hosts.ini ansible_host değiştirilmeli
- ~/.ssh/known_hosts içerisinde ssh error veren ip ile başlayan satır silinebilir
- parallels için preferences->network ekranında vagrant-vnet0 ip bilgileri 172.18.8.1 - 172.18.8.254 olarak değiştirilip kayıt edilebilir.





