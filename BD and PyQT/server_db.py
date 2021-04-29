from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker


class ServerStorage:
    class Goods:
        def __init__(self, good_unit, good_name, good_cat):
            self.good_id = None
            self.good_unit = good_unit
            self.good_name = good_name
            self.good_cat = good_cat

    class Employees:
        def __init__(self, employees_fio, employees_position):
            self.employees_id = None
            self.employees_fio = employees_fio
            self.employees_position = employees_position

    class Vendors:
        def __init__(self, vendor_name, vendor_ownerchipform, vendor_address, vendor_phone, vendor_email):
            self.vendor_id = None
            self.vendor_name = vendor_name
            self.vendor_ownerchipform = vendor_ownerchipform
            self.vendor_address = vendor_address
            self.vendor_phone = vendor_phone
            self.vendor_email = vendor_email

    class Categories:
        def __init__(self, category_name, category_description):
            self.category_id = None
            self.category_name = category_name
            self.category_description = category_description

    class Units:
        def __init__(self):
            self.unit = None

    class Positions:
        def __init__(self):
            self.position = None

    def __init__(self):
        self.creator_database = create_engine('sqlite:///sobesbd.sqlite', echo=False, pool_recycle=7200)
        self.metadata = MetaData()
        categories_table = Table('Categories', self.metadata,
                                 Column('category_id', Integer, primary_key=True),
                                 Column('category_name', String),
                                 Column('category_description', String)
                                 )

        units_table = Table('Units', self.metadata,
                            Column('units_id', Integer, primary_key=True)
                            )

        positions_table = Table('Positions', self.metadata,
                                Column('positions_id', Integer, primary_key=True)
                                )

        goods_table = Table('Goods', self.metadata,
                            Column('good_id', Integer, primary_key=True),
                            Column('good_unit', ForeignKey('Units.units_id')),
                            Column('good_name', String),
                            Column('good_cat', ForeignKey('Categories.category_id'))
                            )
        employees_table = Table('Employees', self.metadata,
                                Column('employees_id', Integer, primary_key=True),
                                Column('employees_fio', String),
                                Column('employees_position', ForeignKey('Positions.positions_id'))
                                )
        vendors_table = Table('Vendors', self.metadata,
                              Column('vendor_id', Integer, primary_key=True),
                              Column('vendor_name', String),
                              Column('vendor_ownerchipform', String),
                              Column('vendor_address', String),
                              Column('vendor_phone', String),
                              Column('vendor_email', String)
                              )

        self.metadata.create_all(self.creator_database)

        mapper(self.Positions, positions_table)
        mapper(self.Units, units_table)
        mapper(self.Categories, categories_table)
        mapper(self.Employees, employees_table)
        mapper(self.Vendors, vendors_table)
        mapper(self.Goods, goods_table)

        Session = sessionmaker(bind=self.creator_database)
        self.session = Session()

        # self.session.query(self.ActiveUsers).delete()
        self.session.commit()

    def goods_list(self):
        query = self.session.query(
            self.Goods.good_name,
            self.Goods.good_cat,
        )
        return query.all()


if __name__ == '__main__':
    db_test = ServerStorage()
    print(db_test.goods_list())
