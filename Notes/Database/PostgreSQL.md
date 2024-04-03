# PostgreSQL for Windows メモ

- [PostgreSQL for Windows メモ](#postgresql-for-windows-メモ)
  - [ドキュメント](#ドキュメント)
    - [基礎的な概念](#基礎的な概念)
    - [使い方](#使い方)
  - [導入](#導入)
      - [PostgreSQLサーバーの起動](#postgresqlサーバーの起動)
      - [Postgresサーバーにアクセス](#postgresサーバーにアクセス)
      - [DBの作成](#dbの作成)
  - [Glossary](#glossary)


## ドキュメント
[公式サイト](https://www.postgresql.org/docs/)からアクセスできる．
PDFでダウンロードもできる．

### 基礎的な概念
- アーキテクチャ
    - Server/Clientモデル
        - Supervisor serverが常に実行され，clientからアクセスされるたびに新しいプロセスをForkする

### 使い方
## 導入
PostgreSQLのインストーラを[公式サイト](https://www.postgresql.org/download/)から取得しインストールする．
インストールしたbinディレクトリにパスを通す．

#### PostgreSQLサーバーの起動
Windowsでインストーラを使って導入した場合，サービス(postgresql-xxx-xx)として登録されるため，これをサービスマネージャで操作する．
デフォルトではスタートアップ時に起動するため，起動の操作は基本的に必要ない．

#### Postgresサーバーにアクセス
```cmd
$ psql -U <user_name>
```
Windowsインストーラでインストールした場合，superuserのユーザー名は`postgres`．

- よく使うコマンド
    - `\l`: データベースのリスト表示
        - `\l+`: 詳細表示
    - `\c <db_name>`: データベースアクセス
    - `\h <command>`: コマンドヘルプ
    - `\q`: 終了

#### DBの作成
```bash
create database <db_name>;
```
db_nameのデフォルト値は`default`．




## Glossary
- RDBMS(ORDBMS): (object-)relational database management system