class PlaneView:
    def __init__(self, image):
        self.original_image = image
        self.image = image

    def draw(self, screen, position):
        #Отрисовка самолётика
        rect = self.image.get_rect(center=position)
        screen.blit(self.image, rect)
        return rect

    def get_rect(self, position):
        #Обновление расположения самолётика
        return self.image.get_rect(center=position)