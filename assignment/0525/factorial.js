const fact = (number) => {
  if (number === 0) return 1;

  if (number === 1 || number === -1) {
    return number;
  }

  let nextNum = 0;
  if (number > 0) {
    nextNum = number - 1;
  } else {
    nextNum = number + 1;
  }

  return number * fact(nextNum);
}

const userInput = document.getElementById('numberInput');
userInput.addEventListener('change', (e) => {
  const value = parseInt(e.target.value);

  if (!value) {
    document.getElementById('output').innerText = '';
  }

  document.getElementById('output').innerText = `${value}! = ${fact(value)}`;
})