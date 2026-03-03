import streamlit as st

st.set_page_config(
    page_title="Project Consilium | JMPetrus",
    layout="wide",
    initial_sidebar_state="collapsed",
)

page_html = """
<html lang="en">
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Segoe UI', sans-serif;
      background: #0f0f0f;
      color: #f0f0f0;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 24px 48px;
      border-bottom: 1px solid #222;
    }

    header .brand {
      font-size: 13px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #aaa;
    }

    header nav a {
      color: #aaa;
      text-decoration: none;
      margin-left: 32px;
      font-size: 14px;
      transition: color 0.2s;
    }

    header nav a:hover { color: #fff; }

    .hero {
      text-align: center;
      padding: 120px 24px 80px;
    }

    .hero h1 {
      font-size: 56px;
      font-weight: 700;
      letter-spacing: -1px;
      line-height: 1.1;
      margin-bottom: 24px;
    }

    .hero h1 span { color: #c9a84c; }

    .hero .tagline {
      font-size: 20px;
      color: #999;
      max-width: 560px;
      margin: 0 auto 40px;
      line-height: 1.7;
    }

    .btn {
      display: inline-block;
      padding: 14px 36px;
      background: #c9a84c;
      color: #0f0f0f;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 1px;
      text-decoration: none;
      border-radius: 4px;
      transition: background 0.2s;
      border: none;
      cursor: pointer;
    }

    .btn:hover { background: #e0bb65; }

    .section {
      padding: 80px 48px;
      max-width: 900px;
      margin: 0 auto;
    }

    .section-title {
      font-size: 11px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #c9a84c;
      margin-bottom: 32px;
    }

    .section p {
      color: #999;
      font-size: 16px;
      line-height: 1.8;
      margin-bottom: 20px;
    }

    .section p strong {
      color: #f0f0f0;
    }

    .section p em {
      color: #ccc;
    }

    .highlight {
      border-left: 3px solid #c9a84c;
      padding: 24px 32px;
      margin: 32px 0;
      background: #1a1a1a;
      border-radius: 0 8px 8px 0;
    }

    .highlight p {
      color: #ccc;
      margin-bottom: 8px;
    }

    .highlight p:last-child {
      margin-bottom: 0;
    }

    .list-group {
      margin: 32px 0;
    }

    .list-group h3 {
      font-size: 17px;
      margin-bottom: 14px;
      color: #f0f0f0;
    }

    .list-group ul {
      list-style: none;
      padding: 0;
    }

    .list-group ul li {
      color: #999;
      font-size: 15px;
      line-height: 1.9;
      padding-left: 20px;
      position: relative;
    }

    .list-group ul li::before {
      content: "\\2022";
      color: #c9a84c;
      position: absolute;
      left: 0;
    }

    .divider {
      border: none;
      border-top: 1px solid #222;
      margin: 0 48px;
    }

    .author {
      text-align: center;
      padding: 40px 24px;
      margin-top: 16px;
    }

    .author .name {
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
    }

    .author .role {
      color: #999;
      font-size: 15px;
      margin-bottom: 12px;
    }

    .author a {
      color: #c9a84c;
      text-decoration: none;
      font-size: 14px;
      letter-spacing: 1px;
    }

    .author a:hover { color: #e0bb65; }

    .products {
      text-align: center;
      padding: 80px 24px;
      max-width: 900px;
      margin: 0 auto;
    }

    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 24px;
      max-width: 600px;
      margin: 32px auto 40px;
    }

    .product-card {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      border-radius: 8px;
      padding: 36px 28px;
      text-align: center;
      transition: border-color 0.2s;
    }

    .product-card:hover { border-color: #c9a84c; }

    .product-card h3 {
      font-size: 17px;
      margin-bottom: 8px;
    }

    .product-card .badge {
      display: inline-block;
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #c9a84c;
      border: 1px solid #c9a84c;
      padding: 4px 12px;
      border-radius: 20px;
      margin-top: 12px;
    }

    .two-col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 48px;
    }

    footer {
      text-align: center;
      padding: 48px;
      border-top: 1px solid #222;
      color: #666;
      font-size: 14px;
      line-height: 1.7;
      max-width: 700px;
      margin: 0 auto;
    }

    footer p {
      margin-bottom: 0;
    }

    @media (max-width: 768px) {
      .hero h1 { font-size: 36px; }
      .section { padding: 60px 24px; }
      .two-col { grid-template-columns: 1fr; }
      header { padding: 16px 24px; flex-direction: column; gap: 12px; }
      footer { padding: 36px 24px; }
    }
  </style>
</head>
<body>

  <header>
    <div class="brand">Project Consilium</div>
    <nav>
      <a href="#start">Start Here</a>
      <a href="#what">What Is It</a>
      <a href="#tools">Tools</a>
      <a href="#products">Products</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Project <span>Consilium</span></h1>
    <p class="tagline">Structured decision tools for complex environments.</p>
  </section>

  <hr class="divider"/>

  <section class="section" id="start">
    <div class="section-title">Start Here</div>
    <p>Project Consilium is the product ecosystem of <strong>JMPetrus</strong> — an evolving suite of practical tools designed to help leaders make sound decisions, strengthen organizational governance and accelerate impact in complex, risk-exposed environments.</p>
    <p>Each tool encodes structured judgment into usable and defensible formats — diagnostics, frameworks, impact measurement, briefs, and decision supports.</p>
    <p>Built for leaders who need decisions to hold up under scrutiny and reputation risk.</p>
  </section>

  <hr class="divider"/>

  <section class="section" id="what">
    <div class="section-title">What is Project Consilium?</div>
    <p><em>"Consilium"</em> is Latin for counsel or deliberate judgment.</p>
    <p>The premise is simple:</p>
    <div class="highlight">
      <p>Good decisions rarely fail because of intelligence. They fail because of misaligned incentives, hidden risks, or incomplete framing.</p>
    </div>
    <p>Project Consilium exists to surface those blind spots before they compound. It reflects an ongoing effort to encode structured judgment into tools that are portable, scalable, and decision-focused. It will evolve as the risk landscape evolves, and client need evolves</p>
  </section>

  <hr class="divider"/>

  <section class="section" id="tools">
    <div class="section-title">What You'll Find Here</div>

    <div class="two-col">
      <div class="list-group">
        <h3>Tools designed for:</h3>
        <ul>
          <li>ESG and sustainability leaders navigating regulatory pressure</li>
          <li>Governance teams facing ambiguity</li>
          <li>Organizations managing reputation or operational exposure</li>
          <li>Cross-functional teams making irreversible commitments</li>
        </ul>
      </div>

      <div class="list-group">
        <h3>Formats may include:</h3>
        <ul>
          <li>Readiness diagnostics</li>
          <li>Risk mapping tools</li>
          <li>Decision briefs</li>
          <li>Governance checklists</li>
          <li>AI-enabled impact frameworks</li>
        </ul>
      </div>
    </div>

    <p style="margin-top: 24px;">Each artifact is built to be clear, practical, usable without direct consulting engagement.</p>
  </section>

  <hr class="divider"/>

  <div class="author">
    <div class="name">Joelle Petrus</div>
    <div class="role">Decision Advocate for risk-exposed teams.</div>
    <a href="https://jmpetrus.com" target="_blank">Jmpetrus.com</a>
  </div>

  <hr class="divider"/>

  <section class="products" id="products">
    <div class="section-title">Products Coming Soon</div>
    <div class="product-grid">
      <div class="product-card">
        <h3>Sustainability Supplier Readiness</h3>
        <div class="badge">Coming Soon</div>
      </div>
      <div class="product-card">
        <h3>Proposal Go / No go Tool</h3>
        <div class="badge">Coming Soon</div>
      </div>
    </div>
    <a href="#" class="btn">Join the Waitlist</a>
  </section>

  <hr class="divider"/>

  <footer>
    <p>Project Consilium is an initiative by JMPetrus Consulting — a consulting practice focused on equipping organizations with practical tools for clarity, alignment, and growth. We believe great diagnostics are the foundation of great strategy.</p>
  </footer>

</body>
</html>
"""

st.components.v1.html(page_html, height=4000, scrolling=True)
