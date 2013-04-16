fabric-sample
=============

Fabric sample code

shiumachi のブログにて紹介したFabricのサンプルコードです。

今日からすぐに使える構成管理ツール Fabric 入門

http://d.hatena.ne.jp/shiumachi/20130414/1365920515

Fabric の run() メソッドと sudo() メソッド

http://d.hatena.ne.jp/shiumachi/20130417/1366126368


使い方
======

git clone あるいはダウンロードしたら、そのディレクトリに移動して ```fab --list``` と入力してください。
コマンド一覧が出力されます。

コマンドを実行するには、以下のように入力してください。

```
 $ fab -u [ユーザ名] -i [sshの公開鍵] -H [ホスト名] [コマンド名]
```



例:

```
 $ fab -u ec2-user -i ~/.ssh/id_rsa -H ec2-XXX.ap-northeast-1.compute.amazonaws.com install_git
```
