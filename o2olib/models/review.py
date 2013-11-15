# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.models.guest import GuestModel
from o2olib.peewee import *
from o2olib.utils import utils

class ReviewModel(ModelBase):
    class Meta:
        db_table = 'map_guest_reviews'
    id = IntegerField()
    product_id = IntegerField()
    guest_id = ForeignKeyField(GuestModel,db_column="guest_id")
    is_approved = BooleanField()
    comment = TextField()
    ranked_stars = IntegerField()
    review_date = DateTimeField(default = None)

    @classmethod
    def build_con_dict(cls,con_dict):
        is_approved_strs = con_dict.get("is_approved")
        if is_approved_strs:
            is_approved_str = is_approved_strs[0]
            is_approved = utils.str2bool(is_approved_str)
            if is_approved is not None:
                con_dict["is_approved"] = is_approved
        return con_dict

