let delivers_by_Santa = 0;
let delivers_by_elfs = 0;
let delivers_by_PR = 0;

function add_delivery_by_Santa(){
    delivers_by_Santa += 1;
    document.getElementById('devs_by_Santa').innerHTML = String(delivers_by_Santa);
}

function add_delivery_by_elfs(){
    delivers_by_elfs += 1;
    document.getElementById('devs_by_elfs').innerHTML = String(delivers_by_elfs);
}

function add_delivers(){
    delivers_by_Santa += 1;
    delivers_by_elfs += 1;
    delivers_by_PR += 1;

    document.getElementById('devs_by_Santa').innerHTML = String(delivers_by_Santa);
    document.getElementById('devs_by_elfs').innerHTML = String(delivers_by_elfs);
    document.getElementById('devs_by_PR').innerHTML = String(delivers_by_PR);
}
