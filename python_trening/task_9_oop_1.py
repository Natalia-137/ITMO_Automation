from task_9_checks import Checks

class Input (Checks):

    def __init__(self, text, loc):
        super ().__init__(loc)
        self.text = text
        self.loc = loc

search = Input('One', 'input#search')

# print(search.text)
# print(search.loc)

class Button (Checks):

    def __init__(self,text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

button = Button('Кнопка', 'button#button')

# print(button.text)
# print(button.loc)

class Title (Checks):

    def  __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


title = Title('Заголовок', 'title#title')

# print(title.text)
# print(title.loc)

class Link (Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

link = Link('Ссылка', 'link#link')

# print(link.text)
# print(link.loc)

search.check_text()
button.check_text()
title.check_text()
link.check_text()