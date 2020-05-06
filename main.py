import os
import plugin1
import plugin2

print('Команды:\n'
    'list_plugins() - выводит на экран список всех имеющихся плагинов.\n'
    'plugin1.run() - запускает первый плагин.\n'
    'plugin1.help() - выводит справочную информацию по первому плагину.\n'
    'plugin2.run()  - запускает второй плагин.\n'
    'plugin2.help() - выводит справочную информацию по второму плагину.')


def list_plugins():
    
    list_modules = os.listdir()
    for name in list_modules:
        
        if name.startswith('plugin'):
            print(name[:-3])
            

