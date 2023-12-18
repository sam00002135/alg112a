def gradientDescent(f, p, eta=0.01, h=10000):
    params = p.copy()
    
    for _ in range(h):
        gradient = computeGradient(f, params)
        
        for i in range(len(params)):
            params[i] = params[i] - eta * gradient[i]
        
        print('params=', params, 'f(params)=', f(*params))
    
    return (params, f(*params))

def computeGradient(f, params, h=0.01):
    gradient = []
    
    for i in range(len(params)):
        params1 = params.copy()
        params2 = params.copy()
        params1[i] += h
        params2[i] -= h
        
        gradient.append((f(*params1) - f(*params2)) / (2 * h))
    
    return gradient

def f(x, y, z):
    return -1*(x**2 + y**2 + z**2)
    
gradientDescent(f, [2, 1, 3])

