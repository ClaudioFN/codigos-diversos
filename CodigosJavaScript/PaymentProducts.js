/*
Created Date: 14/01/2024
Last Update: 14/12/2024
Description: One of the main imports
Observation: Import to test the price and show how the final value
*/

console.log('Testing calculation price using JS.')
// paymentConditions = ['CREDIT', 'DEBIT', 'MONEY', 'PIX']

const productOriginalPrice = 100.0;


const selectedPaymentCondition = 'DEBIT';
const timesParcel = 2;
let valueToPay = 0.0;

if (selectedPaymentCondition === 'CREDIT'){
    if (timesParcel <= 2){
        valueToPay = productOriginalPrice / timesParcel;
    } else {
        valueToPay = (productOriginalPrice * 1.10) / timesParcel;
    }
} else if (selectedPaymentCondition === 'DEBIT') {
    valueToPay = productOriginalPrice - (productOriginalPrice * 0.1);
} else if(selectedPaymentCondition === 'MONEY' || selectedPaymentCondition === 'PIX') {
    valueToPay = productOriginalPrice - (productOriginalPrice * 0.15);
}

console.log('Value to pay $', valueToPay);


