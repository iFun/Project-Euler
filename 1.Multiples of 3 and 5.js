//If we list all the natural numbers below 10 that are multiples of 3 or 5, 
//we get 3, 5, 6 and 9. The sum of these multiples is 23.

//Find the sum of all the multiples of 3 or 5 below 1000.

//stupid method
var result = {};
var sum = 0;


var count = 1;

var tmp;

while (3 * count < 1000) {
    result[3*count] = 3*count;
    count++;
}
count = 1;
while (5 * count < 1000) {
    result[5*count] = 5*count;
    count++;
}
for(key in result){
    sum += parseInt(key);
}


console.log(sum);

//fast method
//a,b=0,0
// for a in range (1,1000):
//     if a%5==0 or a%3==0 :
//         b=b+a    
// print (b,a)
