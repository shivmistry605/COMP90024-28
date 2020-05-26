//curl -X GET http://admin:admin1234@172.26.132.189:5984/instance3/_all_docs\?include_docs\=true > /Users/meghna_panda/Desktop/instance3.json;

var fs = require('fs');
fs.readFile('./zh_instance1_tweets.json', 'utf8', (err, jsonString) => {
    if (err) {
        console.log("Error reading file from disk:", err)
        return
    }
    try {
        
        const db = JSON.parse(jsonString)
        var count = Object.keys(db.rows).length;
        console.log("size " , count);
        //console.log(db.rows[0].doc.place);
       var data_lang = {};
        for (var i = 0; i < count; i++) {
            if ((db.rows[i].coordinates != null) && (db.rows[i].lang == 'zh') &&
            ((db.rows[i].place.name=="Sydney"))) 
            {
                var json_data = { 
                        type: "Feature",
                        geometry: {
                            type: "Point",
                            coordinates: db.rows[i].coordinates.coordinates
                        },
                    properties: {
                        id: String(db.rows[i].id),
                        city: db.rows[i].place.name,
                        user: db.rows[i].user.screen_name,
                        lang:db.rows[i].lang
                        },
    
            }
                
            data_lang =   JSON.stringify(json_data) + ',';
            //console.log(data_lang.length);
           fs.appendFileSync('zh_instance1_tweets_syd.geojson', data_lang);

        }
        
        //console.log(i);
    }}
            
    catch (err) {
    console.log('Error parsing JSON string:', err)
}
}) 



