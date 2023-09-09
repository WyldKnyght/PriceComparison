const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');

const productRoutes = require('./routes/product-routes');
const pageRoutes = require('./routes/page-routes');

const app = express();

app.use(cors());
app.use(
   express.urlencoded({
      limit: '50mb',
      extended: 'true',
      parameterLimit: 50000,
   })
);
app.use(express.json({ limit: '50mb' }));

app.use(express.static(path.join(__dirname, 'src')));

app.use('/', pageRoutes);
app.use('/product', productRoutes);

app.use((err, req, res, next) => {
   console.log(err);
   res.status(err.status || 500).json({
      message: err.message,
      data: err.data,
   });
});

mongoose
   .connect(
      '',
      {
         useNewUrlParser: true,
         useUnifiedTopology: true,
      }
   )
   .then((result) => {
      app.listen(5050).setTimeout(500000);
      console.log('app started ' + 5050);
      app.emit('app_started');
   })
   .catch((err) => {
      throw err;
   });

module.exports = app;
