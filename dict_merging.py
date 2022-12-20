url_responses = [
   {
      "empty_requests":[
         {
            "request_url":"https://apps.fas.usda.gov/OpenData/api/gats/censusImports/partnerCode/A1/year/2017/month/1"
         }
      ]
   }
      ,
   {
      "censusimports":[
         {
            "consumptionQuantity1":0.0,
            "consumptionQuantity2":0.0,
            "consumptionValue":13046.0,
            "consumptionCIFValue":17166.0,
            "cifValue":4120.0,
            "date":"201701",
            "countryCode":"Z1",
            "hS10Code":"0301110090",
            "censusUOMId1":95,
            "censusUOMId2":95,
            "fasConvertedUOMId":0,
            "fasNonConvertedUOMId":0,
            "quantity1":0.0,
            "quantity2":0.0,
            "value":13046.0,
            "sha1_hash":"C6DF2323A1D3AAB55BA342963856542C0D3205CF"
         }
         ]
      }
      ,
   {
      "censusimports":[
         {
            "consumptionQuantity1":0.0,
            "consumptionQuantity2":0.0,
            "consumptionValue":13046.0,
            "consumptionCIFValue":17166.0,
            "cifValue":4120.0,
            "date":"201701",
            "countryCode":"CH",
            "hS10Code":"0301110090",
            "censusUOMId1":95,
            "censusUOMId2":95,
            "fasConvertedUOMId":0,
            "fasNonConvertedUOMId":0,
            "quantity1":0.0,
            "quantity2":0.0,
            "value":13046.0,
            "sha1_hash":"C6DF2323A1D3AAB55BA342963856542C0D3205CF"
         }
         ]
      }
      ,
   {
      "censusexports":[
         {
            "consumptionQuantity1":0.0,
            "consumptionQuantity2":0.0,
            "consumptionValue":13046.0,
            "consumptionCIFValue":17166.0,
            "cifValue":4120.0,
            "date":"201701",
            "countryCode":"Z1",
            "hS10Code":"0301110090",
            "censusUOMId1":95,
            "censusUOMId2":95,
            "fasConvertedUOMId":0,
            "fasNonConvertedUOMId":0,
            "quantity1":0.0,
            "quantity2":0.0,
            "value":13046.0,
            "sha1_hash":"C6DF2323A1D3AAB55BA342963856542C0D3205CF"
         }
         ]
      }
      ,
   {
      "censusexports":[
         {
            "consumptionQuantity1":0.0,
            "consumptionQuantity2":0.0,
            "consumptionValue":13046.0,
            "consumptionCIFValue":17166.0,
            "cifValue":4120.0,
            "date":"201701",
            "countryCode":"CH",
            "hS10Code":"0301110090",
            "censusUOMId1":95,
            "censusUOMId2":95,
            "fasConvertedUOMId":0,
            "fasNonConvertedUOMId":0,
            "quantity1":0.0,
            "quantity2":0.0,
            "value":13046.0,
            "sha1_hash":"C6DF2323A1D3AAB55BA342963856542C0D3205CF"
         }
         ,
         {
            "consumptionQuantity1":0.0,
            "consumptionQuantity2":0.0,
            "consumptionValue":13046.0,
            "consumptionCIFValue":17166.0,
            "cifValue":4120.0,
            "date":"201701",
            "countryCode":"CH",
            "hS10Code":"0301110090",
            "censusUOMId1":95,
            "censusUOMId2":95,
            "fasConvertedUOMId":0,
            "fasNonConvertedUOMId":0,
            "quantity1":0.0,
            "quantity2":0.0,
            "value":13046.0,
            "sha1_hash":"C6DF2323A1D3AAB55BA342963856542C0D3205CF"
         }
         ]
      }
]

response_json = {
        "insert" : {},
        "schema" : {}
    }

inserts = {
    k: [val for sublist in [d[k] for d in url_responses if k in d] for val in sublist]
    for k in set().union(*url_responses)
    }

print(inserts)

response_json["insert"] = inserts

print(response_json)

{"primary_key": ["sha1_hash"]}

entities = ['censusreexports', 'customsdistrictexports', 'censusimports', 'censusexports', 'customsdistrictreexports', 'customsdistrictimports', 'empty_requests']

schemas = {i: ({"primary_key": ["sha1_hash"]} if i != "empty_requests" else {"primary_key": ["request_url"]} ) for i in entities}

print(schemas)
