# Demo
日常代码存储库;将日常优秀的代码存于此库;

## Python常用模块

| 模块名称 | 说明           | 参考文档                                                   |
| -------- | -------------- | ---------------------------------------------------------- |
| loguru   | 记录日志       | [详情请点击此链接](https://www.jianshu.com/p/3794c018886b) |
| tqdm     | 进度条         | [详情请点击此链接](https://www.jianshu.com/p/21cf48be6bf6) |
| pandas   | 操作XLS文件    |                                                            |
| pprint   | 格式化打印格式 | 内置模块;from pprint import pprint                         |
| timeit   | 性能分析       |                                                            |
|          |                |                                                            |
|          |                |                                                            |

## pip导出依赖包

```python
# 1.导出python依赖包
pip freeze > requirements.txt
# 2.根据导出依赖包文件批量安装依赖包并且从指定镜像地址下载
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 3.根据导出依赖包文件批量卸载依赖包
pip uninstall -r requirements.txt -y

```