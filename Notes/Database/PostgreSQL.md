# PostgreSQL for Windows メモ

- [PostgreSQL for Windows メモ](#postgresql-for-windows-メモ)
  - [ドキュメント](#ドキュメント)
    - [基礎的な概念](#基礎的な概念)
    - [使い方](#使い方)
      - [導入](#導入)
      - [PostgreSQLサーバーの起動](#postgresqlサーバーの起動)
      - [Postgresサーバーにアクセス](#postgresサーバーにアクセス)
      - [DBの作成](#dbの作成)
    - [SQLの基礎](#sqlの基礎)
      - [Tableの作成](#tableの作成)
      - [Tableの削除](#tableの削除)
      - [Rowの追加](#rowの追加)
  - [Glossary](#glossary)


## ドキュメント
[公式サイト](https://www.postgresql.org/docs/)からアクセスできる．
PDFでダウンロードもできる．

### 基礎的な概念
- アーキテクチャ
    - Server/Clientモデル
        - Supervisor serverが常に実行され，clientからアクセスされるたびに新しいプロセスをForkする

### 使い方
#### 導入
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
    - `\dt`: テーブルのリスト表示
      - `\dt+`: 詳細表示
    - `\d <table_name>`: カラムの表示
    - `\h <command>`: コマンドヘルプ
    - `\q`: 終了

#### DBの作成
```bash
create database <db_name>;
```
db_nameのデフォルト値は`default`．

### SQLの基礎
#### Tableの作成
```bash
CREATE TABLE <schema_name>.<table_name> (
    <column_name> <type> <constraint>,
    ...
    <constraint>
)
```
- typeの例
  - `int`: 32-bit integer
  - `smallint`: 16-bit integer
  - `real`: 32-bit floating point number
  - `double` : 64-bit floating point number
  - `char(N)`: Fixed-length string (space padding)
  - `varchar(N)`: Variable-length string
  - `date`: Date
  - `time`: Time
  - `timestamp`: Date and time
  - `interval`: Time interval
  - PostgreSQL-specific data type
    - `serial`: 整数値，自動で増分されるシーケンス
    - `point`: 2D geometric point represented by x and y coordinates
- constraintの例
  - `PRIMARY KEY`: 主キー
  - `NOT NULL`: 非NULL
  - `UNIQUE`: 一意
  - `CONTRAINT <constraint_name> CHECK (<condition>)`: カスタムconstraint
    - サンプル: `CONSTRAINT age_check CHECK (age >= 0)`
- schemaを指定しない場合，`public` schemaに作成される

#### Tableの削除
```bash
DROP TABLE <table_name>
```

#### Rowの追加
```bash
INSERT INTO <table_name> VALUES (<value>, ...)
```


## Glossary
- RDBMS(ORDBMS): (object-)relational database management system