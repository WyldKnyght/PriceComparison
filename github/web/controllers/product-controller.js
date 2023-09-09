const Product = require('../models/mongoose/product');

exports.getProducts = async (req, res, next) => {
   const product = req.body.productName;
   console.log(req);
   Product.find({
      'PutRequest.Item.productName.S': { $regex: product, $options: 'i' },
   })
      .sort({ 'PutRequest.Item.price.S': 1 })
      .collation({ locale: 'en_US', numericOrdering: true })
      .then((products) => {
         const mappedProducts = products.map((item) => {
            return {
               name: item.PutRequest.Item.productName.S,
               price: item.PutRequest.Item.price.S,
               link: item.PutRequest.Item.productLink.S,
            };
         });
         if (mappedProducts.length > 0) {
            res.status(200).json({
               success: true,
               mappedProducts,
            });
         } else {
            res.status(400).json({
               success: false,
            });
         }
      })
      .catch((err) => res.status(500).json(err));
};
