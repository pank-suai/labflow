# Labflow

Универсальный workflow для лабораторных, практических и курсовых работ.

Labflow не содержит требований конкретного вуза, языка программирования или формата отчёта. Он разделяет работу на независимые этапы и позволяет подключать внешние skills и report adapters.

## Skills

- `assignment-workflow` — общий orchestrator.
- `assignment-context` — извлечение задачи, ограничений и deliverables.
- `assignment-coding` — реализация и проверка программной части.
- `assignment-math` — воспроизводимые вычисления, формулы, графики и таблицы.
- `assignment-report` — сборка отчёта из проверенных артефактов.
- `assignment-self-review` — self-review через отдельного subagent.
- `typst-report` — optional skill для создания отчётов Typst по одному базовому GOST-шаблону.

## Базовый запуск

1. Загрузить методичку и исходные данные в проект;
2. Запустить `assignment-workflow`;
3. Получить `context/TASK.md`, код, вычисления, артефакты, отчёт и `SELF_REVIEW.md`.

## Optional typst

```bash
python optional-skills/typst-report/scripts/init_typst.py \
  --output-dir . \
  --kind lab \
  --title "Название работы" \
  --subject "Предмет" \
  --author "Фамилия Имя" \
  --group "Группа"
```

Скрипт создаёт neutral GOST-based skeleton. Вуз, факультет, кафедра и другие поля передаются параметрами и не зашиваются в skill.

## Примеры

`examples/suai/` содержит два benchmark-сценария: курсовой проект и лабораторная по математическим основам систем управления. Это примеры применения одного workflow к задачам разного типа, а не обязательная зависимость.

## License

MIT
