let grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

let neighbours = [];
let row = grid.length;
let column = grid[0].length;

var maxAreaOfIsland = function(grid) {
    let maxarea = 0;
    let row = grid.length;
    let counter = 0;
    for(let i=0;i<row;i++){
        let column = grid[i].length;
        for(let j=0;j<column;j++){
            let entity = grid[i][j]
            if(entity === 1){
                let ans = getNeighbours(grid, i, j);
                maxarea = Math.max(ans, maxarea);
                counter++;
            }
        }
    }
    console.log(maxarea)
    console.log(counter)
};


var getNeighbours = function(grid, i, j){
    
    if(i >= row || j >= column || i < 0 || j < 0 || grid[i][j] != 1){
        return 0;
    }

    grid[i][j] = 2
    
    return 1 + getNeighbours(grid, i, j-1) + getNeighbours(grid, i, j+1) + getNeighbours(grid, i-1, j) +  getNeighbours(grid, i+1, j);
}

maxAreaOfIsland(grid);