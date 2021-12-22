/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
*/
console.log("Start")
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
    let array = []
    for(let i =0;i<h;i++){
        for(let j=0;j<w;j++){
            array.push([i,j])
        }
    }
    console.log(array)
};

maxArea(5,4,1,3)
