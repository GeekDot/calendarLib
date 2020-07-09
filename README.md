<h2 align= center> calendarLib 天干地支纪年法库 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`calendarLib` 天干地支纪年法库，是对中国古代传统的天干地支纪年法进行算法实现和次封装

下面是对 `calendarLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `calendarLib` 的使用 `demo`

### 二、安装

`calendarLib` 是以源码的方式呈现，使用的时候直接导入即可

	from calendarLib import cl
    
### 三、使用

`calendarLib` 库只有一个 `get` 方法，参数类型为 `int` 型，输入其他类型会报错，返回值是字符串型

    cl.get(2019)
