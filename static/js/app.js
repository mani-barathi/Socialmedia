const userImg  =  document.getElementById('user-image');
const dropDownDiv  =  document.getElementById('dropdown');


if (userImg){
	userImg.onclick = (e) => {
  		dropDownDiv.classList.toggle('show');
  		return false
	}

}
// takes care to close the dropdown if user clicks out of dropdown, when it is displyed
window.onclick = function(event) {
  // cheak if the dropdown in displayed  
  if(dropDownDiv.classList.contains('show')){
    if (event.target.id!=='dropdown' && event.target.id!=='user-image' && event.target.id!=='user-name' && event.target.id!=='dropdown-img' && event.target.id!=='user-email' ) {
      dropDownDiv.classList.toggle('show');
    }
  }
}