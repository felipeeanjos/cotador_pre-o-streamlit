import streamlit as st

st.title('Bem vindo ao seu cotador de preços')

custo = st.number_input('Custo do Produto')
p_plataforma = st.number_input('Porcentagem da plataforma de venda')
p_imposto = st.number_input('Imposto devido')
venda = st.number_input('Valor de Venda do Produto')

porcentagem = (p_plataforma + p_imposto)/100
st.markdown('Porcentagem de desconto é:  ' +str(porcentagem*100)+'%')

desconto = venda*porcentagem
lucro = venda-custo-desconto
st.markdown('Lucro em R$ '+str(lucro))

lucro_p = lucro/venda
st.markdown('Lucro em % : '+str(lucro_p*100)+'%')

quantidade = st.number_input('número de produtos vendidos')
lucro_quantidade = lucro*quantidade
st.markdown('Vendendo '+str(quantidade)+' produtos o lucro será de R$'+str(lucro_quantidade))
