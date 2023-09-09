const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const productSchema = new Schema({
   _id: mongoose.SchemaTypes.ObjectId,
   PutRequest: {
      Item: {
         productName: {
            S: String,
         },
         price: {
            S: String,
         },
         productLink: {
            S: String,
         },
      },
   },
});

module.exports = mongoose.model('Product', productSchema);
