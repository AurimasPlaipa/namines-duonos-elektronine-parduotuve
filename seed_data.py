
from app import Bread, db




db.create_all()

bread1 = Bread(name="Naminė duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis ", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis, be konservantų", price= 8.00),
bread2 = Bread(name="Naminė duona su saulėgrąžomis ir moliūgų sėklomis", description="Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis ir moliūgų sėklomis, be konservantų", price= 7.00),
bread3 = Bread(name="Naminė duona su saulėgrąžomis ir kanapių sėklomis", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgražomis ir kanapių sėklomis, be konservantų", price= 7.00),
bread4 = Bread(name="Naminė duona su kmynais", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su kmynais, be konservantų", price=6.00),
bread5 = Bread(name="Naminė duona su saulėgrąžomis", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis, be konservantų", price= 6.00),
bread6 = Bread(name="Naminė duona su riešutais ir medumi", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su riešutais ir medumi, be konservantų", price= 6.00),
bread7 = Bread(name="Naminė duona su vaisiais", description= "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su vaisiais, be konservantų", price= 7.00)

db.session.add_all([bread1, bread2, bread3, bread4, bread5, bread6, bread7])

db.session.commit()



