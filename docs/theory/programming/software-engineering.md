# Software Engineering

Building a small program is straightforward. Building software used by millions of people, that must be maintained for decades, that must be secure, fast, and correct — that requires engineering. Software engineering applies systematic, disciplined approaches to developing software.

> [!NOTE] Grade 12
> Software engineering methodologies (Waterfall, Agile, RAD) are primarily Grade 12 content, linked to PAT preparation.

---

## What is Software Engineering?

**Software engineering** is the application of engineering principles to the design, development, testing, and maintenance of software systems.

It addresses:
- How to organise large development teams
- How to manage changing requirements
- How to ensure quality at scale
- How to deliver on time and budget

---

## The Software Development Life Cycle (SDLC)

The **SDLC** is the structured process for planning, creating, testing, and deploying software.

```
1. Requirements analysis
       ↓
2. System design
       ↓
3. Implementation (coding)
       ↓
4. Testing
       ↓
5. Deployment
       ↓
6. Maintenance
```

### Phase Details

| Phase | Activities | Output |
|---|---|---|
| **Requirements** | Gather user needs; document what system must do | Requirements specification |
| **Design** | Architecture, database design, interface design | Design documents, ERDs |
| **Implementation** | Write code | Source code |
| **Testing** | Find and fix errors; verify requirements met | Test results, bug reports |
| **Deployment** | Install and release to users | Running system |
| **Maintenance** | Fix bugs, add features, improve performance | Updated software |

---

## Development Methodologies

A **methodology** is a structured approach to software development — it defines who does what, when, and how.

---

## Waterfall Model

The **Waterfall model** is a sequential, linear development process — each phase must be complete before the next begins.

```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
```

No going back — like water falling; once you've passed a phase, you don't return.

### Advantages of Waterfall
- Simple and easy to understand
- Clear milestones and deliverables
- Good documentation — each phase has defined outputs
- Works well when requirements are clear and fixed
- Easy to manage — clear phase progression

### Disadvantages of Waterfall
- Very rigid — difficult to accommodate changing requirements
- Testing happens late — bugs found at the end are expensive to fix
- Client sees no working software until near the end
- High risk — if design is wrong, everything built on it is wrong
- Poor for complex, long-term projects where requirements change

### When to use Waterfall:
- Small, well-defined projects
- Requirements are completely clear and unlikely to change
- Regulated industries (medical devices, aerospace) requiring documentation

---

## Agile Methodology

**Agile** is an iterative, flexible approach where software is developed in short cycles called **sprints** (usually 1–4 weeks).

```
Plan → Design → Build → Test → Review → (repeat)
         ↑________________________________↓
                  Sprint cycle
```

After each sprint, a working piece of software is delivered and reviewed. Requirements can change between sprints.

**Agile values (Agile Manifesto):**
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

### Advantages of Agile
- Flexible — requirements can change throughout development
- Client sees working software frequently (after each sprint)
- Bugs found early — testing in every sprint
- High client satisfaction — continuous collaboration
- Reduced risk — problems identified early

### Disadvantages of Agile
- Less predictable — hard to estimate total cost and time upfront
- Requires constant client involvement
- Less documentation — can be problematic for maintenance
- Can lose sight of overall architecture
- Not suitable for fixed-scope contracts

### Scrum (Agile Framework)
**Scrum** is the most popular Agile framework:
- **Product backlog** — prioritised list of all features
- **Sprint backlog** — tasks committed to for this sprint
- **Daily standup** — 15-minute team meeting
- **Sprint review** — demo working software to stakeholders
- **Sprint retrospective** — team reflects on how to improve

**Scrum roles:**
- **Product Owner** — represents client; prioritises features
- **Scrum Master** — facilitates process; removes obstacles
- **Development Team** — builds the software

---

## RAD — Rapid Application Development

**RAD** is a methodology focused on delivering software quickly through:
- Prototyping — build rough working versions early
- Heavy user involvement in prototype review
- Iterative refinement until final product

```
Requirements planning → User design → Rapid construction → Cutover
       ↑________________________↓
           Prototype cycles
```

### Advantages of RAD
- Very fast development
- Users see and interact with prototypes early
- Reduced risk — problems caught during prototyping
- Good for projects where speed is critical

