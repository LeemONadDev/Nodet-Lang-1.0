"""Nodetс компилирует ваш код, написанный на Nodet в код на С.
   Текущая версия v1.0.1"""

import sys
import stdlib #standart
file = sys.argv[1]
compile_path_result = "compiled.c"

class Builtin:
    prn = "!prn:"

f = open(file,'r+')

mainf_code = ""
lib_incl = ""

compilling_process_mainf = True

while compilling_process_mainf:
    current_line = f.readline()
    if not current_line:
        print("[NodetC] OK..")
        break
    if "#" in current_line:
        pass
    if "print" in current_line[0:5]:
        mainf_code = mainf_code + stdlib.PrintString(current_line) + "\n"
        if not("stdio.h" in lib_incl):
            lib_incl = lib_incl + "#include <stdio.h>\n"
    elif "return" in current_line[0:6]:
        mainf_code = mainf_code + stdlib.Return(current_line) + "\n"
    elif "var" in current_line[0:4]:
        mainf_code = mainf_code + stdlib.CreateVariable(current_line) + "\n"
    elif ";" in current_line:
        mainf_code = mainf_code + current_line[1:]
f = open("result.c","w")
f.write(lib_incl)
f.write("\n\n")
f.write("int main(){\n")
f.write(mainf_code)
f.write("}")
f.close()