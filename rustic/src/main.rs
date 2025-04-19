fn main(){
    let s = String::from("Pavan");
    greet_me(s);
    println!("{s}");  // This will throw error without reference
}

fn greet_me(s: String){
    println!("Hello {s}");
}