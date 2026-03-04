const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/resorts', (req, res) => {
  res.sendFile(path.join(__dirname, 'resorts.json'));
});

app.listen(PORT, () => {
  console.log(`Club Med EMEA Quiz ➜  http://localhost:${PORT}`);
});
