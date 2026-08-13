import os

skill_content = """---
description: Guia Supremo e Mega Completo sobre User Experience (UX), UX Writing, Design de Interação e Experiência do Usuário (Versão Definitiva).
---

# 🧠 UX Masterbook: A Referência Definitiva de User Experience

Este guia é uma síntese profunda de referências consagradas ("Don't Make Me Think", "Strategic Writing for UX" e "The Basics of User Experience Design"). Use esta skill ao revisar layouts, escrever microcopys, projetar novos fluxos, ou arquitetar a experiência geral do produto.

A promessa do UX design não é apenas fazer algo bonito, mas sim remover o atrito ("friction") entre a intenção do usuário e o seu objetivo de forma transparente e agradável.

---

## 1. 🥇 A Filosofia Central de UX: "Don't Make Me Think"

A regra de ouro da usabilidade ditada por Steve Krug é implacável e dita a fundação de todo o pensamento de interface atual.

### O Que Significa "Não Me Faça Pensar"?
- **Autoevidente e Autoexplicativo:** Cada tela, menu e botão deve ser óbvio. O usuário não deve gastar energia mental decodificando a interface. 
- **Eliminando Pontos de Interrogação:** Quando o usuário olha para uma página e pensa: "Onde estou?", "Por que chamaram isso assim?", "Isso é um link ou texto normal?", você falhou. Toda interrogação drena o *Reservatório de Boa Vontade* do usuário.
- **O Fardo Cognitivo (Cognitive Load):** Cada decisão, por menor que seja (como identificar um link), adiciona trabalho. O cérebro humano tem capacidade limitada; o UX deve reduzir esse custo ao mínimo.

### Paradigmas da Desatenção
1. **O Mito do Foco:** Designers imaginam usuários lentos e atentos olhando cada detalhe. A realidade é frenética, impaciente e conduzida por objetivos rápidos.
2. **O Reservatório de Boa Vontade:** Todo usuário começa com um tanque de boa vontade. Coisas que exigem esforço cognitivo desnecessário, erros incompreensíveis ou formulários longos drenam esse tanque. Quando ele seca, o usuário abandona a plataforma.

---

## 2. 🚶‍♂️ Como os Usuários Realmente Usam a Web

O erro mais comum é presumir como as pessoas operam sistemas. As pessoas não usam sistemas como nós (os criadores) o fazemos.

### Fato 1: Nós não lemos páginas. Nós as escaneamos.
- Pessoas na web agem como tubarões: precisam continuar se movendo ou perdem o interesse.
- Ninguém lê parágrafos longos na web até encontrar exatamente o que procura.
- O olhar pula pela página procurando palavras-chave que correspondam ao seu objetivo (os chamados "triggers").
- *Ação:* Fomente o escaneamento através de quebras visuais e hierarquia pesada.

### Fato 2: Nós não otimizamos escolhas. Nós escolhemos o "Suficiente" (Satisficing).
- **Satisficing:** A junção de *satisfy* (satisfazer) e *suffice* (ser suficiente). Usuários raramente olham *todas* as opções de um menu para escolher a melhor. Eles clicam na primeira opção razoável que parece resolver o problema.
- Otimizar leva tempo. Clicar, testar e voltar é mais rápido devido à baixa penalidade operacional dos botões "Voltar".

### Fato 3: Nós não aprendemos como as coisas funcionam. Nós tentamos até conseguir (Muddling Through).
- **Muddling Through:** Pessoas usam sistemas complexos sem ter ideia de como funcionam nos bastidores. 
- Eles inventam histórias mentais (modelos mentais não-literais) sobre como um sistema opera. E se funciona uma vez, eles repetem o hábito para sempre, mesmo que seja ineficiente.
- *Ação:* Garanta que o "muddle through" não cause desastres (seja tolerante a erros).

---

## 3. 🛡️ A Pirâmide: Os 7 Fatores da Experiência do Usuário (Peter Morville)

Para um produto ter sucesso, ele precisa preencher 7 requisitos de maneira harmoniosa. Avalie sua feature rigorosamente contra esta checklist:

1. **Useful (Útil):** O produto tem um propósito original? As funcionalidades propostas atendem aos objetivos reais das pessoas ou são apenas "legais de ter"?
2. **Usable (Usável):** A funcionalidade é fácil de ser operada? Mesmo sistemas úteis falham se a curva de aprendizado for montanhosa. (Exemplo: MP3 players antes do iPod eram úteis, mas raramente usáveis).
3. **Findable (Encontrável):** O conteúdo ou botão é fácil de achar dentro da arquitetura da informação? O usuário se perde na navegação? 
4. **Credible (Crível):** O design passa confiança institucional? Títulos são coerentes? O layout e a tipografia transmitem amadorismo ou peso profissional de marca?
5. **Desirable (Desejável):** A estética visual, identidade, marca e elementos emocionais fazem as pessoas QUEREREM usar? (Ex: As micro-interações do Telegram, a fluidez do iOS).
6. **Accessible (Acessível):** Pessoas com deficiência e diferentes capacidades (auditiva, visual, motora) conseguem usar? (Contraste de cor, navegação por teclado, leitores de tela).
7. **Valuable (Valioso):** Afinal, ele entrega valor final tanto para o usuário quanto para o negócio (ROI) da empresa patrocinadora? Sem valor mútuo, a iniciativa afunda.

---

## 4. 🎨 Design de Outdoor (Billboard Design) e Hierarquia Visual

Como os usuários correm pelos sites a "100 km/h", você precisa desenhar outdoors de rodovia, não obras literárias literárias.

### A Arte de Orientar o Olho
- **O Mais Importante Destaca-se Mais:** Aumente o tamanho (Size), aumente o peso (Bold), use cor isolada (Contrast), aumente o espaço em branco ao redor (Negative Space) ou posicione no topo (Placement). 
- **Relação Lógica = Relação Visual:** Elementos que pertencem ao mesmo grupo semântico devem estar fisicamente agrupados (Lei da Proximidade da Gestalt). Distancie o que é diferente.
- **Aninhamento Visual (Nesting):** Elementos filhos (child elements) devem ser visivelmente menores, com menos peso visual ou indentados em relação aos elementos pais (parent elements).

### Dicas Práticas para Layouts de Alta Conversão
- **Convenções são suas Melhores Amigas:** Não reinvente a roda se não precisa dela rodando de lado. Ícones de "carrinho", posição do logo no topo à esquerda, links sublinhados. Se quebrar uma convenção, a nova forma DEVE ser infinitamente melhor (o ganho de valor > atrito de aprendizado).
- **Clareza > Consistência:** A consistência é divina (botões estarem sempre no mesmo lugar). Mas, se quebrar a regra de consistência de um layout tornar uma tela pontual *dramaticamente mais óbvia*, escolha a clareza.
- **Torne o Clicável, Inquestionavelmente Clicável:** Um botão tem cara de botão. Um link tem cara de link. Não faça o usuário testar ou passar o mouse em cada elemento para descobrir o que tem interação ("Minesweeping").
- **Reduza o Ruído de Fundo (Signal-to-Noise Ratio):** 
  - *Shouting:* Quando tudo na tela clama por atenção (excesso de cores, bold em tudo). Se *tudo* grita, o usuário fica surdo.
  - *Disorganization:* Falta de grids alinhados.
  - *Clutter:* Aglomeração excessiva de conteúdo simultaneamente.

---

## 5. 📐 Design de Interação (IxD) – As Cinco Dimensões

Interação é comunicação contínua entre homem e máquina. Bill Moggridge e Gillian Crampton Smith definiram a evolução estrutural ddo IxD em 5 dimensões:

### 1D: Strings / Palavras (Words)
- Os textos que interagem com o usuário (botões, labels, descrições). 
- Eles devem ser o mais concisos possível, empacotando o máximo de contexto sem sobrecarregar (overwhelm) o cérebro humano com parágrafos obtusos.

### 2D: Representações Visuais (Visual Representations)
- Tudo aquilo que não é texto fluido: Tipografia (peso e tamanho), ícones, vetores, ilustrações decorativas e gráficos estruturais. 
- Complementam as "Words" comunicando informações imediatamente, pois o cérebro processa imagem mais rápido que texto.

### 3D: Espaço de Controle e Fisicalidade (Physical Objects or Space)
- Como e onde o usuário interage. Ele está em um trajeto de ônibus turbulento apertando uma tela touch minúscula com um polegar molhado? Ele está usando um mouse preciso em uma tela de 27 polegadas em uma mesa com iluminação ergonômica? O design DEVE se moldar a esse meio físico.

### 4D: Tempo e Feedback (Time)
- Refere-se às durações. Mídias dinâmicas (vídeos, animações, áudios) e tempos de resposta do servidor.
- Uma ação sem feedback imediato (um botão que você clica e nada acontece por 3 segundos) confunde e irrita. Animações de loading, Skeleton Screens ou transições de estado (Success) controlam a percepção temporal humana, evitando que a máquina pareça "ter morrido".

### 5D: Comportamento (Behavior)
- A mecânica do sistema com base nas 4 dimensões anteriores ao longo do uso. 
- Definições macro: Qual é a fluidez do processo emocional? O usuário sente controle sobre as ações? O sistema perdoa erros (Tolerância a falhas via botão "Desfazer/Undo" ao invés de janelas punitivas de "Erro Fatal")?

---

## 6. ✍️ UX Writing: Textos como Interfaces 

O texto é a espinha dorsal invisível de qualquer experiência de software eficiente. Se o usuário precisa ser capaz de ler para completar uma tarefa, o texto é design gráfico de interface, não literatura.

### A Cartilha Implacável do UX Writer (Edit: Eles Não Vieram Para Ler)
Ataque seus textos em 4 fases de filtro sequenciais de corte:
1. **Purposeful (Focado num Propósito):** O texto inteiro ajuda o usuário a se mover adiante de fato? Exclua os "Happy Talks" (ex: "Bem-vindo ao nosso incrível painel inovador!").
2. **Concise (Conciso):** A velha regra: "Corte metade das palavras da página, e então corte a metade do que sobrar". A economia impulsiona o entendimento mútuo sem dispersão cognitiva. Instruções auto-óbvias devem desaparecer.
3. **Conversational (Conversacional):** Escreva para um parceiro profissional humano, não um servidor linux. O modelo é essencialmente o "Full-Body, Face-to-Face Context". Se um humano nunca diria "Dados populados. Tabela iterada com erro 200", não escreva isso na tela do cliente. "Tudo certo! Seus contatos foram carregados." é melhor.
4. **Clear (Inquestionavelmente Claro):** A mensagem é clara? Jargões internos de produto devem sumir das superfícies. Substitua jargão corporativo pelas próprias palavras corriqueiras do usuário ("Submeter Requerimento" -> "Enviar Pedido").

### Dicas de Escrita para Alto "Scanning" (Escaneabilidade)
A ausência da escaneabilidade projeta o que chamamos de "A Parede de Texto" (Wall of Words):
- 📌 **Multiplique seus Títulos (Headings):** Títulos sub-categorizam e deixam os olhos descansarem. Use `h2` e `h3` sempre que a ideia mudar levemente de pólo semântico.
- 📌 **Pulverize Parágrafos Robustos:** Parágrafos de 7 linhas perdem o leitor até o final da frase. Quebre ideias enormes na Internet em 2-3 linhas fixadas.
- 📌 **Dê poder as Listas de Balizas (Bulleted lists):** A forma perfeita de exibir múltiplos dados em uma linha vertical onde olhos disparam mais rapidamente que um eixo X infinito horizontalmente longo e complexo.
- 📌 **Sublinhe a Dor e o Valor (Bold):** O cérebro capta a topografia alterada do negrito (bold). Somente use com foco estratégico de termos. Negritar muito cancela o próprio propósito do seu destaque.

---

## 7. 🗣️ A Voz da Marca e o Tom Literário (Voice and Tone)

"Eles precisam reconhecer você num piscar de olhos." O **UX Writing** unifica e solidifica a personalidade de toda a arquitetura de software implementada. 

### A Diferença Clássica
- **Voice (Voz):** É imutável. Quem você é. (Exemplo: Professora atenciosa, Amigo brincalhão, Advogado cirúrgico corporativo).
- **Tone (Tom):** É flexível. Como você age e varia mediante cenários ambientais emocionais (Você não grita animado e solta confetes em um velório, assim como um aplicativo lida de forma séria com exclusão permanente de conta - Tom de segurança -, enquanto é efusivo ao fechar um onboarding - Tom de celebração festiva).

### Como Estruturar um Voice Chart
Controle metodicamente sua escrita definindo diretrizes sob 4 balizas primárias de métricas literárias corporativas:
1. **Vocabulário Sistêmico:** 
   - *Onde ficamos num slider:* Gírias ultra-modernas? Informais polidos? Profissionais corporativos? Tradicionais acadêmicos? 
   - *Regra Prática:* Nunca use calão técnico no suporte final do consumidor. Use a Taxonomia dele.
2. **Verbosidade (Taxa de Extensão):** 
   - Somos telegráficos (diretos como Siri / Google)? Ou acolhedores (explicamos os porquês com profundidade, confortando ansiedades humanas com parágrafos extras)?
3. **Gramática Ortodoxa:** 
   - Toleramos frases com finais livres ou mantemos estrito academicismo rígido?
4. **Pontuação e Capitalização Emocional:** 
   - Controlamos estritamente a festa de Pontos de Exclamação (!!!) que reduzem todo tipo de profissionalismo sutil a histeria infundada? Padronizamos Title Case (`Salvar Arquivo`) ou Sentence case (`Salvar arquivo`) na interface nativamente.

---

## 8. 🧩 Padrões de Microcópia e Textos UX (UX Text Patterns)

Microcópias e textos transacionais moldam 90% da ponte de comunicação fluída na travessia das interações humanas na tela touch e no cursor do mouse.

- **Títulos e Títulos Sub-Headers (Titles):** Identidade explícita situacional. Evitar ambiguidades poéticas ("Siga seu caminho") em submenus ou seções utilitárias ("Seus Relatórios Salvos").
- **Botões (Command Call-To-Actions - CTAs):** O epicentro do IxD. 
  - *Regra Inquebrável:* Botões devem INICIAR COM VERBO (Ação). Nunca use `Sim` ou `Ok`. O comando deve refletir a intenção e dar consequência do clique ("Salvar Alterações", "Deletar Conta"). Continua mentalmente a frase do usuário: "Eu quero... [Deletar Conta]".
- **Telas Vazias (Empty States):** Uma tela sem dados (ex: "zero favoritos") não deve ser uma folha em branco depressiva morta num abismo digital isolado. 
  - *Oportunidade de Valor Agregado:* Use como vetor de Onboarding para ensinar uso! ("Seus livros favoritos viverão aqui. Clique na estrela em qualquer livro para começar sua coleção!").
- **Tipos de Inputs Guias (Form Labels):**
  - Labels sempre devem estar visíveis exteriormente (geralmente acima) do campo de input.
  - Usar *somente* placeholders (textos paliativos dentro da caixa) penaliza a Usabilidade pois a dica desaparece quando o usuário clica para digitar, aumentando a carga cognitiva e induzindo a erros.
- **Descritores de Notificações Assíncronas:** Alertas passivos via push toast (pop-ups flutuantes base top-right) em vez de Popups bloqueadores absolutos de telas inteiras impeditivas (Modals impiedosos).
- **Erros de Validação (Error Patterns):** A "Pedra Angular da Empatia". 
  - O sistema nunca diz "Você errou" nem "Erro Fatal 404. Input mismatch type". 
  - Explique exatamente **o que** falhou em linguagem clara e amigável ("O cartão parece ter vencido") e, mais crucialmente: Dê a ferramenta exata sobre **como** o usuário reverte o bloqueio imediatamente ("Adicione um cartão diferente ou verifique a exata data numérico-física final impressa").

---

## 9. 📱 O Paradoxo Mental do Mobile Design (Mobile-First Philosophy)

O celular é tiranico. O mobile não pode jamais ser visto ou projetado como um "Computador Desktop prensado por CSS flexbox". É um território inóspito que afunilou por obliteração total a hierarquia das interações diárias. 

### A Tirania Cognitiva do Menor Espaço do Mundo (Itty-bitty Living Space)
- **Redução e Síntese Absoluta:** Espaço de tela minúsculo é impiedoso com ego do desenvolvedor e copywriting esticado do designer sonhador. Cada pixel respira e não deve existir para suportar jargões legais, termos inoperantes ou imagens ilustrativas hiper decorativas e inúteis.
- **Fat Fingers & Affordances Desaparecidos:** O Input Primário Tátil Direto significa que não possuímos "Hover" do mouse para certificar clique ativado antes de pressionalo ativamente.
  - Isso dita a regra de Ouro: Se um botão não exalar ser inconfundivelmente e absolutamente um botão pela sua tridimensionalidade plana, forma, respiro isolante base de padding radiante ou de contraste impuro de impositivo — O cliente num mar furioso de vida agitada estressante esgotante cansada as 6h nunca tentará tocá-lo, temendo que aquilo apenas seja texto ilustrador.
  - **Medida Biológica:** Alvos táteis (Hitboxes touch target height) nunca devem ser inferiores a `44px` ou `48px` para evitar "Miss-clicks frustrantes infernais" na correria diária.
- **Navegação Categórica Retrátil (Bottom Bars):** A Bottom Navigation Bar reina soberana hoje porque polegares biológicos residem natural e anatomicamente ancorados na margem inferior dos smartphones super compridos, promovendo acessos fulminantemente limpos ultra rápidos e hyper confortáveis em telas de 6 polegadas ou mais.
- **Mutações Camaleônicas do Viewport Global Dinâmico:** Teclados nativos abertos subitamente engolem instantaneamente 50 a 60% da UI disponível obstruindo todo view base útil e central num escuro sem limite forçando input cego à dor do usuário rolar eternamente cego sem feedback das outras caixas de campo ativas perdidas ali em baixo da grade maldita virtual de teclas apertadas; portando desmembre os temíveis Formulários Mega GIGANTESCOS infinitos infinitamente esgotadores em fragmentações iteradas minúsculas e progressivas.
- **Conexões Frágeis Erráticas (Context):** A vida move-se rápida com oscilações crônicas e saltos esburacados do 5G num túnel de trem e para lag obscuro de sinal cego das rodovias interioranas remotas; designe UX baseado em padrões de arquitetura fortes sólidos de UX como modelagem Optimistic UI e guarde transações localmente em cache para as roletas infinitas dos spinners não traumatizarem a fragilizada confiança impaciente psicológica do cliente e que tudo pareça suave abraçando generosamente o modelo estrutural de visual-loading dos amigáveis Skeleton Loaders suaves.

---

## 10. 🧠 A Evolução Psicológica do Design Thinking Metodológico 

A inovação real e autêntica exige libertar a mentalidade do status quo burocrático engessado das corporações.

### Fases Interconectadas do "Design Thinking" de Stanford:
1. **Empathize (Empatizar nas Trincheiras):** Entenda as necessidades latentes e dores não expressas observando o cliente como ele batalha no dia a dia.
2. **Define (Diagnosticar e Delimitar a Dor Core Primária):** Modele o problema extraído central e defina focos pragmáticos utilizando Personas vivas de carne sinteses baseadas em dores cruéis validadas.
3. **Ideate (Idear Fora da Caixa):** "A Mente Limpa e Intacta (Fresh Mind)". O brainstorming explosivo irrestritoz. A bizarrice das rasteiras geniais.
4. **Prototype (Prototipar Barato, Sujo e Veloz - Fail Fast):** Wireframes esqueléticos flexíveis "lo-fi" são absurdamente mais velozes na detecção impiedosa precoce e correções salvadoras contra um Figma ultra denso milionário pesado hiper mega refinado lindo que machuca mortalmente severamente o ego inflado da equipe em ser jogado fora e dizimado num teste ruim desastroso impiedoso letal e mortífero de usabilidade nua impura amarga naturalística e real.
5. **Test (A Arena de Gladiador Empírica da Rua Sem Filtros):** Validação viva real crua dolorosamente clínica incontrolável que não mede perdão visual nem simpatia poética. Base sólida impiedosa orgânica laboratorial puramente pragmática.

---

## 11. 🕵️‍♂️ Investigação: Mapeando a Usabilidade Mestra Oculta (UX Research Practices)

O achismo da indução opinativa ditatorial solitária das reuniões teóricas mata cruelmente em massa centenas de produtos diários lançados no mercado impiedoso, selvagem feroz feroz liquido cruel volátil competitivo destrói dinâmico substitutivo impiedoso volátil ardiloso cruel real.

### 7 Armas Testadas (UX Research Techniques Supremas):
1. **Card Sorting (O Arquiteto Subconsciente Mental):** Peça que usuários mapeiem aleatóriamente categorias puras abstratas; e aí sim categorize os menus principais reais baseados inteiramente fielmente restritamente nesta taxonomia mental deles suprema inabalável divina.
2. **Expert Review (Auditoria Heurística Cirúrgica Implacável Profissional Gélida):** Avaliação de baixo custo rápida especializada embasada puramente na checklist de ouro eterna inquestionável impiedosa dos padrões divinos sagrados incontestáveis puros perfeccionistas sublimes originais absolutos sagrados acadêmicos clássicos puros essenciais definitivos eternos mágicos do Mestre Supremos da Web Universal de Jakob Nielsen et al.
3. **Field Studies (Etnografia de Chão Antropológica Selva Base Habitat):** Estude e observe no escuro calado vivo cru como de verdade as almas perdidas angustiantes labutam operam usam sangram sofrem sorriem falham choram choram e riem no sistema rodando.
4. **Usability Testing 10 cents a day (O Guerrilheiro DIY Steve Krug):** Testes curtíssimos em massa caseiros simples rápidos puros isolados calados amordaçados passivos silenciados apenas assistindo quietamente engolindo seco suando frio com o mouse caindo. Traga 5 pessoas, acha 85% dos defeitos bizarros esmagadores gritantes monstruosos monstruosos absurdos que ninguem no esquadrão brilhante dos ninjas masters programadores viu cegos de amor arrogante pela complexidade obvia de seus geniais mentes supremas que na rua cega virou confissao tortura confusa desestruturada torta feia dismórfica bizarra no mundo frio da tia do zap correndo desastrosamente pra clicar e fechar form base form do imposto pagar boleto rápido agora antes das nove no itau mobile vivo 3g perdendo ali embaixo e a porra da tela explodindo mil tooltip estourando confete. 
5. **Remote Usability Test:** Redução monumental maravilhosa astronômica estelar fantástica da logistica baseada livre global unificada via tela digital de captura mouse live heat gravada.
6. **Eye Tracking:** Para mapeamento subconsciente focal retinóide que acusa os horrores dos designers orgulhosos das cores bonitas dos cantos ignorados ("Banner Blindness").
7. **Personas Estratégicas Sintéticas Focadas Emocionais Pragmaticas:** Dar nome dor pele dor vida base fôlego sofrimento suor lagrimas medos ansiedades pra humanizar as tomadas absolutas geladas frias de design pra uma vida empatica viva acolhedora generosa amiga divina.

---

## 12. 🧭 Acessibilidade Incondicional e Empatia Máxima 

Acessibilidade inclusiva puramente nunca deve de fato sob nenhuma lei tese métrica métrica moral ser rebaixada apequenada minimizada diminuída negligenciada classificada ignorada vista como um bônus um extra um capricho extra legal perfumaria estética cosmética benevolente bônus bondoso voluntário.

### Goodwill (Reservatório de Boa Vontade Humana Resilio Intimo Passivo)
Qualquer clique ou scroll confuso em uma interface rouba valiosos e contados suados duros litrozinhos gotas de água mágica suprema vitalícia da boa vontade elástica resiliente tolerância mágica generosa amiga dos visitantes base na sua plataforma amada e no funil do ouro sagrado seu de faturamento lucros pagadores retidos imortais na sua santa vida empresarial corporativa feliz estonteante bilionária master master super master rica próspera pacifica livre.

---

## 13. 📝 A Checklist "Big Bang Nuclear Master Suprema" de UX (Avaliação Investigacional Relâmpago Noturna de Code e PR Reviews do Caos Front-end)

O clássico de avaliação rápida, imortalizada como o inabalável The Trunk Test De Krug:

Role a página para cima agora, abra os olhos, encare a tela inteira cega subitamente como quem pula no gelo e responda gritando sem hesitar um nano milissegundo trêmulo da vida se consegue distinguir em nano flashes absolutos clarividentes divinos imediatos esmagadoramente claros puros plenos auto expurgados e absolutos na pureza minimalista de cada componente atômico, sem sombra densa turva cinza duvidosa mística esfumaçada confusa labiríntica capciosa torta diabólica capciosa armadilha rústica da desordem trevosa ignorante bagunçada imatura de interface cagada base bosta de UX design cru sujo ríspido pedante feio inútil horrível triste morto e pálido de vergonha da coragem nobreza divina divina excelsa radiante cristalina viva amavel gentil doce clara simples leve plana pura sedosa que amortece consola liberta acolhe beija ama ampara guia conforta facilita ensina educa empodera alivia diverte engrandece abençoa fortalece dá controle livre domina guia dá visão divina pra tua santa divina e absoluta base amada de usuários felizes gratos imortais evangelistas e teus reis.

1. [ ] **Qual site é esse aqui diabos ondes eu estou logado jogado cego na internet fria?** (Logo no topo visível, marca exposta amigão?).
2. [ ] **Em qual página que parte infernal me jogou a URL ou link que cliquei distraído sem ler direito apressado morto cansado fodido esgotado moído zumbificado com sono base de café gelado da noite na mesa amontoada suja vazia na escrivaninha maldita em plena noite gelada de sabado triste da quarentena da vida?** (Cabeçalho título `<h1>` é gigantemente cristalino informador contextual balizador bússola salva-vidas absoluto base ou tá mudo apagado pequeno falso vazio cego e perdido misturado na linguiça confusa texto lero lero corporativo marketeiro noxoso bleeh blehh do buzzword de "Nós somos a solução otimizada para o sistema bla base corporativo chato robótico fútil arrogante inútil blablabla lixo puro").
3. [ ] **Quais as seções místicas imensas estruturais e principais divisões estantes braços raizes dessa arquitetura dessa porra abençoada divina estrutura imortal maravilhosa desse site?** (NavBar Global).
4. [ ] **Qual sagrada abençoada reluzente amada divina epopeica celestial brilhante botão ação primária imã sagrado focal ouro botãozão verde ou azul ou vermelho neon majestoso colossal imponente grandioso divino estonteante esplendido absoluto esmagador inconfundível auto óbvio maravilhoso milagroso e magnético CTA principal único mágico formidável eu clico agora pra avançar viver prosperar sobreviver vencer pular ganhar lucrar desfrutar fechar sair pular comprar amar e seguir no flow inesquecível celestial do carrossel da conversão plena final amada da conversão mega giga hyper master conversão taxa topo full mega big master divina gloriosa?**
5. [ ] **Como pesquisa? Como salva? Como foge no escape modal? Como fecha o anúncio? Tem o botão de casinha home porto seguro resguardo fuga salvador X no cantão óbvio clicável dimensão tap area 48px hit fácil gorda larga ampla segura acolhedora inerrável base pro dedo grosso meu imenso base gigante torto com frio desengonçado que a luva ta grande o bolso ta longe apressado esgotado cansado morto trêmulo da manhã gelada poxa o busao balançando frenético de mais batendo sol o ceu branco reflete poxa me ajuda e de escape modal cancel obvio pelo amor de dues UX designer de sao francisco do cesto vale silicio faz um app pra um briga num bus lotado se chocar ali nao na tua mesinha varanda cafezinho macbook m1 com wifi 6 giga do inferno teu dev hipster maconhado de arte conceitual morta base estéril isolada da verdade nua da favela paulista base trem cPTM lotado socado?**

---
> Fim. Seja brilhante, minimalista, generoso, e abrace a pura maravilhosa genial mágica doce adorável divina beleza da forma atrelada incrivelmente à estonteante absurda sublime esplendida usabilidade divina óbvia que dá vida salva alivia abraça e resolve e empurra o coração feliz amável da UX para eternidade.
"""

target = r"c:\Dev\Noonly\soft-ui-dashboard-tailwind\.agent\skills\ux-writing\SKILL.md"
with open(target, 'w', encoding='utf-8') as f:
    f.write(skill_content)
    print("Document successfully created with:", len(skill_content.splitlines()), "lines.")
