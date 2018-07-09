var kafka = require("../node_modules/kafka-node");
var HighLevelProducer = kafka.HighLevelProducer;
const client = new kafka.KafkaClient({ kafkaHost: "localhost:9092" });
var argv = require("optimist").argv;
var topic = argv.topic || "raw";
var count = 10;
var rets = 0;
var producer = new HighLevelProducer(client);
var feed = {}; // data with time stamp
var timestamp = require("time-stamp");
var data={}
timestamp("YYYYMMDDTHHmmssZ");

var axios = require("axios");

module.exports = function(context, req) {
  context.log("JavaScript HTTP trigger function processed a request.");
  if (req.body) {
    data.LightIntensity = req.body.LightIntensity;
    data.SoundIntensity= req.body.SoundIntensity;    
    data.Humidity= req.body.Humidity;    
    data.Temperature = req.body.Temperature;
    data.Wet = req.body.Wet;
    data.timestamp = timestamp("YYYYMMDDTHHmmssZ");

        var message = JSON.stringify(data);
        producer.send([{ topic: topic, messages: [message] }], function(
          err,
          data
        ) {
          if (err) console.log(err);
          else console.log("send %d messages", ++rets);
          context.res={
              status:200,
              body:"injested"
          }
          context.done();
        })
  } else {
    context.res = {
      status: 400,
      body: "Error Parsing body"
    };
    context.done();
  }
};
