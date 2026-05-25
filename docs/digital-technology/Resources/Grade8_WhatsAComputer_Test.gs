// ============================================================
//  GRADE 8 – "What's a Computer?" – 40 Mark Test
//  Google Apps Script — paste into script.google.com and Run
//  Topic coverage:
//    Section 1: Multiple Choice   (10 x 1 mark = 10)
//    Section 2: True/False        (10 x 1 mark = 10)  [with correction option]
//    Section 3: Match the Column  ( 5 x 1 mark =  5)  [drop-down matching]
//    Section 4: Short Answer      ( 5 x 3 marks = 15)
//  TOTAL: 40 marks
// ============================================================

function createGrade8ComputerTest() {

  var form = FormApp.create('Grade 8 – What\'s a Computer? (40 Marks)');
  form.setDescription(
    'Name: _______________________   Class: _______   Date: ___________\n\n' +
    'This test covers the history of computers, computer organisation, hardware and software.\n' +
    'Total: 40 marks. Answer ALL questions.'
  );
  form.setIsQuiz(true);
  form.setCollectEmail(false);

  // ============================================================
  //  SECTION 1 — MULTIPLE CHOICE (10 x 1 mark)
  // ============================================================

  form.addSectionHeaderItem()
    .setTitle('SECTION 1: Multiple Choice')
    .setHelpText('Choose the ONE best answer for each question. (10 x 1 mark = 10 marks)');

  // Q1
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle('1. Which of the following BEST defines a computer?')
    .setChoices([
      q1.createChoice('A device that can only browse the internet', false),
      q1.createChoice('A computing machine that performs calculations according to precise instructions', true),
      q1.createChoice('A physical machine made only of metal and silicon', false),
      q1.createChoice('A program that runs on a screen', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q2
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle('2. What was the FIRST computing device ever recorded in history?')
    .setChoices([
      q2.createChoice('The ENIAC', false),
      q2.createChoice('Charles Babbage\'s Analytical Engine', false),
      q2.createChoice('The Chinese Abacus (2600 BC)', true),
      q2.createChoice('The Turing Machine', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q3
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle('3. Moore\'s Law states that the processing speed of a computer should:')
    .setChoices([
      q3.createChoice('Double every 10 years', false),
      q3.createChoice('Double every 5 years', false),
      q3.createChoice('Double every 2 years', true),
      q3.createChoice('Stay constant over time', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q4
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle('4. A single binary digit (a 0 or a 1) is called a:')
    .setChoices([
      q4.createChoice('Byte', false),
      q4.createChoice('Bit', true),
      q4.createChoice('Megabyte', false),
      q4.createChoice('Nibble', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q5
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle('5. RAM (Random Access Memory) is best described as:')
    .setChoices([
      q5.createChoice('Permanent storage that keeps data even when power is off', false),
      q5.createChoice('External memory used to store music and files long-term', false),
      q5.createChoice('Fast, temporary memory that is lost when the computer is switched off', true),
      q5.createChoice('Read-only memory that stores the BIOS', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q6
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle('6. Which component is described as the "brain" of the computer that carries out program instructions?')
    .setChoices([
      q6.createChoice('The Motherboard', false),
      q6.createChoice('The RAM', false),
      q6.createChoice('The CPU (Central Processing Unit)', true),
      q6.createChoice('The Hard Drive', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q7
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle('7. Which of the following is an OUTPUT device?')
    .setChoices([
      q7.createChoice('Keyboard', false),
      q7.createChoice('Microphone', false),
      q7.createChoice('Scanner', false),
      q7.createChoice('Monitor', true)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q8
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle('8. A router is best described as:')
    .setChoices([
      q8.createChoice('A type of external storage device', false),
      q8.createChoice('The centre of a network that receives and routes data between computers', true),
      q8.createChoice('An input device that connects to a keyboard', false),
      q8.createChoice('A program that manages the operating system', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q9
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle('9. Which of the following is an example of SYSTEM software?')
    .setChoices([
      q9.createChoice('A web browser like Chrome', false),
      q9.createChoice('A word processor like Microsoft Word', false),
      q9.createChoice('The Windows or Mac operating system', true),
      q9.createChoice('A computer game', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // Q10
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle('10. In binary, a high voltage signal represents ___ and a low voltage signal represents ___.')
    .setChoices([
      q10.createChoice('0 and 1', false),
      q10.createChoice('1 and 0', true),
      q10.createChoice('True and False', false),
      q10.createChoice('On and Off only in ROM', false)
    ])
    .setRequired(true)
    .setPoints(1);

  // ============================================================
  //  SECTION 2 — TRUE / FALSE (10 x 1 mark)
  // ============================================================

  form.addSectionHeaderItem()
    .setTitle('SECTION 2: True or False')
    .setHelpText('State whether each statement is TRUE or FALSE. (10 x 1 mark = 10 marks)');

  var tfStatements = [
    {
      q: '11. The word "computer" was first used in 1613 to describe a PERSON who performed calculations.',
      answer: 'True'
    },
    {
      q: '12. The ENIAC (1946) was the first electronic general-purpose computer and could be reprogrammed for different tasks.',
      answer: 'True'
    },
    {
      q: '13. ROM (Read Only Memory) loses all its data when the computer is switched off.',
      answer: 'False'
    },
    {
      q: '14. Hardware refers to the programs and software that run on a computer.',
      answer: 'False'
    },
    {
      q: '15. A LAN (Local Area Network) connects computers that are very far apart across different cities.',
      answer: 'False'
    },
    {
      q: '16. Eight bits grouped together make one byte.',
      answer: 'True'
    },
    {
      q: '17. The motherboard connects all the different parts of the computer together and provides the clock signal for the CPU.',
      answer: 'True'
    },
    {
      q: '18. User application software is pre-installed on hardware and cannot be installed by the user.',
      answer: 'False'
    },
    {
      q: '19. A Wi-Fi card allows a computer to connect to a router by sending radio waves.',
      answer: 'True'
    },
    {
      q: '20. The operating system (OS) manages memory allocation, multitasking, and provides a graphical user interface.',
      answer: 'True'
    }
  ];

  tfStatements.forEach(function(item) {
    var tfItem = form.addMultipleChoiceItem();
    tfItem.setTitle(item.q)
      .setChoices([
        tfItem.createChoice('True',  item.answer === 'True'),
        tfItem.createChoice('False', item.answer === 'False')
      ])
      .setRequired(true)
      .setPoints(1);
  });

  // ============================================================
  //  SECTION 3 — MATCHING (5 x 1 mark)
  //  Implemented as drop-down questions
  // ============================================================

  form.addSectionHeaderItem()
    .setTitle('SECTION 3: Match the Column')
    .setHelpText(
      'Match each term (Column A) to the correct description (Column B) using the drop-down. (5 x 1 mark = 5 marks)\n\n' +
      'COLUMN B options:\n' +
      '  P – Stores data permanently; examples include USB drives and hard drives\n' +
      '  Q – Theoretical computing model that formed the foundation of computer science\n' +
      '  R – Software layer between user applications and hardware that makes the computer usable\n' +
      '  S – Physical components built into circuits that process binary signals\n' +
      '  T – Network that connects computers across very large distances using multiple routers'
    );

  var matchData = [
    { term: '21. Secondary Storage',  answer: 'P – Stores data permanently; examples include USB drives and hard drives' },
    { term: '22. The Turing Machine',  answer: 'Q – Theoretical computing model that formed the foundation of computer science' },
    { term: '23. Operating System',    answer: 'R – Software layer between user applications and hardware that makes the computer usable' },
    { term: '24. Logic Gates',         answer: 'S – Physical components built into circuits that process binary signals' },
    { term: '25. WAN (Wide Area Network)', answer: 'T – Network that connects computers across very large distances using multiple routers' }
  ];

  var allChoiceLabels = [
    'P – Stores data permanently; examples include USB drives and hard drives',
    'Q – Theoretical computing model that formed the foundation of computer science',
    'R – Software layer between user applications and hardware that makes the computer usable',
    'S – Physical components built into circuits that process binary signals',
    'T – Network that connects computers across very large distances using multiple routers'
  ];

  matchData.forEach(function(item) {
    var ddItem = form.addListItem();
    var choices = allChoiceLabels.map(function(label) {
      return ddItem.createChoice(label, label === item.answer);
    });
    ddItem.setTitle(item.term)
      .setChoices(choices)
      .setRequired(true)
      .setPoints(1);
  });

  // ============================================================
  //  SECTION 4 — SHORT ANSWER (5 x 3 marks)
  // ============================================================

  form.addSectionHeaderItem()
    .setTitle('SECTION 4: Short Answer')
    .setHelpText('Answer each question in 2–4 sentences. (5 x 3 marks = 15 marks)\n\nNOTE: Short answer questions are marked manually by the teacher.');

  var shortAnswers = [
    {
      q: '26. (3 marks) Explain the difference between RAM and ROM. In your answer, state ONE feature of each and give ONE example of what each stores.',
      hint: 'Suggested answer: RAM (Random Access Memory) is temporary — it stores currently running applications and data, but loses everything when power is off. ROM (Read Only Memory) is permanent — it cannot be written to, keeps data without power, and stores important information like the BIOS.'
    },
    {
      q: '27. (3 marks) Describe what an operating system does. Name TWO tasks it performs and give ONE example of a well-known operating system.',
      hint: 'Suggested answer: The OS manages user applications, handles memory allocation, enables multitasking, and provides a graphical user interface (GUI). Examples of OS: Windows, Mac OS, Linux.'
    },
    {
      q: '28. (3 marks) Explain the difference between an INPUT device and an OUTPUT device. Give ONE example of each and explain how each converts data.',
      hint: 'Suggested answer: Input devices take physical data from the outside world and convert it into digital data the computer can process (e.g. a keyboard or microphone). Output devices take digital data from inside the computer and convert it into physical information humans can understand (e.g. a monitor or printer).'
    },
    {
      q: '29. (3 marks) Why was the development of the ENIAC (1946) considered a major milestone in computing history? Mention at least TWO reasons in your answer.',
      hint: 'Suggested answer: The ENIAC was the first electronic general-purpose computer — unlike earlier machines it could be reprogrammed to compute different calculations. It was used by the military to calculate missile trajectories and proved that computers could be used for complex, varied tasks. It was also notable because its programmers were all women.'
    },
    {
      q: '30. (3 marks) Explain how the CPU, RAM, and Motherboard work TOGETHER when you click a button on your computer. Describe the role of each component in the process.',
      hint: 'Suggested answer: The motherboard connects all components and provides the clock signal that drives the CPU. When you click a button (input), an electrical signal is sent to the CPU. The CPU fetches the relevant instructions and data from RAM, performs the required calculations on each clock cycle, and sends the result to the appropriate output device. RAM temporarily holds the running application and its data so the CPU can access it quickly.'
    }
  ];

  shortAnswers.forEach(function(item) {
    var saItem = form.addParagraphTextItem();
    saItem.setTitle(item.q)
      .setHelpText(item.hint)
      .setRequired(true);
    // Short answer questions are not auto-graded in Google Forms
  });

  // ============================================================
  //  DONE — Log the form URL
  // ============================================================

  var url = form.getPublishedUrl();
  Logger.log('✅ Form created successfully!');
  Logger.log('📋 Form URL (share with students): ' + url);
  Logger.log('✏️  Edit URL (for you): ' + form.getEditUrl());
  Logger.log('');
  Logger.log('REMINDER: Section 4 short answer questions (Q26–Q30) must be marked manually.');
  Logger.log('Total auto-markable: 25 marks | Manually marked: 15 marks | Grand total: 40 marks');
}
