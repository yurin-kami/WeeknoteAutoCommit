# 仅用于方便学校的同学
## 食用方法
### 安装依赖python==3.12
```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 下载浏览器session driver直接解压到项目根目录path/to/WeeknoteAutoCommit/
![image](https://github.com/user-attachments/assets/2f2535bb-8e08-48a8-b18a-f1869a8e919f)
![image](https://github.com/user-attachments/assets/c32889d4-23a5-4669-b163-bca54166a5cf)
#### 创建Experience目录存放心得并按周数命名
![image](https://github.com/user-attachments/assets/e324fccf-e2e6-4439-9514-799ff0eb47ae)
#### 周记同上
![image](https://github.com/user-attachments/assets/a19b5be9-d37d-4c90-929a-305be46ca234)
### 在main.py文件中配置浏览器driver 路径，示例
![image](https://github.com/user-attachments/assets/4835a848-1dd6-448d-a344-8c9d399f08b5)
### 编辑commit.bat(示例配置)
```cmd
D:#切换到盘符
cd D:\path\to\WeeknoteAutoCommit#切换目录到项目根路径
path\to\python main.py#启动项目
pause#卡住终端
```
### 设置Windows系统的定时任务，每周的某一天启动commit.bat，百度即可
