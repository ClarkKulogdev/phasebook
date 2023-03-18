from flask import Blueprint, request, redirect

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("", methods=['POST','GET'])
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    if(isEmpty(args) == True):
        return USERS
    else:
        return searchByInput(args)


def isEmpty(args):
    if bool(args):
        countEmpty = 0
        for key in args:
            if args[key] == "":
                countEmpty += 1
        if countEmpty == 4:
            isEmpty = True
        else:
            isEmpty = False
    else:
        isEmpty = True
    
    return isEmpty

def searchByInput(args):
    foundIds = {}
    prioriyList = ["id","name","age","occupation"]
    idsbasedonpriority = []

    # sorted based on ids
    # for user in USERS:
        # for key in args:
    
    ## Sorted based on priority
    for key in prioriyList:
        for user in USERS:
            if(args[key]!= ""):
                if(user[key] == args[key]):
                    foundIds[user["id"]] = user["id"]
                    # idsbasedonpriority.append(user["id"])
                elif key=="name" or key=="occupation":
                    if(user[key].lower() == args[key].lower()):
                        foundIds[user["id"]] = user["id"]
                        # idsbasedonpriority.append(user["id"])
                    elif args[key].lower() in user[key].lower():
                        foundIds[user["id"]] = user["id"]
                        # idsbasedonpriority.append(user["id"])
                elif key == "age":
                    if int(user[key]) == int(args[key])+1 or int(user[key]) == int(args[key])-1 or int(user[key]) == int(args[key]):
                        foundIds[user["id"]] = user["id"]
                        # idsbasedonpriority.append(user["id"])
    return collectSearchedUser(foundIds)
    # return idsbasedonpriority

def collectSearchedUser(foundIds):
    foundUsers = []
    for id in foundIds:
        for user in USERS:
            if foundIds[id] == user["id"]:
                foundUsers.append(user)
    return foundUsers
