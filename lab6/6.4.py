def fun(**kwargs):
    """if 'end' in kwargs.keys():

        endF1 = kwargs['end']

    else:
        endF1 = "\n" """
    endF1 = kwargs.get('end','\n')
    for key,value in kwargs.items():
        print(key,value,end = endF1)




fun(a = 12, xd = 34,xxd = "Janek")