import json

invoice_detail = dict(
    invoice_no = 1234,
    customer_name = "john",
    email = "john@gmail.com",
    tags = [1,2,3]
)
convert_json = json.dumps("invoice_detail")
print(convert_json)

#converted python dictionary

convert_python = json.loads("convert_json")
print(convert_python)