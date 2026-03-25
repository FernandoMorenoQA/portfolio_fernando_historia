const { defineConfig } = require("cypress");

module.exports = defineConfig({
  allowCypressEnv: false,

  e2e: {
    experimentalStudio: true, // Adicione esta linha aqui
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});


