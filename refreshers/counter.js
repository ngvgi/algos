// counter that refreshes time difference to input date

const updateTimeDiff = (targetTime) => {
  targetTime = new Date(targetTime);
  const timeDiff = targetTime - Date.now();
  return timeDiff;
};

console.log(updateTimeDiff("2023-08-04T00:00.00.000-07.00"));
