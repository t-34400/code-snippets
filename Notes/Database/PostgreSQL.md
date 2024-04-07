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
      - [Operators](#operators)
      - [Tableの作成](#tableの作成)
      - [Tableの削除](#tableの削除)
      - [Rowの追加](#rowの追加)
      - [SELECT文](#select文)
        - [Table間の結合](#table間の結合)
        - [Aggregate functions](#aggregate-functions)
      - [UPDATE文](#update文)
      - [DELETE文](#delete文)
      - [VIEW](#view)
      - [Foreign Key](#foreign-key)
      - [Transaction](#transaction)
        - [Savepoint](#savepoint)
      - [Window function](#window-function)
      - [flat-textファイルからの読み込み](#flat-textファイルからの読み込み)
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
#### Operators
- Unary
  - `+`, `-`
- Binary
  - `+`,`-`,`*`,`/`: Arithmetic operators
  - `||`: 文字列の結合
  - 
#### Tableの作成
```bash
CREATE TABLE <schema_name>.<table_name> (
    <column_name> <type> <constraint>,
    ...
    <constraint>
);
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
  - `primary key`: 主キー
  - `not null`: 非NULL
  - `unique`: 一意
  - `CONTRAINT <constraint_name> CHECK (<condition>)`: カスタムconstraint
    - サンプル: `CONSTRAINT age_check CHECK (age >= 0)`
- schemaを指定しない場合，`public` schemaに作成される

#### Tableの削除
```bash
DROP TABLE <table_name>;
```

#### Rowの追加
```bash
INSERT INTO <table_name> (<column_name>, ...) VALUES (<value>, ...), ...;
```
- 成功した場合，`INSERT <AFFECTED_ROWS_COUNT> <INSERTED_ROW_COUNT>`と出力される．

#### SELECT文
```bash
SELECT <column_expresiion>, ... 
    FROM <table_name> 
    WHERE <condition> 
    ORDER BY <column_expresiion>;
```
- カラムの部分はexpressionを使うことができる
  - サンプル: `SELECT (column_1 + column_2)/2 AS avg FROM my_table`
- 一意のデータを取得するときには，`SELECT DISTINCT`を使う．
- 文字列でフィルタリングする場合`WHERE <string_column_name> LIKE <pattern>`を使う．
  - ワイルドカード
    - `%`: 0文字以上の任意の文字列
    - `_`: 任意の1文字
- 降順で並べたい場合は`ORDER BY <column_expression> DESC`を使う．

##### Table間の結合
```bash
SELECT <column_expression> 
    FROM <first_table_name>
    JOIN <second_table_name>
    ON <condition>;
```
- 同じテーブルを`JOIN`することもできる．
- デフォルトでは結合条件を満たさないrowは返さない(inner join)．
  - `JOIN`コマンドを変更することで，挙動を変えることができる．
    - `INNER JOIN`: 結合条件を満たすrowのみ返す
    - `LEFT OUTER JOIN`: 左側のtableのすべてのrowと，右側のtableの条件を満たすrowを返す
    - `RIGHT OUTER JOIN`: 右側のtableのすべてのrowと，左側のtableの条件を満たすrowを返す
    - `FULL OUTER JOIN`: 両方のtableに存在するすべてのrowを返す
- カラム名を指定する際に，明示的に属するテーブルを指定できる(`<table_name>.<column_name>`)
  - FROM句やJOIN句でエイリアスを宣言できる（`SELECT t1.column1, t2.column2 FROM table1 t1 JOIN table2 t2`）

##### Aggregate functions
`SELECT`句内で複数の列から1つの値を得るために使う．
```bash
SELECT <aggregate_expression> 
    FROM <table_name>;
```

- 例:
  - `max()`
  - `min()`
  - `avg()`
  - `sum()`
  - `count()`
- `GROUP BY <column_name>`であるカラムごとにグループ化して返すことができる．
  - `HAVING <aggregate_condition>`で返すグループをフィルタリングできる．
    - サンプル:
      ```bash
      SELECT column1, count(*), max(column2)
        FROM table1
        GROUP BY column1
        HAVING max(column2) < 100;
      ```
  - `WHERE`句はaggregateが計算される前に実行されるのに対し，`HAVING`はaggregateが計算されたあとに実行される．
    - そのため，`WHERE`句内ではaggregate functionを使用できない．
      - 同様のことを`WHERE`句で行いたい場合は，`WHERE`句内でqueryの結果を利用する．
          ```bash
          SELECT * FROM table1
              WHERE column1 = (SELECT max(column1) FROM table1);
          ``` 
    - aggregate functionを含まない`HAVING`句は`WHERE`句で同等の操作を行うよりも効率が落ちるため，一般的に`HAVING`句はaggregate functionを常に含む．
  - `FILTER`句で，一部のaggregate計算への入力のフィルタリングを行うことができる．
    - サンプル: `SELECT count(*) FILTER (WHERE column1 >= 0), max(column1);`
      - この場合，column1が0よりも小さいrowはcountには入力されないが，maxには入力される．
    - aggregateが計算される前に実行されるため，aggregate functionは使用できない．

#### UPDATE文
```bash
UPDATE <table_name>
    SET <column_name> = <column_expression>, ...
    WHERE <condition>;
```

#### DELETE文
```bash
DELETE FROM <table_name>
    WHERE <condition>
```

#### VIEW
複数のTableからデータを取得して仮想的なTableとして扱うことができる．
```bash
CREATE VIEW <view_name> AS
    SELECT <column_expression>, ...
    FROM <table_name>, ...
    WHERE <condition>;
```
- 普通のtableと同様にFROM句で名前を指定してアクセスできる
  - `SELECT <column_expression> FROM <view_name>;`

#### Foreign Key
１つのtable(child-table)の列の値が，他のtable(parent-table)の列の値と一致する必要がある場合に使う．
```bash
CREATE TABLE <child_table_name> (
    <column_name> <type> references <parent_table_name>(<parent_column_name>),
    ...
);
```
- 外部キーが参照する列は`unique`か`primary key` constraintをもつ必要がある．

#### Transaction
一連の動作を不可分として扱い一部のみが実行されないことを保証したい際に使われる．
これに加え，transactional databaseでは以下が保証される．
- 処理が成功したときに永続ストレージに保存される．
- transactionの処理中に同時に実行中の他のtransactionの影響を受けない．

```bash
BEGIN;

# UPDATE ...

COMMIT;
```
- 変更を保存せず元の状態に戻したい場合は`ROLLBACK`を使う．
- PostgreSQLでは，transaction blockに囲まれていないすべてのSQL文が，暗黙的に`BEGIN`と`COMMIT`で囲まれているものとして扱う．

##### Savepoint
ロールバックする内容を細かく制御したい場合は`SAVEPOINT`を使用する．
```bash
BEGIN;
# UPDATE ...
SAVEPOINT <savepoint_name>;
# UPDATE ...
ROLLBACK TO <savepoint_name>;
# UPDATE ...
COMMIT;
```
- 不要なSavepointは`RELEASE SAVEPOINT <savepoint_name>`で解放するとリソースを回収できる．
  - 解放するSavepointよりも後に定義されたSavepointも解放される．

#### Window function
現在のrowに関連するrowのセット(window frame)に対して計算を実行したい場合に用いる．
```bash
SELECT <window_expression> OVER (
            PARTITION BY <partition_column_name>
            ORDER BY <column_name>
        ) AS <window_column_name>
    FROM <table_name>;
```
- `PARTITION BY`を指定しない場合，すべての行を含む単一のpartitionの上で計算が行われる．
- `ORDER BY`句が指定されている場合，window frameにはpartition内の最初の行から現在の行までのすべての行が含まれる．
  - `ORDER BY`句が指定されていない場合は，partition内のすべての行が含まれる．
  - `ORDER BY`句に複数のカラムを指定すると，最初のカラムが同じ値の場合に次のカラムの値で順序が決まる．
- window functionは，`SELECT`リストと`ORDER BY`句の中でのみ使うことができる．
  - `WHERE`などでwindow functionの結果を使用したい場合は，サブクエリを使う
    - サンプル:
        ```bash
        SELECT name
            FROM 
                (SELECT rank OVER (PARTITION BY class, ORDER BY score)　AS score_rank
                    FROM score_table
                ) AS ss
        WHERE score_rank < 3;
        ```
- 同一クエリ内で複数のwindow functionに同一の入力を行いたい場合，`WINDOW`句で定義することができる．
    ```bash
    SELECT <window_expression> OVER <window_name>, ...
        FROM <table_name>
        WINDOW <window_name> AS (...);
    ```
  
#### flat-textファイルからの読み込み
```bash
COPY <table_name> FROM <file_path>;
```

## Glossary
- RDBMS(ORDBMS): (object-)relational database management system
- atomic: Transactionが一連の操作を不可分の単位として扱う性質のこと．途中の何処かでエラーが発生した場合すべての変更がロールバックする．