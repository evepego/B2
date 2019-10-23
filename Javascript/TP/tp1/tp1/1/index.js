const datasets = require("./datasets.json")
const reset = '\x1b[0m'
const bright = '\x1b[1m'

exports = module.exports = {
  name: "Marathon",
  datasets,
  algo: function (input) {
    // YOUR CODE BETWEEN HERE
    const input = [];
    position = input[0];
    count = 0;
    price = 0;
    km = 0;
    km_max = 42;

    // Algo classement
    while km < km_max {
      const tab = input.push('');
    }


    // Algo des paris
    if tab[0] <= 100 {
      price = 1000;
    }
    else if tab[i+1]> 10000 {
      price = 0;
    }
    else {
      price = 100;
    }

    // AND HERE
  },
  verify: function (dataset, output) {
    if (dataset.output !== output) {
      throw new Error(`${bright}Got ${output} but expected ${dataset.output}${reset}`)
    } else {
      return true
    }
  }
}