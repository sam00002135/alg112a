from micrograd import Value

def gradientDescent(f, params, eta=0.01, h=10000):
    params = [Value(x) for x in params]

    for _ in range(h):
        # 前向传播
        f_val = f(*[p.data for p in params])

        # 打印当前状态
        print('params=', [p.data for p in params], 'f(params)=', f_val.data)

        # 反向传播
        f_val.backward()

        # 更新参数
        for p in params:
            p.data -= eta * p.grad

        # 清零梯度
        for p in params:
            p.grad = 0.0

    return ([p.data for p in params], f(*[p.data for p in params]))

def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

gradientDescent(f, [2, 1, 3])
