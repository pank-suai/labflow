# Labflow

Универсальный workflow для лабораторных, практических и курсовых работ.

Labflow не содержит требований конкретного вуза, языка программирования или формата отчёта. Он разделяет работу на независимые этапы и позволяет подключать внешние skills и report adapters.

## Skills

- `labflow` — общий workflow.
- `labflow-context` — извлечение задачи, ограничений и deliverables.
- `labflow-coding` — реализация программной части.
- `labflow-math` — воспроизводимые вычисления, формулы, графики и таблицы.
- `labflow-report` — сборка отчёта из проверенных артефактов.
- `labflow-self-review` — self-review через отдельного subagent.
- `labflow-typst` — optional skill для создания общей Typst-структуры отчёта.

`labflow-self-review` запускается отдельным subagent через `delegate_task` и проверяет покрытие требований, качество кода, математические артефакты и визуальное качество отчёта. Результат сохраняется в `SELF_REVIEW.md`.

## Базовый запуск

1. Загрузить методичку и исходные данные в проект.
2. Запустить `labflow`.
3. Передать полученный контекст в `labflow-typst`, если требуется Typst-отчёт.
4. Получить код, вычисления, отчёт и `SELF_REVIEW.md`.

## Typst

`labflow-typst` не просит агента придумывать структуру проекта и не принимает метаданные отдельными флагами. Он получает полный контекст задания и сам создаёт всю структуру Typst-проекта:

```bash
python optional-skills/labflow-typst/scripts/init_typst.py \
  --context context/context.yaml \
  --output-dir .
```

Скрипт создаёт:

```text
docs/
├── index.typ
├── content.typ
└── lib/
    ├── context.typ
    ├── gost.typ
    └── titlepage.typ

artifacts/
data/
images/
math/
src/
tests/
```

`gost.typ` и `titlepage.typ` построены на общей структуре из курсового проекта и лабораторной по математическим основам систем управления. Конкретные данные берутся только из `context/context.yaml`.

## License

MIT
