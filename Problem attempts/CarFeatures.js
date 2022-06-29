const count_1s = (num) => {
    let count = 0;
    while (num > 0) {
        num &= num - 1;
        count++;
    }
    return count;
};

const solution = (cars) => {
    cars = cars.map((car) => parseInt(car, 2));
    let left = new Array(cars.length).fill(0);
    let right = new Array(cars.length).fill(0);

    let current_idx = 0;
    let front_idx = 1;
    let similar_cars = 0;
    let bin_1s = 0;

    // pass right comparing feature differences using XOR
    while (current_idx < cars.length) {
        if (front_idx == cars.length) {
            break;
        }
        let xor = cars[current_idx] ^ cars[front_idx];
        bin_1s = count_1s(xor);
        if (bin_1s == 1 || bin_1s == 0) {
            similar_cars++;
        }
        front_idx++;
        if (front_idx == cars.length) {
            right[current_idx] = similar_cars;
            current_idx++;
            front_idx = current_idx + 1;
            similar_cars = 0;
        }
    }

    // Pass left comparing feature differences using XOR
    current_idx = cars.length - 1;
    let prev_idx = cars.length - 2;

    while (current_idx > 0) {
        if (prev_idx == -1) {
            break;
        }
        let xor = cars[current_idx] ^ cars[prev_idx];
        if (count_1s(xor) == 1 || count_1s(xor) == 0) {
            similar_cars++;
        }
        prev_idx--;

        if (prev_idx == -1) {
            left[current_idx] = similar_cars;
            current_idx--;
            prev_idx = current_idx - 1;
            similar_cars = 0;
        }
    }

    let result = right.map((num, idx) => {
        return num + left[idx];
    })

    return result;
};

cars = ["100", "110", "010", "011", "100"];

console.log(solution(cars));
