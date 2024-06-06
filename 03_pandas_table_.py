import pandas

all_names = ["chairs", "cloth", "tables"]
var_how_much = [4, 1, 2]
price = [12, 22.99, 35]

assessment_dict = {
    "Name": all_names,
    "quantity": var_how_much,
    "price": price,
}

assessment_frame = pandas.DataFrame(assessment_dict)

assessment_frame['total'] = assessment_frame['quantity'] * assessment_frame['price']
print(assessment_frame)
