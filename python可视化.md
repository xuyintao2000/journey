# 本节课目标
 可视化是量化中的关键辅助工具之一，量化中往往需要通过可视化技术来更清晰的理解交易，理解数据。通过可视化技术可以更加快速的对量化交易系统中的问题进行分析，更容易发现策略中的问题，进一步指导策略的开发。今天我们就以一个零投资组合的输出数据为基础，看看如何绘制一个累计收益图和收益分布直方图。这个组合的因子是销售毛利率，时间跨度从2017年1月1日至2018年1月1日，调仓周期为30天。

# 使用matplotlib可视化数据



## 什么是matplotlib
### Matplotlib来源
-  Matplotlib最早是为了可视化癫痫病人的脑皮层电图相关的信号而研发。因为在函数的设计上参考了MATLAB，所以叫做Matplotlib。


### matplot的核心
  Matplotlib的核心对象是一套绘图API。在我们熟悉了核心对象之后，可以轻易的定制图像：包括散点图;等高线图;条形图;柱状图;3D图形,甚至是图形动画等等。
  事实上matplotlib是python最基础也最常用的可视化工具，许多更高级的可视化库就是在matplotlib的基础上再次开发。而且matplotlib的使用方式和绘制思想已经成为python绘图库的标杆。其他大多数绘图库都会特意使用与Matplotlib类似的函数名称，参数、以及思想。如果掌握了matplotlib的绘制方式及思想，那么在python中使用任何一个可视化库，都会觉得简单易用。
  
  在下面的章节中，我会通过实战案例，讲解matplotlib中常用的绘图API。首先我以《零投资组合累计收益》统计图为例子来介绍一下matplotlib的基本元素。


## matplotlib的基本元素
我们看一下这张图。
首先最外层的是figure,可以理解为画板。
接下来是subplot或Axes，也就是我们实际绘图的区域，可以理解为子画布。
一个画板上可以准备多个子画布，子画布可以按照按顺序排列在画板上。也可以重叠放在一起。也就是说一个figure,包含了多个subplot以及axes。

我解释一下什么是Subplot。举个例子，在画板中央，横竖各画一条线，就形成了4块区域。每一块区域就是一个subplot。
也就是说subplot是按网格分割figure后的子画布。当我们创建了一个subplot，事实上也同时创建了一个Axes数轴区域。

那什么是Axes呢，axes是整个数轴区域。也就是说Axes对应的就是一张子画布。
通常每一个Axes实例包含两个Axis对象。分别是XAxis实例，也就是图上的X轴区域，另外一个是YAxis实例，对应图上的Y轴区域。

我们接着看，这张图的名字是《零投资组合累计收益》，这个名字就是axes实例的title属性。
在图片右上方，红线组合收益，黄线首档收益以及绿线末档收益的这一整块区域就是axes实例的legend属性。

再来看看图上的X轴或Y轴区域，分别对应Axis对象的实例：XAxis以及YAxis。以XAxis为例子，包含了刻度标签tick label、轴的名字label。我这里没有一一标识Axis的所有属性，此外还有刻度tick,以及轴对应的横向空间grid等。

前面介绍的所有的对象。通常在绘制之前， 需要我们决定如何渲染。
也就是设置内容，尺寸size、颜色color以及显示的样式style等。接下看我们看看matplotlib标准的绘图流程。


## matplotlib 绘图流程
 第一步：创建一个画板（figure）实例。
 第二步：使用画板创建一个或多个Axes或subplot实例。
 第三部：调用Axes实例的函数，设置基础图形的各项属性，显示的样式，坐标轴上的数据等等。最后完成图形基础数据。
 前三部都是我们需要完成的工作。接下来是matplotlib帮我们完成的工作。
 第四部：创建基础的Artist实例，也就是我们要绘制的图形，例如我们前面的收益曲线图。
 第五步：把完成的Artist实例，添加到我们制定的画布中。
 第六步：在我们需要的时候绘制图像。
 
 Axes是matplotlib API中最重要的类，因为Axes几乎是所有对象的绘制区域，它有很多函数（plot(),text()）来创建图形基础数据（Line2D）。Axes是我们接下来要介绍的重点。我们下面直接从如何绘制零投资组合累计收益图开始。


