import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import desc


from ..models import Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel, \
    Plan as PlanModel, \
    ClientProvider as ClientProviderModel



# Provider Object
class ProviderObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = ProviderModel
        interfaces = (relay.Node, )


# Client Object
class ClientObject(SQLAlchemyObjectType):
    client_id = graphene.Int(source='id')

    class Meta:
        model = ClientModel
        interfaces = (relay.Node, )

    journal_entries = graphene.List(
        lambda: JournalObject, 
        entry=graphene.String(), date_entered=graphene.DateTime() 
        )

    def resolve_journal_entries(self, info):
        query = JournalObject.get_query(info=info)
        query = query.filter(JournalModel.client_id == self.id)
        query = query.order_by(desc(JournalModel.date_entered))

        return query.all()


# Plan Object
class PlanObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = PlanModel
        interfaces = (relay.Node, )



# Client|Provider|Plan Object
class ClientProviderObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = ClientProviderModel
        interfaces = (relay.Node, )



# Journal Object
class JournalObject(SQLAlchemyObjectType):

     class Meta:
        model = JournalModel
        interfaces = (relay.Node, )

