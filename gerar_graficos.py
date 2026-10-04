import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dados da tabela
dados = {
    'Projeto/Feature': [
        'Projeto Base',
        'Carrinho Gratuito',
        'Checkout Gratuito',
        'Login Gratuito Completo',
        'Carrinho Pago',
        'Login Pago',
        'Checkout Único'
    ],
    'IA': ['Base', 'Gratuita', 'Gratuita', 'Gratuita', 'Paga', 'Paga', 'Paga'],
    'Total Code Smells': [43, 50, 63, 75, 43, 70, 75],
    'Code Smells Individuais': [43, 7, 20, 32, 0, 27, 32],
    'Linhas de Código': [3168, 667, 916, 1622, 916, 4353, 3876],
    'Densidade Code Smells': [0.014, 0.010, 0.022, 0.020, 0.000, 0.006, 0.008]
}

df = pd.DataFrame(dados)

# Separar dados por tipo de IA
df_gratuita = df[df['IA'] == 'Gratuita']
df_paga = df[df['IA'] == 'Paga']

# Criar figura com subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Comparação: IA Gratuita vs IA Paga\nAnálise de Code Smells', fontsize=16, fontweight='bold')

# Gráfico 1: Total de Code Smells
ax1 = axes[0, 0]
x = np.arange(len(df))
width = 0.35
cores = ['#FF6B6B' if ia == 'Gratuita' else '#4ECDC4' for ia in df['IA']]
ax1.bar(x, df['Total Code Smells'], color=cores, alpha=0.8)
ax1.set_xlabel('Projeto/Feature', fontweight='bold')
ax1.set_ylabel('Total de Code Smells', fontweight='bold')
ax1.set_title('Total de Code Smells por Projeto')
ax1.set_xticks(x)
ax1.set_xticklabels(df['Projeto/Feature'], rotation=45, ha='right')
ax1.grid(axis='y', alpha=0.3)
ax1.legend(['Gratuita', 'Paga'], loc='upper left')

# Gráfico 2: Densidade de Code Smells
ax2 = axes[0, 1]
ax2.bar(x, df['Densidade Code Smells'], color=cores, alpha=0.8)
ax2.set_xlabel('Projeto/Feature', fontweight='bold')
ax2.set_ylabel('Densidade de Code Smells', fontweight='bold')
ax2.set_title('Densidade de Code Smells (Smells/Linhas de Código)')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Projeto/Feature'], rotation=45, ha='right')
ax2.grid(axis='y', alpha=0.3)

# Gráfico 3: Comparação resumida (Gratuita vs Paga)
ax3 = axes[1, 0]
categorias = ['Total\nCode Smells', 'Code Smells\nIndividuais', 'Densidade\nCode Smells']
media_gratuita = [
    df_gratuita['Total Code Smells'].mean(),
    df_gratuita['Code Smells Individuais'].mean(),
    df_gratuita['Densidade Code Smells'].mean()
]
media_paga = [
    df_paga['Total Code Smells'].mean(),
    df_paga['Code Smells Individuais'].mean(),
    df_paga['Densidade Code Smells'].mean()
]

x_cat = np.arange(len(categorias))
width = 0.35
ax3.bar(x_cat - width/2, media_gratuita, width, label='IA Gratuita', color='#FF6B6B', alpha=0.8)
ax3.bar(x_cat + width/2, media_paga, width, label='IA Paga', color='#4ECDC4', alpha=0.8)
ax3.set_xlabel('Métricas', fontweight='bold')
ax3.set_ylabel('Valor Médio', fontweight='bold')
ax3.set_title('Comparação Média: IA Gratuita vs Paga')
ax3.set_xticks(x_cat)
ax3.set_xticklabels(categorias)
ax3.legend()
ax3.grid(axis='y', alpha=0.3)

# Gráfico 4: Linhas de Código
ax4 = axes[1, 1]
ax4.bar(x, df['Linhas de Código'], color=cores, alpha=0.8)
ax4.set_xlabel('Projeto/Feature', fontweight='bold')
ax4.set_ylabel('Linhas de Código', fontweight='bold')
ax4.set_title('Linhas de Código por Projeto')
ax4.set_xticks(x)
ax4.set_xticklabels(df['Projeto/Feature'], rotation=45, ha='right')
ax4.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('comparacao_ia_gratuita_vs_paga.png', dpi=300, bbox_inches='tight')
print("Gráfico salvo como 'comparacao_ia_gratuita_vs_paga.png'")

# Gerar relatório em texto
print("\n" + "="*60)
print("RELATÓRIO COMPARATIVO: IA GRATUITA vs IA PAGA")
print("="*60)

print("\n📊 RESUMO ESTATÍSTICO:")
print("-" * 60)
print(f"\n IA GRATUITA (3 features):")
print(f"   • Total Code Smells (média): {df_gratuita['Total Code Smells'].mean():.2f}")
print(f"   • Code Smells Individuais (média): {df_gratuita['Code Smells Individuais'].mean():.2f}")
print(f"   • Densidade Code Smells (média): {df_gratuita['Densidade Code Smells'].mean():.4f}")
print(f"   • Linhas de Código (média): {df_gratuita['Linhas de Código'].mean():.2f}")

print(f"\n IA PAGA (3 features):")
print(f"   • Total Code Smells (média): {df_paga['Total Code Smells'].mean():.2f}")
print(f"   • Code Smells Individuais (média): {df_paga['Code Smells Individuais'].mean():.2f}")
print(f"   • Densidade Code Smells (média): {df_paga['Densidade Code Smells'].mean():.4f}")
print(f"   • Linhas de Código (média): {df_paga['Linhas de Código'].mean():.2f}")

print("\n📈 ANÁLISE COMPARATIVA:")
print("-" * 60)

diff_total = ((df_paga['Total Code Smells'].mean() - df_gratuita['Total Code Smells'].mean()) / 
              df_gratuita['Total Code Smells'].mean() * 100)
diff_densidade = ((df_paga['Densidade Code Smells'].mean() - df_gratuita['Densidade Code Smells'].mean()) / 
                  df_gratuita['Densidade Code Smells'].mean() * 100)

print(f"\n   Variação no Total Code Smells: {diff_total:+.2f}%")
print(f"   Variação na Densidade Code Smells: {diff_densidade:+.2f}%")

if diff_densidade < 0:
    print(f"\n   ✅ IA PAGA é MELHOR em qualidade (menos code smells por linha)")
else:
    print(f"\n   ✅ IA GRATUITA é MELHOR em qualidade (menos code smells por linha)")

print("\n" + "="*60)
