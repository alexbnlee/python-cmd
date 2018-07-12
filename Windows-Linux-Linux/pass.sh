#!/bin/bash
### 时间：2015年12月2日
### 作者：李炳南
### 功能：将文件从 Linux 文件夹中复制到 ZhuanWang-Windows 文件夹中
###___________________________________________________________

# 如果沒有指定 Linux 的文件夹，则自动使用当前的工作空间

	export home=/home/ocean/alex/Others/Linux-Windows
	from_folder=$home/Data

	str_file='*'

	echo "
-----------程序运算开始-----------

-----------进入 “"$from_folder"” 文件夹-----------
"
	cd $from_folder

	echo "----拷贝文件到 “F:/User/LocalUser/jhyang/Download/alex_network” 文件夹中----

包括以下文件：
"
	ls -1 $str_file

	putftp=jhyang:RSyang123jh@192.168.1.3

	#局域网络控制，打开内网网卡
	sudo ifup eth0 2> /dev/null
	
		lftp $putftp  <<FTPIT
		cd /
		cd /Download/alex_network/
		mput -c $str_file
		cd  /
		bye
FTPIT

	#局域网络控制，关闭内网网卡
	sudo ifdown eth0 2> /dev/null

	echo "
------------------数据复制完成，程序退出！------------------
"

	cd $from_folder
	rm *

exit 1

