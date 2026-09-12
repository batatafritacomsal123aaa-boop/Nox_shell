comandos = [
    'version', 'help', 'exit', 'clear', 'ping', 'time', 'uptime',
    'sysinfo (os,sys)', 'echo', 'upper', 'lower', 'sleep', 'length', 'reverse', 'whoami', 'nexus', 'cwd', 'cd', 'ls', 'mkdir',
    'color', 'touch', 'cat', 'write', 'append', 'rm', 'title', 'date', 'history'
]
cores = [
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
    'gray', 'brightred', 'brightgreen', 'brightyellow', 'brightblue',
    'brightmagenta', 'brightcyan', 'brightwhite', 'default, reset'
]
usuario = 'User'
titulo = 'Nox'
import socket
import time
import sys
import os
from datetime import datetime
import platform
import getpass
import subprocess
import shutil
if getattr(sys, 'frozen', False):
    pasta_nox = os.path.dirname(sys.executable)
else:
    pasta_nox = os.path.dirname(os.path.abspath(__file__))
memoria = os.path.join(pasta_nox, 'memoria.txt')
if os.path.exists(memoria):
    with open(memoria, 'r') as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) > 0:
            usuario = linhas[0].strip()
        if len(linhas) > 1:
            titulo = linhas[1].strip()

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def ativar_cores():
    if os.name == 'nt':
        os.system('')
def definir_titulo():
    if os.name == 'nt':
        os.system('title ' + titulo)
    else:
        print('\033]0;' + titulo + '\007', end='')
