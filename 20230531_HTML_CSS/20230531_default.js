/*var cels = parseFloat(prompt("섭씨 입력 : "));
var forn = cels * (9/5)+32;

document.write("화씨 : "+forn);*/

/*var num1 = 20;
var num2 = 10;
var num3 = "10";
var num4 = 20;
var num5 = 15;

console.log("비교연산자");
console.log(num1 > num2,num1, ">" ,num2);
console.log(num1 >= num2,num1, ">=" ,num2);
console.log(num1 < num2,num1, "<" ,num2);
console.log(num1 <= num2,num1, "<=" ,num2);

console.log("같은지 여부 확인")
console.log(num1 == num4,num1, "==" ,num4);
console.log(num1 != num4,num1, "!=" ,num4);

console.log("===")
console.log(num1 === num3,num1," === ",num3);
console.log(num2 === num3,num2," === ",num3);
console.log(num1 == num3,num1," == ",num3);

console.log("논리연산자")
console.log("num1 > num2 && num1 < num5 : ",num1 > num2 && num1 < num5);
console.log("num1 > num2 || num1 < num5 : ",num1 > num2 || num1 < num5);
console.log("num1 > num2 && num1 < num5 : ",num1 > num2 && !(num1 < num5));
*/

/*var num1 = parseInt(prompt("첫번째 숫자 입력 : "));
var num2 = parseInt(prompt("두번째 숫자 입력 : "));

console.log("=========================");
if (num1>num2){
    console.log("큰 수는 num1 : " + num1);
}
if(num1<num2){
    console.log("큰 수는 num2 : " + num2);
}
if(num1 == num2){
    console.log("같은 수");
}
*//*코드가 간결해짐*//*
console.log("=========================");
if(num1>num2){
    console.log("큰 수 num1 : "+ num1);
}else if(num1 < num2){
    console.log("큰 수 num2 : "+ num2);
}else{
    console.log("같은 수");
}
console.log("=========================");*/

/*모음 자음 구별하기*/
/*console.log("=========================");
var letter = prompt("Enter a letter : ");
letter = letter.toLowerCase();

if(letter == "a" || letter == "e" ||
    letter == "i" || letter == "o"||
    letter =="v"){
    console.log("Vowel");
}else{
    console.log("Consonant");
}*/
/*switch문 */
/*
console.log("=========================");
var digit = parseInt(prompt("Enter is number : "));
switch (digit){
    case 0 :
        document.write("Zero");
        break;
    case 1 :
        document.write("One");
        break;
    case 2 :
        document.write("Two");
        break;
    case 3 :
        document.write("Three");
        break;
    case 4 :
        document.write("Four");
        break;
    case 5 :
        document.write("Five");
        break;
    case 6 :
        document.write("Six");
        break;
    case 7 :
        document.write("Seven");
        break;
    case 8 :
        document.write("Eight");
        break;
    case 9 :
        document.write("Nine");
        break;
    default:
        document.write("Not a digit");

}
console.log("=========================");
*/
var i = 1

do{
    document.write("멋쟁이사자i :  "+ i++ +"<br>/")
}while(i<=10)
document.write("=========================<br>")
var j = 1

while(j<=10){
    document.write("멋쟁이사자j :  "+ j++ +"<br>/")
}
document.write("=========================<br>")