## 安装matplotlib
-首先我们需要安装matplotlib。与安装python的其他第三方库一样。我们可以使用pip命令下载，也可以使用whl源码包安装。
大家需要注意的是安装版本要兼容。如果你安装的python是3.7版本的。那么在安装matplotlib的时候，你可能会遇到各种奇葩的错误。原因是matplotlib目前还没有基于python3.7的版本，解决办法是卸载python3.7, 重新安装python3.6。

## 创建画版- figure
首先，我们来看一下引用matplotlib的方式。import matplotlib.pyplot as plt， 这是一般习惯及推荐引用的matplotlib的方式。
本节课所有的例子，以 plt 作为 matplotlib.pyplot 的省略。

接下来，我解释一下plt究竟可以做什么。plt包含一系列绘图函数。每个 plt中的函数都可以对当前的图像进行一些修改，例如：产生新的图像，在图像中产生新的绘图区域，在绘图区域中画线，给绘图加上标记，等等…… plt 会自动记住当前的图像和绘图区域，因此这些函数会直接作用在当前的图像上。

重点说一下，plt.show()函数， 默认是在新窗口打开一幅图像，并且提供对图像进行操作的按钮。默认情况下，plt 不会直接显示图像，只有调用 plt.show()函数时，图像才会显示出来。

已经介绍了如何引用plt以及plt的可以做的事情。接下来我们看看在代码中，如何使用plt来创建图形数据？

下面代码中，我们通过plt.figure命令创建了一个Figure对象实例，也就是我们要绘图的画板。画板figure是最外层的绘图单位，默认是以 1 开始编号，这种编号方法来源于MATLAB 风格。

接下来我解释一下plt.figure函数接收的参数。
plt.figure函数接收的参数就是当前画板要设置的属性，包括大小，背景色等等。我们这里设置了两个参数，分别是figsize和facecolor。
figsize是一个tuple类型的数据:表示图片宽度和高度，单位是英寸，在使用默认dpi时，1英寸=100px。我们这里设置了figsize=(14,5),也就是说我们生成的图像大小是1400*500。
facecolor是背景色，可接受的范围有三类：第一类是16进制编码的颜色，例如#FFFFFF表示黑色。第二类是表达颜色的英文单词，例如blue，white等。第三类是第二类的英文首字母。例如‘W’表示白色。更多的取值范围可查看matplotlib的API。
除了figsize,facecolor参数外，可以指定的参数还有num,dpi等，我已经给出了注释，这里就不再一一详细介绍了。这些参数都是figure的属性，同样的也可以通过 Figure 对象的 set函数来改变。
我下面给出的是完整代码，可直接运行。这段代码最后生成了一张背景是白色，大小是1400*500的png图片。


```
import matplotlib.pyplot as plt

# 创建自定义图像
# num :编号
# figsize : 图像大小
# dpi :分辨率
# facecolor :背景色  blue/white/#FFFFFF等等 
# edgecolor : 边界颜色
# frameon - 边框
fig=plt.figure(figsize=(14,5),facecolor='white')
plt.show()

```

### 分割画板，创建子画布 - subplot


我们前面讲过，figure是画板，axes和subplot是画布，我们已经准备好了画板，接下来开始创建画布。
这里我们使用add_subplot函数新增子画布，这个函数可以规划画板，将画板划分为n个子画布，并指明子画布的位置。但每条add_subplot命令只会创建一个子画布。 我们第一次调用add_subplot命令，输入参数是1,2,1, 是将画板分成1行两列，并在第一行第一列的位置生成子画布ax1。第二次调用add_subplot命令，输入参数是1,2,2，表示在第一行第二列生成子画布ax2。
接下来我们看看add_subplot的参数。
我们的代码中使用了三个参数numrows，numcols，fignum，关于每个参数的意义，你可以看一下代码中的注释。我这里提下需要的地方。在传入这三个参数的时候，如果三者乘积小于10，可以不使用逗号分开。例如， 221和2,2,1都表示numrows=2，numcols=2， fignum =1。为了增加代码的可读性，我建议大家还是要使用逗号分开参数的写法。
在这段代码中，我们使用的是add_subplot命令创建子画布。事实上，figure还提供了add_axes函数，用来创建一个数轴区域axes。我们之前讲过，axes是更灵活的subplot。
也就是说axes可以座落在figure内的任意位置上，而且axes可任意设置大小。因为我们的实战案例没有使用到这个功能。我就不在这里演示了。

