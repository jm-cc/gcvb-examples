#modifier example that changes all the test ids.

def modify(data):
    test_id=0
    for p in data["Packs"]:
        for t in p["Tests"]:
            t["id"]="id_{}".format(test_id)
    return data

