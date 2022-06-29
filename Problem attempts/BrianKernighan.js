const count_1s = (num) => {
    let count = 0;
    while (num > 0) {
        num &= num - 1;
        count++;
    }
    return count;
};

let ans = count_1s(32767);
console.log(ans)