// default preloads config
window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector);
    if (element) {
      element.innerText = text;
    }
  };
  const fields = ['chrome', 'node', 'electron'];
  for (const defaultFields of fields) {
    replaceText(`${defaultFields}-version`, process.versions[defaultFields]);
  }
});
