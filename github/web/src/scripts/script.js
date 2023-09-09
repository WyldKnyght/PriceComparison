const buttonClick = (document.getElementById('searchButton').onclick =
   searchHandler);
const input = document.getElementById('searchInput');
const productList = document.getElementById('productList');
const infoText = document.getElementById('infoText');
infoText.style.visibility = 'hidden';
async function searchHandler() {
   infoText.style.visibility = 'visible';
   if (!input.value) {
      infoText.innerText = 'Please Enter a Value';
   } else {
      infoText.innerText = 'Searching';

      while (productList.firstChild) {
         productList.firstChild.remove();
      }
      const rawResponse = await fetch('product/get-products', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },

         body: JSON.stringify({
            productName: input.value,
         }),
      });
      if (rawResponse.status == 200) {
         const response = await rawResponse.json();
         console.log(`response`, response);
         infoText.innerText = 'Listing';

         response.mappedProducts.forEach((element) => {
            let domain = new URL(element.link);
            domain = domain.hostname.replace('www.', '');
            let splitArr = domain.split('.');
            let domainName =
               splitArr[0].charAt(0).toUpperCase() + splitArr[0].slice(1);

            let row = document.createElement('tr');
            let productName = document.createElement('td');
            let productSeller = document.createElement('td');
            let productPrice = document.createElement('td');
            let productLink = document.createElement('td');
            let link = document.createElement('a');
            link.href = element.link;
            link.target = '_blank';
            link.innerText = element.link;
            productLink.appendChild(link);
            productSeller.innerHTML = domainName;
            productPrice.innerHTML = element.price;
            productName.innerHTML = element.name;
            // productLink.innerHTML = element.link;
            row.appendChild(productName);
            row.appendChild(productSeller);
            row.appendChild(productPrice);
            row.appendChild(productLink);
            productList.append(row);
         });
         infoText.style.visibility = 'hidden';
      } else {
         infoText.innerText = 'Nothing Found';
      }
   }
}
