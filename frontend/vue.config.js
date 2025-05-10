const path = require('path');

module.exports = {
  css: {
    loaderOptions: {
      sass: {
        // Configure `node_modules` resolution for imports
        sassOptions: {
          includePaths: [path.resolve(__dirname, 'node_modules')],
        },
      },
    },
  },
};
