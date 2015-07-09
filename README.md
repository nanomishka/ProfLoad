# ProfLoad
Web-приложение для расчета нагрузки преподавателя

#### Инструкция по установке web-версии "Системы разчета нагрузки преподавателей" на ОС: UBUNTU 12.04 (LINUX)

##### Настройка системы сотоит из 3х этапов:
* I Настройка программного окружения системы
* II Настройка базы данных для системы
* III Настройка системы

##### I Настройка программного окружения системы:
1. mysql-server 5.5 или выше
2. python v2.7.3
3. pip
4. python-mysqldb _(требуется pip)_
5. xlwt _(требуется pip)_
6. django v1.7.6 _(требуется pip)_
7. git

_Подробнее:_

1. mysql

	`$ sudo apt-get install mysql-server` 
	
	(в процессе установке потребуется указать пароль для root)
	
	`$ sudo apt-get install libmysqlclient-dev`
2. python v2.7.3 _(см. документацию на python)_
3. pip
4. 
	`$ sudo apt-get install python-pip`
4. python-mysqldb _(требуется pip)_

	`$ sudo apt-get install python-mysqldb`
5. xlwt (требуется pip)

	`$ sudo pip install xlwt`
6. django v1.7.6 _(требуется pip)_

	`$ sudo pip install Django==1.7.6`
7. git

	`$ sudo apt-get install git`


#####  II Инструкция по настройке базы данных для системы:
1. войти в консоль mysql
	
	`>> mysql -u root -p`

	(потребуется ввести пароль пользователя root)
2. создание базы данных для системы
	
	`mysql> CREATE DATABASE 'profdb' CHARACTER SET utf8 COLLATE utf8_general_ci;`
3. создать пользователя для системы
	
	`mysql> CREATE USER 'prof'@'localhost' IDENTIFIED BY 'prof';`
4. дать права пользователю системы на работу с базой данных

	`mysql> GRANT ALL PRIVILEGES ON `profdb`.* TO 'prof'@'localhost';`


##### III Инструкция по настройке системы:
1. скачиваем проект с git-репозитория

	`$ git clone https://github.com/nanomishka/ProfLoad.git && cd ProfLoad`
2. создаем таблицы в базе данных

	`$ python manage.py makemigrations`
	
	`$ python manage.py migrate`
3. запускаем локальный сервер django

	`$ python manage.py runserver 8080`

###### Система настроена и находится по адресу http://127.0.0.1:8080/
