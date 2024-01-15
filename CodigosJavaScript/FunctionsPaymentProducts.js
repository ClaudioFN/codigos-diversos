console.log('Testing functions using JS.');
// paymentConditions = ['CREDIT', 'DEBIT', 'MONEY', 'PIX']

const productOriginalPrice = 100.0;

const selectedPaymentCondition = 'DEBIT';
const timesParcel = 2;
let valueToPay = 0.0;
const feesCredit = 1.10;
const discountValueDebit = 0.1;
const discountValueMP = 0.15;

function moneyMask(value){
    value = value.replace('.', '').replace(',', '').replace(/\D/g, '')
  
    const options = { minimumFractionDigits: 2 }
    const result = new Intl.NumberFormat('en-IN', options).format( // pt-BR
      parseFloat(value) / 100
    )
  
    return '$ ' + result;
  }

function applyDiscount(prodOrigPrice, discountValue) {
    return prodOrigPrice - (prodOrigPrice * discountValue);
}

function parcelValue(prodOrigPrice, tParcel, fees) {
    let finalValue = 0.0;
    if (tParcel <= 2) {
        finalValue = prodOrigPrice / tParcel;
    } else {
        finalValue = (prodOrigPrice * fees) / tParcel;
    }

    return finalValue;
}

if (selectedPaymentCondition === 'CREDIT'){
    valueToPay = parcelValue(productOriginalPrice, timesParcel, feesCredit);
} else if (selectedPaymentCondition === 'DEBIT') {
    valueToPay = applyDiscount(productOriginalPrice, discountValueDebit);
} else if(selectedPaymentCondition === 'MONEY' || selectedPaymentCondition === 'PIX') {
    valueToPay = applyDiscount(productOriginalPrice, discountValueMP);
}

console.log('Value to pay', moneyMask(valueToPay.toFixed(2)));