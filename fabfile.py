# -*- coding: utf-8 -*-
from fabric.api import sudo


#
# 「今日からすぐに使えるデプロイ・システム管理ツール Fabric 入門」用サンプルコード
# http://d.hatena.ne.jp/shiumachi/20130414/1365920515
#


def install_git():
    sudo("yum -y install git")


def remove_git():
    sudo("yum -y remove git")

    
def adduser_hoge():
    sudo("adduser hoge")
  
