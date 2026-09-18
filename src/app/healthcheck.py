"""Проверка окружения: ключ OpenAI и модель заданы и отвечают.

Запуск: python -m app.healthcheck  (из папки src/ или с PYTHONPATH=src)
"""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv


def check_env() -> list[str]:
    """Вернуть список незаполненных обязательных переменных окружения."""
    load_dotenv()
    required = ("OPENAI_API_KEY", "OPENAI_MODEL")
    return [name for name in required if not os.getenv(name)]


def main() -> int:
    missing = check_env()
    if missing:
        print(f"Не заданы переменные: {', '.join(missing)}. Заполните .env (см. .env.example).")
        return 1

    from openai import OpenAI

    client = OpenAI()
    response = client.responses.create(
        model=os.environ["OPENAI_MODEL"],
        input="Ответь одним словом: ок",
    )
    print(f"OK: модель ответила -> {response.output_text!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
