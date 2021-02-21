from abc import ABC, abstractmethod


class OfficeEquipmentWarehouse:
    warehouse_info = []

    @staticmethod
    def get_warehouse_info():
        OfficeEquipmentWarehouse.warehouse_info.append(Printer.printer_wh_info)
        OfficeEquipmentWarehouse.warehouse_info.append(Scanner.scanner_wh_info)
        OfficeEquipmentWarehouse.warehouse_info.append(Copier.copier_wh_info)
        return OfficeEquipmentWarehouse.warehouse_info

    @classmethod
    def incoming_office_equipment(cls):
        type_equip = input('Введите тип номенклатуры для прихода: ')
        for el in cls.warehouse_info:
            if type_equip == el['type_equip']:
                for key in el.keys():
                    if key == 'type_equip':
                        continue
                    if key == 'invent_number' or key == 'quantity':
                        while True:
                            try:
                                item = int(input(f'Введите: {key}: '))
                                break
                            except ValueError as err:
                                print(f'Нужно ввести число. Повторите ввод: ')
                        if key == 'invent_number' and item in el[key]:
                            while True:
                                try:
                                    quantity = int(input(f'Введите количество: '))
                                    break
                                except ValueError as err:
                                    print(f'Количество должно быть числом. Повторите ввод: ')
                            el['quantity'][el['invent_number'].index(item)] += quantity
                            break
                        el[key].append(item)
                    else:
                        el[key].append(input(f'Введите: {key}: '))

    @classmethod
    def outgo_office_equipment(cls):
        type_equip = input('Введите тип номенклатуры для отгрузки: ')
        while True:
            try:
                invent_number = int(input('Введите инвентарный номер: '))
                break
            except ValueError as err:
                print(f'Нужно ввести число. Повторите ввод: ')
        for el in cls.warehouse_info:
            if type_equip == el['type_equip'] and invent_number in el['invent_number']:
                while True:
                    try:
                        quantity = int(input('Введите количество: '))
                        break
                    except ValueError as err:
                        print(f'Нужно ввести число. Повторите ввод: ')
                el['quantity'][el['invent_number'].index(invent_number)] -= quantity
                break


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self, invent_number, name, quantity, color):
        self.name = name
        self.invent_number = invent_number
        self.quantity = quantity
        self.color = color


class Printer(OfficeEquipment):
    printer_wh_info = {'type_equip': 'Принтер',
                       'invent_number': [],
                       'name': [],
                       'quantity': [],
                       'color': [],
                       'multicolour': [],
                       'printer_type': []
                       }

    def __init__(self, invent_number, name, quantity, color, multicolour, printer_type):
        super().__init__(invent_number, name, quantity, color)
        self.multicolour = multicolour
        self.printer_type = printer_type
        if self.invent_number in Printer.printer_wh_info['invent_number']:
            Printer.printer_wh_info['quantity'][Printer.printer_wh_info['invent_number'].index(self.invent_number)] += self.quantity
        else:
            Printer.printer_wh_info['invent_number'].append(self.invent_number)
            Printer.printer_wh_info['name'].append(self.name)
            Printer.printer_wh_info['quantity'].append(self.quantity)
            Printer.printer_wh_info['color'].append(self.color)
            Printer.printer_wh_info['multicolour'].append(self.multicolour)
            Printer.printer_wh_info['printer_type'].append(self.printer_type)


class Scanner(OfficeEquipment):
    scanner_wh_info = {'type_equip': 'Сканер',
                       'invent_number': [],
                       'name': [],
                       'quantity': [],
                       'color': [],
                       'scanner_type': []
                       }

    def __init__(self, invent_number, name, quantity, color, scanner_type):
        super().__init__(invent_number, name, quantity, color)
        self.scanner_type = scanner_type
        if self.invent_number in Scanner.scanner_wh_info['invent_number']:
            Scanner.scanner_wh_info['quantity'][Scanner.scanner_wh_info['invent_number'].index(self.invent_number)] += self.quantity
        else:
            Scanner.scanner_wh_info['invent_number'].append(self.invent_number)
            Scanner.scanner_wh_info['name'].append(self.name)
            Scanner.scanner_wh_info['quantity'].append(self.quantity)
            Scanner.scanner_wh_info['color'].append(self.color)
            Scanner.scanner_wh_info['scanner_type'].append(self.scanner_type)


class Copier(OfficeEquipment):
    copier_wh_info = {'type_equip': 'Копир',
                      'invent_number': [],
                      'name': [],
                      'quantity': [],
                      'color': [],
                      'multicolour': []
                      }

    def __init__(self, invent_number, name, quantity, color, multicolour):
        super().__init__(invent_number, name, quantity, color)
        self.multicolour = multicolour
        if self.invent_number in Copier.copier_wh_info['invent_number']:
            Copier.copier_wh_info['quantity'][Copier.copier_wh_info['invent_number'].index(self.invent_number)] += self.quantity
        else:
            Copier.copier_wh_info['invent_number'].append(self.invent_number)
            Copier.copier_wh_info['name'].append(self.name)
            Copier.copier_wh_info['quantity'].append(self.quantity)
            Copier.copier_wh_info['color'].append(self.color)
            Copier.copier_wh_info['multicolour'].append(self.multicolour)


printer_1 = Printer(name='HP', invent_number=3141, quantity=3, color='black', multicolour='Yes', printer_type='Laser')
printer_2 = Printer(name='HP', invent_number=3141, quantity=2, color='black', multicolour='Yes', printer_type='Laser')
printer_3 = Printer(name='HP', invent_number=3142, quantity=2, color='white', multicolour='Yes', printer_type='Laser')

print(Printer.printer_wh_info)

scanner_1 = Scanner(name='HP', invent_number=3545, quantity=3, color='black', scanner_type='Двусторонний')
scanner_2 = Scanner(name='HP', invent_number=3545, quantity=4, color='black', scanner_type='Двусторонний')
scanner_3 = Scanner(name='Samsung', invent_number=3555, quantity=3, color='white', scanner_type='Односторонний')
print(Scanner.scanner_wh_info)

copier_1 = Copier(name='HP', invent_number=6352, quantity=3, color='black', multicolour='Yes')
copier_2 = Copier(name='HP', invent_number=6352, quantity=1, color='black', multicolour='Yes')
copier_3 = Copier(name='Samsung', invent_number=6745, quantity=3, color='white', multicolour='No')
print(Copier.copier_wh_info)

print(OfficeEquipmentWarehouse.get_warehouse_info())
OfficeEquipmentWarehouse.incoming_office_equipment()
print(OfficeEquipmentWarehouse.get_warehouse_info())

OfficeEquipmentWarehouse.outgo_office_equipment()
print(OfficeEquipmentWarehouse.get_warehouse_info())
