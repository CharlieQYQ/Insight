# Insight 后端调用说明
> 乔毅 2019210472
> 2021.9.3

**本说明只针对Insight项目后端代码，且随版本不断更新**

## 模块介绍
- 1.短信查询接口
	- 链接地址：http://abc.charlieqyq.top:32222/msg_search
	- 请求关键字
		- msg
			- 查询的短信内容
			- 字符串类型
	- 返回关键字（字典类型）
		- msg_id
			- 短信序号
		- msg_text
			- 短信内容
		- simi_times
			- 相似度超过阈值次数（即返回次数）
		- cs_value
			- 余弦相似度
- 2.短信详情接口
	- 链接地址：http://abc.charlieqyq.top:32222/msg_info
	- 请求关键字
		- id
			- 查询的短信序号
			- 整型
	- 返回关键字
		- msg_text
			- 短信内容
		- msg_analiysis
			- 案例分析
		- simi_times
			- 相似度超过阈值次数（即返回次数）
		- kind_name
			- 案例类别
		- laws
			- 相关法条
		- solutions
			- 解决方法

## 错误信息
- 1.NotFound
	- 输入URL错误时，将返回404错误信息“Room 404 Not Found”
- 2.ServerError
	- 程序运行错误时，将返回ServerError错误信息“Server Error”