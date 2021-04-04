const solution = (A) => {
    let countOccurrences = (arr, val) => {
        return arr.reduce((a, v) =>
            (v === val ? a + 1 : a), 0);
    }

    let pairs = 0;
    let odds = [];
    let evens = [];

    for (let i = 1; i < A[0]; i += 2) {
        if (i % 2 == 1 && !A.includes(i)) {
            odds.push(i);
        } else {
            odds.push("Booked");
        }
    }

    for (let i = 2; i <= A[0]; i += 2) {
        if (i % 2 == 0 && !A.includes(i)) {
            evens.push(i);
        } else {
            evens.push("Booked");
        }
    }

    evens[evens.length - 1] = countOccurrences(A, A[0]) > 1 ? "Booked" : A[0];

    i = 0;
    while (i < odds.length) {
        if (odds[i] != "Booked" && evens[i] != "Booked") {
            pairs++;
        }
        if (i < odds.length - 1) {
            if (odds[i] != "Booked" && odds[i + 1] != "Booked") {
                pairs++;
            }
            if (evens[i] != "Booked" && evens[i + 1] != "Booked") {
                pairs++;
            }
        }

        i++;
    }

    return pairs;
};

// const A = [16, 3, 4, 8, 10, 12]
const A = [12, 2, 6, 7, 11]
// const A = [12, 2, 6, 7, 12];
const ans = solution(A);
console.log(ans);