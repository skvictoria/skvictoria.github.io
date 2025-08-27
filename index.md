---
layout: home
title: Home
---
<div id="top-right-buttons">
  <a href="{{ site.url }}/cv/#publications" class="top-button">
    <i class="fa fa-book icon-right-space"></i>Research
  </a>
  <a href="{{ site.url }}/teaching" class="top-button">
    <i class="fa fa-chalkboard-teacher icon-right-space"></i>Teaching
  </a>
  <a href="{{ site.url }}/coding" class="top-button">
    <i class="fa-solid fa-terminal"></i>Coding for fun
  </a>
</div>

<div id="intro-wrapper" class="l-text">
	<div id="intro-title-wrapper">
		<div id="intro-title-text-wrapper">
			<div id="intro-title-socials">
				{% for link in site.data.social-links %}
					{% if link.on-homepage == true %}
						{% include social-link.html link=link %}
					{% endif %}
				{% endfor %}
				<div id="everything-else" class="social-link">
					<a href="{{ site.url }}/cv"><div><i class="fa fa-portrait icon icon-right-space"></i>CV</div></a>
				</div>
			</div>
			<h1 id="intro-title">Hi! I'm Seulgi Kim  </h1>
		</div>
		<div id="intro-image-wrapper">
			<img id="intro-image" src="/images/seulgi.png">
		</div>
	</div>
	<!-- <div id="everything-else" class="l-middle">
		<a href="{{ site.url }}/cv"><div><i class="fa fa-portrait icon icon-right-space"></i>CV</div></a>
	</div> -->
	<div>
		My research aims to explain <b>Why</b> AI understands video. Specifically, I aim to advance <b>computer vision</b> and <b>multi-modal learning</b> algorithms to interpret temporal and semantic relations between human actions in long-term videos.
	</div>
	<div style="height: 1rem"></div>
	<div>
		I am a second year Ph.D. student at Georgia Tech, advised by <a href="https://alregib.ece.gatech.edu/">Ghassan AlRegib</a>.
		I received my B.S. from Seoul National University, where I was supported by <a href="https://www.hyundai-ngv.com/en/hrd/sub01.do">Hyundai Motor Group Research Scholarship</a>.
	</div>
	<div style="height: 1rem"></div>
	<div>
		Before joining Tech, I worked as a Research Engineer at Hyundai Motor Company for 3 years, where I developed AI models for perception and localization in autonomous driving. We launched <a href="https://youtu.be/0W69PArCRMU?si=Wz9GFV9O9ETwUw7W&t=81" target="_blank">Lv.4 Autonomous Driving Pilot Services</a> for RoboTaxi, RoboShuttle, and RoboTruck.
	</div>
</div>

<hr class="l-middle home-hr">

## Recent News

{::nomarkdown}
{% for degree in site.data.news %}
{% include cv/news.html degree=degree %}
{% endfor %}
{:/}

## Education

{::nomarkdown}
{% for degree in site.data.education %}
{% include cv/degree.html degree=degree %}
{% endfor %}
{:/}

<hr class="l-middle home-hr">
<h2 class="feature-title">Featured <a href="/cv/#publications">Research Publications</a></h2>

<!-- vertical spacing -->
<div style="height:10px"></div>

<div class="cover-wrapper cover-wrapper-3-col l-page">
	{% assign sortedPublications = site.categories.papers | sort: 'feature-order' %}
	{% for feature in sortedPublications %}
		{% if feature.featured == true %}
			{% include feature.html feature=feature %}
		{% endif %}
	{% endfor %}
</div>





<!-- [gt]: http://www.gatech.edu "Georgia Tech"
[cse]: http://cse.gatech.edu "Georgia Tech Computational Science and Engineering"
[coc]: http://www.cc.gatech.edu "Georgia Tech College of Computing"

[cv]: {{ site.url }}/cv
[polo]: http://www.cc.gatech.edu/~dchau/ "Polo Chau"
[poloclub]: http://poloclub.gatech.edu "Polo Club of Data Science" -->