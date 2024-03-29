# Steam-CD-Keys-Utity
Набор инструментов для упрощения работы с steam ключами (Mac)

# Общее описание
Данный набор инструментов помогает быстро работать с файлами Steam ключей и дает возможность проверять ключи на актуальность, быстро выделять нужное количество ключей из файлов и пакетно тегировать ключи.

## Основные компоненты
1. *Automator* - программа для автоматизации действия пользователя на Mac os. 
2. *Python* - отвечает за основную работу скриптов
3. *UI Vision* - плагин для Chrome, который позволяет делать автоматические запросы к сайтам. С помощью него можно проверить список ключей

## Основные инструменты
1. Auto Comment - скрипт добавляет коммент на группу файлов
2. Check Keys - скрипт проверяет файл после UI.Vision и отсеивает только не активированные ключи
3. Key Renamer - скрипт автоматически переименовывыет файл с учетом кол-ва ключей
4. Key Split - скрипт позволяет выделить нужное количество ключей из файла
5. Key Merge - скрипт объединяет несколько файлов ключей в один

## Установка
1. Установите[Python](https://www.python.org)
2. Установите [Google Chrome](https://www.google.com/chrome)
3. Установите плагин [UI.Vision Kantu for Chrome](https://chrome.google.com/webstore/detail/uivision-kantu-for-chrome/gcbalfbdmfieckjlnblleoemohcganoc)
4. Положите этот проект в папку /Users/username/
5. Положите файлы из папки Automator в папку /Users/username/Library/Services
6. Запускайте скрипты через контекстное меню «Быстрые действия»

## Работа инструментов
### Проверка ключей в Steam
1. Перейдите в [Steamworks](https://partner.steamgames.com/querycdkey/)
2. Импортируйте скрипт CSV_KEY_CHECKED.json в UI.Vision
3. Импортируйте файл с ключами (только csv, можно без форматирования)
4. Нажмите Start Macros с указанием количества итераций цикла
5. Макрос автоматически будет проверять ваши ключи.
6. В результате работы вам будет выдан Result.csv

### Проверка ключей на валидность и переименование файла ключа
1. После получения Result.csv используйте на нем *Check Keys*
2. На полученном файле примените *Key Renamer* для быстрого переименования с уютом количества ключей
3. Если вам нужно отделить определенное количество ключей, используйте *Key Split* с указание количества нужных ключей

### Авто-комментарии
Если вам нужно добавить комментарий для группы ключей, используйте *Auto Comment*

### Объединение ключей
Если вам нужно объеденить несктолько файлов ключей, используйте *Key Merge*. Данный скрипт не удаляет исходные файлы!
