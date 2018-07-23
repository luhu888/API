# __author__=luhu
# -*- coding: utf-8 -*-
import json
import jsonschema
import requests

url = 'http://test2.xinheyun.com/api/user-center/auth'
data = {'phone': 'luhu_test', 'password': '123456'}
r = requests.post(url=url, data=data)
print(r.status_code)
data = json.loads(r.text)
print(type(data))
print('手机号码：'+ data['data']['mobile'])
response = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
print('返回数据:' + response)
schema = {
    "$id": "http://example.com/example.json",
    "type": "object",
    "definitions": {
    },
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
        "data": {
            "$id": "/properties/data",
            "type": "object",
            "properties": {
                "channels": {
                    "$id": "/properties/data/properties/channels",
                    "type": "array",
                    "items": {
                        "$id": "/properties/data/properties/channels/items",
                        "type": "string",
                        "title": "The 0th Schema ",
                        "default": "",
                        "examples": [
                            "02f876ef64659b24d243ff1de0bb5d4b"
                        ]
                    }
                },
                "clientType": {
                    "$id": "/properties/data/properties/clientType",
                    "type": "integer",
                    "title": "The Clienttype Schema ",
                    "default": 0,
                    "examples": [
                        0
                    ]
                },
                "client_type": {
                    "$id": "/properties/data/properties/client_type",
                    "type": "integer",
                    "title": "The Client_type Schema ",
                    "default": 0,
                    "examples": [
                        0
                    ]
                },
                "companyName": {
                    "$id": "/properties/data/properties/companyName",
                    "type": "string",
                    "title": "The Companyname Schema ",
                    "default": "",
                    "examples": [
                        ""
                    ]
                },
                "company_name": {
                    "$id": "/properties/data/properties/company_name",
                    "type": "string",
                    "title": "The Company_name Schema ",
                    "default": "",
                    "examples": [
                        ""
                    ]
                },
                "industry": {
                    "$id": "/properties/data/properties/industry",
                    "type": "integer",
                    "title": "The Industry Schema ",
                    "default": 0,
                    "examples": [
                        0
                    ]
                },
                "mobile": {
                    "$id": "/properties/data/properties/mobile",
                    "type": "string",
                    "title": "The Mobile Schema ",
                    "default": "",
                    "examples": [
                        "15856691310"
                    ]
                },
                "paid_type": {
                    "$id": "/properties/data/properties/paid_type",
                    "type": "integer",
                    "title": "The Paid_type Schema ",
                    "default": 0,
                    "examples": [
                        1
                    ]
                },
                "staffId": {
                    "$id": "/properties/data/properties/staffId",
                    "type": "integer",
                    "title": "The Staffid Schema ",
                    "default": 0,
                    "examples": [
                        3893
                    ]
                },
                "staffName": {
                    "$id": "/properties/data/properties/staffName",
                    "type": "string",
                    "title": "The Staffname Schema ",
                    "default": "",
                    "examples": [
                        "卢虎"
                    ]
                },
                "staff_id": {
                    "$id": "/properties/data/properties/staff_id",
                    "type": "integer",
                    "title": "The Staff_id Schema ",
                    "default": 0,
                    "examples": [
                        3893
                    ]
                },
                "staff_name": {
                    "$id": "/properties/data/properties/staff_name",
                    "type": "string",
                    "title": "The Staff_name Schema ",
                    "default": "",
                    "examples": [
                        "卢虎"
                    ]
                },
                "supplier_company_name": {
                    "$id": "/properties/data/properties/supplier_company_name",
                    "type": "null",
                    "title": "The Supplier_company_name Schema ",
                    "default": None,
                    "examples": [
                        None
                    ]
                },
                "tenantID": {
                    "$id": "/properties/data/properties/tenantID",
                    "type": "string",
                    "title": "The Tenantid Schema ",
                    "default": "",
                    "examples": [
                        "dceb93ab-3f89-45e5-9aad-1953b484816d"
                    ]
                },
                "tenantId": {
                    "$id": "/properties/data/properties/tenantId",
                    "type": "string",
                    "title": "The Tenantid Schema ",
                    "default": "",
                    "examples": [
                        "dceb93ab-3f89-45e5-9aad-1953b484816d"
                    ]
                },

            },

        },

        "ret": {
            "$id": "/properties/ret",
            "type": "boolean",
            "title": "The Ret Schema ",
            "default": True,
            "examples": [
                True
            ]
        }
    },
    'required': ['data', 'ret'],
}

jsonschema.validate(data, schema)
print('校验通过！！！')
