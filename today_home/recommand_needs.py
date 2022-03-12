products1 = ["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"]
purchased1 = ["towel", "mattress", "curtain"]
result1 = "blanket"
products2 = ["towel red long thin", "blanket red thick short", "curtain red long wide", "mattress thick", "hat red thin", "pillow red long", "muffler blue thick long"]
purchased2 = ["blanket", "curtain", "hat", "muffler"]
result2 = "towel"

suggest_products = list()
suggest_product_info = list()
un_suggest_products = list()
un_suggest_product_info = list()
total_product = list()

def main():
    suggest_product_index = list()
    suggest_product_ranking_index = {}
    for product in products2:
        product_info = product.split()
        total_product.append(product_info[0])
        if product_info[0] in purchased2:
            suggest_products.append(product_info[0])
            suggest_product_info.append(product_info[1::])
        else:
            un_suggest_products.append(product_info[0])
            un_suggest_product_info.append(product_info[1::])

    print(suggest_product_info)

    for suggest_product in suggest_product_info:
        suggest_product_index += suggest_product
    print(suggest_product_index)

    for suggest_product_index in suggest_product_index:
        try:
            suggest_product_ranking_index[suggest_product_index] += 1
        except:
            suggest_product_ranking_index[suggest_product_index] = 1
    print(suggest_product_ranking_index)

    sorted_suggest_product_ranking_index = dict(sorted(suggest_product_ranking_index.items(), key=lambda x: (-x[1], x[0])))
    print("sorted_suggest_product_ranking_index", sorted_suggest_product_ranking_index)

    un_purchase_product = list(set(total_product) - set(suggest_products))
    print("un_suggest_products: ", un_suggest_products)
    print("un_suggest_products_info: ", un_suggest_product_info)

    result = [0] * len(un_suggest_products)
    score = len(sorted_suggest_product_ranking_index)
    for product_key, product_value in sorted_suggest_product_ranking_index.items():
        for key, un_suggest_product in enumerate(un_suggest_product_info):
            if product_key in un_suggest_product:
                result[key] +=score
        score -= 1

    tmp = max(result)
    index = result.index(tmp)
    print("result: ", un_suggest_products[index])



main()