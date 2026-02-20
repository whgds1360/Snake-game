# 🐍 Snake Game (Змейка)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)](https://docs.python.org/3/library/tkinter.html)
[![Pathlib](https://img.shields.io/badge/Pathlib-Paths-blue)](https://docs.python.org/3/library/pathlib.html)
[![Pillow](https://img.shields.io/badge/Pillow-Images-purple)](https://pillow.readthedocs.io/)
[![ConfigParser](https://img.shields.io/badge/ConfigParser-Configs-orange)](https://docs.python.org/3/library/configparser.html)
[![abc](https://img.shields.io/badge/abc-ABCs-red)](https://docs.python.org/3/library/abc.html)
[![typing](https://img.shields.io/badge/typing-TypeHints-yellow)](https://docs.python.org/3/library/typing.html)
[![__future__](https://img.shields.io/badge/__future__-Future-lightgrey)](https://docs.python.org/3/library/__future__.html)
[![random](https://img.shields.io/badge/random-RNG-teal)](https://docs.python.org/3/library/random.html)
[![Pydantic](https://img.shields.io/badge/Pydantic-DataValidation-teal)](https://docs.pydantic.dev/)

Реализация классической игры "Змейка" с современным интерфейсом на Python.
## 📸 Скриншоты

### Экран меню
![Menu](screenshots/menu.png)

### Игровой процесс
![Gameplay](screenshots/gameplay.png)

### Экран поражения
![Lose Screen](screenshots/losescreen.png)

## 📁 Структура проекта
<pre>
snake-game/
├── 📁 game/
│   ├── 📁 entities/
│   │   ├── 📄 Food.py        # Еда (генерация, отрисовка)
│   │   └── 📄 Snake.py       # Змейка (отрисовка начальной змеи, коллизии)
│   │
│   ├── 📁 scenes/
│   │   ├── 📄 LoadScreen.py  # Загрузочный экран (при запуске игры)
│   │   ├── 📄 Menu.py        # Экран меню
│   │   ├── 📄 LoseScreen.py  # Экран поражения
│   │   ├── 📄 WinScreen.py   # Экран победы
│   │   └── 📄 Game.py        # Основная игровая сцена
│   │
│   ├── 📁 utils/
│   │   ├── 📄 ResourseManager.py   # Управление ресурсами
│   │   └── 📄 Move.py              # Управление движением змейки (Направление, отрисовка сегментов)
│   │
│   ├── 📁 assets/
│   │   │ └── 📁 icon/
│   │   │      └── 🖼️ app_icon.ico
│   │   └── 📁 scenes/
│   │        ├── ️️🖼️BackGroundMenu.jpg  # Задний фон меню
│   │        ├── ️️🖼️BackGroundGame.jpg  # Задний фон экрана игры
│   │        ├── ️️🖼️LoadScreen.png      # Задний фон экрана загрузки
│   │        ├── ️️🖼️LoseScreen.jpg      # Задний фон экрана поражения
│   │        ├── ️️🖼️WinScreen.jpg       # Задний фон экрана победы
│   │        ├── ️️🖼️Start.png           # Кнопка
│   │        └── 🖼️ TryAgain.png       # Кнопка
│   │
│   ├── 📄 config.ini   # Настройки игры  
│   └── 📄 main.py      # Точка входа
│
├── 📄 .gitignore  # Исключения для Git
└── 📄 README.md   # Документация
</pre>
## 🎮 Геймплей

- **Управление**: стрелки клавиатуры (← ↑ → ↓)
- **Цель**: набрать максимальное количество очков, поедая еду
- **Победа**: заполнить всё игровое поле змеей
- **Поражение**: столкновение со стеной или собственным хвостом
- **Счет**: отображается в верхней части экрана

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.12
  - При версии ниже заявленой игра может работать некорректно (могут возникать проблемы с импортами)
  - При версии выше заявленной выявлена проблемы с компиляцией (возникает от версии компилятора 3.13 и выше)
- Tkinter - интерфейс
- Pydantic - современные датаклассы с автоматической валидацией
- Pillow - работа с изображениями
- pathlib - работа с путями файлов
- configparser - работа с конфигурационными файлами
- abc - абстрактные методы
- typing - аннотации типов
- future - современные аннотации в коде
- random - генерация случайных чисел

### Установка и запуск

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/whgds1360/snake-game.git
```
2. **Запустите игру:**
```bash
#Переход к директории игры
cd snake-game

#Переход в основную папку с игрой
cd game

#Запуск python скрипта
python main.py
```

### Компиляция кода
#### Дополнительные требования
- nuitka - это оптимизирующий компилятор для языка Python, который преобразует ваш Python-код в исполняемые файлы или в исходный код на C/C++. 
  - Проверял именно его и с ним всё работает корректно, также рекомендую его потому, что при завершении компиляции на другом устройстве вам не потребуется установленный интерпретатор python.
1. **Установка пакета nuitka:**
```bash
pip install nuitka
```
2. **Для компиляции введите следующую команду в терминал:**
```bash
#Обратите внимание, что вы находитесь в директории игры в основной папке game!
nuitka --standalone --onefile --enable-plugin=tk-inter --include-data-dir=utils=utils --include-data-dir=entities=entities --include-data-dir=scenes=scenes --include-data-dir=assets=assets --include-data-file=config.ini=config.ini main.py
```