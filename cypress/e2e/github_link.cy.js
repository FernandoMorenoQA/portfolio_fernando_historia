describe('Validar Link do Repositório', () => {
    it('Deve verificar se o botão do GitHub aponta para o repositório correto', () => {
        // 1. Visita a página local ou de produção
        // Remova o _ERRO_DE_TESTE
        cy.get('.btn-git').should('have.attr', 'href', 'https://github.com/FernandoMorenoQA/portfolio_fernando_historia')
        // 2. Localiza o botão pelo texto (ajuste se o texto for diferente)
        // Usamos o seletor 'a' porque o botão é um link estilizado no seu CSS
        cy.contains('Ver Código Fonte (Git)')
            .should('be.visible')
            .and('have.attr', 'href')
            .and('include', 'github.com/FernandoMorenoQA/portfolio_fernando_historia')

        // 3. Opcional: Validar se ele abre em uma nova aba (boa prática de UX)
        cy.contains('Ver Código Fonte (Git)')
            .should('have.attr', 'target', '_blank')
    })
})