---
layout: paper
id: clickdiffusion
categories: papers
permalink: papers/clickdiffusion
title: "ClickDiffusion: Harnessing LLMs for Interactive Precise Image Editing"
authors: 
  - Alec Helbling
  - Seongmin Lee
  - Duen Horng (Polo) Chau
venue: CVPR 2024 Workshop on AI for Content Creation Workshop
venue-shorthand: CVPR
year: 2024
url: /papers/clickdiffusion
pdf: https://arxiv.org/pdf/2404.04376
code: https://github.com/poloclub/ClickDiffusion
code-star: 65
selected: false
featured: false
bibtex: |-

  @article{helbling2024clickdiffusion,
    title={{ClickDiffusion}: Harnessing LLMs for Interactive Precise Image Editing},
    author={Helbling, Alec and Lee, Seongmin and Chau, Polo},
    journal={arXiv preprint arXiv:2404.04376},
    year={2024}
  }
---

Recently, researchers have proposed powerful systems for generating and manipulating images using natural language instructions. However, it is difficult to precisely specify many common classes of image transformations with text alone. For example, a user may wish to change the location and breed of a particular dog in an image with several similar dogs. This task is quite difficult with natural language alone, and would require a user to write a laboriously complex prompt that both disambiguates the target dog and describes the destination. We propose ClickDiffusion, a system for precise image manipulation and generation that combines natural language instructions with visual feedback provided by the user through a direct manipulation interface. We demonstrate that by serializing both an image and a multi-modal instruction into a textual representation it is possible to leverage LLMs to perform precise transformations of the layout and appearance of an image. Code available at https://github.com/poloclub/ClickDiffusion.
