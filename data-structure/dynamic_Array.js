let len = 0;
let capacity = 0;
let arr = new Array(capacity);

var array = (capacity) => {
    if (capacity < 0) return "Illegal Capacity " + capacity;
    capacity = capacity;

    arr = new Array(capacity);
}

var size = () => {
    return len;
}

var isEmpty = () => {
    if (size() === 0) {
        return true
    } else {
        false
    }
}

var get = (index) => {
    return arr[index];
}

var set = (index, value) => {
    arr[index] = value;
}

var clear = () => {
    for (let i = 0; i < capacity; i++) {
        arr[i] = null;
    }
    len = 0
}

var add = (value) => {
    if (len + 1 >= capacity) {
        if (capacity == 0) capacity = 1;
        else capacity *= 2 //double the lenght

        new_arr = new Array(capacity);
        for (let i = 0; i < len; i++) {
            new_arr[i] = arr[i]
        }
        arr = new_arr
    }

    arr[len++] = value;
}

var removeAt = (rm_index) => {
    if (rm_index >= len && rm_index < 0) return "Out of bound";

    data = arr[rm_index];
    new_arr = new Array(len - 1);
    for (let i = 0, j = 0; i < len; i++, j++) {
        if (i == rm_index) j--;
        else new_arr[j] = arr[i]
    }
    arr = new_arr;
    capacity = --len;
    return data;
}

var remove = (obj) => {
    for (let i = 0; i < len; i++) {
        if (arr[i] === obj) {
            removeAt(i)
            return true;
        }
    }
    return false
}

var indexOf = (obj) => {
    for (let i = 0; i < len; i++) {
        if (arr[i] === obj) {
            return i;
        }
    }
    return -1;
}

var contain = (obj) => {
    return indexOf(obj) != -1;
}