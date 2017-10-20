# AutomaticTools

## 批量处理工具

### autoCheckOut.py

- 对多个git文件进行批量打tag，提交到服务器
- 批量切换多个git文件tag或分支，从服务器拉取数据

#### 使用前配置

1. 将autoCheckOut.py中的project_path，修改为git文件的上级目录
2. 替换AddTagPlist.plist中的文件夹，名称为需要修改的git文件夹

#### 实际使用
批量打tag
```bash
$ python autoCheckOut.py
请输入需要的操作 1：提交tag 2：切换至tag
$ 1
请输入想提交的tag名称（如600）
$ 604
```

批量切换至指定tag
```bash
$ python autoCheckOut.py
请输入需要的操作 1：提交tag 2：切换至tag
$ 2
请输入想切换的tag或者分支名称（如600或者master）
$ 600
是否在切换前拉取master最新代码? Y/N
$ Y
```
