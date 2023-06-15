async def create_collection(doc_data: dict, collection: str) -> dict:
    doc = await collection.insert_one(doc_data)
    new_doc = await collection.find_one({"_id": doc.inserted_id})
    if not new_doc:
        raise Exception("There are some problems to insert document into collection.")
    return new_doc


async def get_doc(val: str, collection: str) -> dict:
    doc = await collection.find_one({"name": val})
    if doc:
        return dict(doc)


async def delete_collection(collection: str):
    await collection.drop()
