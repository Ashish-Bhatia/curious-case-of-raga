"use strict";
const menu=document.querySelector('#menu'),nav=document.querySelector('#nav');nav.hidden=true;menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.hidden=!open;});nav.addEventListener('click',e=>{if(e.target.closest('a')){nav.hidden=true;menu.setAttribute('aria-expanded','false');}});document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.hidden=true;menu.setAttribute('aria-expanded','false');menu.focus();}});
let scope='';
const articles=[...document.querySelectorAll('article')],search=document.querySelector('#search'),topic=document.querySelector('#topic'),order=document.querySelector('#order');document.querySelector('.tools').hidden=false;
function filter(){const q=search.value.trim().toLowerCase();let n=0;articles.sort((a,b)=>order.value==='newest'?b.dataset.date.localeCompare(a.dataset.date):a.dataset.date.localeCompare(b.dataset.date)).forEach(a=>{a.hidden=!(a.textContent.toLowerCase().includes(q)&&(!topic.value||topic.value===a.dataset.topic)&&(!scope||a.querySelector('.article-top').textContent.includes(scope)));if(!a.hidden)n++;document.querySelector('#articles').append(a);});document.querySelector('#count').textContent=`${n} of ${articles.length} checks · Statement or source dates shown below · Reviewed 18 October 2026 (IST)`;document.querySelector('#empty').hidden=n!==0;}
search.addEventListener('input',filter);topic.addEventListener('change',filter);order.addEventListener('change',filter);
function openLinked(){const id=decodeURIComponent(location.hash.slice(1));const a=articles.find(x=>x.id===id);if(a){search.value='';topic.value='';scope='';syncScope();filter();a.querySelector('details').open=true;a.scrollIntoView();}}window.addEventListener('hashchange',openLinked);if(location.hash)openLinked();

const scopeButtons=[...document.querySelectorAll('[data-scope]')];
function syncScope(){document.querySelectorAll('[data-scope]').forEach(b=>{const active=b.dataset.scope===scope;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});}
document.querySelector('.scope').hidden=false;
scopeButtons.forEach(b=>b.addEventListener('click',()=>{scope=b.dataset.scope;syncScope();filter();}));
document.addEventListener('click',e=>{if(!nav.hidden&&!nav.contains(e.target)&&!menu.contains(e.target)){nav.hidden=true;menu.setAttribute('aria-expanded','false');}});
function progress(){const max=document.documentElement.scrollHeight-innerHeight;document.querySelector('#reading-progress').style.width=(max>0?scrollY/max*100:0)+'%';}addEventListener('scroll',progress,{passive:true});addEventListener('resize',progress);progress();
