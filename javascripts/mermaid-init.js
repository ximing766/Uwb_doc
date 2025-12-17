/* Mermaid init: convert code/pre to div.mermaid and render */
(function(){
  function toDivMermaid() {
    var blocks = [];
    // Convert fenced code blocks: <pre><code class="language-mermaid">...</code></pre>
    document.querySelectorAll('pre > code.language-mermaid').forEach(function(code){
      var pre = code.parentElement;
      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = code.textContent;
      pre.replaceWith(div);
      blocks.push(div);
    });
    // Convert <pre class="mermaid">...</pre>
    document.querySelectorAll('pre.mermaid').forEach(function(pre){
      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = pre.textContent;
      pre.replaceWith(div);
      blocks.push(div);
    });
    // Convert standalone <code class="language-mermaid">
    document.querySelectorAll('code.language-mermaid').forEach(function(code){
      if (!code.closest('pre')) {
        var div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = code.textContent;
        code.replaceWith(div);
        blocks.push(div);
      }
    });
    return blocks;
  }

  function initMermaid(){
    if (typeof mermaid === 'undefined') { return; }
    var scheme = document.body.getAttribute('data-md-color-scheme') || 'default';
    mermaid.initialize({ startOnLoad: false, theme: scheme === 'slate' ? 'dark' : 'default' });
    toDivMermaid();
    try { mermaid.init(); } catch (e) { console.warn('Mermaid init failed:', e); }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMermaid);
  } else {
    initMermaid();
  }
})();