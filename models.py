"""Models for Blogly."""


from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

DEFAULT_IMAGE_URL = https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.freeiconspng.com%2Fuploads%2Ficon-user-blue-symbol-people-person-generic--public-domain--21.png%3Ffbclid%3DIwAR3O4SgpJMY4I6mW8JdC1zsCp9EZdvTir5Ts-Hq3T1Zk5_XaqU8omDf4Y1M&h=AT15uBUNxs0WSTTTZmR163egyYph6H0nBqrlx-_g99OFfiKDwJJ8ZgDSZ-tCliNDLGlV8roBpSTRMo5xsVH0IP9UTA9P7STfpuF4fAOHouPZuzUwgkTkY4SoyTvf5qppPBkaqf3eUJHNsdqRkxF4aJHfjjo


class User(db.model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)


    @property
    def full_name(self):
        """Return full name of user."""


        return f"{self.first_name} {self.last_name}"
    


    def connect_db(app):
        """Connect this database to provided Flask APP
        You should call this in your Flask app.
        """

        db.app = app
        db.init_app(app)

