from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SwapTransition
from kivy.metrics import dp
from kivymd.uix.button import MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ILeftBodyTouch, OneLineListItem, OneLineAvatarIconListItem
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.core.audio import SoundLoader
from data import data

Builder.load_file('layout.kv')


class My(MDScreenManager):
    P = []

    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.add, .1)

    def add(self, _):
        list = self.ids.list
        with open('text/ingredients.txt', 'r+', encoding='utf-8') as f:
            a = f.readline()
            a = a.split(';')
            for i in a:
                if len(i) != 0:
                    x = OneLineAvatarIconListItem(text=i, size_hint_y=None)
                    y = LeftCheckbox()
                    x.add_widget(y)
                    list.add_widget(x)

        list = self.ids.list
        prods = self.ids.meal
        prods.clear_widgets()
        with open('text/meals.txt', 'r+', encoding='utf-8') as f:
            a = f.readline()
            a = a.split(';')
            for i in a:
                for product in data.meal:
                    if str(product['meal_id']) == i:
                        f1 = self.ids.f1
                        f1.clear_widgets()
                        ck = self.ids.ck
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.breakfast:
                    if str(product['meal_id']) == i:
                        f1 = self.ids.f1
                        f1.clear_widgets()
                        ck = self.ids.ck
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.lunch:
                    if str(product['meal_id']) == i:
                        f1 = self.ids.f1
                        f1.clear_widgets()
                        ck = self.ids.ck
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.dessert:
                    if str(product['meal_id']) == i:
                        f1 = self.ids.f1
                        f1.clear_widgets()
                        ck = self.ids.ck
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.veta:
                    if str(product['meal_id']) == i:
                        f1 = self.ids.f1
                        f1.clear_widgets()
                        ck = self.ids.ck
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)

        list = self.ids.fav
        ck = self.ids.fav
        with open('text/fav.txt', 'r+', encoding='utf-8') as f:
            a = f.readline()
            a = a.split(';')
            for i in a:
                for product in data.meal:
                    if str(product['meal_id']) == i:

                        ck = self.ids.fav
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.breakfast:
                    if str(product['meal_id']) == i:

                        ck = self.ids.fav
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.lunch:
                    if str(product['meal_id']) == i:

                        ck = self.ids.fav
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.dessert:
                    if str(product['meal_id']) == i:

                        ck = self.ids.fav
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)
                for product in data.veta:
                    if str(product['meal_id']) == i:

                        ck = self.ids.fav
                        p = Product2()
                        p.meal_id = product['meal_id']
                        p.name = product['name']
                        p.source = product['source']
                        p.cookware = product['cookware']
                        p.ingredients = product['ingredients']
                        p.cook = product['cook']
                        p.bind(on_release=
                               self.view_product
                               )
                        p.bind(on_release=self.view_product)
                        p.bind(on_release=self.update3)
                        ck.add_widget(p)

        for product in data.meal:
            p = Product()
            p.meal_id = product['meal_id']
            p.name = product['name']
            p.source = product['source']
            p.cookware = product['cookware']
            p.ingredients = product['ingredients']
            p.cook = product['cook']
            p.bind(on_release=self.view_product)
            p.bind(on_release=self.update)
            prods.add_widget(p)

    def viewbreakfast(self):
        scr = self.ids.all
        prods = self.ids.lis
        prods.clear_widgets()
        close = MDIconButton(pos_hint = {"top": 1})
        close.icon = "close"
        close.bind(on_release = self.change)
        scr.add_widget(close)
        prods.clear_widgets()
        for product in data.breakfast:
            p = Product2()
            p.meal_id = product['meal_id']
            p.name = product['name']
            p.source = product['source']
            p.cookware = product['cookware']
            p.ingredients = product['ingredients']
            p.cook = product['cook']
            p.bind(on_release=self.view_product)
            p.bind(on_release = self.update2)
            prods.add_widget(p)
    def viewlunch(self):
        scr = self.ids.all
        prods = self.ids.lis
        prods.clear_widgets()
        close = MDIconButton(pos_hint={"top": 1})
        close.icon = "close"
        close.bind(on_release=self.change)
        scr.add_widget(close)
        prods.clear_widgets()
        for product in data.lunch:
            p = Product2()
            p.meal_id = product['meal_id']
            p.name = product['name']
            p.source = product['source']
            p.cookware = product['cookware']
            p.ingredients = product['ingredients']
            p.cook = product['cook']
            p.bind(on_release=self.view_product)
            p.bind(on_release = self.update2)
            prods.add_widget(p)
    def viewdessert(self):
        scr = self.ids.all
        prods = self.ids.lis
        prods.clear_widgets()
        close = MDIconButton(pos_hint={"top": 1})
        close.icon = "close"
        close.bind(on_release=self.change)
        scr.add_widget(close)
        prods.clear_widgets()
        for product in data.dessert:
            p = Product2()
            p.meal_id = product['meal_id']
            p.name = product['name']
            p.source = product['source']
            p.cookware = product['cookware']
            p.ingredients = product['ingredients']
            p.cook = product['cook']
            p.bind(on_release=self.view_product)
            p.bind(on_release = self.update2)
            prods.add_widget(p)
    def viewveta(self):
        scr = self.ids.all
        prods = self.ids.lis
        prods.clear_widgets()
        close = MDIconButton(pos_hint={"top": 1})
        close.icon = "close"
        close.bind(on_release=self.change)
        scr.add_widget(close)
        prods.clear_widgets()

        for product in data.veta:
            p = Product2()
            p.meal_id = product['meal_id']
            p.name = product['name']
            p.source = product['source']
            p.cookware = product['cookware']
            p.ingredients = product['ingredients']
            p.cook = product['cook']
            p.bind(on_release = self.view_product)
            p.bind(on_release = self.update2)
            prods.add_widget(p)

    def view_product(self, product):
        list = self.ids.tab1
        list.clear_widgets()
        list = self.ids.tab2
        list.clear_widgets()
        list = self.ids.tab3
        list.clear_widgets()
        ima= self.ids.ima
        tex = self.ids.tex
        ima.source = product.source
        tex.text = product.name
        a = product.cookware
        self.id2 = product.meal_id
        b = a.split(';')
        x = OneLineAvatarIconListItem(text = "đọc danh sách", size_hint_y = None)
        y = PlayButton()
        y.bind(on_release = self.play1)
        x.add_widget(y)
        self.ids.tab1.add_widget(x)
        x = OneLineAvatarIconListItem(text="đọc danh sách", size_hint_y=None)
        y = PlayButton()
        y.bind(on_release=self.play2)
        x.add_widget(y)
        self.ids.tab2.add_widget(x)
        for i in b:
            self.ids.tab1.add_widget(
                OneLineListItem(text = i, size_hint_y = None)
            )
        a = product.ingredients
        self.meal_id = product.meal_id
        self.name = product.name
        self.source = product.source
        self.ingredients = product.ingredients
        self.cookware = product.cookware
        self.cook = product.cook
        b = a.split(';')
        for i in b:
            self.ids.tab2.add_widget(
                OneLineListItem(text=i, size_hint_y=None)
            )
        x = OneLineAvatarIconListItem(text="đọc công thức", size_hint_y=None)
        y = PlayButton()
        y.bind(on_release=self.play3)
        x.add_widget(y)
        self.ids.tab3.add_widget(x)
        a = product.cook
        b = a.split(';')
        for i in b:
            p = cook()
            p.name = i
            self.ids.tab3.add_widget(p)
        self.transition = SwapTransition()
        self.current = 'scrn_plant'

    def play1(self, x):
        sound = SoundLoader.load('sounds/'+str(chr(self.id2+96))+'.wav')
        sound.play()

    def play2(self, x):
        sound = SoundLoader.load('sounds/'+str(chr(self.id2+96))+'().wav')
        sound.play()

    def play3(self, x):
        sound = SoundLoader.load('sounds/'+str(chr(self.id2+96))+'((.wav')
        sound.play()

    def change(self, x):
        self.current = 'build'
        self.transition.direction = 'down'
    def change1(self):
        self.current = 'build'
        self.transition.direction = 'down'
    def change2(self):
        self.current = 'all'
        self.transition.direction = 'down'
    def change3(self):
        self.current = 'main'
        self.transition.direction = 'down'
    def what(self):
        if self.po == 1:
            self.change1()
        if self.po == 2:
            self.change2()
        if self.po == 3:
            self.change3()
    def update2(self, x):
        self.po = 2
    def update(self, x):
        self.po = 1
    def update3(self, x):
        self.po = 3

    def setting(self):
        list = MDListBottomSheet(
            radius = 10,
            radius_from = 'top'
        )
        data = {
            "Hoàn thành mua sắm": "check-outline"
        }
        for item in data.items():
            list.add_item(
                item[0],
                lambda x, y=item[0]: self.clear(),
                icon=item[1]
            )
        list.open()

    def setting2(self):
        list = MDListBottomSheet(
            radius = 10,
            radius_from = 'top'
        )
        data = {
            "Hoàn thành nấu ăn": "check-outline"
        }
        for item in data.items():
            list.add_item(
                item[0],
                lambda x, y=item[0]: self.clear2(),
                icon=item[1]
            )
        list.open()

    def setting3(self):
        list = MDListBottomSheet(
            radius = 10,
            radius_from = 'top'
        )
        data = {
            "xóa danh sách yêu thích": "check-outline"
        }
        for item in data.items():
            list.add_item(
                item[0],
                lambda x, y=item[0]: self.clear3(),
                icon=item[1]
            )
        list.open()

    def addmeal(self):
        popup = MDDialog(title='Thông báo', text='Thêm vào thực đơn thành công! Vào giỏ hàng để bắt đầu mua sắm')
        popup.open()

        list = self.ids.list
        a = self.ingredients
        with open('text/ingredients.txt', 'a+', encoding='utf-8') as f:
            f.write(a)

        f = open('text/ingredients.txt', 'r', encoding='utf-8')
        a = f.readline()
        a = a.split(';')
        list = self.ids.list
        list.clear_widgets()
        for i in a:
            if len(i) != 0:
                x = OneLineAvatarIconListItem(text=i, size_hint_y=None)
                y = LeftCheckbox()
                x.add_widget(y)
                list.add_widget(x)

        f1 = self.ids.f1
        f1.clear_widgets()
        ck = self.ids.ck
        p = Product2()
        p.meal_id = self.meal_id
        p.name = self.name
        p.source = self.source
        p.cookware = self.cookware
        p.cook = self.cook
        p.ingredients = self.ingredients
        p.bind(on_release=
               self.view_product
               )
        p.bind(on_release=self.view_product)
        p.bind(on_release = self.update3)
        ck.add_widget(p)

        with open('text/meals.txt', 'a', encoding='utf-8') as f:
            f.write(str(p.meal_id))
            f.write(';')

    def addmeal2(self):
        popup = MDDialog(title='Thông báo', text='Thêm vào món ăn yêu thích thành công')
        popup.open()

        ck = self.ids.fav
        p = Product2()
        p.meal_id = self.meal_id
        p.name = self.name
        p.source = self.source
        p.cookware = self.cookware
        p.cook = self.cook
        p.ingredients = self.ingredients
        p.bind(on_release=
               self.view_product
               )
        p.bind(on_release=self.view_product)
        p.bind(on_release=self.update3)
        ck.add_widget(p)

        with open('text/fav.txt', 'a', encoding='utf-8') as f:
            f.write(str(p.meal_id))
            f.write(';')

    def clear(self):
        with open('text/ingredients.txt', 'w', encoding='utf-8') as f:
            f.write('')
        list = self.ids.list
        list.clear_widgets()

    def clear2(self):
        list = self.ids.ck
        list.clear_widgets()
        f1 = self.ids.f1
        f1.add_widget(normal())
        with open('text/meals.txt', 'w', encoding='utf-8') as f:
            f.write('')
    def clear3(self):
        with open('text/fav.txt', 'w', encoding='utf-8') as f:
            f.write('')
        list = self.ids.fav
        list.clear_widgets()


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom right container.'''

class PlayButton(ILeftBodyTouch, MDIconButton):
    icon = 'play'


class Product(ButtonBehavior, MDBoxLayout):
    meal_id = NumericProperty()
    name = StringProperty("")
    source = StringProperty("")
    cookware = StringProperty("")
    ingredients = StringProperty("")
    cook = StringProperty("")
    radiuss = NumericProperty(dp(18))

    def __init__(self, **kw) -> None:
        super().__init__(**kw)


class Product2(ButtonBehavior, MDBoxLayout):
    meal_id = NumericProperty()
    name = StringProperty("")
    source = StringProperty("")
    cookware = StringProperty("")
    ingredients = StringProperty("")
    cook = StringProperty("")
    radiuss = NumericProperty(dp(18))

    def __init__(self, **kw) -> None:
        super().__init__(**kw)


class cook(MDBoxLayout):
    name = StringProperty("")
    radiuss = NumericProperty(dp(18))


class Tab(MDBoxLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Lab(ButtonBehavior, MDLabel):
    pass

class normal(MDFloatLayout):
    pass


