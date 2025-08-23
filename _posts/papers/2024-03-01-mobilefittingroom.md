---
layout: paper
id: mobilefittingroom
categories: papers
permalink: papers/mobilefittingroom
title: "Mobile Fitting Room: On-device Virtual Try-on via Diffusion Models"
authors: 
  - Justin Blalock
  - David Munechika
  - Harsha Karanth
  - Alec Helbling
  - Pratham Mehta
  - Seongmin Lee
  - Duen Horng (Polo) Chau
venue: CVPR 24 Workshop on Virtual Try-On
venue-shorthand: CVPR
year: 2024
url: /papers/mobilefittingroom
pdf: https://arxiv.org/abs/2402.01877
selected: false
featured: false
bibtex: |-

  @article{blalock2024mobile,
    title={{Mobile Fitting Room: On-device Virtual Try-on via Diffusion Models}},
    author={Blalock, Justin and Munechika, David and Karanth, Harsha and Helbling, Alec and Mehta, Pratham and Lee, Seongmin and Chau, Duen Horng},
    journal={arXiv preprint arXiv:2402.01877},
    year={2024}
  }
---

Recently, researchers have proposed powerful systems for generating and manipulating images using natural language instructions. However, it is difficult to precisely specify many common classes of image transformations with text alone. For example, a user may wish to change the location and breed of a particular dog in an image with several similar dogs. This task is quite difficult with natural language alone, and would require a user to write a laboriously complex prompt that both disambiguates the target dog and describes the destination. We propose ClickDiffusion, a system for precise image manipulation and generation that combines natural language instructions with visual feedback provided by the user through a direct manipulation interface. We demonstrate that by serializing both an image and a multi-modal instruction into a textual representation it is possible to leverage LLMs to perform precise transformations of the layout and appearance of an image. Code available at https://github.com/poloclub/ClickDiffusion.
