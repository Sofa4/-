class Colors:
    def __init__(self, name, r, g, b):  # иницилизация класса (конструктор)
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):  # преобразование класса в строку
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):  # сравнение экземпляров класса
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented


red = Colors('красный', 255, 0, 0)
green = Colors('зеленый', 0, 255, 0)
otherRed = Colors('другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red == green)
print(red == otherRed)

# --------------------------------------------------------------------------------------------------------
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # ----------------------------------------------------
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        if w > 0:
            self._width = w
        else:
            raise ValueError

    # ----------------------------------------------------
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if h > 0:
            self._height = h
        else:
            raise ValueError

    # ----------------------------------------------------
    def area(self):
        return self._width * self._height

    # ----------------------------------------------------
    def __str__(self):
        return f"Rectangle (w={self._width}, h={self._height})"


rect = Rectangle(10, 20)
print(rect.width)
print(rect.height)
print(Rectangle(10, 20))
