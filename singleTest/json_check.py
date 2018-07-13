# -*- coding: utf-8 -*-
# __author__=luhu
import jsonschema
schema = {"type": "object", "properties": {"price": {"type": "number"}, "name": {"type": "string"}, }}
data = {"name": "Eggs", "price": '34.99'}

schema3 = {
  "$id": "http://example.com/example.json",
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "checked": {
      "$id": "/properties/checked",
      "type": "boolean",
      "title": "The Checked Schema ",
      "default": False,
      "examples": [
        False
      ]
    },
    "dimensions": {
      "$id": "/properties/dimensions",
      "type": "object",
      "properties": {
        "width": {
          "$id": "/properties/dimensions/properties/width",
          "type": "integer",
          "title": "The Width Schema ",
          "default": 0
        },
        "height": {
          "$id": "/properties/dimensions/properties/height",
          "type": "integer",
          "title": "The Height Schema ",
          "default": 0,
          "examples": [
            10
          ]
        }
      }
    },
    "id": {
      "$id": "/properties/id",
      "type": "integer",
      "title": "The Id Schema ",
      "default": 0,
      "examples": [
        1
      ]
    },
    "name": {
      "$id": "/properties/name",
      "type": "string",
      "title": "The Name Schema ",
      "default": "",
      "examples": [
        "A green door"
      ]
    },
    "price": {
      "$id": "/properties/price",
      "type": "number",
      "title": "The Price Schema ",
      "default": 0,
      "examples": [
        12.5
      ]
    },
    "tags": {
      "$id": "/properties/tags",
      "type": "array",
      "items": {
        "$id": "/properties/tags/items",
        "type": "string",
        "title": "The 0th Schema ",
        "default": "",
        "examples": [
          "home",
          "green"
        ]
      }
    }
  }
}
data3 = {
  "checked": False,
  "dimensions": {
    "width": 5,
    "height": 10
  },
  "id": 1,
  "name": "A green door",
  "price": '12.5',
  "tags": [
    "home",
    "green"
  ]
}


jsonschema.validate(data3, schema3)
print('校验通过！！！')
