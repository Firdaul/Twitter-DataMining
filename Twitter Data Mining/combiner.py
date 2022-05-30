import json

result = []
for num in range(1, 107):
    with open("YOURFILENAME"+str(num)+".json") as infile:
        json_data = json.load(infile)
        if json_data.get('results') is not None:
            for data in json_data.get('results'):
                result.append(data)
with open("FULLDATACOMBINEFILENAME.json", "w") as outfile:
    json.dump(result, outfile)  # print(result)
     
print("DONE!!!")