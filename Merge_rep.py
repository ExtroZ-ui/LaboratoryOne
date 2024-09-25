import os
import subprocess
import sys
import msvcrt

if not os.path.exists('.git'):
    print('Скрипт должен выполняться в корневом каталоге Git-репозитория.')
    sys.exit(1)

# Перенос ревизии из ветки dev в prd
subprocess.run(["git", "checkout", "prd"])
subprocess.run(["git", "merge", "--no-ff", "dev"])

print('Введите название тега')
new_tag = input()
# Установка тега
subprocess.run(["git", "tag", "-a", "{new_tag}", "-m", "тест сообщения"])

# Отправка изменений
subprocess.run(["git", "push", "origin", "prd", "--tag"])

print('Ветка dev в prd объединилась с установкой тэга\n Для завершения нажмите любую клавишу')
msvcrt.getche()

