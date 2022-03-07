import React from 'react';
import clsx from 'clsx';
import styles from './HomepageSearch.module.css';

export default function HomepageSearch() {
  return (
  <section class="hero container">
    <div class="hero container">
      <div class="hero__title">
        <h1 class="hero__title">搜索文档中的任何内容</h1>
        <div class="row justify-content-center">
      <form action="/search/" method="get" class="col-xs-8 col-sm-offset-6 col-sm-6 col-md-offset-6 col-md-6 col-lg-offset-6 col-lg-4">
        <input
          id="st-search-input"
          class="form-control"
          name="q"
          placeholder="安装, 账号密码，维护等"
          type="search"
          autocomplete="off"
          spellcheck="false"
          dir="auto"
          autofocus
        />
        <div id="autocompleteResults"></div>
      </form>
    </div>
      </div>
    </div>
    
  </section>  );
}