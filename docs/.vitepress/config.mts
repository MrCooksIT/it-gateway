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
      { text: '🏠 Home', link: '/' },
      { text: '📚 Theory', link: '/theory/' },
      { text: '💻 Practical', link: '/practical/' },
      { text: '⚡ Quick Study', link: '/quick-study/' },
      {
        text: 'More',
        items: [
          { text: 'Google Classroom', link: 'https://classroom.google.com' },
          { text: 'About this site', link: '/about' },
        ],
      },
    ],

    // ─── Sidebar ──────────────────────────────────────────────────────────
    sidebar: {

      // ── THEORY ────────────────────────────────────────────────────────
      '/theory/': [
        {
          text: '🖥️ Systems Technologies',
          collapsed: false,
          items: [
            { text: 'Topic overview', link: '/theory/systems/' },
            { text: 'What is Computing?', link: '/theory/systems/what-is-computing' },
            { text: 'Hardware', link: '/theory/systems/hardware' },
            { text: 'Peripherals & Devices', link: '/theory/systems/peripherals' },
            { text: 'Computer Performance', link: '/theory/systems/performance' },
            { text: 'Types of Computers', link: '/theory/systems/types-of-computers' },
            { text: 'Mobile Technologies', link: '/theory/systems/mobile-tech' },
            { text: 'Software', link: '/theory/systems/software' },
            { text: 'OS & File Management', link: '/theory/systems/os-management' },
            { text: 'Data Representation', link: '/theory/systems/data-representation' },
            { text: 'Cloud & Virtualisation', link: '/theory/systems/cloud-virtualisation' },
          ],
        },
        {
          text: '🌐 Communication Technologies',
          collapsed: true,
          items: [
            { text: 'Topic overview', link: '/theory/networks/' },
            { text: 'Network Concepts', link: '/theory/networks/network-concepts' },
            { text: 'Types of Networks', link: '/theory/networks/network-types' },
            { text: 'Network Hardware', link: '/theory/networks/network-hardware' },
            { text: 'Network Topologies', link: '/theory/networks/topologies' },
            { text: 'Protocols', link: '/theory/networks/protocols' },
            { text: 'Wireless Technologies', link: '/theory/networks/wireless' },
            { text: 'Network Security', link: '/theory/networks/network-security' },
            { text: 'E-Communication', link: '/theory/networks/e-communication' },
          ],
        },
        {
          text: '🌍 Internet Technologies',
          collapsed: true,
          items: [
            { text: 'Topic overview', link: '/theory/internet/' },
            { text: 'The Internet & WWW', link: '/theory/internet/internet-www' },
            { text: 'Web Evolution (1.0–3.0)', link: '/theory/internet/web-evolution' },
            { text: 'Internet Services', link: '/theory/internet/internet-services' },
            { text: 'Multimedia & Streaming', link: '/theory/internet/multimedia' },
            { text: 'Website Design', link: '/theory/internet/website-design' },
            { text: 'HTML Basics', link: '/theory/internet/html-basics' },
            { text: 'Web Scripting', link: '/theory/internet/web-scripting' },
            { text: 'Online Services & Cookies', link: '/theory/internet/online-services' },
          ],
        },
        {
          text: '🗄️ Data & Information Management',
          collapsed: true,
          items: [
            { text: 'Topic overview', link: '/theory/databases/' },
            { text: 'Data Concepts', link: '/theory/databases/data-concepts' },
            { text: 'Database Concepts', link: '/theory/databases/database-concepts' },
            { text: 'Database Design & ERDs', link: '/theory/databases/database-design' },
            { text: 'Normalisation', link: '/theory/databases/normalisation' },
            { text: 'Data Integrity & Security', link: '/theory/databases/data-integrity' },
            { text: 'SQL — Theory', link: '/theory/databases/sql-theory' },
            { text: 'DBMS Software & Roles', link: '/theory/databases/dbms-software' },
          ],
        },
        {
          text: '⚖️ Social Implications',
          collapsed: true,
          items: [
            { text: 'Topic overview', link: '/theory/social/' },
            { text: 'Copyright & Licensing', link: '/theory/social/copyright' },
            { text: 'Cybercrime', link: '/theory/social/cybercrime' },
            { text: 'Online Safety', link: '/theory/social/online-safety' },
            { text: 'Privacy & Ethics', link: '/theory/social/privacy-ethics' },
            { text: 'Digital Divide', link: '/theory/social/digital-divide' },
            { text: 'Environment & Society', link: '/theory/social/environment-society' },
          ],
        },
        {
          text: '💡 Solution Development (Theory)',
          collapsed: true,
          items: [
            { text: 'Topic overview', link: '/theory/programming/' },
            { text: 'Programming Concepts', link: '/theory/programming/programming-concepts' },
            { text: 'Algorithms (Theory)', link: '/theory/programming/algorithms-theory' },
            { text: 'OOP Principles', link: '/theory/programming/oop-principles' },
            { text: 'Software Engineering', link: '/theory/programming/software-engineering' },
          ],
        },
      ],

      // ── PRACTICAL ─────────────────────────────────────────────────────
      '/practical/': [
        {
          text: '📐 Algorithms',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/practical/algorithms/' },
            { text: 'Sequential Algorithms', link: '/practical/algorithms/sequential' },
            { text: 'Decision Algorithms', link: '/practical/algorithms/decision' },
            { text: 'Repetition Algorithms', link: '/practical/algorithms/repetition' },
            { text: 'Classic Problems', link: '/practical/algorithms/classic-problems' },
          ],
        },
        {
          text: '🔵 Delphi Programming',
          collapsed: false,
          items: [
            { text: 'Delphi overview', link: '/practical/delphi/' },
            { text: 'Components & IDE', link: '/practical/delphi/components' },
            { text: 'Variables & Data Types', link: '/practical/delphi/variables' },
            { text: 'Operators', link: '/practical/delphi/operators' },
            { text: 'Selection (IF / CASE)', link: '/practical/delphi/selection' },
            { text: 'Loops (FOR / WHILE / REPEAT)', link: '/practical/delphi/loops' },
            { text: '1D Arrays', link: '/practical/delphi/arrays-1d' },
            { text: '2D Arrays', link: '/practical/delphi/arrays-2d' },
            { text: 'String Functions', link: '/practical/delphi/strings' },
            { text: 'Math Methods', link: '/practical/delphi/math-methods' },
            { text: 'Input Validation', link: '/practical/delphi/validation' },
            { text: 'Procedures & Functions', link: '/practical/delphi/procedures-functions' },
            { text: 'Text Files', link: '/practical/delphi/text-files' },
            { text: 'ShowMessage & Dialogs', link: '/practical/delphi/showmessage' },
            { text: 'OOP in Delphi', link: '/practical/delphi/oop-delphi' },
          ],
        },
        {
          text: '🗃️ SQL & Databases',
          collapsed: true,
          items: [
            { text: 'SQL overview', link: '/practical/sql/' },
            { text: 'SELECT Basics', link: '/practical/sql/select-basics' },
            { text: 'SELECT Advanced', link: '/practical/sql/select-advanced' },
            { text: 'JOINs', link: '/practical/sql/joins' },
            { text: 'INSERT / UPDATE / DELETE', link: '/practical/sql/data-manipulation' },
            { text: 'CREATE TABLE (DDL)', link: '/practical/sql/ddl' },
            { text: 'Databases in Delphi', link: '/practical/sql/delphi-database' },
          ],
        },
        {
          text: '🔢 Number Systems',
          collapsed: true,
          items: [
            { text: 'Overview', link: '/practical/number-systems/' },
            { text: 'Binary', link: '/practical/number-systems/binary' },
            { text: 'Hexadecimal', link: '/practical/number-systems/hexadecimal' },
            { text: 'Data Sizes', link: '/practical/number-systems/data-sizes' },
          ],
        },
      ],

      // ── QUICK STUDY ───────────────────────────────────────────────────
      '/quick-study/': [
        {
          text: '📋 Theory Summaries',
          collapsed: false,
          items: [
            { text: '🖥️ Systems Technologies', link: '/quick-study/systems-summary' },
            { text: '🌐 Networks', link: '/quick-study/networks-summary' },
            { text: '🌍 Internet Technologies', link: '/quick-study/internet-summary' },
            { text: '🗄️ Databases', link: '/quick-study/databases-summary' },
            { text: '⚖️ Social Implications', link: '/quick-study/social-summary' },
            { text: '🔢 Number Conversion', link: '/quick-study/number-conversion' },
          ],
        },
        {
          text: '💻 Practical Reference',
          collapsed: false,
          items: [
            { text: 'Delphi Syntax', link: '/quick-study/delphi-syntax' },
            { text: 'String Functions', link: '/quick-study/string-functions' },
            { text: 'SQL Cheat Sheet', link: '/quick-study/sql-cheatsheet' },
            { text: 'Algorithms & Flowcharts', link: '/quick-study/algorithms-flowchart' },
          ],
        },
      ],
    },

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
