var card = {suit:"하트", rank:"A"};
console.log(card.suit);

// 객체리터럴 추가
card.value = 14;
console.log(card);

// 리터털 삭제
delete card.rank;
console.log(card);

// 객체리터럴에 프로퍼티가 있는지 검사
console.log("하트" in card);
console.log("suit" in card);

// 모든 객체는 참조이다.
var va1={"a":1, "b":2};
console.log(va1);

var va2=va1;
va2.a = 11;

console.log(va1);