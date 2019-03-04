# bitcoin-wallet-classification
Automatic wallet labelling method

Send a wallet address or a batch of addresses and the method returns the type of the requested wallet(s) in json format. For example: Cold storage, Main exchange etc.

```
Free API: https://bitcoin-wallet-classifier.herokuapp.com/

Usage:
Input:
https://bitcoin-wallet-classifier.herokuapp.com/392LK4ZQD3gixWg5xJRTv1a24N3YDgCbwP,36ZzG7KZ91D8TZhvzxzw79vv8evzP85Fob

Output:
{"Address":{"0":"392LK4ZQD3gixWg5xJRTv1a24N3YDgCbwP","1":"36ZzG7KZ91D8TZhvzxzw79vv8evzP85Fob"},"Label":{"0":"Main Exhange","1":"intermediate address"}}
```
