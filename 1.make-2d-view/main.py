from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        imageObject = OnscreenImage(image='me.png', pos=(-0.5, 0, 0.02))
        # Reparent the model to render.
        imageObject.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        imageObject.setScale(10, 10, 10)
        imageObject.setPos(0, 42, 0)

        car = OnscreenImage(image="car.png", pos=(0,0,0))
        car.reparent_to(self.render)
        car.setScale(3, 3, 3)
        car.setPos(0, 41, 0)

        self.accept('arrow_left-up', self.car_go_left, [car])
        self.accept('arrow_right-up', self.car_go_right, [car])

    def car_go_left(self, car):
        pos = car.getPos()
        car.setPos(pos.x-1, pos.y, pos.z)

    def car_go_right(self, car):
        pos = car.getPos()
        car.setPos(pos.x+1, pos.y, pos.z)

app = MyApp()
app.run()
