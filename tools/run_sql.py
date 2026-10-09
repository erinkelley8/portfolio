"""Run a project's numbered SQL files, in order, against a local DuckDB database.

Usage:  uv run python tools/run_sql.py <project-folder-name> [--only 02]
Paths inside the SQL are relative to the repository root.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project")
    parser.add_argument("--only", help="run only files whose name starts with this prefix, e.g. 02")
    args = parser.parse_args()

    project = ROOT / "projects" / args.project
    sql_files = sorted((project / "sql").glob("*.sql"))
    if args.only:
        sql_files = [f for f in sql_files if f.name.startswith(args.only)]
    if not sql_files:
        print("No SQL files found.")
        return 1

    os.chdir(ROOT)  # SQL paths are repo-root relative
    db_path = project / "data" / "processed" / f"{args.project}.duckdb"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(db_path))
    for sql_file in sql_files:
        print(f"-- {sql_file.name}")
        # Drop full-line comments first so a ';' inside a comment cannot split a statement.
        lines = sql_file.read_text(encoding="utf-8").splitlines()
        script = "\n".join(line for line in lines if not line.lstrip().startswith("--"))
        for statement in script.split(";"):
            if not statement.strip():
                continue
            con.execute(statement)
            if con.description:  # statement returned rows
                print(con.fetchdf().to_string(index=False))
    con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
