git pull
cp -r ./the_front /home/hcwiley/webapps/the_front_django/
cd /home/hcwiley/webapps/the_front_django/the_front/
export PYTHONPATH=/home/hcwiley/webapps/the_front_django/lib/python2.7/
export PATH=$PATH:/home/hcwiley/webapps/timmy_hubot/bin/
/usr/local/bin/python2.7 manage.py collectstatic --noinput
cp -r ./collected-static/* /home/hcwiley/webapps/the_front_static/
source ../.env
/usr/local/bin/python2.7 manage.py migrate
$HOME/bin/pip install --upgrade -r requirements.txt
../apache2/bin/restart
exit
