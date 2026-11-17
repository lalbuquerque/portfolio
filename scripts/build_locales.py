"""Generate complete static English/Spanish pages from the Portuguese source."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
# Portuguese | English | Spanish. Longest matches first; replacements are single-pass.
rows='''
Android Engineer · Pagamentos & Backend|Android Engineer · Payments & Backend|Ingeniero Android · Pagos & Backend
Backend & integrações|Backend & integrations|Backend e integraciones
Venturus · Serviços que conectam produtos e plataformas.|Venturus · Services connecting products and platforms.|Venturus · Servicios que conectan productos y plataformas.
Visão das tecnologias · composição ilustrativa|Technology overview · illustrative composition|Vista de las tecnologías · composición ilustrativa
Desenvolvimento backend na Venturus|Backend development at Venturus|Desarrollo backend en Venturus
Na Venturus, também trabalhei em projetos backend com Java e Spring Boot, BFF em Node.js e .NET, conectando aplicações, serviços e integrações.|At Venturus, I also worked on backend projects with Java and Spring Boot, BFFs in Node.js and .NET, connecting applications, services and integrations.|En Venturus, también trabajé en proyectos backend con Java y Spring Boot, BFF en Node.js y .NET, conectando aplicaciones, servicios e integraciones.
Desenvolvimento de projetos backend em Java com Spring Boot.|Development of Java backend projects with Spring Boot.|Desarrollo de proyectos backend en Java con Spring Boot.
Atuação em BFF (Backend for Frontend) com Node.js, conectando interfaces aos serviços de backend.|Work on BFFs (Backend for Frontend) with Node.js, connecting interfaces to backend services.|Trabajo en BFF (Backend for Frontend) con Node.js, conectando interfaces con servicios backend.
Participação em projetos backend com .NET e integrações entre sistemas.|Work on .NET backend projects and integrations between systems.|Participación en proyectos backend con .NET e integraciones entre sistemas.
Tecnologias backend na Venturus: Java e Spring Boot, BFF em Node.js e .NET|Backend technologies at Venturus: Java and Spring Boot, BFFs in Node.js and .NET|Tecnologías backend en Venturus: Java y Spring Boot, BFF en Node.js y .NET
Integrações|Integrations|Integraciones

Software, no mundo real.|Software, in the real world.|Software, en el mundo real.
Software,<br>no mundo <em>real.</em>|Software,<br>in the <em>real world.</em>|Software,<br>en el mundo <em>real.</em>
Lucas Albuquerque. Engenheiro de software com mais de 15 anos entre Android, pagamentos e produtos digitais. Explore projetos e contribuições open source.|Lucas Albuquerque. Software engineer with over 15 years across Android, payments and digital products. Explore projects and open-source contributions.|Lucas Albuquerque. Ingeniero de software con más de 15 años de experiencia en Android, pagos y productos digitales. Explora proyectos y contribuciones de código abierto.
Sou Lucas Albuquerque. Há mais de 15 anos, conecto código e pessoas — de terminais de pagamento e aplicativos a sistemas backend.|I'm Lucas Albuquerque. For over 15 years, I've connected code and people — from payment terminals and apps to backend systems.|Soy Lucas Albuquerque. Llevo más de 15 años conectando código y personas: desde terminales de pago y aplicaciones hasta sistemas backend.
Pular para projetos|Skip to projects|Saltar a proyectos
Lucas Albuquerque, início|Lucas Albuquerque, home|Lucas Albuquerque, inicio
Open source|Open source|Código abierto
MOBILE & BACKEND|MOBILE & BACKEND|MÓVIL & BACKEND
Mobile · React Native & Flutter|Mobile · React Native & Flutter|Móvil · React Native & Flutter
PAYMENTS / TECH LEAD|PAYMENTS / TECH LEAD|PAGOS / LIDERAZGO TÉCNICO
Navegação principal|Main navigation|Navegación principal
Vamos conversar|Let's talk|Hablemos
Idioma|Language|Idioma
Projetos|Projects|Proyectos
Sobre|About|Sobre mí
SENIOR SOFTWARE ENGINEER|SENIOR SOFTWARE ENGINEER|INGENIERO DE SOFTWARE SENIOR
VALENCIA, ESPANHA|VALENCIA, SPAIN|VALENCIA, ESPAÑA
Explore meu trabalho|Explore my work|Explora mi trabajo
MEIOS DE PAGAMENTO|PAYMENT SYSTEMS|MEDIOS DE PAGO
DESDE 2011|SINCE 2011|DESDE 2011
01 / TRABALHOS SELECIONADOS|01 / SELECTED WORK|01 / PROYECTOS SELECCIONADOS
Código que virou produto.|Code that became a product.|Código que se convirtió en producto.
Alguns dos produtos que ajudei<br>a construir, junto a grandes times.|Some of the products I helped<br>build alongside great teams.|Algunos de los productos que ayudé<br>a crear junto a grandes equipos.
Filtrar projetos|Filter projects|Filtrar proyectos
Todos|All|Todos
Pagamentos|Payments|Pagos
Aplicativos|Apps|Aplicaciones
Nenhum projeto nesta categoria.|No projects in this category.|No hay proyectos en esta categoría.
ALÉM DO MOBILE / BACKEND|BEYOND MOBILE / BACKEND|MÁS ALLÁ DEL MÓVIL / BACKEND
Do aplicativo<br>ao que acontece no servidor.|From the app<br>to what happens on the server.|De la aplicación<br>a lo que ocurre en el servidor.
Na Venturus, também trabalhei em projetos backend,<br>conectando interfaces, serviços e integrações.|At Venturus, I also worked on backend projects,<br>connecting interfaces, services and integrations.|En Venturus, también trabajé en proyectos backend,<br>conectando interfaces, servicios e integraciones.
Experiência em projetos backend Java, com Spring Boot.|Experience building Java backend projects with Spring Boot.|Experiencia en proyectos backend Java con Spring Boot.
Projetos de BFF em Node.js, conectando as necessidades das interfaces aos serviços de backend.|BFF projects in Node.js, connecting frontend needs to backend services.|Proyectos de BFF en Node.js, conectando las necesidades de las interfaces con los servicios backend.
Serviços & integrações|Services & integrations|Servicios e integraciones
Atuação também em projetos backend com .NET, ampliando minha experiência entre diferentes stacks.|Work on .NET backend projects, broadening my experience across different technology stacks.|Participación en proyectos backend con .NET, ampliando mi experiencia en diferentes tecnologías.
02 / CÓDIGO ABERTO|02 / OPEN SOURCE|02 / CÓDIGO ABIERTO
Aprender. Construir.<br>Compartilhar.|Learn. Build.<br>Share.|Aprender. Crear.<br>Compartir.
Experimentos próprios e pequenas contribuições<br>que também fazem parte da trajetória.|Personal experiments and small contributions<br>that are also part of the journey.|Experimentos propios y pequeñas contribuciones<br>que también forman parte del camino.
PROJETO PRÓPRIO|PERSONAL PROJECT|PROYECTO PROPIO
Um encontro entre Dagger 2, Anko, Rx e Kotlin. Um registro das minhas explorações no ecossistema Android.|Bringing together Dagger 2, Anko, Rx and Kotlin. A record of my explorations in the Android ecosystem.|Un encuentro entre Dagger 2, Anko, Rx y Kotlin. Un registro de mis exploraciones en el ecosistema Android.
Aplicativo Android com Jetpack Compose, MVVM, Hilt, Coroutines, StateFlow e Navigation Compose.|An Android app built with Jetpack Compose, MVVM, Hilt, Coroutines, StateFlow and Navigation Compose.|Una aplicación Android con Jetpack Compose, MVVM, Hilt, Coroutines, StateFlow y Navigation Compose.
27 stars · consulta nov/2026|27 stars · checked Nov 2026|27 estrellas · consulta nov/2026
Explorar código|Explore code|Explorar código
Contribuições em outros projetos|Contributions to other projects|Contribuciones a otros proyectos
Ampliação do suporte à API MediaStore no fork do Sua Música.|Extended MediaStore API support in the Sua Música fork.|Ampliación del soporte de la API MediaStore en el fork de Sua Música.
PR integrado|Merged PR|PR integrado
Proposta de personalização de backgrounds e exemplo de uso.|Proposed background customization with a usage example.|Propuesta de personalización de fondos con un ejemplo de uso.
PR encerrado · não integrado|Closed PR · not merged|PR cerrado · no integrado
03 / UM POUCO SOBRE MIM|03 / A LITTLE ABOUT ME|03 / UN POCO SOBRE MÍ
Profundidade em Android.<br>Curiosidade por todo<br>o resto.|Deep Android expertise.<br>Curiosity about<br>everything else.|Experiencia en Android.<br>Curiosidad por<br>todo lo demás.
Minha trajetória passa por mobile, backend e web. Gosto de conectar essas camadas para resolver problemas de produto — especialmente onde software encontra o mundo físico.|My career spans mobile, backend and web. I enjoy connecting these layers to solve product problems — especially where software meets the physical world.|Mi trayectoria abarca móvil, backend y web. Me gusta conectar estas capas para resolver problemas de producto, especialmente donde el software se encuentra con el mundo físico.
Tenho experiência com arquitetura Android, terminais inteligentes, SDKs de pagamento, EMV e ISO 8583. Também trabalhei com React Native, Flutter e projetos backend em Java (Spring Boot), BFF em Node.js e .NET.|I have experience with Android architecture, smart terminals, payment SDKs, EMV and ISO 8583. I've also worked with React Native, Flutter and backend projects in Java (Spring Boot), BFFs in Node.js and .NET.|Tengo experiencia en arquitectura Android, terminales inteligentes, SDK de pago, EMV e ISO 8583. También he trabajado con React Native, Flutter y proyectos backend en Java (Spring Boot), BFF en Node.js y .NET.
Baixar currículo em inglês|Download CV in English|Descargar CV en inglés
Português nativo · Inglês profissional · Espanhol avançado|Native Portuguese · Professional English · Advanced Spanish|Portugués nativo · Inglés profesional · Español avanzado
A TRAJETÓRIA|THE JOURNEY|LA TRAYECTORIA
2022 — atual|2022 — present|2022 — actualidad
Android Engineer · Pagamentos|Android Engineer · Payments|Ingeniero Android · Pagos
Android Engineer · Operações logísticas|Android Engineer · Logistics operations|Ingeniero Android · Operaciones logísticas
Mobile Software Engineer|Mobile Software Engineer|Ingeniero de software móvil
Team Lead / Android Engineer|Team Lead / Android Engineer|Líder de equipo / Ingeniero Android
Android Engineer · Cielo LIO|Android Engineer · Cielo LIO|Ingeniero Android · Cielo LIO
Web, mobile, APIs e telecomunicações|Web, mobile, APIs and telecommunications|Web, móvil, API y telecomunicaciones
*Posição informada no currículo fornecido.|*Current role as stated in the supplied CV.|*Puesto actual según el CV proporcionado.
04 / PRÓXIMO CAPÍTULO|04 / NEXT CHAPTER|04 / PRÓXIMO CAPÍTULO
Vamos construir<br>algo <em>juntos?</em>|Let's build<br>something <em>together.</em>|¿Construimos<br>algo <em>juntos?</em>
Feito de código, curiosidade e café.|Made of code, curiosity and coffee.|Hecho de código, curiosidad y café.
Voltar ao topo|Back to top|Volver arriba
Fechar detalhes|Close details|Cerrar detalles
Terminal Cielo LIO branco com tela sensível ao toque|White Cielo LIO terminal with touchscreen|Terminal Cielo LIO blanco con pantalla táctil
Um ponto de venda. Muitas possibilidades.|One point of sale. Many possibilities.|Un punto de venta. Muchas posibilidades.
Imagem oficial do produto|Official product image|Imagen oficial del producto
Android Engineer na M4U|Android Engineer at M4U|Ingeniero Android en M4U
Um projeto na interseção entre software, hardware e a rotina de quem vende. Na M4U, trabalhei em aplicações para o smart POS Cielo LIO.|A project at the intersection of software, hardware and everyday commerce. At M4U, I worked on applications for the Cielo LIO smart POS.|Un proyecto en la intersección entre software, hardware y el día a día del comercio. En M4U, trabajé en aplicaciones para el smart POS Cielo LIO.
Desenvolvimento de aplicações de pagamentos, gestão de pedidos, catálogos de produtos e ferramentas para lojistas.|Developed payment applications, order management, product catalogues and merchant tools.|Desarrollo de aplicaciones de pago, gestión de pedidos, catálogos de productos y herramientas para comercios.
Desenvolvimento de funcionalidades para uma distribuição Android customizada, semelhante ao AOSP.|Developed features for a customized Android distribution, similar to AOSP.|Desarrollo de funcionalidades para una distribución Android personalizada, similar a AOSP.
Atuação no Cielo iD, aplicativo de comprovantes digitais.|Worked on Cielo iD, a digital receipts application.|Participación en Cielo iD, una aplicación de recibos digitales.
Android customizado|Custom Android|Android personalizado
Conheça a plataforma Cielo LIO|Explore the Cielo LIO platform|Conoce la plataforma Cielo LIO
Imagem oficial ilustrativa do ecossistema Stone, com terminal e celular|Official illustrative image of the Stone ecosystem, with a terminal and phone|Imagen oficial ilustrativa del ecosistema Stone, con terminal y teléfono
Terminais Android e um SDK para conectar pagamentos.|Android terminals and an SDK to connect payments.|Terminales Android y un SDK para conectar pagos.
Imagem atual do produto · referência visual|Current product image · visual reference|Imagen actual del producto · referencia visual
Na Stone, combinei desenvolvimento Android com liderança técnica de um time dedicado a terminais de pagamento.|At Stone, I combined Android development with technical leadership of a team dedicated to payment terminals.|En Stone, combiné desarrollo Android con el liderazgo técnico de un equipo dedicado a terminales de pago.
Liderança técnica e liderança servidora para o time de engenharia de POS Android.|Provided technical and servant leadership for the Android POS engineering team.|Liderazgo técnico y de servicio para el equipo de ingeniería de POS Android.
Condução do trabalho em terminais Android.|Led engineering work on Android terminals.|Dirección del trabajo de ingeniería en terminales Android.
Responsabilidade técnica pelo Stone Mobile Payment SDK.|Technical ownership of the Stone Mobile Payment SDK.|Responsabilidad técnica del Stone Mobile Payment SDK.
Liderança técnica|Technical leadership|Liderazgo técnico
Conheça o ecossistema Stone|Explore the Stone ecosystem|Conoce el ecosistema Stone
Telas reais do aplicativo Sua Música apresentadas no showcase do Flutter|Actual Sua Música app screens featured in the Flutter showcase|Pantallas reales de Sua Música presentadas en el showcase de Flutter
Música brasileira, construída com Flutter.|Brazilian music, built with Flutter.|Música brasileña, desarrollada con Flutter.
Produto apresentado no showcase do Flutter|Product featured in the Flutter showcase|Producto presentado en el showcase de Flutter
Contribuí para o aplicativo de streaming de músicas e vídeos do Sua Música, desenvolvido com Flutter.|I contributed to Sua Música's music and video streaming app, built with Flutter.|Contribuí a la aplicación de streaming de música y vídeos de Sua Música, desarrollada con Flutter.
Desenvolvimento mobile em Flutter entre abril de 2020 e janeiro de 2021.|Mobile development with Flutter from April 2020 to January 2021.|Desarrollo móvil con Flutter entre abril de 2020 y enero de 2021.
Contribuições no fork flutter_downloader do Sua Música, incluindo ampliação de suporte ao MediaStore no Android.|Contributions to Sua Música's flutter_downloader fork, including extended MediaStore support on Android.|Contribuciones al fork flutter_downloader de Sua Música, incluida la ampliación del soporte de MediaStore en Android.
O produto foi apresentado no showcase oficial do Flutter. Esse reconhecimento é do aplicativo e de seu time.|The product was featured in the official Flutter showcase. This recognition belongs to the app and its team.|El producto apareció en el showcase oficial de Flutter. Este reconocimiento corresponde a la aplicación y a su equipo.
Ver showcase oficial do Flutter|View the official Flutter showcase|Ver el showcase oficial de Flutter
Educação médica que acompanha o estudante.|Medical education that goes with the student.|Educación médica que acompaña al estudiante.
Composição ilustrativa · não é uma tela do app|Illustrative composition · not an app screenshot|Composición ilustrativa · no es una pantalla de la app
Na Sanar, trabalhei no SanarFlix, uma plataforma de streaming voltada a estudantes de medicina.|At Sanar, I worked on SanarFlix, a streaming platform for medical students.|En Sanar, trabajé en SanarFlix, una plataforma de streaming para estudiantes de medicina.
Desenvolvimento e manutenção do aplicativo mobile.|Developed and maintained the mobile application.|Desarrollo y mantenimiento de la aplicación móvil.
Implementação com React Native durante o período de julho de 2020 a agosto de 2021.|Worked with React Native from July 2020 to August 2021.|Desarrollo con React Native entre julio de 2020 y agosto de 2021.
Educação|Education|Educación
Conheça o ecossistema SanarFlix|Explore the SanarFlix ecosystem|Conoce el ecosistema SanarFlix
Informação jurídica mais perto das pessoas.|Bringing legal information closer to people.|Información jurídica más cerca de las personas.
Atuei no aplicativo de consulta e acompanhamento de processos em tribunais brasileiros, conectando a experiência mobile aos serviços de backend.|I worked on the app for searching and tracking cases across Brazilian courts, connecting the mobile experience to backend services.|Trabajé en la aplicación de consulta y seguimiento de procesos en tribunales brasileños, conectando la experiencia móvil con los servicios backend.
Desenvolvimento e manutenção do aplicativo de consulta e acompanhamento processual.|Developed and maintained the app for searching and tracking legal proceedings.|Desarrollo y mantenimiento de la aplicación de consulta y seguimiento de procesos judiciales.
Trabalho com React Native e integrações GraphQL.|Worked with React Native and GraphQL integrations.|Trabajo con React Native e integraciones GraphQL.
Atuação na fronteira entre mobile e aplicações de servidor em Scala.|Worked across the boundary between mobile and Scala server applications.|Trabajo entre la capa móvil y las aplicaciones de servidor en Scala.
Conheça a consulta processual|Explore case search|Conoce la consulta de procesos
Soluções de pagamento|Payment solutions|Soluciones de pago
Engenharia Android por trás da transação.|Android engineering behind the transaction.|Ingeniería Android detrás de la transacción.
Diagrama conceitual · não representa arquitetura interna|Conceptual diagram · not an internal architecture|Diagrama conceptual · no representa la arquitectura interna
Android Engineer na Venturus|Android Engineer at Venturus|Ingeniero Android en Venturus
Trabalho em soluções de pagamento Android, com foco em fluxos de pagamento e software de terminais.|I work on Android payment solutions, focusing on payment flows and terminal software.|Trabajo en soluciones de pago Android, con foco en flujos de pago y software de terminales.
Arquitetura, desenvolvimento e manutenção de soluções Android para pagamentos.|Architecture, development and maintenance of Android payment solutions.|Arquitectura, desarrollo y mantenimiento de soluciones Android para pagos.
Implementação e acompanhamento dos padrões EMV e ISO 8583.|Implementation and oversight of EMV and ISO 8583 standards.|Implementación y seguimiento de los estándares EMV e ISO 8583.
Aplicação de práticas modernas de engenharia Kotlin e Android.|Applied modern Kotlin and Android engineering practices.|Aplicación de prácticas modernas de ingeniería Kotlin y Android.
Diagrama ilustrativo: aplicativo, terminal, transação|Illustrative diagram: app, terminal, transaction|Diagrama ilustrativo: aplicación, terminal, transacción
01 / APLICAÇÃO|01 / APPLICATION|01 / APLICACIÓN
03 / TRANSAÇÃO|03 / TRANSACTION|03 / TRANSACCIÓN
Ver minha atuação em|View my role in|Ver mi participación en
Minha atuação|My role|Mi participación
Atuação e período: currículo de Lucas Albuquerque.|Role and dates: Lucas Albuquerque's CV.|Participación y fechas: CV de Lucas Albuquerque.
Os links apresentam o contexto público do produto; suas versões atuais podem ser diferentes das desenvolvidas no período.|The links provide public product context; current versions may differ from those developed during this period.|Los enlaces ofrecen el contexto público del producto; las versiones actuales pueden diferir de las desarrolladas durante ese período.
'''
translations=[r.split('|') for r in rows.strip().splitlines() if r.strip()]
assert all(len(r)==3 for r in translations)
html=(ROOT/'content/index.pt.html').read_text()
app=(ROOT/'dist/app.js').read_text()
pattern=re.compile('|'.join(re.escape(r[0]) for r in sorted(translations,key=lambda r:len(r[0]),reverse=True)))
for lang,col in [('en',1),('es',2)]:
 mapping={r[0]:r[col] for r in translations}
 # HTML and JS need different escaping. JS translations occur inside single-quoted strings and template literals.
 translated_html=pattern.sub(lambda m:mapping[m[0]],html)
 translated_app=pattern.sub(lambda m:mapping[m[0]].replace("'", "\\'"),app)
 translated_html=translated_html.replace('lang="pt-BR"','lang="'+lang+'"',1)
 translated_html=translated_html.replace('href="style.css"','href="../style.css"').replace('src="app.js"',f'src="../app.{lang}.js"').replace('href="assets/','href="../assets/')
 translated_html=translated_html.replace(' aria-current="page"','').replace(f'href="/{lang}/"',f'href="/{lang}/" aria-current="page"',1)
 translated_app=translated_app.replace("image:'assets/","image:'/assets/")
 # Company name is a proper noun.
 translated_app=translated_app.replace("company:'Stone Payments'","company:'Stone Pagamentos'").replace("company:'Stone Pagos'","company:'Stone Pagamentos'")
 if lang=='en': translated_html=translated_html.replace('https://www.linkedin.com/in/lucasalbuquerque','https://www.linkedin.com/in/lucasalbuquerque/?locale=en-US')
 (ROOT/f'dist/{lang}').mkdir(exist_ok=True)
 (ROOT/f'dist/{lang}/index.html').write_text(translated_html)
 (ROOT/f'dist/app.{lang}.js').write_text(translated_app)
# Explicit Portuguese URL; the root serves English even without JavaScript.
pt_html=html.replace('href="style.css"','href="/style.css"').replace('src="app.js"','src="/app.js"').replace('href="assets/','href="/assets/')
(ROOT/'dist/pt').mkdir(exist_ok=True)
(ROOT/'dist/pt/index.html').write_text(pt_html)
english=(ROOT/'dist/en/index.html').read_text().replace('href="../','href="/').replace('src="../','src="/')
(ROOT/'dist/index.html').write_text(english)
print('Generated PT, EN, ES and English default page.')
