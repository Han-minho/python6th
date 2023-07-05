import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='library',
    user='postgres',
    password='admin1234',
)

cur = conn.cursor()

# cur.execute('''
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# ''')

# conn.commit()
# cur.execute('INSERT INTO test_table (name) VALUES (%s)',("Test Name",))
# conn.commit()

cur.execute("UPDATE test_table SET name='Change' WHERE id=1")
conn.commit()


cur.execute('SELECT * FROM test_table order by id')
rows = cur.fetchall()

for row in rows:
    print(row)


cur.close()
conn.close()

# coffee_menu = {
#     '1':{'name':'에스프로소','price':3000},
#     '2':{'name':'아메리카노','price':4000},
#     '3':{'name':'카페라떼','price':5000},
#     '4':{'name':'카푸치노','price':5000},
# }
# total_price = 0
#
# def print_menu():
#     print("\n===커피 주문 시스템")
#     for id,coffee in coffee_menu.items():
#         print(f"{id}.{coffee['name']}-{coffee['price']}원")
#     # print("5.주문 종료")
#
# while True:
#     print_menu()
#     choice = input("원하는 메뉴를 선택하세요: ")
#     if choice in coffee_menu:
#         total_price += coffee_menu[choice]['price']
#         print(f"{coffee_menu[choice]['name']}을(를) 주문하셨습니다.\n 현재까지의 총 금액은 {total_price}원 입니다.")
#     elif choice == '5':
#         print(f"\n주문을 종료합니다. 총 주문금액은 {total_price}원 입니다.")
#         break
#     else:
#         print("\n 잘못된 선택입니다. 다시 선택해주세요.")

