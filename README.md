# QJEditor - редактор обменных интегралов J

Визуальный редактор для работы с распределением обменных интегралов J с функцией масштабирования. 

## Функции

- Визуализация распределения обменных интегралов из файлов типа cell (_/examples/_).
- Редактирование значений обменных интегралов (+-J).
- Масштабирование систем с сохранением паттерна распределения.
- Создание пустых систем без cell-файлов.

## Начало работы

Последняя версия в разделе _Releases_.

## Запуск

```bash
git clone https://github.com/Chesnokov-ma/J-QEditor.git
python -m venv venv
.venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Сборка

```bash
git clone https://github.com/Chesnokov-ma/J-QEditor.git
python -m venv venv
.venv/bin/activate
pip install -r requirements.txt
python -m PyInstaller --onefile --windowed -n JQEditor main.py
```

Исполняемый файл находится в _/dist/_.
