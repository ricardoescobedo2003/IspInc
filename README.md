# IspInc

mysql-connector-python
pip install tkcalendar
pip3 install svglib pillow
pip3 install reportlab


# Permisos de mysql del servidor
CREATE USER 'dni'@'%' IDENTIFIED BY 'MinuzaFea265/';
GRANT ALL PRIVILEGES ON *.* TO 'dni'@'%' WITH GRANT OPTION;
UPDATE mysql.user SET Host='%' WHERE User='dni' AND Host='localhost';
FLUSH PRIVILEGES;


# Permisos SQL
sudo nano /etc/mysql/my.cnf
# bind-address = 127.0.0.1

sudo systemctl restart mysql

sudo ufw allow 3306/tcp
