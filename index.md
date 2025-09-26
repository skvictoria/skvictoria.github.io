---
layout: home
title: Home
---
<div id="top-right-buttons">
  <a href="{{ site.url }}/#" class="top-button">Research</a>
  <a href="{{ site.url }}/#" class="top-button">Teaching</a>
  <a href="{{ site.url }}/#" class="top-button">Hobby</a>
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

<hr class="l-middle home-hr">
<h2 class="feature-title">Featured Research Publications</h2>

<div style="height:10px"></div>

<div class="cover-wrapper cover-wrapper-3-col l-page">
	{% assign sortedPublications = site.categories.papers | sort: 'feature-order' %}
	{% for feature in sortedPublications %}
		{% if feature.featured == true %}
			{% include feature.html feature=feature %}
		{% endif %}
	{% endfor %}
</div>

## Education
{::nomarkdown}
{% for degree in site.data.education %}
{% include cv/degree.html degree=degree %}
{% endfor %}
{:/}

## Work Experience
{% for experience in site.data.experiences %}
{% if experience.type == 'industry' %}
{% include cv/experience.html experience=experience %}
{% endif %}
{% endfor %}

## Publications
{% assign selectedBoolForBibtex = false %}
{% for pub in site.categories.papers %}
{% include cv/publication.html pub=pub selectedBoolForBibtex=selectedBoolForBibtex %}
{% endfor %}

## Teaching
{% for teach in site.data.teaching %}
{% include cv/teaching.html teach=teach %}
{% endfor %}

## Honors and Awards
{% for award in site.data.awards %}
{% include cv/award.html award=award %}
{% endfor %}

## Patent
{% for patent in site.data.patents %}
{% include cv/patent.html patent=patent %}
{% endfor %}

## Service
<div class="cv-service-title"><b>Reviewer</b></div>
{% for venue in site.data.reviewer %}
{% include cv/venue.html venue=venue %}
{% endfor %}

<div class="cv-service-title"><b>Member</b></div>
{% for member in site.data.memberships %}
{% include cv/member.html member=member %}
{% endfor %}

## Skills
{% for skill in site.data.skills %}
{% include cv/skill.html skill=skill %}
{% endfor %}

## Book
{% for book in site.data.books %}
{% include cv/book.html book=book %}
{% endfor %}

## References
{% for reference in site.data.references %}
{% include cv/reference.html reference=reference %}
{% endfor %}