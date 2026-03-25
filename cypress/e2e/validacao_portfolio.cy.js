describe('Smoke Test Simples', () => {
  it('Deve validar a formação acadêmica dentro do iframe', () => {
    cy.visit('https://portfoliofernandohistoria-wacedwvmyw6rub566bvfaa.streamlit.app/');

    // 1. Espera o iframe carregar e acessa o corpo (body) dele
    cy.get('iframe', { timeout: 20000 })
      .its('0.contentDocument.body').should('not.be.empty')
      .then(cy.wrap) // Agora o Cypress está "dentro" do iframe
      .as('iframeBody');

    // 2. Agora buscamos o texto dentro do corpo do iframe
    cy.get('@iframeBody')
      .contains('Mestre em TI', { timeout: 15000 })
      .should('be.visible');

    // 3. Validando o próximo badge para garantir a consistência
    cy.get('@iframeBody')
      .contains('MBA')
      .should('be.visible');
  });

});