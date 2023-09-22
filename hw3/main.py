import csv
import json

books_file = 'books.csv'
users_file = 'users.json'
result_file = 'result.json'


def get_book():
    try:
        with open(books_file, "r", encoding="utf-8") as f:
            books_raw = csv.DictReader(f)
            books = [dict(filter(lambda key: key[0] != "Publisher", row.items())) for row in books_raw]
            return books
    except (Exception, IOError) as e:
        print(e)


def get_users():
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            users_raw = json.loads(f.read())
            keys = ("name", "gender", "address", "age")
            users = [dict(filter(lambda key: key[0] in keys, row.items())) for row in users_raw]
            list(map(lambda d: d.update({"books": []}), users))
            return users
    except (Exception, IOError) as e:
        print(e)


def distribute_books(users, books):
    if isinstance(users, list) and isinstance(books, list):
        i = 0
        while i < len(books):
            for index, user in enumerate(users):
                user["books"].append(books[i])
                users[index]["books"] = user["books"]
                i += 1
                if i == len(books):
                    break
        return users
    return


def write_result(result):
    if isinstance(result, list):
        try:
            f = open(result_file, "w", encoding="utf-8")
            f.write(json.dumps(result, indent=4, ensure_ascii=False))
            f.close()
        except (Exception, IOError) as e:
            print(e)


def main():
    r = distribute_books(get_users(), get_book())
    write_result(r)


if __name__ == '__main__':
    main()
