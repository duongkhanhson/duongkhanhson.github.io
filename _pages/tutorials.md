---
title: "Hướng Dẫn & Knowledge (Tutorials)"
permalink: /tutorials/
layout: single
author_profile: true
---

<h2>Tiếng Việt</h2>
<p>Chào mừng đến với danh mục Hướng dẫn & Phân tích chuyên sâu về lộ trình Kỹ thuật Cơ điện tử 4.0.</p>
<h2>English</h2>
<p>Welcome to the Tutorials section, featuring in‑depth guides and analyses on the Mechatronics 4.0 curriculum.</p>

<div class="entries-list">
  {% for post in site.categories.Tutorials %}
      <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        <h2 class="archive__item-title" itemprop="headline">
          <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.title }}</a>
        </h2>
        <p class="page__meta">
          <i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%d/%m/%Y" }}
        </p>
        <p class="archive__item-excerpt" itemprop="description">{{ post.content | strip_html | truncate: 250 }}</p>
      </article>
  {% endfor %}
</div>
