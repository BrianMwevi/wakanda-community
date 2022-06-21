# heroku create wakanda-community
heroku config:set ALLOWED_HOSTS=wakanda-community.herokuapp.com
heroku config:set API_KEY=123334979696849
heroku config:set API_SECRET=Jvd78nFKUziejHAW-b5Qn0gLuHk
heroku config:set CLOUDINARY_URL=cloudinary://123334979696849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
heroku config:set CLOUD_NAME=da7srpwm6
heroku config:set DEBUG=False
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set MODE=prod
heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'



git branch main
git switch main

python manage.py collectstatic
pip freeze > requirements.txt

git add .
git commit -m "heroku deployment"
git push heroku main



# heroku run python manage.py makemigrations
# heroku run python manage.py migrate

heroku pg:push wakanda_community DATABASE_URL --app wakanda-community
heroku open