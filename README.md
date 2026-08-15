# labflow

универсальный workflow для лабораторных, практических и курсовых работ.

labflow не содержит требований конкретного вуза, языка программирования или формата отчёта. он разделяет работу на независимые этапы и позволяет подключать внешние skills и report adapters.

## skills

- `assignment-workflow` — общий orchestrator.
- `assignment-context` — извлечение задачи, ограничений и deliverables.
- `assignment-coding` — реализация и проверка программной части.
- `assignment-math` — воспроизводимые вычисления, формулы, графики и таблицы.
- `assignment-report` — сборка отчёта из проверенных артефактов.
- `assignment-verification` — независимая проверка результата.
- `typst-report` — optional skill для создания отчётов Typst по одному базовому GOST-шаблону.

## базовый запуск

1. загрузить методичку и исходные данные в проект;
2. запустить `assignment-workflow`;
3. получить `context/TASK.md`, код, вычисления, артефакты, отчёт и `VERIFICATION.md`.

## optional typst

```bash
python optional-skills/typst-report/scripts/init_typst.py \
  --output-dir . \
  --kind lab \
  --title "Название работы" \
  --subject "Предмет" \
  --author "Фамилия Имя" \
  --group "Группа"
```

скрипт создаёт neutral GOST-based skeleton. вуз, факультет, кафедра и другие поля передаются параметрами и не зашиваются в skill.

## примеры

`examples/suai/` содержит два benchmark-сценария: курсовой проект и лабораторная по математическим основам систем управления. это примеры применения одного workflow к задачам разного типа, а не обязательная зависимость.

## license

MIT
