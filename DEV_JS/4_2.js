var va = {
    center : {x:1.0, y:2.0},
    redius : 2.5,
    area : function(){
        return Math.PI * this.redius * this.redius;
    }
}

console.log(va.area());


// 희한하게 함수를 실시간 추가할 수 있어
va.translate = function (){
    return this.center.x * 100;
}

console.log(va.translate());