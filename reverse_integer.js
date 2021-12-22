var reverse = function(x) {
    if(x >= 2**31 || x<=(-2)**31) return 0
    
    let y = parseFloat(
        x.toString()
        .split("")
        .reverse()
        .join("")
    )*Math.sign(x)
    console.log(y)

    if(y >= 2**31 || y<=(-2)**31) return 0

    return y
};


reverse(-90)