@echo  off

cd ./Scripts

pscp.exe -pw lj666yjh D:\Windows-Linux\Data\* ocean@192.168.14.28:/home/ocean/alex/Others/Linux-Windows/Data

echo.
echo ����Linux���ԣ�������192.168.14.28���û�����ocean,���룺lj666yjh
echo.
echo ִ�д��롾pass.sh��

start /min cmd /c python Pass_Data_3.py

putty.exe -pw lj666yjh ocean@192.168.14.28

echo.
echo ���ݴ���ɹ���
echo.