from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()

# create_app 関数を作成する
def create_app():
    # Flask インスタント生成
    app =  Flask(__name__)
    # アプリのコンフィグ設定をする
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=
            f"sqlite:///{Path(__file__).parent.parent / 'local.splite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    #Migrateとアプリを連携する
    Migrate(app, db)

    # crud パッケージから views を import する
    from apps.crud import views as crud_views

    # register_blueprint を使い views の crud をアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app