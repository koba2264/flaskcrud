from flask import Flask

# create_app 関数を作成する
def create_app():
    # Flask インスタント生成
    app =  Flask(__name__)

    # crud パッケージから views を import する
    from apps.crud import views as crud_views

    # register_blueprint を使い views の crud をアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app