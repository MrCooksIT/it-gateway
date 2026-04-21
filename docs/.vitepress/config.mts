import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'IT Gateway',
  description: 'Your complete CAPS Information Technology resource for Grades 10–12',
  base: '/it-gateway/',

  head: [
    ['meta', { name: 'theme-color', content: '#0f766e' }],
    ['link', { rel: 'icon', href: '/favicon.ico' }],
  ],

  themeConfig: {
    siteTitle: 'IT Gateway',

    // ─── Top navigation bar ───────────────────────────────────────────────
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Theory', link: '/theory/' },
      { text: 'Practical', link: '/practical/' },
      { text: 'Quick Study', link: '/quick-study/' },
      {
        text: 'More',
        items: [
          { text: 'Google Classroom', link: 'https://classroom.google.com' },
          { text: 'About this site', link: '/about' },
        ],
      },
    ],

    // ─── Unified sidebar ──────────────────────────────────────────────────
    // Single structure shown on all pages — textbook style:
    // Theory → Practical → Quick Study → Digital Technology (Gr 8–9)
    sidebar: [

      // ══════════════════════════════════════════════════════════════════
      //  THEORY — Paper 2
      // ══════════════════════════════════════════════════════════════════
      {
        text: '📚 Theory — Paper 2',
        collapsed: false,
        items: [

          // ── Systems Technologies ──────────────────────────────────────
          {
            text: '🖥️ Systems Technologies',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/systems/' },
              { text: 'What is Computing?',      link: '/theory/systems/what-is-computing',   badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Hardware',                link: '/theory/systems/hardware',             badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Peripherals & Devices',   link: '/theory/systems/peripherals',          badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Software',                link: '/theory/systems/software',             badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'OS & File Management',    link: '/theory/systems/os-management',        badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Types of Computers',      link: '/theory/systems/types-of-computers',   badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Computer Performance',    link: '/theory/systems/performance',          badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Mobile Technologies',     link: '/theory/systems/mobile-tech',          badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Data Representation',     link: '/theory/systems/data-representation',  badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Cloud & Virtualisation',  link: '/theory/systems/cloud-virtualisation', badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Communication Technologies ────────────────────────────────
          {
            text: '🌐 Communication Technologies',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/networks/' },
              { text: 'Network Concepts',      link: '/theory/networks/network-concepts',  badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Types of Networks',     link: '/theory/networks/network-types',     badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Network Hardware',      link: '/theory/networks/network-hardware',  badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Network Topologies',    link: '/theory/networks/topologies',        badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Protocols',             link: '/theory/networks/protocols',         badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'E-Communication',       link: '/theory/networks/e-communication',  badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Wireless Technologies', link: '/theory/networks/wireless',          badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'Network Security',      link: '/theory/networks/network-security',  badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Internet Technologies ─────────────────────────────────────
          {
            text: '🌍 Internet Technologies',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/internet/' },
              { text: 'The Internet & WWW',        link: '/theory/internet/internet-www',     badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Web Evolution (1.0–3.0)',    link: '/theory/internet/web-evolution',    badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Internet Services',          link: '/theory/internet/internet-services', badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Multimedia & Streaming',     link: '/theory/internet/multimedia',       badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Website Design',             link: '/theory/internet/website-design',   badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'HTML Basics',                link: '/theory/internet/html-basics',      badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Web Scripting',              link: '/theory/internet/web-scripting',    badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'Online Services & Cookies',  link: '/theory/internet/online-services',  badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Data & Information Management ─────────────────────────────
          {
            text: '🗄️ Data & Information Management',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/databases/' },
              { text: 'Data Concepts',           link: '/theory/databases/data-concepts',      badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Database Concepts',        link: '/theory/databases/database-concepts',  badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Database Design & ERDs',   link: '/theory/databases/database-design',    badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Normalisation',            link: '/theory/databases/normalisation',      badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'SQL — Theory',             link: '/theory/databases/sql-theory',         badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Data Integrity & Security',link: '/theory/databases/data-integrity',     badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'DBMS Software & Roles',    link: '/theory/databases/dbms-software',      badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Social Implications ───────────────────────────────────────
          {
            text: '⚖️ Social Implications',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/social/' },
              { text: 'Copyright & Licensing', link: '/theory/social/copyright',           badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Cybercrime',            link: '/theory/social/cybercrime',          badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Online Safety',         link: '/theory/social/online-safety',       badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Privacy & Ethics',      link: '/theory/social/privacy-ethics',      badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Digital Divide',        link: '/theory/social/digital-divide',      badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'Environment & Society', link: '/theory/social/environment-society', badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Solution Development ──────────────────────────────────────
          {
            text: '💡 Solution Development',
            collapsed: true,
            items: [
              { text: 'Topic overview', link: '/theory/programming/' },
              { text: 'Programming Concepts', link: '/theory/programming/programming-concepts', badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Algorithms (Theory)',   link: '/theory/programming/algorithms-theory',   badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'OOP Principles',        link: '/theory/programming/oop-principles',      badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'Software Engineering',  link: '/theory/programming/software-engineering', badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

        ],
      },

      // ══════════════════════════════════════════════════════════════════
      //  PRACTICAL — Paper 1
      // ══════════════════════════════════════════════════════════════════
      {
        text: '💻 Practical — Paper 1',
        collapsed: false,
        items: [

          // ── Algorithms & Flowcharts ───────────────────────────────────
          {
            text: '📐 Algorithms & Flowcharts',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/practical/algorithms/' },
              { text: 'Sequential Algorithms', link: '/practical/algorithms/sequential',      badge: { type: 'tip',  text: 'Gr 10' } },
              { text: 'Decision Algorithms',   link: '/practical/algorithms/decision',        badge: { type: 'tip',  text: 'Gr 10' } },
              { text: 'Repetition Algorithms', link: '/practical/algorithms/repetition',      badge: { type: 'info', text: 'Gr 11' } },
              { text: 'Classic Problems',      link: '/practical/algorithms/classic-problems', badge: { type: 'info', text: 'Gr 11' } },
            ],
          },

          // ── Delphi Programming ────────────────────────────────────────
          {
            text: '🔵 Delphi Programming',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/practical/delphi/' },
              { text: 'Components & IDE',            link: '/practical/delphi/components',          badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Variables & Data Types',      link: '/practical/delphi/variables',           badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Operators',                   link: '/practical/delphi/operators',           badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Selection (IF / CASE)',        link: '/practical/delphi/selection',           badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'Loops (FOR / WHILE / REPEAT)',link: '/practical/delphi/loops',               badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'ShowMessage & Dialogs',       link: '/practical/delphi/showmessage',         badge: { type: 'tip',     text: 'Gr 10' } },
              { text: '1D Arrays',                   link: '/practical/delphi/arrays-1d',           badge: { type: 'info',    text: 'Gr 11' } },
              { text: '2D Arrays',                   link: '/practical/delphi/arrays-2d',           badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'String Functions',            link: '/practical/delphi/strings',             badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Math Methods',                link: '/practical/delphi/math-methods',        badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Input Validation',            link: '/practical/delphi/validation',          badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Procedures & Functions',      link: '/practical/delphi/procedures-functions', badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'Text Files',                  link: '/practical/delphi/text-files',          badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'OOP in Delphi',               link: '/practical/delphi/oop-delphi',          badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── SQL & Databases ───────────────────────────────────────────
          {
            text: '🗃️ SQL & Databases',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/practical/sql/' },
              { text: 'SELECT — Basics',         link: '/practical/sql/select-basics',      badge: { type: 'tip',     text: 'Gr 10' } },
              { text: 'SELECT — Advanced',       link: '/practical/sql/select-advanced',    badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'Multi-Table Queries',     link: '/practical/sql/joins',              badge: { type: 'info',    text: 'Gr 11' } },
              { text: 'INSERT / UPDATE / DELETE',link: '/practical/sql/data-manipulation',  badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'DDL (CREATE / ALTER / DROP)', link: '/practical/sql/ddl',            badge: { type: 'warning', text: 'Gr 12' } },
              { text: 'SQL in Delphi',           link: '/practical/sql/delphi-database',    badge: { type: 'warning', text: 'Gr 12' } },
            ],
          },

          // ── Number Systems ────────────────────────────────────────────
          {
            text: '🔢 Number Systems',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/practical/number-systems/' },
              { text: 'Binary',        link: '/practical/number-systems/binary',       badge: { type: 'tip',  text: 'Gr 10' } },
              { text: 'Hexadecimal',   link: '/practical/number-systems/hexadecimal',  badge: { type: 'info', text: 'Gr 11' } },
              { text: 'Data Sizes',    link: '/practical/number-systems/data-sizes',   badge: { type: 'info', text: 'Gr 11' } },
            ],
          },

        ],
      },

      // ══════════════════════════════════════════════════════════════════
      //  QUICK STUDY
      // ══════════════════════════════════════════════════════════════════
      {
        text: '⚡ Quick Study',
        collapsed: true,
        items: [
          {
            text: '📋 Theory Summaries',
            collapsed: false,
            items: [
              { text: 'Systems Technologies', link: '/quick-study/systems-summary' },
              { text: 'Networks',             link: '/quick-study/networks-summary' },
              { text: 'Internet Technologies',link: '/quick-study/internet-summary' },
              { text: 'Databases',            link: '/quick-study/databases-summary' },
              { text: 'Social Implications',  link: '/quick-study/social-summary' },
              { text: 'Number Conversion',    link: '/quick-study/number-conversion' },
            ],
          },
          {
            text: '💻 Practical Reference',
            collapsed: false,
            items: [
              { text: 'Delphi Syntax',         link: '/quick-study/delphi-syntax' },
              { text: 'String Functions',       link: '/quick-study/string-functions' },
              { text: 'SQL Cheat Sheet',        link: '/quick-study/sql-cheatsheet' },
              { text: 'Algorithms & Flowcharts',link: '/quick-study/algorithms-flowchart' },
            ],
          },
        ],
      },

      // ══════════════════════════════════════════════════════════════════
      //  DIGITAL TECHNOLOGY — Grades 8–9
      // ══════════════════════════════════════════════════════════════════
      {
        text: '🎓 Digital Technology (Gr 8–9)',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/digital-technology/' },
        ],
      },

    ],

    // ─── Search ───────────────────────────────────────────────────────────
    search: {
      provider: 'local',
    },

    // ─── Social / external links ──────────────────────────────────────────
    socialLinks: [
      { icon: 'github', link: 'https://github.com/MrCooksIT/it-gateway' },
    ],

    // ─── Footer ───────────────────────────────────────────────────────────
    footer: {
      message: 'IT Gateway — CAPS Information Technology for Grades 10–12',
      copyright: '© 2026 A. Coetzee · Marist Brothers College',
    },

    // ─── Doc footer nav ───────────────────────────────────────────────────
    docFooter: {
      prev: '← Previous',
      next: 'Next →',
    },
  },

  // ─── Markdown extensions ──────────────────────────────────────────────
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark',
    },
    lineNumbers: true,
  },
})
