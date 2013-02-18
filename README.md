# Simple Blog

I wrote this very simple blog based on an example found somewhere else. 
I found very interesting to try to have a very simple blog that's heroku ready

## instructions

clone this repo

    git clone https://github.com/mcniac/simple-blog.git

create the virtualenv

    cd simple-blog
    virtualenv --distribute env
    source env/bin/activate
    pip install -r requirements.txt
  
then you need to install mongo, if you're running OSX I recommend to use brew
  
    brew install mongodb
  
if you're using some other platform, follow the instructions here http://docs.mongodb.org/manual/installation/#installation-guides

then run the mongod server

    sudo mongod
    
then run the website

    cd /path/to/the/repo/copy
    source env/bin/activate
    python manage.py runserver
    
    