```
    import matplotlib.pyplot as plt

    # 新建figure对象
    fig = plt.figure(figsize=(14, 5), facecolor='white')
     # numrows：subplot的行数
     # numcols：subplot的列数
     # fignum： 位置标号
     
     # sharex：为所有的subplot指定相同的X轴刻度
     # sharey：为所有的subplot指定相同的Y轴刻度
     # subplot_kw：用于创建各subplot的关键字字典
     # **fig_kw：创建figure时的其他关键字 如plt.add_subplots(2,2,figuresize=(14, 5))
    # 新建子图1。将figure分成1x2个格子，占用第一个，即第一行第一列的子图
    ax1 = fig.add_subplot(1, 2, 1)
    # 新建子图2
    ax2 = fig.add_subplot(1, 2, 2)
    # 显示图片
    plt.show()
```


### 累计收益曲线图
按着matplotlib的画图流程，在创建了画板和画布后，就可以准备绘图了。
接下来我们开始绘制零投资组合累计收益曲线图。
我们首先加载零投资组合累计收益统计数据，在统计区间内，有多个调仓日，每个调仓日，分别对应的有hs300收益、首档收益、末档收益以及组合收益。这些数据都是我们提前准备好的。
有了统计数据以后，通过调用plot函数分别绘制4条收益曲线。以调仓日，做为X轴数据，以4组收益的值做为Y轴数据。
plot函数的签名参数有color, linewidth, linestyle等。
首先看一下color参数。我们前面讲过如何使用plt.figure函数创建画板figure实例，plt.figure函数有一个设置背景色的签名参数facecolor，facecolor与color一样，可接受的颜色取值范围
与color一样。

接着看一下plot函数的签名参数linestyle。可接受的参数范围有两类：第一类是可表达形状的字符串，第二类是描述形状的单词等。
我在代码中分别使用了实线，虚点线、点线以及虚线的表达方式。喜欢动手的同学可以运行源代码，对比一下显示效果。更多关于linestyle参数的取值范围可以参考API中关于linestyle的说明。

我在代码中分4次调用plot函数设置4条线的数据，是为了演示不同曲线的设置参数。这样的重复调用，代码虽然清晰，但是看起来也比较笨重。你大可不必分4步调用，一条plot命令可接受多条线的数据。


```
    import matplotlib.pyplot as plt
    # 新建figure对象
    fig = plt.figure(figsize=(16, 5), facecolor='white')
    #新建子图1
    ax1 = fig.add_subplot(1, 2, 1)
    # hs300 : hs300收益
    # top: 首档收益
    # bottom: 末档收益
    # group: 组合收益
    # date : 调仓日
    hs300, top, bottom, group, dates = load_data()
    
    # 收益曲线颜色
    colors = ['red', 'y', '#53d79a', '#2f4554']
    
    # color:曲线颜色 linewidth:线条宽度  linestyle:线条颜色
    ax1.plot(dates, hs300, color=colors[0], linewidth=1, linestyle="dashed")
    ax1.plot(dates, top, color=colors[1], linewidth=2, linestyle=":")
    ax1.plot(dates, bottom, color=colors[2], linewidth=2, linestyle="-.")
    ax1.plot(dates, group, color=colors[3], linewidth=2, linestyle="-",)
    
    # 新建子图2
    ax2 = fig.add_subplot(1, 2, 2)
    # 显示图片
    plt.show()
```

### 设置数轴-xticks

我们首先设置了画版figure，然后设置了subplot将画板分割成了2块，并且在第一块画布使用plot函数，绘制了累计收益曲线图。在绘制之前，我们分别设置了曲线的颜色，线条的宽度。
在这个实战案例中，我们的X轴接收的都是日期格式的字符串，如果日期很多，那么在X轴上就很拥挤，看一下这个图。

关于坐标轴刻度的问题，如果坐标轴接收的是数字，数轴在显示的时候会统一刻度。例如我们的Y轴，接收了从-20到30区间的不同数字。最后统一个-20-20这个区间来显示。如果接收的是多组字符串，那么刻度就是所有的字符串。例如X轴。

我们需要对X轴刻度处理一下。每隔1个调仓日，我们定义一个刻度。最后通过set_xticks函数设置设置X轴显示的刻度。注意我们并没有修改收益对应的日期，这里只是设置了绘制的刻度。

