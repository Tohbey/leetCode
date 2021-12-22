
//Solution 1
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let largest = nums[0] + nums[nums.length  - 1];

    let smallest = nums[0] + nums[1];

    if(largest === target){
        return [0, nums.length -1]
    }else if(smallest === target){
        return [0, 1]
    }
    console.log(smallest, largest)

    if(smallest != target){
        for(let i = 0; i < nums.length; i++){
           for(let j = i + 1; j < nums.length; j++){
              if (nums[i] + nums[j] === target) {
                indexes.push(i);
                indexes.push(j);
              }
           }
        }
        return indexes;        
    }
};


//solution 2

let nums = [-3,4,3,90]; 
let target = 0;

console.log(twoSum(nums, target))
