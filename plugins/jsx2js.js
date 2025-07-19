const babel = require('@babel/standalone');
const fs = require('fs');

const input = fs.readFileSync(process.argv[2], 'utf8');
const output = babel.transform(input, {
  presets: ['react'],
}).code;
fs.writeFileSync(process.argv[3], output);
