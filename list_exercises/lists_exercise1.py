def middle(t):
    a = [];

    for element in t:
        a.append(element);
    
    del a[0];
    del a[len(a)-1];
    print('Array input');
    print(t);
    print('Array output');
    print(a);
    return a;
