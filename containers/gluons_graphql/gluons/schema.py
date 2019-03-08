import graphene
import graphql_jwt

import graphql_api.schema
import users.schema


class Query(
        users.schema.Query,
        graphql_api.schema.Query,
        graphene.ObjectType):
    pass

class Mutation(
        users.schema.Mutation,
        graphql_api.schema.Mutation,
        graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

