let textarea = document.querySelector('.post_textarea');
let form = document.querySelector('.comment_form')
form.addEventListener('submit', function(e) {
  e.preventDefault();
  if(!textarea.value) {
    return;
  }
  this.submit();
});