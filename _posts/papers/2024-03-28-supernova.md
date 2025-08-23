---
layout: paper
id: supernova
categories: papers
permalink: papers/supernova
title: "SuperNOVA: Design Strategies and Opportunities for Interactive Visualization in Computational Notebooks"
authors: 
  - Zijie J. Wang
  - David Munechika
  - Seongmin Lee
  - Duen Horng (Polo) Chau
venue: Extended Abstracts on ACM Human Factors in Computing Systems
venue-shorthand: CHI
year: 2024
url: /papers/supernova
pdf: https://arxiv.org/pdf/2305.03039
code: https://github.com/poloclub/supernova
code-star: 62
demo: https://poloclub.github.io/supernova/
selected: false
type: preprint
figure: /images/papers/23-supernova.webp
image: /images/papers/23-supernova.png
featured: false
bibtex: |-

  @article{wangSuperNOVADesignStrategies2023,
    title = {{{SuperNOVA}}: {{Design Strategies}} and {{Opportunities}} for {{Interactive Visualization}} in {{Computational Notebooks}}},
    shorttitle = {{{SuperNOVA}}},
    author = {Wang, Zijie J. and Munechika, David and Lee, Seongmin and Chau, Duen Horng},
    year = {2024},
    url = {http://arxiv.org/abs/2305.03039},
    booktitle = {Extended {{Abstracts}} of the 2022 {{CHI Conference}} on {{Human Factors}} in {{Computing Systems}}},
    publisher = {{ACM}}
  }
---

Computational notebooks such as Jupyter Notebook have become data scientists' de facto programming environments. Many visualization researchers and practitioners have developed interactive visualization tools that support notebooks. However, little is known about the appropriate design of visual analytics (VA) tools in notebooks. To bridge this critical research gap, we investigate the design strategies in this space by analyzing 159 notebook VA tools and their users' feedback. Our analysis encompasses 62 systems from academic papers and 103 systems sourced from a pool of 55k notebooks containing interactive visualizations that we obtain via scraping 8.6 million notebooks on GitHub. We also examine findings from 15 user studies and user feedback in 379 GitHub issues. Through this work, we identify unique design opportunities and considerations for future notebook VA tools, such as using and manipulating multimodal data in notebooks as well as balancing the degree of visualization-notebook integration. Finally, we develop SuperNOVA, an open-source interactive tool to help researchers explore existing notebook VA tools and search for related work.