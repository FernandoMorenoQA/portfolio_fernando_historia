describe('Smoke Test Simples', () => {
  it('Deve carregar a página inicial', () => {
    // Visita a URL e aguarda a resposta do servidor
    cy.visit('https://portfoliofernandohistoria-wacedwvmyw6rub566bvfaa.streamlit.app/')

    // Apenas verifica se o elemento "body" (corpo do site) existe e está visível
    // O timeout de 15 segundos ajuda caso o Streamlit demore a "acordar"
    cy.get('body', { timeout: 15000 }).should('be.visible')
  })
})
