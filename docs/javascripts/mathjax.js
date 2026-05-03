// 配置 MathJax 全局选项
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// 监听 Material 主题的页面内容更新事件
document$.subscribe(() => {
  if (typeof MathJax !== "undefined") {
    MathJax.typesetPromise();
  }
});