definir_titulo()
print("Type 'help' to see the available commands existing in this version, how to use some commmands like the nexus command. (nox-0.05)")
ativar_cores()
up = time.perf_counter()
history = []
while True:
    comando = input(usuario + 'NOX@ > : ')
    partes = comando.split(' ', 1)
    history.append(comando)
    comando = partes[0].lower()
    match comando:
        case 'version':
            print(' Nox V: 0.05')
        case 'help':
            print('\033[96m', end='')

            print('''
NOX Commands:

SYSTEM
  version              Show the current NOX version
  sysinfo              Show some hardware and software informations
  whoami               Show the operating system username
  time                 Show the current time
  date                 Show the current date
  uptime               Show how long NOX has been running

NAVIGATION
  cwd                   Show the current directory
  cd <path>             Change the current directory
  ls                    List files and directories

FILES
  touch <file>          Create a new file
  cat <file>            Display file contents
  write <file>          Replace the contents of a file
  append <file>         Add text to the end of a file
  rm <file>             Delete a file
  mkdir <directory>     Create a directory

TEXT
  echo <text>           Print text
  upper <text>          Convert text to uppercase
  lower <text>          Convert text to lowercase
  length <text>         Show text length and repeat the text
  reverse <text>        Reverse text

NOX
  nexus [name]          Show or change the NOX username (nexus to show)
  color [color]         Show available colors or change the text color (color to show)
  title <title>         Change the terminal title
  history               Show commands entered in this session
  run <program>         Run an external program 
  clear                 Clear the terminal
  sleep <seconds>       Pause NOX for a specified time
  exit                  Exit NOX

OTHER
  ping                  Test NOX responsiveness
  stopwatch             Measure elapsed time

Examples:
  cd Desktop
  color brightgreen
  run notepad
''')

            print('\033[0m', end='')
        case 'exit':
            print('leaving...')
            time.sleep(0.6)
            break
        case 'clear':
            print('Charging...')
            time.sleep(0.3)
            limpar()
        case 'ping':
            print('pong')
        case 'time':
            hours = datetime.now().strftime('%H:%M:%S')
            print(' ' + hours)
        case 'uptime':
            print(time.perf_counter() - up)
        case 'sys' | 'os' | 'sysinfo':
            sinfo = platform.system()
            sinfo2 = platform.release()
            sinfo3 = platform.machine()
            sinfo4 = platform.processor()
            sinfo5 = platform.python_version()
            sinfo6 = socket.gethostname()
            print('Host_Name: ' + sinfo6)
            print('System: ' + sinfo)
            print('Release: ' + sinfo2)
            print('Machine: ' + sinfo3)
            print('Processor: ' + sinfo4)
            print('Python_Version: ' + sinfo5)
        case 'echo':
            if len(partes) > 1:
                print(partes[1])
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'upper':
            if len(partes) > 1:
                print(partes[1].upper())
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'lower':
            if len(partes) > 1:
                print(partes[1].lower())
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'sleep':
            try:
                if len(partes) > 1:
                    tempo = float(partes[1])
                    time.sleep(tempo)
                else:
                    print('invalid argument:')
                    print('you missed something?')
            except ValueError:
                print('ValueError:')
                print('try numbers next time!')
        case 'length':
            if len(partes) > 1:
                tamanho = len(partes[1])
                print(tamanho)
                print(partes[1])
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'reverse':
            if len(partes) > 1:
                texto = partes[1][::-1]
                print(texto)
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'whoami':
            print(getpass.getuser())
        case 'nexus':
            if len(partes) > 1:
                with open(memoria, 'w') as arquivo:
                    usuario = partes[1]
                    arquivo.write(usuario + '\n')
                    arquivo.write(titulo)
                    print('User sucessfully changed!')
            else:
                print(usuario)   
        case 'cwd':
            sla = os.getcwd()
            print(sla)
        case 'cd':
            if len(partes) > 1:
                try:
                    os.chdir(partes[1])
                except FileNotFoundError:
                    print('File not found')
                except NotADirectoryError:
                    print('not a directory')
            else:
                print('invalid argument:')
                print('you missed something?') 
        case 'ls':
           arc = os.listdir()
           for item in arc:
                if os.path.isdir(item):
                    print('[DIR] ' + item)
                else:
                    print('[FILE] ' + item)
        case 'mkdir':
            try:
                if len(partes) > 1:
                    os.mkdir(partes[1])
                    print('Directory sucessfully created!')
                else:
                    print('invalid argument:')
                    print('you missed something?')
            except FileExistsError:
                print('Path already exists')
        case 'color':
            if len(partes) > 1:
                match partes[1]:
                    case 'black':
                        print('\033[30m', end='')
                    case 'red':
                        print('\033[31m', end='')
                    case 'green':
                        print('\033[32m', end='')
                    case 'yellow':
                        print('\033[33m', end='')
                    case 'blue':
                        print('\033[34m', end='')
                    case 'magenta':
                        print('\033[35m', end='')
                    case 'cyan':
                        print('\033[36m', end='')
                    case 'white':
                        print('\033[37m', end='')
                    case 'gray' | 'grey':
                        print('\033[90m', end='')
                    case 'brightred':
                        print('\033[91m', end='')
                    case 'brightgreen':
                        print('\033[92m', end='')
                    case 'brightyellow':
                        print('\033[93m', end='')
                    case 'brightblue':
                        print('\033[94m', end='')
                    case 'brightmagenta':
                        print('\033[95m', end='')
                    case 'brightcyan':
                        print('\033[96m', end='')
                    case 'brightwhite':
                        print('\033[97m', end='')
                    case 'reset' | 'default':
                        print('\033[0m', end='')
                    case _:
                        print('invalid color')
            else:
                for cor in cores:
                    print(cor)
                print('"default" sets the text to the default color; the same applies to "reset".')
        case 'touch':
            if len(partes) > 1:
                try:
                    with open(partes[1], 'x') as arquivo:
                        print('File created with 0 errors!')
                except FileExistsError:
                    print('File already exists')
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'cat':
            try:
                if len(partes) > 1:
                    with open(partes[1], 'r') as arquivo:
                        conteudo = arquivo.read()
                        print(conteudo)
                else:
                    print('invalid argument:')
                    print('you missed something?')
            except FileNotFoundError:
                print('File not exists')
        case 'write':
            if len(partes) > 1:
                texto = input('Text > :')
                with open(partes[1], 'w') as arquivo:
                    arquivo.write(texto)
                    print('File successfully changed!')
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'append':
            if len(partes) > 1:
                texto = input('Text > :')
                with open(partes[1], 'a') as arquivo:
                    arquivo.write('\n' + texto)
                    print('File successfully changed!')
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'rm':
            if len(partes) > 1:
                try:
                    os.remove(partes[1])
                    print('File sucessfully deleted!')
                except FileNotFoundError:
                    print('File not found')
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'title':
            if len(partes) > 1:
                titulo = partes[1]
                with open(memoria, 'w') as arquivo:
                    arquivo.write(usuario + '\n')
                    arquivo.write(titulo)
                    definir_titulo()
            else:
                print('invalid argument:')
                print('you missed something?')
        case 'date':
            data = datetime.now().strftime('%d/%m/%Y')
            print(data)
        case 'history':
            for bibi in history:
                print(bibi)
        case 'run':
            try:
                if len(partes) > 1:
                    if os.name == 'nt':
                        execucao = partes[1].split()
                        subprocess.Popen(execucao, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    else:
                        execucao = partes[1].split()
                        subprocess.Popen(execucao)
                else:
                    print('invalid argument:')
                    print('you missed something?')
            except FileNotFoundError:
                print('Program not found')
        case 'stopwatch':
            inicio = time.perf_counter()
            input('Enter > : ')
            fim = time.perf_counter()
            resultado = fim - inicio
            print(f'{resultado:.2f}')
        case _:
            print('> : invalid syntax')