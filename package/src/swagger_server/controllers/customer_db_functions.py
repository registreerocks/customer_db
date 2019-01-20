from pymongo import MongoClient, ReturnDocument
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.customer_database
customer_details = db.customer_details
invoice_details = db.invoice_details
payment_status = db.payment_status

def post_customer(body):
    return str(customer_details.insert_one(body).inserted_id)

def get_customer(id):
    result = customer_details.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def put_customer(id, body):
    result = customer_details.find_one_and_update(
                {'_id': ObjectId(id)},
                {'$set':{body.get('field'): body.get('value')}},
                return_document=ReturnDocument.AFTER
            )
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def post_invoice(body):
    return str(invoice_details.insert_one(body).inserted_id)

def get_invoice(id):
    result = invoice_details.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def put_invoice(id, body):
    result = invoice_details.find_one_and_update(
                {'_id': ObjectId(id)},
                {'$set':{body.get('field'): body.get('value')}},
                return_document=ReturnDocument.AFTER
            )
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def post_payment(body):
    return str(payment_status.insert_one(body).inserted_id)

def get_payment(id):
    result = payment_status.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def put_payment(id, body):
    result = payment_status.find_one_and_update(
                {'_id': ObjectId(id)},
                {'$set':{body.get('field'): body.get('value')}},
                return_document=ReturnDocument.AFTER
            )
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409