@echo  off
rename.sav
cd MODIS

for /r . %%a in (*021KM*.hdf) do (set b=%%a)
echo #!/bin/csh -f >fname.txt
echo setenv TIME %b:~27,31% >>fname.txt

for /r  %%d in (MOD03*.hdf) do (
echo MOD03数据格式处理结束，开始数据发送 
move %%d MOD03.%b:~27,31%.hdf
)

for /r  %%f in (MYD03*.hdf) do (
echo MYD03数据格式处理结束，开始数据发送 %%f %g%
move %%f MYD03.%b:~27,31%.hdf
)

cd ..
pscp.exe -pw lj666yjh D:\MODISPRO\MODIS\fname.txt ocean@192.168.14.28:/home/ocean/RUN/TrueColor/
pscp.exe -pw lj666yjh D:\MODISPRO\MODIS\*.hdf ocean@192.168.14.28:/home/ocean/RUN/TrueColor/data/
echo 开始数据处理界面运行，主机：192.168.14.28，用户名：ocean,密码：lj666yjh

start /min cmd /c python D:\MODISPRO\Scripts\ylc1.py

putty.exe  -pw lj666yjh ocean@192.168.14.28

:: 用来返回处理结果
:: echo 获取数据处理后的数据，并保存在result中
:: pscp.exe -pw lj666yjh ocean@192.168.14.28:/home/ocean/RUN/TrueColor/image/* D:\MODISPRO\result\

:: echo 获取数据成功！

:: pause