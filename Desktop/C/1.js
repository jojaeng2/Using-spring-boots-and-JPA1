const increase = function (num) {
    return ++num;
};
const decrease = function (num) {
    return --num;
};

const predicates = { increase, decrease};

function makeCounter(predicate) {
    let num = 0;
    console.log("make", num);
    return function () {
        console.log("function");
        num = predicate(num);
        return num;
    };
}

const increaser = makeCounter(predicates.increase);
console.log(increaser());

const increaserr = makeCounter(predicates.increase);
console.log(increaserr());

console.log("@@@@@@@@@@");


function what() {
    let number = 0;
    
    number = number + 1;

    return number;
}
console.log(what());
console.log(what());