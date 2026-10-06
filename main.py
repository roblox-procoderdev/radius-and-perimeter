class circle:
    def __init__(self):
        self.area=""
        self.perimeter=""
    def constructor(self):
        radial=float(input("enter a number:"))
        self.area=3.14*(radial**2)
        self.perimeter=2*3.14*radial
    def metriks(self):
        print("area and perimeter are",self.area,self.perimeter,"respectively")
cirkal=circle()
cirkal.constructor()
cirkal.metriks()