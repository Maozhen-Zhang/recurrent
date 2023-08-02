import visdom

# 创建一个 Visdom 实例
vis = visdom.Visdom()

# 创建一个简单的条形图
x = [1, 2, 3, 4, 5]
y = [10, 5, 7, 3, 8]
vis.bar(X=y, opts=dict(rownames=x))

# 创建一个简单的折线图
x = [1, 2, 3, 4, 5]
y = [0.1, 0.2, 0.3, 0.2, 0.4]
vis.line(Y=y, X=x)
