@echo  off
rename.sav
cd MODIS

for /r . %%a in (*021KM*.hdf) do (set b=%%a)
echo #!/bin/csh -f >fname.txt
echo setenv TIME %b:~27,31% >>fname.txt

for /r  %%d in (MOD03*.hdf) do (
echo MOD03���ݸ�ʽ�����������ʼ���ݷ��� 
move %%d MOD03.%b:~27,31%.hdf
)

for /r  %%f in (MYD03*.hdf) do (
echo MYD03���ݸ�ʽ�����������ʼ���ݷ��� %%f %g%
move %%f MYD03.%b:~27,31%.hdf
)

cd ..
pscp.exe -pw lj666yjh D:\MODISPRO\MODIS\fname.txt ocean@192.168.14.28:/home/ocean/RUN/TrueColor/
pscp.exe -pw lj666yjh D:\MODISPRO\MODIS\*.hdf ocean@192.168.14.28:/home/ocean/RUN/TrueColor/data/
echo ��ʼ���ݴ���������У�������192.168.14.28���û�����ocean,���룺lj666yjh

start /min cmd /c python D:\MODISPRO\Scripts\ylc1.py

putty.exe  -pw lj666yjh ocean@192.168.14.28

:: �������ش�����
:: echo ��ȡ���ݴ��������ݣ���������result��
:: pscp.exe -pw lj666yjh ocean@192.168.14.28:/home/ocean/RUN/TrueColor/image/* D:\MODISPRO\result\

:: echo ��ȡ���ݳɹ���

:: pause