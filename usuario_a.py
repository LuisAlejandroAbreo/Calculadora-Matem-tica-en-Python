def fibonacci(n):
    serie = []
    a, b = 0, 1
    
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    
    return serie
