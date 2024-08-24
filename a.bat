

@echo off
:: Указываем URL и имена файлов
set "url1=https://www.dropbox.com/scl/fi/odl1rjv9ttmg4f3mjk55z/True.csv?rlkey=9d5lv7ltc1ob9mlo9iionemrm&st=tzc6sp4n&dl=0"
set "url2=https://www.dropbox.com/scl/fi/303jbuwuytw9cjm9u6iyf/Fake.csv?rlkey=948fk1wbt34hppldi80vnnl9c&st=mpqkmljo&dl=0"
set "output1=True.csv"
set "output2=False.csv"

:: Скачиваем первый файл и переименовываем его
curl -L -o "%output1%" "%url1%"

:: Скачиваем второй файл и переименовываем его
curl -L -o "%output2%" "%url2%"

:: Завершаем выполнение
echo Download complete.
pause
