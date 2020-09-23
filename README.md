# 自用脚本
## addNewGitAccount.sh
添加git环境
命令
```sh
sh ./addNewGitAccount.sh -h 'github.com' -n 'github.com' -u 'yulinfox@163.com' -i 'C:/Users/Toroto/.ssh/id_rsa_github'
```
执行后在命令行得到：
```
#config文件通过host区分不同的托管库
Host github.com
HostName github.com
User yulinfox@163.com
IdentityFile C:/Users/Toroto/.ssh/id_rsa_github
```
拷贝后放到自己的 .ssh 文件夹下的 config 文件中保存即可
