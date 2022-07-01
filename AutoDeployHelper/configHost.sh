#!/bin/sh

###################################### 
# @Author: Jocx
# @Time: 2022-6-15
# @Description: 自动配置计算节点网络地址
######################################

cd /opt/lagou/software
echo "配置hosts"
sudo cp /opt/lagou/software/hosts /etc/hosts -af
echo "正在生成.ssh"
cd ~
sudo ssh-keygen -t rsa
cd ~/.ssh
sudo cat id_rsa.pub >> ~/.ssh/authorized_keys
sudo scp ~/.ssh/id_rsa.pub root@slave01:/home/
sudo scp ~/.ssh/id_rsa.pub root@slave02:/home/
sudo scp ~/.ssh/id_rsa.pub root@slave03:/home/