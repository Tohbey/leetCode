/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let substring = [];
    for(let i=0;i<s.length;i++){
        if(i === 0){
            substring.push(s[0])
            findCharInArray(substring, s[0], s.length-1, i)
        }
        findCharInArray(substring, s[i], s.length-1, i)
    }
};

var findCharInArray = function(a, letter, last, current){
    console.log("Array", a)
    console.log("Letter", letter)
    console.log("last", last)
    console.log("current", current)
    for(let j=0;j<a.length;j++){
        if(last === current){
            console.log("final part")
        }else{
            if(a[j] === letter){
                a.length = []
                console.log("duplicate letter")
            }else{
                console.log("new letter")
            }
        }
    }
}

let s = "pwwkew";

lengthOfLongestSubstring(s)