# Тестовое для Lexicom.ai
Тестовое задание состоит из двух частей:
1) для запуска нужно клонировать репозиторий и выполнить команды:
```
docker-compose build
docker-compose up -d
```
Убедитесь, что на машине запущен docker и свобеден порт 6379 (для redis)

2) ответ на задачу SQL
```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name_ = split_part(full_names.name_, '.', 1)
```