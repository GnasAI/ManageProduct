import requests
import json


class Product:
    def __init__(self, id, name, description, price, in_stock) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock

    def DictPro(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "in_stock": self.in_stock,
        }


class ExistName(Exception):
    pass


class ExistID(Exception):
    pass


class PriceValueError(ValueError):
    pass


class InStockValueError(ValueError):
    pass


class QLSP:
    def __init__(self, filename):
        self.filename = filename
        self.products = []
        self.Read()

    def Add(self, newProduct):
        try:
            self.Read()
            if newProduct["price"] <= 0:
                raise PriceValueError
            elif newProduct["in_stock"] < 0:
                raise InStockValueError
            for product in self.products:
                if product["id"] == newProduct["id"]:
                    raise ExistID
                oldname = product["name"].strip()
                newname = newProduct["name"].strip()
                if oldname.lower() == newname.lower():
                    raise ExistName
            self.products.append(newProduct)
            self.Write()
            return 1
        except ExistID:
            return 0
        except PriceValueError:
            return -1
        except InStockValueError:
            return -2
        except ExistName:
            return -3

    def Delete(self, productID):
        self.Read()
        for product in self.products:
            if product["id"] == productID:
                self.products.remove(product)
                self.Write()
                return 1
        return 0

    def Update(self, productID, newDaTa):
        try:
            self.Read()
            if newDaTa["price"] <= 0:
                raise PriceValueError
            elif newDaTa["in_stock"] < 0:
                raise InStockValueError
            for product in self.products:
                if product["id"] == newDaTa["id"] and product["id"] != productID:
                    raise ExistID
                oldname = product["name"].strip()
                newname = newDaTa["name"].strip()
                if (
                    oldname.lower() == newname.lower()
                    and product["name"].lower() != oldname.lower()
                ):
                    raise ExistName
            for product in self.products:
                if product["id"] == productID:
                    product.update(newDaTa)
                    self.Write()
                    return 1
            else:
                return 0

        except PriceValueError:
            return -1
        except InStockValueError:
            return -2
        except ExistID:
            return -4
        except ExistName:
            return -3

    def Read(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                self.products = json_data
            return 1
        except FileNotFoundError:
            return 0
        except json.JSONDecodeError:
            return 0

    def Write(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.products, file, ensure_ascii=False, indent=4)
        return 1

    def getAPI(self, url_api):
        res = requests.get(url_api)
        data = json.loads(res.text)
        lenList = len(self.products)
        count = lenList + 1
        for item in data:
            id = str(count)
            if len(id) < 2:
                id = "SP00" + id
            elif len(id) < 3:
                id = "SP0" + id
            else:
                id = "SP" + id
            product = Product(
                id, item["name"], item["description"], item["price"], item["in_stock"]
            ).DictPro()
            check = self.Add(product)
            if check == 1:
                count += 1

    def Sort(self, mode):
        self.Read()
        if mode == "Giá tăng dần":
            temp = self.products.copy()
            temp.sort(key=lambda item: item["price"])
        elif mode == "Giá giảm dần":
            temp = self.products.copy()
            temp.sort(key=lambda item: item["price"], reverse=True)
        elif mode == "Hàng tồn kho tăng dần":
            temp = self.products.copy()
            temp.sort(key=lambda item: item["in_stock"])
        else:
            temp = self.products.copy()
            temp.sort(key=lambda item: item["in_stock"], reverse=True)            
        return temp


# Ví dụ sử dụng
if __name__ == "__main__":
    qlsp = QLSP("abcd.json")
    qlsp.getAPI("https://vudev1412.github.io/Apijson/sanpham.json")
    qlsp.Sort("Hàng tồn kho giảm dần")
