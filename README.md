# QJEditor - редактор обменных интегралов J

Визуальный редактор для работы с распределением обменных интегралов J с функцией масштабирования для квадратных спиновых решеток. 

## Функции

- Визуализация распределения обменных интегралов из файлов типа cell (_/examples/_).
- Редактирование значений обменных интегралов (+-J).
- Редактирование значений спинов (с чтением mfsys файлов).
- Масштабирование систем с сохранением паттерна распределения.
- Создание пустых систем.
- Переворот случайных спинов и прилежащих связей.
- Калькулятор стат-показателей.

## Запуск

```bash
git clone https://github.com/Chesnokov-ma/J-QEditor.git
cd J-QEditor
python -m venv venv
.venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Для Linux
```bash
source .venv/bin/activate
```


## Сборка

```bash
git clone https://github.com/Chesnokov-ma/J-QEditor.git
cd J-QEditor
python -m venv venv
.venv/bin/activate
pip install -r requirements.txt

pip install pyinstaller
python -m PyInstaller --onefile --windowed -n JQEditor main.py
```

Исполняемый файл находится в _/dist/_.
