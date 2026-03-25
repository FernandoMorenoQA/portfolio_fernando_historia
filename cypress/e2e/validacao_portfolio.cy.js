describe('Validação do Link do GitHub', () => {
  it('Deve clicar no botão e validar a URL de destino', () => {
    cy.visit('https://portfoliofernandohistoria-wacedwvmyw6rub566bvfaa.streamlit.app/');

    cy.contains('Ver Código Fonte (Git)')
      .should('be.visible')
      // Mudei o final para 'ERRO_DE_TESTE' para forçar a falha
      .and('have.attr', 'href', 'https://github.com/FernandoMorenoQA/portfolio_fernando_historia_ERRO_DE_TESTE')
      .and('have.attr', 'target', '_blank');
  });
});