d = {
  "pageNumber": 1,
  "dataList": [
    {
      "memberships": [],
      "customFields": [],
      "links": [],
      "tags": [],
      "engagementScore": "",
      "firstName": "Miguel",
      "lastName": "Aburto",
      "name": "Miguel Aburto",
      "middleName": "",
      "preferredFirstName": "",
      "secondLastName": "",
      "prefix": "",
      "suffix": "",
      "gender": "",
      "primaryOrganization": {
        "contactIds": [],
        "parentCompanyId": "",
        "description": "",
        "branchName": "",
        "tags": [],
        "acronym": "",
        "engagementScore": "",
        "region": "",
        "id": "b6d63055-8128-44f2-91d2-c95b47558b24",
        "customerType": "O",
        "recordNumber": "1117",
        "title": "",
        "name": "Oxbo International",
        "addresses": [],
        "imageUri": "https://access.blueberry.org/images/no-org-image-available.png",
        "emails": [],
        "phones": [],
        "webSite": "",
        "memberships": [],
        "category": "",
        "categories": [],
        "customFields": [],
        "showInDirectory": True,
        "links": [],
        "oldId": ""
      },
      "id": "d3d8d2c6-a6f5-46dd-8a46-6da286eae759",
      "customerType": "I",
      "recordNumber": "5599",
      "showInDirectory": True,
      "addresses": [],
      "emails": [],
      "phones": [],
      "categories": [],
      "email": "",
      "imageUri": "https://access.blueberry.org/images/no-ind-image-available.png",
      "title": ""
    },
    {
      "memberships": [],
      "customFields": [],
      "links": [],
      "tags": [],
      "engagementScore": "",
      "firstName": "Filip",
      "lastName": "Adam",
      "name": "Filip Adam",
      "middleName": "",
      "preferredFirstName": "",
      "secondLastName": "",
      "prefix": "",
      "suffix": "",
      "gender": "",
      "primaryOrganization": {
        "contactIds": [],
        "parentCompanyId": "",
        "description": "",
        "branchName": "",
        "tags": [],
        "acronym": "",
        "engagementScore": "",
        "region": "",
        "id": "5ff63bf8-59de-4dc5-b1c5-50fbab4076b1",
        "customerType": "O",
        "recordNumber": "1124",
        "title": "",
        "name": "Thunderbird Plastics, Ltd.",
        "addresses": [],
        "imageUri": "https://access.blueberry.org/images/no-org-image-available.png",
        "emails": [],
        "phones": [],
        "webSite": "",
        "memberships": [],
        "category": "",
        "categories": [],
        "customFields": [],
        "showInDirectory": True,
        "links": [],
        "oldId": ""
      },
      "id": "f22d84d5-5b03-40d0-a302-246e3d1224d5",
      "customerType": "I",
      "recordNumber": "2143",
      "showInDirectory": False,
      "addresses": [],
      "emails": [],
      "phones": [],
      "categories": [],
      "email": "",
      "imageUri": "https://access.blueberry.org/images/no-ind-image-available.png",
      "title": ""
    },
    {
      "memberships": [],
      "customFields": [],
      "links": [],
      "tags": [],
      "engagementScore": "",
      "firstName": "mark",
      "lastName": "adams",
      "name": "mark adams",
      "middleName": "",
      "preferredFirstName": "",
      "secondLastName": "",
      "prefix": "",
      "suffix": "",
      "gender": "",
      "primaryOrganization": {
        "contactIds": [],
        "parentCompanyId": "",
        "description": "",
        "branchName": "",
        "tags": [
          "USHBC Handler"
        ],
        "acronym": "",
        "engagementScore": "",
        "region": "",
        "id": "931d7caa-4660-4175-bbe7-4a68c8dddf53",
        "customerType": "O",
        "recordNumber": "1009",
        "title": "",
        "name": "Berryhill Foods, Inc.",
        "addresses": [],
        "imageUri": "https://access.blueberry.org/images/no-org-image-available.png",
        "emails": [],
        "phones": [],
        "webSite": "",
        "memberships": [],
        "category": "",
        "categories": [],
        "customFields": [],
        "showInDirectory": True,
        "links": [],
        "oldId": ""
      },
      "id": "2b4c072f-1b7b-4e6b-9ad3-bfdffa8372bd",
      "customerType": "I",
      "recordNumber": "5816",
      "showInDirectory": False,
      "addresses": [],
      "emails": [],
      "phones": [],
      "categories": [],
      "email": "",
      "imageUri": "https://access.blueberry.org/images/no-ind-image-available.png",
      "title": ""
    }
 ]
}

individual_ids = [i["id"] for i in d["dataList"]]

print(individual_ids)