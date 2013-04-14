from fabric.api import sudo


def install_git():
    sudo("yum -y install git")


def remove_git():
    sudo("yum -y remove git")

    
def adduser_hoge():
    sudo("adduser hoge")
  
