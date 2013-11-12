# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import *

class ReviewModel(ModelBase):
    class Meta:
        db_table = 'map_guest_reviews'
    id = IntegerField()
    product_id = IntegerField()
    guest_id = IntegerField()
    is_approved = BooleanField()
    comment = TextField()
    ranked_stars = IntegerField()
    review_date = DateTimeField(default = None)

