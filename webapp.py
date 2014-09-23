from flask import Flask, request
from canvas_signed_request import SignedRequest
app = Flask(__name__)
import os

@app.route("/")
def hello():
	return "Hello World!"

# add a new route
@app.route('/canvas', methods=['POST'])
def canvas():
	secret = os.environ.get('SECRET')
	sr_param = request.form['signed_request']
	srHelper = SignedRequest(secret,sr_param)
	canvasRequestJSON = srHelper.verifyAndDecode()
	return canvasRequestJSON['context']['enviroment']['record']['id']

if __name__ == "__main__":
	app.run()
	'''
	{  
   "algorithm":"HMACSHA256",
   "issuedAt":-1555461611,
   "userId":"005i0000001CPTiAAO",
   "client":{  
      "refreshToken":null,
      "instanceId":"_:python_salesforce_test:j_id0:j_id1:canvasapp",
      "targetOrigin":"https://c.na15.visual.force.com",
      "instanceUrl":"https://na15.salesforce.com",
      "oauthToken":"00Di0000000dulO!AQsAQBW2erVp284P5sxb3hJ1h_4EWCJbZVlVrazphaX3AN06nps8mdPooT_P2ywIjiEv06nxFbKUOoZkP7qxBIvlLA4w_qr0"
   },
   "context":{  
      "user":{  
         "userId":"005i0000001CPTiAAO",
         "userName":"steven.m.simoni@gmail.com",
         "firstName":"Steven",
         "lastName":"Simoni",
         "email":"steven.m.simoni@gmail.com",
         "fullName":"Steven Simoni",
         "locale":"en_US",
         "language":"en_US",
         "timeZone":"America/Los_Angeles",
         "profileId":"00ei00000013FPB",
         "roleId":null,
         "userType":"STANDARD",
         "currencyISOCode":"USD",
         "profilePhotoUrl":"https://c.na15.content.force.com/profilephoto/005/F",
         "profileThumbnailUrl":"https://c.na15.content.force.com/profilephoto/005/T",
         "siteUrl":null,
         "siteUrlPrefix":null,
         "networkId":null,
         "accessibilityModeEnabled":false,
         "isDefaultNetwork":true
      },
      "links":{  
         "loginUrl":"https://login.salesforce.com/",
         "enterpriseUrl":"/services/Soap/c/31.0/00Di0000000dulO",
         "metadataUrl":"/services/Soap/m/31.0/00Di0000000dulO",
         "partnerUrl":"/services/Soap/u/31.0/00Di0000000dulO",
         "restUrl":"/services/data/v31.0/",
         "sobjectUrl":"/services/data/v31.0/sobjects/",
         "searchUrl":"/services/data/v31.0/search/",
         "queryUrl":"/services/data/v31.0/query/",
         "recentItemsUrl":"/services/data/v31.0/recent/",
         "chatterFeedsUrl":"/services/data/v31.0/chatter/feeds",
         "chatterGroupsUrl":"/services/data/v31.0/chatter/groups",
         "chatterUsersUrl":"/services/data/v31.0/chatter/users",
         "chatterFeedItemsUrl":"/services/data/v31.0/chatter/feed-items",
         "userUrl":"/005i0000001CPTiAAO"
      },
      "application":{  
         "namespace":null,
         "name":"python salesforce test",
         "canvasUrl":"https://sfcanvaspythonapptest.herokuapp.com/canvas",
         "applicationId":"06Pi0000000Ik9T",
         "version":"1.0",
         "authType":"SIGNED_REQUEST",
         "referenceId":"09Hi00000008jRM",
         "options":[  

         ],
         "samlInitiationMethod":"None",
         "developerName":"python_salesforce_test"
      },
      "organization":{  
         "organizationId":"00Di0000000dulOEAQ",
         "name":"Marketo",
         "multicurrencyEnabled":false,
         "namespacePrefix":null,
         "currencyIsoCode":"USD"
      },
      "environment":{  
         "locationUrl":"https://c.na15.visual.force.com/servlet/servlet.Integration?lid=066i0000004JMXr&ic=1",
         "displayLocation":"Visualforce",
         "sublocation":null,
         "uiTheme":"Theme3",
         "dimensions":{  
            "width":"500px",
            "height":"100px",
            "maxWidth":"1000px",
            "maxHeight":"2000px",
            "clientWidth":"1148px",
            "clientHeight":"30px"
         },
         "parameters":{  

         },
         "record":{  
            "Id":"003i000000IMVhXAAX",
            "attributes":{  
               "type":"Contact",
               "url":"/services/data/v31.0/sobjects/Contact/003i000000IMVhXAAX"
            }
         },
         "version":{  
            "season":"SUMMER",
            "api":"31.0"
         }
      }
   }
}
	'''