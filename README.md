# PracticeDjango

## 基本操作

#### djangoのインストール
pip install django
#### バージョンの指定(4.2.2)
pip install django==<version>
#### djangoプロジェクトの作り方
django-admin startproject <project_name>
#### django簡易サーバーの起動
py manage.py runserver
#### djangoアプリケーションの作成(1つ目のdjango_app上の階層)
py manage.py startapp <app_name>
#### アプリケーションのrequest
http://localhost:8000/<app_name>
#### sessionを扱うには、settings.pyに追記する
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
---
## urls.pyの設定(routeの設定)
