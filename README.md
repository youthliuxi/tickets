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
2. 需要安装的：requests、docopt、colorama、prettytable
3. 编程过程中使用的：pprint

### 遗留问题
1. 多次测试时，总会出现，莫名报错
    测试推测，组建url访问时，时间和车站传递存在遗漏的话，返回的网页就将会是报错网页，而不是json数据包，因此，无法转化为json数据进行解析，才会出现json行报错现象。
    但为什么组建的url会有问题，到底是某个数据的遗漏还是request的过程中，出了问题，还需要进一步讨论。
    不过，最近的测试结果，即便是报错，打印url时，url直接复制到浏览器是可以访问的，所以，应该不是url的问题，问题估计出在request上（mark一下）
2. better的程序在linux系统运行时，各列数据会随机排布，至今不知道为什么。
3. cmd和powershell对Fore定义的色彩显示无效，gitBash打印表格时，所有中文均是雪花，无法显示，xshell已过期，暂未测试。（待更新）
