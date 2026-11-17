const {test} = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const dist = path.join(__dirname, '../dist');
const code = fs.readFileSync(path.join(dist, 'language.js'), 'utf8');
function visit({languages=[], language='', saved=null, pathname='/', basePath='/', blocked=false}={}) {
  const result={redirect:null,saved};
  vm.runInNewContext(code, {
    URL,
    navigator:{languages,language},
    location:{pathname,search:'?ref=portfolio',hash:'#projetos',replace:url=>result.redirect=url},
    localStorage:{getItem(){if(blocked)throw Error('blocked');return saved},setItem(k,v){if(blocked)throw Error('blocked');result.saved=v}},
    document:{currentScript:{src:'https://example.com'+basePath+'language.js'},addEventListener(type,fn){result.click=fn}}
  });
  return result;
}
test('browser variants and ordered preferences',()=>{
  for(const [languages,expected] of [[['pt-BR'],'pt'],[['es-ES'],'es'],[['en-US','pt'],'en'],[['fr-FR','es-MX'],'es'],[['de'],'en'],[[],'en']])
    assert.equal(visit({languages}).redirect,`/${expected}/?ref=portfolio#projetos`);
  assert.equal(visit({language:'pt-PT'}).redirect,'/pt/?ref=portfolio#projetos');
});
test('saved choice takes priority; invalid preference is ignored',()=>{
  assert.equal(visit({saved:'es',languages:['en-US']}).redirect,'/es/?ref=portfolio#projetos');
  assert.equal(visit({saved:'invalid',languages:['pt']}).redirect,'/pt/?ref=portfolio#projetos');
});
test('explicit links do not redirect or overwrite preference',()=>{
  for(const pathname of ['/en/','/es/','/pt/']) {
    const r=visit({pathname,saved:'en',languages:['es']});
    assert.equal(r.redirect,null);assert.equal(r.saved,'en');
  }
});
test('manual selection persists; disabled storage does not break navigation',()=>{
  const r=visit({pathname:'/en/'});
  r.click({target:{closest:()=>({getAttribute:()=> 'pt'})}});
  assert.equal(r.saved,'pt');
  const blocked=visit({blocked:true,languages:['es']});
  assert.equal(blocked.redirect,'/es/?ref=portfolio#projetos');
  assert.doesNotThrow(()=>blocked.click({target:{closest:()=>({getAttribute:()=> 'en'})}}));
});
test('root is English without JS; locale assets and language links resolve',()=>{
  for(const route of ['','pt','en','es']){
    const file=path.join(dist,route,'index.html');const html=fs.readFileSync(file,'utf8');
    assert.ok(html.includes(`lang="${route==='pt'?'pt-BR':route||'en'}"`));
    for(const language of ['pt','en','es'])assert.ok(html.includes(`href="/${language}/"`));
    for(const [,url] of html.matchAll(/(?:src|href)="([^"]+)"/g)){
      if(url.startsWith('#')||/^[a-z]+:/i.test(url))continue;
      const resolved=url.startsWith('/')?path.join(dist,url):path.resolve(path.dirname(file),url);
      assert.ok(fs.existsSync(resolved),`${file}: missing ${url}`);
    }
    if(route===''||route==='en')assert.ok(html.includes('linkedin.com/in/lucasalbuquerque/?locale=en-US'));
  }
});

test('project Pages base path preserves locale and query/hash',()=>{
  assert.equal(visit({pathname:'/portfolio/',basePath:'/portfolio/',languages:['pt-BR']}).redirect,'/portfolio/pt/?ref=portfolio#projetos');
  assert.equal(visit({pathname:'/portfolio/index.html',basePath:'/portfolio/'}).redirect,'/portfolio/en/?ref=portfolio#projetos');
  assert.equal(visit({pathname:'/portfolio/es/',basePath:'/portfolio/'}).redirect,null);
});