```
    #定义x轴刻度列表
    xticks_date = []
    
    # 每隔两个刻度设置一次日期
    for i in range(len(dates)):
        if i % 2 == 0:
            xticks_date.append(dates[i])
        else:
            xticks_date.append('')
            
    # 设置X轴显示的刻度
    ax1.set_xticks(xticks_date)
```


### 画布标题-title, 图例标注-legend


我们使用plot函数绘制了4条收益曲线，并优先了日期的显示问题。但是最终的图中并没有标注哪一条曲线是HS300收益，哪一条曲线是组合收益。下面的代码展示的是如何通过legend函数操作标注，参数loc代表标注的位置。
到这里，我们首次输入了中文表，很快就会发现中文没有办法显示。
产生这个问题的主要原因是matplotlib库中没有中文字体。我下面第二段代码展示的是通过设置默认字体来解决。还有其他解决方法，好奇的同学可以自己探索一下。需要主要的是，通常我们在导入pyplot之后，创建画板之前，设置默认字体。因为这个是全局的属性。此外，负号通常也不能正常显示，我们这里设置unicode_minus来解决。

每个收益曲线都对应到了自己的名字。现在是时候给整个画布命名了。这里我们使用的是title函数。看一下第三段代码。

- 


```
#设置legend标注
ax1.legend(['HS300收益', '首档收益', '末档收益', '组合收益'], loc=1)

```


```
#中文乱码问题
import matplotlib.pyplot as plt
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 坐标轴负号显示
plt.rcParams['axes.unicode_minus'] = False
# 新建figure对象
fig = plt.figure(figsize=(16, 5), facecolor='white')
```

```
#图片命名
ax1.set_title('零投资组合累计收益')
```

### 收益分布直方图

本节课的目标是绘制零投资组合的累计收益图和收益分布直方图。前面我们定义了两块画布，第一块已经完成了累计收益图的绘制，接下来，我们再来看看如何绘制另外一个收益分布图。
首先还是准备数据，通过bar函数我们开始绘制直方图。
事实上，bar函数最终返回的是BarContainer对象。它的签名参数有4个，分别是left,height,width,bottom,这个参数确定了柱体的位置和大小。需要额外注意的是，默认情况下，left为柱体的居中位置。
可以通过align参数来改变left值的含义。
举个列子：我们可以通过设置left-width/2
剩下的设置就与画直线图的流程一样。
如前面不同的是，这里设置了X轴的旋转，主要是因为单个收益区间名，字符串比较长，但是又必须完全显示。所以这里使用旋转字符串，防止刻度彼此重叠。


```
# 期数
counts = [1, 0, 1, 2, 0, 1, 1, 1, 0, 2]
# 收益区间
profits = ["-4.95~-4.07", "-4.07~-3.19", "-3.19~-2.31", "-2.31~-1.43",
           "-1.43~-0.55", "-0.55~0.34", "0.34~1.22", "1.22~2.1",
           "2.1~2.98", "2.98~3.86"]
#设置x轴以及bar的高度
ax2.bar(profits, counts)
ax2.set_title('零投资组合收益分布')
# 设置X轴名字
ax2.set_xlabel('收益区间')
# 设置Y轴名字
ax2.set_ylabel('期数')

#旋转X轴刻度
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(15)
# 显示图片
plt.show()

````





### 保存图片

我们已经绘制完成了零投资组合的统计图。接着看看如何保存已经绘制的图片。
在下面代码中，savefig命令保存图片。需要注意的是，先使用savefig命令，再调用show函数。一定要按顺序来。为什么这么做，你可以回想一下matplotlib的绘图流程。matplotlib库实现量化数据可视化的介绍就讲解到这里。更多关于matplotlib的用法可以访问它的官方网址。

有些时候将一段数据可视化以后，还会有交互操作的要求，举个例子，如果我们零投资组合设置回测周期为10年，调仓周期10天，最后的期数有200多期，受限于屏幕宽度，没办法在X轴上一一显示。这个时候就需要能拖动X轴的时间窗口，查看不同时间段的调仓统计。实现这种交互的解决方案一般是通过网页形式的可视化，配合javascript与网页完成交互。请关注我们接下来的课程《HTML5可视化》，学习量化数据如何通过网页可视化。今天我的分享就到这里了，谢谢大家。

```
    # 默认保存为png格式
    plt.savefig('零投资组合.png')
    plt.show()
```





