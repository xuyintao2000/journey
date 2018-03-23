# 为什么要可视化
可视化是量化中的关键辅助工具之一，量化中往往需要通过可视化技术来更清晰的理解交易，理解数据。通过可视化技术可以更加快速的对量化交易系统中的问题进行分析，更容易发现策略中的问题，进一步指导策略的开发。

# matplotlib的优点
matplotlib是python最基础也最常用的可视化工具，许多更高级的可视化库就是在matplotlib的基础上再次开发。而且matplotlib的使用方式和绘制思想已经成为python绘图库的标杆。其他大多数绘图库都会特意使用与Matplotlib类似的函数名称，参数、以及思想。如果掌握了matplotlib的绘制方式及思想，那么在python中使用任何一个可视化库，都会觉得简单易用。



# matplotlib的基本元素

首先最外层的是figure,可以理解为画板。接下来是subplot或axes，也就是我们实际绘图的区域，可以理解为子画布。

什么是subplot。subplot是按网格分割figure后的子画布。当我们创建了一个subplot，事实上也同时创建了一个axes数轴区域。

那什么是axes呢，axes是一个数轴区域。通常一个axes包含两个axis对象。分别是xaxis实例，也就是X轴区域，另外一个是yaxis实例，对应Y轴区域。另外axes还包含legend(图例)、title（子图标题）等属性。

Axis实例则包含了刻度标签tick label、轴的名字label、有刻度tick,以及轴对应的横向空间grid等。

通常在绘制之前，需要设置内容，尺寸size、颜色color以及style，来决定图形如何渲染。

# 使用对象式操作绘图流程

 第一步：创建一个画板（figure）实例。
 第二步：使用画板创建一个或多个axes或subplot。
 第三步：调用Axes实例的函数，设置基础图形的各项属性，显示的样式，坐标轴上的数据等等。最后完成图形基础数据。
 第四步：创建基础的artist实例，也就是我们要绘制的图形。
 第五步：把完成的artist实例，添加到我们指定的画布中。
 第六步：在我们需要的时候绘制图像。通常是调用show函数。
 
 前面三步是我们需要实现的，后面三步是matplotlib根据我们设置的图形数据完成的。
 
# 绘制零投资组合收益统计
 
 组合的因子是销售毛利率，时间跨度从2017年1月1日至2018年1月1日，调仓周期为30天。
 通过计算，一共得到4组数据。
 ```
    # hs300 : hs300收益
    # top: 首档收益
    # bottom: 末档收益
    # group: 组合收益
    # date : 调仓日
    
 ```
 
 开始绘图
 
 ```
import matplotlib.pyplot as plt

# 用来正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 坐标轴负号显示
plt.rcParams['axes.unicode_minus'] = False

 # 新建figure实例
fig = plt.figure(figsize=(16, 5), facecolor='white')
# 新建子图1，这里设置1*2个子画布。实际只用了一个
ax = fig.add_subplot(1, 2, 1)
# 加载数据
hs300, top, bottom, group, dates = load_data()
# 收益曲线颜色 
colors = ['red', 'y', '#53d79a', '#2f4554']
# color:曲线颜色 linewidth:线条宽度  linestyle:线条颜色
# 为了方便观察，分4次调用
ax.plot(dates, hs300, color=colors[0], linewidth=1, linestyle="dashed")
ax.plot(dates, top, color=colors[1], linewidth=2, linestyle=":")
ax.plot(dates, bottom, color=colors[2], linewidth=2, linestyle="-.")
ax.plot(dates, group, color=colors[3], linewidth=2, linestyle="-", )

# 设置legend标注
ax.legend(['HS300收益', '首档收益', '末档收益', '组合收益'], loc=1)

# 图片命名
ax.set_title('零投资组合累计收益')
# 显示图片
plt.show()
 ```
 
 
 有些时候将一段数据可视化以后，还会有交互操作的要求，举个例子，如果我们零投资组合设置回测周期为10年，调仓周期是10天，最后的期数有200多期，受限于屏幕宽度，没办法在X轴上一一显示。这个时候就需要能拖动X轴的时间窗口，查看不同时间段的调仓统计。实现这种交互的解决方案一般是通过网页形式的可视化，配合javascript与网页完成交互。
 
 
 
 
