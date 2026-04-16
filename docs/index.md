---
layout: home

hero:
  name: "IT Gateway"
  text: "Your complete CAPS IT resource"
  tagline: "Grades 10 · 11 · 12 — everything you need for Paper 1 and Paper 2"
  image:
    src: /images/hero.svg
    alt: IT Gateway
  actions:
    - theme: brand
      text: 📚 Theory — Paper 2
      link: /theory/
    - theme: alt
      text: 💻 Practical — Paper 1
      link: /practical/
    - theme: alt
      text: ⚡ Quick Study
      link: /quick-study/

features:
  - icon: 📚
    title: Theory (Paper 2)
    details: All 6 CAPS theory topics with grade indicators, key term tables, and exam focus questions for every concept.
    link: /theory/
    linkText: Browse Theory →

  - icon: 💻
    title: Practical Guide (Paper 1)
    details: Step-by-step Delphi programming, SQL queries, algorithms, and number systems with worked examples and exercises.
    link: /practical/
    linkText: Browse Practical →

  - icon: ⚡
    title: Quick Study
    details: Cheat sheets, syntax cards and topic summaries — everything in one page. Ideal for the night before an exam.
    link: /quick-study/
    linkText: Browse Quick Study →
---

<div class="topic-grid-section">
  <h2>Theory Topics</h2>
  <p class="topic-grid-sub">Click any topic to go straight to that section</p>

  <div class="topic-grid">
    <a href="/theory/systems/" class="topic-card systems">
      <span class="topic-icon">🖥️</span>
      <span class="topic-title">Systems Technologies</span>
      <span class="topic-detail">Hardware · Software · OS · Cloud</span>
    </a>
    <a href="/theory/networks/" class="topic-card networks">
      <span class="topic-icon">🌐</span>
      <span class="topic-title">Communication Technologies</span>
      <span class="topic-detail">Networks · Protocols · Security</span>
    </a>
    <a href="/theory/internet/" class="topic-card internet">
      <span class="topic-icon">🌍</span>
      <span class="topic-title">Internet Technologies</span>
      <span class="topic-detail">WWW · HTML · Web Design · Scripting</span>
    </a>
    <a href="/theory/databases/" class="topic-card databases">
      <span class="topic-icon">🗄️</span>
      <span class="topic-title">Data & Information Management</span>
      <span class="topic-detail">Databases · ERDs · Normalisation · SQL</span>
    </a>
    <a href="/theory/social/" class="topic-card social">
      <span class="topic-icon">⚖️</span>
      <span class="topic-title">Social Implications</span>
      <span class="topic-detail">Copyright · Cybercrime · Privacy · POPIA</span>
    </a>
    <a href="/theory/programming/" class="topic-card programming">
      <span class="topic-icon">💡</span>
      <span class="topic-title">Solution Development</span>
      <span class="topic-detail">Algorithms · OOP · Software Engineering</span>
    </a>
  </div>

  <h2 style="margin-top: 3rem;">Practical Topics</h2>
  <p class="topic-grid-sub">Paper 1 skills with worked examples and exercises</p>

  <div class="topic-grid four-col">
    <a href="/practical/algorithms/" class="topic-card algorithms">
      <span class="topic-icon">📐</span>
      <span class="topic-title">Algorithms</span>
      <span class="topic-detail">Sequential · Decision · Loops · Classic Problems</span>
    </a>
    <a href="/practical/delphi/" class="topic-card delphi">
      <span class="topic-icon">🔵</span>
      <span class="topic-title">Delphi Programming</span>
      <span class="topic-detail">Variables · Arrays · Strings · OOP · Files</span>
    </a>
    <a href="/practical/sql/" class="topic-card sqlcard">
      <span class="topic-icon">🗃️</span>
      <span class="topic-title">SQL & Databases</span>
      <span class="topic-detail">SELECT · JOINs · INSERT · Delphi connection</span>
    </a>
    <a href="/practical/number-systems/" class="topic-card numbersys">
      <span class="topic-icon">🔢</span>
      <span class="topic-title">Number Systems</span>
      <span class="topic-detail">Binary · Hexadecimal · Data Sizes</span>
    </a>
  </div>
</div>

<style>
.topic-grid-section {
  max-width: 1152px;
  margin: 0 auto;
  padding: 3rem 1.5rem 4rem;
}

.topic-grid-section h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: var(--vp-c-text-1);
}

.topic-grid-sub {
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.topic-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.topic-grid.four-col {
  grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 960px) {
  .topic-grid.four-col {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .topic-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .topic-grid,
  .topic-grid.four-col {
    grid-template-columns: 1fr;
  }
}

.topic-card {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding: 1.25rem 1.5rem;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.15s;
}

.topic-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  transform: translateY(-2px);
  text-decoration: none;
}

.topic-icon {
  font-size: 1.6rem;
  line-height: 1;
}

.topic-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

.topic-detail {
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  line-height: 1.4;
}

/* Accent colours per topic */
.systems     { border-left: 4px solid #0ea5e9; }
.networks    { border-left: 4px solid #6366f1; }
.internet    { border-left: 4px solid #10b981; }
.databases   { border-left: 4px solid #f59e0b; }
.social      { border-left: 4px solid #ef4444; }
.programming { border-left: 4px solid #8b5cf6; }
.algorithms  { border-left: 4px solid #f97316; }
.delphi      { border-left: 4px solid #3b82f6; }
.sqlcard     { border-left: 4px solid #14b8a6; }
.numbersys   { border-left: 4px solid #ec4899; }
</style>
