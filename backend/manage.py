#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_settings.settings')

    # --- ДОДАЙ ЦЕЙ РЯДОК ---
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parent))
    # -----------------------

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # ... текст помилки ...
        raise
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