### Disadvantages of RAD
- Requires committed, available users throughout
- Not suitable for large teams
- Performance issues may be overlooked in rush to deliver
- Poor for complex system integrations

---

## Methodology Comparison

| Feature | Waterfall | Agile | RAD |
|---|---|---|---|
| Approach | Sequential | Iterative | Prototype-based |
| Flexibility | Low | High | Medium |
| Client involvement | At start and end | Continuous | Continuous |
| Testing | End of project | Every sprint | During prototyping |
| Documentation | Extensive | Minimal | Moderate |
| Suitable for | Fixed, clear requirements | Changing requirements | Fast delivery |
| Risk | High (late testing) | Low (early feedback) | Medium |
| Team size | Any | Small-medium | Small |

---

## Software Quality Attributes

| Attribute | Meaning |
|---|---|
| **Correctness** | Does what it's supposed to do |
| **Reliability** | Works consistently without failure |
| **Efficiency** | Uses minimal resources (CPU, memory) |
| **Maintainability** | Easy to update and modify |
| **Usability** | Easy for users to learn and use |
| **Portability** | Works on different platforms |
| **Security** | Protected against attacks and unauthorised access |
| **Scalability** | Handles increased load without performance loss |

---

## PAT — Practical Assessment Task

The **PAT** is a major component of Grade 12 IT assessment (25% of final mark).

**PAT phases:**
| Phase | What it covers |
|---|---|
| **Phase 1** | Requirements, system design (ERDs, class diagrams, interface design) |
| **Phase 2** | Coding — implement the designed system in Delphi |
| **Phase 3** | Testing — test plans, test results, evidence of testing |

**Documentation required:**
- Project plan with milestones
- System requirements specification
- ERD and database design
- Class diagrams (OOP)
- Interface mockups
- Source code
- Test plan with test data
- Test results

**PAT relates to:**
- Software engineering (design documentation)
- OOP (class design)
- Database design (ERD, normalisation)
- SQL (queries in Delphi)
- Algorithms (problem-solving)

---

## Version Control

**Version control** systems track changes to code over time, allowing teams to collaborate and revert to earlier versions.

| Feature | Benefit |
|---|---|
| **History** | See every change ever made and who made it |
| **Branching** | Work on features in isolation; merge when ready |
| **Rollback** | Revert to any previous version |
| **Collaboration** | Multiple developers work on the same codebase |

**Git** is the most widely used version control system.  
**GitHub** is a hosting platform for Git repositories.

---

## Key Terms

| Term | Definition |
|---|---|
| **SDLC** | Software Development Life Cycle — structured software development process |
| **Waterfall** | Sequential development methodology — one phase at a time |
| **Agile** | Iterative methodology delivering working software in short sprints |
| **Sprint** | Short development cycle (1–4 weeks) in Agile |
| **RAD** | Rapid Application Development — fast prototyping-based methodology |
| **Prototype** | Early working version of software for feedback |
| **Scrum** | Popular Agile framework with sprints and specific roles |
| **PAT** | Practical Assessment Task — Grade 12 major project |
| **Version control** | System tracking changes to code over time |
| **Maintenance** | Ongoing updates, bug fixes, and improvements after deployment |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Compare Waterfall and Agile methodologies — give TWO advantages of each"** — Waterfall: clear documentation, simple management, good for fixed requirements; Agile: flexible to changing requirements, client sees working software frequently, bugs found early
>
> 2. **"Give TWO disadvantages of the Waterfall model"** — very rigid, difficult to change requirements; testing only at the end means bugs discovered late (expensive); client sees no working software until near the end
>
> 3. **"What is a sprint in Agile? How long is it typically?"** — A short development cycle delivering a working piece of software; typically 1–4 weeks
>
> 4. **"Give THREE phases of the SDLC"** — requirements analysis; design; implementation; testing; deployment; maintenance
>
> 5. **"Why is Agile more suitable than Waterfall for a project where client requirements may change frequently?"** — Agile accommodates changing requirements between sprints; clients are involved throughout; working software delivered after each sprint so changes can be incorporated; Waterfall requires fixed requirements from the start
