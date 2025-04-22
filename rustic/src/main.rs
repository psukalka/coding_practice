fn main(){
    let s = String::from("Pavan");
    greet_me(s);
}

fn greet_me(s: String){
    println!("Hello {s}");
}