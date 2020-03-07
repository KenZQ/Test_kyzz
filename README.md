# ttsx_kyzz

pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r plist.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
数据库
CREATE DATABASE IF NOT EXISTS ttsx default charset utf8 COLLATE utf8_general_ci;

python manage.py  migrate
python manage.py  makemigration
