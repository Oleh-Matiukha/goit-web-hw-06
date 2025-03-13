import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "test",
    "user": "postgres",
    "password": "567234"
}


def execute_query(filename):
    """Функція для виконання SQL-запиту з файлу"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        with open(filename, 'r', encoding='utf-8') as file:
            query = file.read()
        cur.execute(query)
        try:
            result = cur.fetchall()
            for row in result:
                print(row)
        except psycopg2.ProgrammingError:
            print("Запит виконано без повернення результату")
        conn.commit()
    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    execute_query("queries/query_12.sql")
