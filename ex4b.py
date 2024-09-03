def calculator():
    a = request.form.get("a",type = int,default = 0)
    b = request.form.get("b",type = int,default = 0)
    operation = request.form.get("operation")
    if(operation == 'add'):
        res = a+b
    elif(operation == 'sub'):
        res = a-b
    elif(operation == 'mul'):
        res = a*b
    elif(operation == 'div'):
        res = a/b
    else:
        print("no operation")
        

    