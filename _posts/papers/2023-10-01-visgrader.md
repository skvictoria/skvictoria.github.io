---
layout: paper
id: visgrader
categories: papers
permalink: papers/visgrader
title: "VisGrader: Automatic Grading of D3 Visualizations"
authors: 
  - Matthew Hull
  - Vivian Pednekar
  - Hannah Murray
  - Nimisha Roy
  - Emmanuel Tung
  - Susanta Routray
  - Connor Guerin
  - Justin Chen
  - Zijie J. Wang
  - Seongmin Lee
  - Mahdi Roozbahani
  - Duen Horng (Polo) Chau
venue: Full Paper, IEEE Visualization and Visual Analytics
venue-shorthand: VIS
year: 2023
url: /papers/visgrader
pdf: https://arxiv.org/pdf/2310.12347.pdf
code: https://github.com/poloclub/visgrader
selected: false
type: conference
figure: /images/papers/23-visgrader.png
featured: false
feature-order: 1
feature-title: VisGrader
feature-description: Automatic grading method for D3 visualizations
bibtex: |-

  @article{hull2023visgrader,
    title={VISGRADER: Automatic Grading of D3 Visualizations},
    author={Hull, Matthew and Pednekar, Vivian and Murray, Hannah and Roy, Nimisha and Tung, Emmanuel and Routray, Susanta and Guerin, Connor and Chen, Justin and Wang, Zijie J and Lee, Seongmin and others},
    journal={IEEE Transactions on Visualization and Computer Graphics},
    year={2023},
    publisher={IEEE}
  }
---

Manually grading D3 data visualizations is a challenging endeavor, and is especially difficult for large classes with hundreds of students. Grading an interactive visualization requires a combination of interactive, quantitative, and qualitative evaluation that are conventionally done manually and are difficult to scale up as the visualization complexity, data size, and number of students increase. We present VisGrader, a first-of-its kind automatic grading method for D3 visualizations that scalably and precisely evaluates the data bindings, visual encodings, interactions, and design specifications used in a visualization. Our method enhances students’ learning experience, enabling them to submit their code frequently and receive rapid feedback to better inform iteration and improvement to their code and visualization design. We have successfully deployed our method and auto-graded D3 submissions from more than 4000 students in a visualization course at Georgia Tech, and received positive feedback for expanding its adoption.
