import os
import subprocess
import sys
import msvcrt

if not os.path.exists('.git'):
    print('Скрипт должен выполняться в корневом каталоге Git-репозитория.')
    sys.exit(1)

# Очищаем 
subprocess.call(["git", "reset", "--hard"])
subprocess.call(["git","clean","-fdx"])

print('Очистка выполнена\n Для завершения нажмите любую клавишу')
msvcrt.getch()


