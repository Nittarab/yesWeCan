# Yes, We Can!

## The Problem
Nowadays all of us are fighting against environmental problems: global warming, greenhouse effect, pollution. One of the more considerable issue regarding our planet is the waste crisis.
During these years all over the world, people has began or are going to begin making recycling so it should be a very important task to make it easily available for everyone.
We are from Italy and in our country people usually know where most things have to be stored but sometimes this knowledge is not easily available.
There are some factors that cause this issue. Recycling in Italy change from region to region. Sometimes even between two cities.
##The Idea
These days it’s not so easy to find something usefull that would be worth to spent time on. What we thought about was that a cool idea could be to make something that helps people to trash their garbage in the correct way. 

###Where we started from
To get an idea of ​​how waste collection is in Barcelona we took some data from “http://ajuntament.barcelona.cat” where we found a form to search about wastes, to know where to bring them to get rid of them.
That solution was simple and reliable and inspired us to aspire about making something smarter and more usable.

##Google Assistant
After a long think about our best possibilities to implement our idea we have opted for a Google Assistant extender module.
It would be very reliable and easy to create, thanks to Google Awesome API and it would have been able to run our project on tons of different device. Android Phones, Smartwatches, Smart TV, iOS Devices and many others.

## Google DialogFlow and Amazon AWS (Lambda Function)
When Google DialogFlow recieve a demand for indication about waste disposal he search entities in the sentence inside a database containing words about recycling world and their synonyms. After that it will be done a call to a Lambda Function (Serverless) on Amazon AWS.
The Serverless Lambda Function will then match received data with the garbage can data. After the search it will respond to Google Assistant with the related garbage can or with the Google Maps indication to nearest recycling centre. 

##Serverless
To work in a better way with the Lambda Function of Amazon AWS, we have used a framework called Serverless. Thanks to this application we are allowed to create in a easy way a the function to execute on the AWS servers. The advantages of using this technologies are: saving money and the chance to have all the power we want for a very short time, only for executing the lambda function.


##Machine Learning
One of the thing we have tried during the competition was to introduce the Machine Learning to provide “prediction” about the box in which the garbage would be gone, depending on lots of rubbish attributes, for example material, weight, cleanliness, origin and so on. 
Anyway we decided that it could be a reasonable and winning method only after a long time and much more in-depth studies.
##Possible Future Developments
Our idea boasts all the awesome Google Assistant future prospective, with the possibility to be present on every Mobile Device, IoT Device and more generally “Smart Device” in the world. 
This idea could be evolved and transformed in something even more useful for our and our planet, for example introducing a kind of gamification and explaining children the important of the environment and the recycling


