const selectedClass = "select";
let selected = null;

function SetSelection(elem) {
  if (selected != null) {
    selected.classList.remove(selectedClass);
  }

  if (!elem.classList.contains(selectedClass)) {
    elem.classList.add(selectedClass);
  }
  selected = elem;
}
