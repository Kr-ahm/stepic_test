import matplotlib.pyplot as plt

def read_sales_data(file_path):
    sales_list = []
    try:
        with open(f'{file_path}', 'r', encoding='utf-8') as file:
            for line in file:
                line_list = line.strip().split(', ')
                sale = dict.fromkeys(['product_name', 'quantity', 'price', 'date'])
                line_element = 0
                for sale_element in sale:
                    sale[sale_element] = line_list[line_element]
                    line_element += 1
                sales_list.append(sale)

    except FileNotFoundError as e:
        print(f'{e} Файл не найден!')
        exit()
    except PermissionError as e:
        print(f'Нет разрешения на доступ к файлу {e}')
        exit()
    return sales_list


def total_sales_per_product(sales_data):
    total_dict = dict()
    for sale in sales_data:
        if sale['product_name'] in total_dict.keys():
            total_dict[f'{sale['product_name']}'] += int(sale['quantity']) * float(sale['price'])
        else:
            total_dict[f'{sale['product_name']}'] = int(sale['quantity']) * float(sale['price'])
    return total_dict


def sales_over_time(sales_data):
    total_dict = dict()
    for sale in sales_data:
        if sale['date'] in total_dict.keys():
            total_dict[f'{sale['date']}'] += int(sale['quantity']) * float(sale['price'])
        else:
            total_dict[f'{sale['date']}'] = int(sale['quantity']) * float(sale['price'])
    return total_dict


sales_from_file = read_sales_data('Sales.txt')
total_product = total_sales_per_product(sales_from_file)
total_time = sales_over_time(sales_from_file)
sorted_total_time = dict(sorted(total_time.items()))

print(f'Продукт принес наибольшую выручку: {max(total_product, key=total_product.get)}')
print(f'День с наибольшей суммой продаж: {max(total_time, key=total_time.get)}')

plt.title('График общей суммы продаж по каждому продукту')
plt.xlabel('Продукт')
plt.ylabel('Выручка')
plt.plot(total_product.keys(), total_product.values())
plt.show()

plt.title('График общей суммы продаж по дням')
plt.xlabel('Дата')
plt.ylabel('Выручка')
plt.plot(sorted_total_time.keys(), sorted_total_time.values())
plt.show()
