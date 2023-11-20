def PrintString(code_str: str):
    required_lib = ["stdio.h"]
    print_value = code_str[code_str.index("print")+7:]
    return f"   printf({print_value});"

def Return(code_str:str):
    return_value = code_str[code_str.index("return")+8:]
    return f"   return {return_value};"
def CreateVariable(code_str:str):
    code = code_str.split()
    type, name, value = code[1], code[2], code[3]
    return f"   {type} {name} = {value};"