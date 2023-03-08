var fs = require('fs')

var fileContent = {
    "name": "Nguggzz",
    "location": "Kiambu"
};

fs.writeFile('data.json', fileContent, err=> console.log(err));