        let validation = document.querySelector('validate');

// let screenwidth= document.querySelector('.bodydiv').clientWidth;


    
// let click= document.querySelector("#clickit");
// click.addEventListener('click', function(){
//     let rightelement= document.querySelector('.right_in');
//     rightelement.classList.replace('slideInRight','slideOutRight');
//     rightelement.classList.add('delay-1s')
//     let leftelement= document.querySelector('.left_in');
//     leftelement.classList.add('fadeOut');
//     click.classList.add('fadeOut');
//     click.classList.replace('delay','delay-2s');

//     let bodytag= document.querySelector('#bodyelements');
//     bodytag.classList.add('bodydisplay');
//     bodytag.classList.add('slideInLeft');

//     let bodyappear= document.querySelector('#body');
//     bodyappear.classList.add('fadeIn');
    
// })
const emailregex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

let slider =  document.querySelector('.started a');


slider.addEventListener('click', (e)=>{
    e.preventDefault();
    let bod =  document.querySelector('body');
    if (bod.classList.contains('close')) {
        bod.classList.remove('close');
    }    

    $('html,body').animate({
        scrollTop: $("#intro").offset().top},
        'slow');
})


setTimeout(() => {
    document.querySelector('body').classList.remove('wait');


}, 2000);


let form = document.querySelector('form');
let count  = 0
form.addEventListener('submit', (e)=>{
    if (count==0){
        e.preventDefault;
        count +=1;
    }

    let email= document.querySelector('#user_mail');
    if (!emailregex.test(email.value)) {
        email.nextElementSibling.textContent ='Please enter a valid email';
        email.nextElementSibling.classList.add('validate');
    }

    else{
        email.nextElementSibling.textContent = ''
        email.nextElementSibling.classList.remove('validate');
    }

    let project_type = document.querySelector('#project_type');
    if ( project_type.value == 'Choose Project Type' ) {
        project_type.nextElementSibling.textContent ='This field is required'
        project_type.nextElementSibling.classList.add('validate')
    
    }
    else{
        project_type.nextElementSibling.textContent = '';
        project_type.nextElementSibling.classList.remove('validate');
    }

        count = 0
        let validation = document.querySelectorAll('.page');
        for (const a of validation) {
            if (a.classList.contains('validate')) {
                count+=1;
            }
        }    
    
        if (count >=1) {
            e.preventDefault();
        }
})

