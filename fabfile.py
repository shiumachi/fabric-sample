# -*- coding: utf-8 -*-
from fabric.api import sudo, run, puts


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


#
# 「Fabric の run() メソッドと sudo() メソッド」用サンプルコード
#  (permal link が決定次第挿入)
#


def run_error_warn_only():
    run("hoge", warn_only=True)


def run_error_warn_only_with_quiet():
    run("hoge", warn_only=True, quiet=True)


def succeeded_sample():
    res = run("hostname", warn_only=True)
    if res.succeeded is True:
        puts("succeeded!")
        return
