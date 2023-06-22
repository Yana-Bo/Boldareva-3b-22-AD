class Classmate:
  def __init__(self, name, class1):
       self.name = name
       self.class1 = class1
  def presentation(self):
    print("{name} учится в {class1} классе.".format(name=self.name, class1=self.class1))
st = Classmate("Полина", 9)
st.presentation()