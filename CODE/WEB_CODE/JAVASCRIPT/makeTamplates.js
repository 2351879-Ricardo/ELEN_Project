// This script is based on one oroginally created by J Jandrell for a personal project
// GROOP my use this code however they may not claim ownership of it. This script was not made on company time
// J Jandrell owns the rights to this scrip and may use it eleswhere
//
// Owner Joshua Jandrell
// version 0.0
// staus: complete 05/30/22

funtion Maketemplates(templateClass){
	let templates = document.getElementsByTagName('template');
	Array.from(templates).forEach((template)=> {
		let tempId = template.id;
		
	);
}

funtion MakeShadowtemplate(templateName){
	customElements.define(
		templateName,
		// Define class
		class extends HTMLElement{
			constructor(){
			}
		}
}
