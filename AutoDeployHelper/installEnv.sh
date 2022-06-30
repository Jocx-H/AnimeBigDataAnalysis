#!/bin/sh

###################################### 
# @Author: Jocx
# @Time: 2022-6-15
# @Description: 自动部署分布式开发环境
######################################

echo "开始安装配置Java、Hadoop、Spark、Hive、MySQL环境！"
echo "创建Java、Hive安装地址"
mkdir -p /opt/lagou/servers/
echo "创建Hadoop、Spark、MySQL安装地址"
mkdir -p /home/apps/servers/

cd /opt/lagou/software

echo "安装jdk..."
tar -zxvf jdk-8u171-linux-x64.tar.gz -C /opt/lagou/servers/

echo "安装Hadoop"
tar -zxvf hadoop-2.7.7.tar.gz -C /home/apps/servers/
mv /home/apps/servers/hadoop-2.7.7 /home/apps/servers/hadoop

echo "安装Spark"
tar -zxvf spark-3.1.1-bin-hadoop2.7.tgz -C /home/apps/servers/
mv /home/apps/servers/spark-3.1.1-bin-hadoop2.7 /home/apps/servers/spark

echo "安装Hive"
tar zxvf apache-hive-2.3.7-bin.tar.gz -C /opt/lagou/servers/
mv /opt/lagou/servers/apache-hive-2.3.7-bin /opt/lagou/servers/hive

echo "更新环境变量"
\cp /opt/lagou/software/profile /etc/profile -af
source /etc/profile

echo "配置Hadoop"
\cp /opt/lagou/software/hadoop/ /home/apps/servers/hadoop/etc/ -arf

echo "配置Spark"
\cp /opt/lagou/software/conf/ /home/apps/servers/spark/ -arf

echo "配置Hive"
rm -rf /opt/lagou/servers/hive/conf
\cp /opt/lagou/software/conf2/ /opt/lagou/servers/hive/ -arf
mv /opt/lagou/servers/hive/conf2 /opt/lagou/servers/hive/conf

echo "安装MySQL"
rpm -aq | grep mariadb
rpm -e --nodeps mariadb-libs
yum install perl -y
yum install net-tools -y
yum install libaio

tar xvf mysql-5.7.26-1.el7.x86_64.rpm-bundle.tar
rpm -ivh mysql-community-common-5.7.26-1.el7.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.26-1.el7.x86_64.rpm
rpm -ivh mysql-community-client-5.7.26-1.el7.x86_64.rpm
rpm -ivh mysql-community-server-5.7.26-1.el7.x86_64.rpm

echo "开始配置MySQL"
systemctl start mysqld
grep password /var/log/mysqld.log
echo -n "Enter your name: "
read name
mysql -u root -p$name -e"/opt/lagou/software/configMySQL.sql"


echo "安装jdbc驱动"
\cp /opt/lagou/software/mysql-connector-java-5.1.46.jar /opt/lagou/servers/hive/lib

echo "初始化元数据库"
schematool -dbType mysql -initSchema

echo "格式化集群"
/home/apps/servers/hadoop/bin/hdfs namenode -format

echo "开启防火墙"
systemctl start firewalld
echo "开启防火墙端口"
firewall-cmd --zone=public --add-port=50070/tcp --permanent
firewall-cmd --zone=public --add-port=9000/tcp --permanent
firewall-cmd --zone=public --add-port=8088/tcp --permanent
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --zone=public --add-port=7077/tcp --permanent
firewall-cmd --reload
firewall-cmd --zone=public --list-ports

echo "环境安装完成，请使用`source /etc/profile使配置文件生效`请先启动hadoop和spark，再启动hive"
