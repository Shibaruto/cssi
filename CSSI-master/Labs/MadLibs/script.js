let counter= 0;

function init()
{
	document.getElementById('cl').addEventListener('click',generateMsg);
}

function generateMsg()
{
	if(counter === 0)
	{
	const ms=['m','s','g','l','p'] //Create a constant array of the ids of the input textfields.*/

 	let values = [];
for (let i=0; i< ms.length; i++){
	values[i]=document.getElementById(ms[i]).value;
}

	/*Using a for loop, populate the values array with the values of the
	 textfields*/


	let msg = `If anybody is wondering, please know that I am <strong>${values[2]}</strong> at/to <strong>${values[4]}</strong> without you.
	You might want to consider <strong>${values[3]}</strong> <strong>${values[0]}</strong>... then again, you always preferred
	<strong>${values[1]}</strong>.`;

	document.getElementById('msg').innerHTML=msg;
document.querySelector('body').classList.add('black');
document.getElementById('cl').innerHTML='reset';
}
else {
	resetgame();
}
counter = (counter+1)%2;	//Display the msg string in the paragraph element with id 'msg'
}

function resetgame(){

document.querySelector('body').classList.remove('black');
document.getElementById('msg').innerHTML='';
document.getElementById('cl').innerHTML='Go Mad!';
}
