from o2olib.utils import utils
from o2olib.models.manual import ManualModel
from o2olib.peewee import  DeleteQuery,SelectQuery
from o2olib.models.modelbase import update_model

def gets(con_dic):
    con = ManualModel.build_con(con_dic)
    if con:
        query = ManualModel.select().where(con)
    else:
        query = ManualModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get(con):
    manuals = gets(con)
    if len(manuals) == 0:
        manual = {}
    else:
        manual = manuals[0]
    return manual

def count(con_dic):
    con = ManualModel.build_con(con_dic)
    sq = SelectQuery(ManualModel).where(con)
    return sq.count()
    
def add(obj):
    if obj:
        obj_in_db = get(obj)
        if not obj_in_db:
            model = ManualModel().create()
            update_model(model,obj)
            model.save()
            return model.id
        else:
            return obj_in_db.get("id")

def delete(obj):
    if obj:
        obj_in_db = get(obj)
        if obj_in_db:
            id = obj_in_db.get("id")
            delQuery = DeleteQuery(ManualModel).where(id = id)
            delQuery.execute()
            return id


