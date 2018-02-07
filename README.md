# python脚本查火车票余票量

### 使用方法
python tickets.py [-dgktzl] 起点 终点 日期
例如：
> python tickets.py -d 北京 上海 2018-02-07
> // -d 动车
> // -g 高铁
> // -k 快速
> // -t 特快
> // -z 直达
> // -l 临时

### 运行环境
1. python3
2. 安装了requests、docopt包