#!/bin/bash
### 时间：2015年12月2日
### 作者：李炳南
### 功能：将文件从 ZhuanWang-Windows 文件夹中复制到 Linux 文件夹中
###___________________________________________________________

# 如果沒有指定 Linux 的文件夹，则自动使用当前的工作空间

	export home=/home/ocean/alex/Others/Linux-Windows
	to_folder=$home/Data

	cd $to_folder
	rm *

	str_file='*'

	echo "
-----------程序运算开始-----------

-----------进入 “"$to_folder"” 文件夹-----------
"
	cd $to_folder

	echo "----将文件从 “F:/User/LocalUser/jhyang/Download/alex_network” 中拷贝出来----

包括以下文件：
"

	pdsuser=jhyang:RSyang123jh@192.168.1.3/

	#局域网络控制，打开内网网卡
	sudo ifup eth0 > /dev/null
	
		lftp $pdsuser  <<FTPIT
		cd /Download/alex_network/
		ls -1 $str_file
		mget -c $str_file
		bye
FTPIT

	#局域网络控制，关闭内网网卡
	sudo ifdown eth0 > /dev/null

	echo "
------------------数据复制完成，程序退出！------------------
"


exit 1

