// When back arrow is clicked, show previous section 
window.onpopstate = function(event) { 
    if (event.state && event.state.section) {
        console.log(event.state.section); 
        showSection(event.state.section); 
    }
} 
 
function showSection(section) { 
    fetch(`/singlepage/sections/${section}`) 
    .then(response => response.text()) 
    .then(text => { 
        console.log(text); 
        document.querySelector('#content').innerHTML = text; 
    }); 
 
} 
 
document.addEventListener('DOMContentLoaded', function() { 
    // Initially hide the content div
    document.querySelector('#content').style.display = 'none';
    
    document.querySelectorAll('button').forEach(button => { 
        button.onclick = function() { 
            const section = this.dataset.section; 
 
            // Show the content div when button is clicked
            document.querySelector('#content').style.display = 'block';
            
            // Add the current state to the history 
            history.pushState({section: section}, "", `section${section}`); 
            showSection(section); 
        }; 
    }); 
});