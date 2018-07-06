# -*- coding: utf-8 -*-
# __author__=luhu
import jsonschema
schema = {"type": "object", "properties": {"price": {"type": "number"}, "name": {"type": "string"}, }}
data = {"name": "Eggs", "price": '34.99'}

schema3 = {
	"type": "object",
	"properties": {
		"age": {
			"type": "object",
            "properties": {
                "name": {
                    "type": "number"
                }
            }
		}
	}
}
data3 = {"age": {"name": "qewq"}}


jsonschema.validate(data3, schema3)
print('校验通过！！！')
