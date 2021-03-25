### 基本的SQL指令
- 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。
INSERT INTO user (name, username, password) VALUES ('Bonnie','ply', 'ply');
```
mysql> INSERT INTO user (name, username, password) VALUES ('Bonnie','ply', 'ply'
);
Query OK, 1 row affected (0.04 sec)
```


- 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。
SELECT * FROM user;
```
mysql> SELECT * FROM user;
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  1 | Bonnie | ply      | ply      | 2021-03-25 21:17:54 |
|  2 | Tina   | tina     | 1234     | 2021-03-25 21:20:56 |
|  3 | Ray    | ray      | ray00    | 2021-03-25 21:21:40 |
|  4 | Sonia  | sonia    | 0000     | 2021-03-25 21:22:04 |
|  5 | Kay    | kay      | kay000   | 2021-03-25 21:23:37 |
|  6 | Play01 | ply01    | ply      | 2021-03-25 21:24:02 |
|  7 | Play02 | ply02    | ply      | 2021-03-25 21:24:31 |
+----+--------+----------+----------+---------------------+
7 rows in set (0.02 sec)
```


- 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
SELECT COUNT(id) FROM user;
```
mysql> SELECT COUNT(id) FROM user;
+-----------+
| COUNT(id) |
+-----------+
|         7 |
+-----------+
1 row in set (0.09 sec)
```


- 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。
SELECT * FROM user ORDER BY time DESC;
```
mysql> SELECT * FROM user ORDER BY time DESC;
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  7 | Play02 | ply02    | ply      | 2021-03-25 21:24:31 |
|  6 | Play01 | ply01    | ply      | 2021-03-25 21:24:02 |
|  5 | Kay    | kay      | kay000   | 2021-03-25 21:23:37 |
|  4 | Sonia  | sonia    | 0000     | 2021-03-25 21:22:04 |
|  3 | Ray    | ray      | ray00    | 2021-03-25 21:21:40 |
|  2 | Tina   | tina     | 1234     | 2021-03-25 21:20:56 |
|  1 | Bonnie | ply      | ply      | 2021-03-25 21:17:54 |
+----+--------+----------+----------+---------------------+
7 rows in set (0.00 sec)
```


- 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
SELECT * FROM user ORDER BY time DESC LIMIT 1,3;
```
mysql> SELECT * FROM user ORDER BY time DESC LIMIT 1,3;
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  6 | Play01 | ply01    | ply      | 2021-03-25 21:24:02 |
|  5 | Kay    | kay      | kay000   | 2021-03-25 21:23:37 |
|  4 | Sonia  | sonia    | 0000     | 2021-03-25 21:22:04 |
+----+--------+----------+----------+---------------------+
3 rows in set (0.00 sec)
```


- 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
SELECT * FROM user WHERE username='ply';
```
mysql> SELECT * FROM user WHERE username='ply';
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  1 | Bonnie | ply      | ply      | 2021-03-25 21:17:54 |
+----+--------+----------+----------+---------------------+
1 row in set (0.00 sec)
```


- 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。

SELECT * FROM user WHERE username='ply' AND password='ply';
```
mysql> SELECT * FROM user WHERE username='ply' AND password='ply';
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  1 | Bonnie | ply      | ply      | 2021-03-25 21:17:54 |
+----+--------+----------+----------+---------------------+
1 row in set (0.00 sec)
```


- 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。

UPUPDATE user SET name='丁滿' WHERE username = 'ply';
```
mysql> UPUPDATE user SET name='丁滿' WHERE username = 'ply';
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM user;
+----+--------+----------+----------+---------------------+
| id | name   | username | password | time                |
+----+--------+----------+----------+---------------------+
|  1 | 丁滿   | ply      | ply      | 2021-03-25 21:17:54 |
|  2 | Tina   | tina     | 1234     | 2021-03-25 21:20:56 |
|  3 | Ray    | ray      | ray00    | 2021-03-25 21:21:40 |
|  4 | Sonia  | sonia    | 0000     | 2021-03-25 21:22:04 |
|  5 | Kay    | kay      | kay000   | 2021-03-25 21:23:37 |
|  6 | Play01 | ply01    | ply      | 2021-03-25 21:24:02 |
|  7 | Play02 | ply02    | ply      | 2021-03-25 21:24:31 |
+----+--------+----------+----------+---------------------+
7 rows in set (0.00 sec)
```


- 使用 DELETE 指令刪除所有在 user 資料表中的資料。



### 結合資料表 SQL JOIN 的操作 (Optional)
- 使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。

SELECT user.name, message.user_id, message.content, message.time 
FROM message 
LEFT JOIN user ON message.user_id=user.id;
```
mysql> SELECT user.name, message.user_id, message.content, message.time
    -> FROM message
    -> LEFT JOIN user ON message.user_id=user.id
    -> ;
+--------+---------+----------------------------+---------------------+
| name   | user_id | content                    | time                |
+--------+---------+----------------------------+---------------------+
| 丁滿   |       1 | no comment                 | 2021-03-25 21:51:27 |
| Tina   |       2 | Love this very much        | 2021-03-25 21:51:49 |
| Ray    |       3 | Can do better              | 2021-03-25 21:52:13 |
| Sonia  |       4 | la la la la la la la la la | 2021-03-25 21:52:35 |
| Kay    |       5 | no comment                 | 2021-03-25 21:53:49 |
| Play01 |       6 | Love this very much        | 2021-03-25 21:54:06 |
| Play02 |       7 | Can do better              | 2021-03-25 21:54:20 |
| 丁滿   |       1 | dadadadadadadadadadadada   | 2021-03-25 21:54:37 |
| Ray    |       3 | nothing happen             | 2021-03-25 21:55:37 |
+--------+---------+----------------------------+---------------------+
9 rows in set (0.00 sec)
```


- 使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留言，資料中須包含留言會員的姓名。
  SELECT user.name, user.username, message.content, message.time
  
FROM user
LEFT JOIN message ON user.id= message.user_id
WHERE user.username='ply';
```
mysql> SELECT user.name, user.username, message.content, message.time
    -> FROM user
    -> LEFT JOIN message ON user.id= message.user_id
    -> WHERE user.username='ply';
+--------+----------+--------------------------+---------------------+
| name   | username | content                  | time                |
+--------+----------+--------------------------+---------------------+
| 丁滿   | ply      | no comment               | 2021-03-25 21:51:27 |
| 丁滿   | ply      | dadadadadadadadadadadada | 2021-03-25 21:54:37 |
+--------+----------+--------------------------+---------------------+
2 rows in set (0.00 sec)
```
