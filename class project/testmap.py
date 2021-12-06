from kivy_garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=41.257160, lon=-95.995102)
        return mapview

MapViewApp().run()




#mapview = MapView(zoom=11, lat=41.257160, lon=-95.995102)