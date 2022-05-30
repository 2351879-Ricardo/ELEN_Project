// Replace the content of the element eleme with the content inside another element
function ReplaceContent(elemId, newContentId) {
  let elem = document.getElementById(elemId);
  let newContent = document.getElementById(newContentId);
  elem.innerHTML = newContentId.innerHTML;
}
